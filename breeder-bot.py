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


howmany = [0] * 100

show = [0] * 100


def checkList(output,dino) :
    req = dict()
    listlen = len(output["data"])
    howmany = [0] * 100
    show = [0] * 100
    passNum = 0
    platInfo = [0] * 100
    idInfo = [0] * 100

    j=0
    for i in range(listlen):
        if str(output["data"][i][exec("%s = %s" % (dino,dino))]) == '' or 0:
            passNum = passNum+1
            continue
        else:
            howmany[i-passNum] = str(output["data"][i][exec("%s = %s" % (dino,dino))])
            req[str(output["data"][i][ingame])] = howmany[i-passNum]
            platInfo[i] = str(output["data"][i][platform])
            idInfo[i] = str(output["data"][i][plat_id])



    for key, val in req.items():
        show[j] = platInfo[j]+" : "+idInfo[j]+"\n"+"Name: "+key+"\n"+"Quantity: "+val+"\n"
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
        if message.content == ';arthro':
            dino = message[1:]
            checkList(output,dino)
            await message.channel.send("it's about top 10\n"+show[0])
            return
        if message[:-2] == '-a':
            await message.channel.send("it's about all list")
            return


client.run(os.environ['token'])
#"```"+arthroShow[0]+'\n'+arthroShow[1]+'\n'+arthroShow[2]+'\n'+arthroShow[3]+'\n'+arthroShow[4]+"```"