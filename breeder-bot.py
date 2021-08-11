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


howmany = []

show = []


def checkList(output,dino) :
    req = dict()
    listlen = len(output["data"])
    howmany = []
    show = []
    passNum = 0
    platInfo = []
    idInfo = []

    print("this is dino :  "+dino+"\n")

    j=0
    for i in range(listlen):
        if str(output["data"][i][dino]) == '' or 0:
            passNum = passNum+1
            continue
        else:
            howmany.append(str(output["data"][i][dino]))
            req[str(output["data"][i][ingame])] = howmany[i-passNum]
            platInfo.append(str(output["data"][i][platform]))
            idInfo.append(str(output["data"][i][plat_id]))



    for key, val in req.items():
        show.append(platInfo[j]+" : "+idInfo[j]+"\n"+"Name: "+key+"\n"+"Quantity: "+val+"\n")
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
            await message.channel.send("it's about top 10\n"+str(show))
            return
        # if message.content[:-2] == '-a':
        #     await message.channel.send("it's about all list")
        #     return


client.run(os.environ['token'])
#"```"+arthroShow[0]+'\n'+arthroShow[1]+'\n'+arthroShow[2]+'\n'+arthroShow[3]+'\n'+arthroShow[4]+"```"