from collections import UserList
import discord
import json
from discord import channel
import requests
from requests.api import request
from requests.sessions import Request
import os


url = 'https://script.google.com/macros/s/AKfycbwIGjc6merW4KOIh_fQ1hTOLw28nB_B0iRHiWDJG103gBskGHLVIVjb_s_YZIiPfSUW6w/exec?sheetName=requestList'

global passNum
global j

platform = "Discord / Wechat"
plat_id = "Discord ID or WeChat ID"
ingame = "INGAME NAME"


arthro = " [Arthro/古马陆]"


howmany = [0] * 300


def checkList(output,dino) :
    req = dict()
    listlen = len(output["data"])
    howmany = [0] * 300
    show = [0] * 300
    passNum = 0
    platInfo = [0] * 300
    idInfo = [0] * 300

    print("this is dino :  "+dino+"\n")

    j=0
    for i in range(listlen):
        if str(output["data"][i][dino]) == '' or 0:
            passNum = passNum+1
            continue
        else:
            howmany[i-passNum] = str(output["data"][i][dino])
            print("this is howmany :  "+str(howmany[i])+"\n")
            req[str(output["data"][i][ingame])] = howmany[i-passNum]
            platInfo[i] = str(output["data"][i][platform])
            print("this is palt :  "+str(platInfo[i])+"\n")
            idInfo[i] = str(output["data"][i][plat_id])
            print("this is id :  "+str(idInfo[i])+"\n")



    for key, val in req.items():
        show[j] = str(platInfo[j])+" : "+str(idInfo[j])+"\n"+"Name: "+key+"\n"+"Quantity: "+val+"\n"
        print("this is output :  "+str(show[j])+"\n")
        j=j+1



client = discord.Client()

@client.event
async def on_ready():

    
    await client.change_presence(status=discord.Status.online, activity=discord.Game("곰젤리 먹방"))

    print('We have logged in as {0.user}'.format(client)) #실행 콘솔로그

@client.event
async def on_message(message):
    output = requests.get(url).json()

    if message.author == client.user: # 봇 메시지 무시
        return


    if message.content.startswith(';arthro'):
        checkList(output,arthro)
        if message.content == ';arthro':
            await message.channel.send("it's about top 10\n"+str(show[0])+str(show[1])+str(show[2])+str(show[3]))
            return
        # if message.content[:-2] == '-a':
        #     await message.channel.send("it's about all list")
        #     return


client.run(os.environ['token'])
#"```"+arthroShow[0]+'\n'+arthroShow[1]+'\n'+arthroShow[2]+'\n'+arthroShow[3]+'\n'+arthroShow[4]+"```"