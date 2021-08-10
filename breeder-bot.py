from collections import UserList
import discord
import json
from discord import channel
import requests
from requests.api import request
from requests.sessions import Request
import os


url = 'https://script.google.com/macros/s/AKfycbwIGjc6merW4KOIh_fQ1hTOLw28nB_B0iRHiWDJG103gBskGHLVIVjb_s_YZIiPfSUW6w/exec?sheetName=request_list'

global passNum
global j

showList = [0] * 100
howmany = [0] * 100


arthroReq = dict()
gigaReq = dict()
daeodonReq = dict()


def arthro(output) :
    listlen = len(output["data"])
    showList = [0] * 100
    howmany = [0] * 100
    passNum = 0
    j=0
    for i in range(listlen):
        if str(output["data"][i][" [Arthro/古马陆]"]) == '' or 0:
            passNum = passNum+1
            continue
        else:
            howmany[i-passNum] = str(output["data"][i][" [Arthro/古马陆]"])
            arthroReq[str(output["data"][i]["DISCORD ID / INGAME NAME / Main Server"])] = howmany[i-passNum]


    for key, val in arthroReq.items():
        showList[j] = "Name: "+key+"\n"+"Quantity: "+val+"\n"
        j=j+1

def giga(output) :
    listlen = len(output["data"])
    showList = [0] * 100
    howmany = [0] * 100
    passNum = 0
    j=0
    for i in range(listlen):
        if str(output["data"][i][" [Giga/南巨]"]) == '' or 0:
            passNum = passNum+1
            continue
        else:
            howmany[i-passNum] = str(output["data"][i][" [Giga/南巨]"])
            gigaReq[str(output["data"][i]["DISCORD ID / INGAME NAME / Main Server"])] = howmany[i-passNum]


    for key, val in gigaReq.items():
        showList[j] = "Name: "+key+"\n"+"Quantity: "+val+"\n"
        j=j+1

def daeodon(output) :
    listlen = len(output["data"])
    howmany = [0] * 100
    showList = [0] * 100
    passNum = 0
    j=0
    for i in range(listlen):
        if str(output["data"][i][" [Daeodon/回血猪]"]) == '' or 0:
            passNum = passNum+1
            continue
        else:
            howmany[i-passNum] = str(output["data"][i][" [Daeodon/回血猪]"])
            daeodonReq[str(output["data"][i]["DISCORD ID / INGAME NAME / Main Server"])] = howmany[i-passNum]


    for key, val in daeodonReq.items():
        showList[j] = "Name: "+key+"\n"+"Quantity: "+val+"\n"
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

    if message.content == ';arthro':
        arthro(output)
        await message.channel.send("```"+str(showList[0])+'\n'+str(showList[1])+'\n'+str(showList[2])+'\n'+str(showList[3])+'\n'+str(showList[4])+"```")
        return

    if message.content == ';giga':
        giga(output)
        await message.channel.send("```"+str(showList[0])+'\n'+str(showList[1])+'\n'+str(showList[2])+'\n'+str(showList[3])+'\n'+str(showList[4])+"```")
        return

    if message.content == ';daeodon':
        daeodon(output)
        await message.channel.send("```"+str(showList[0])+'\n'+str(showList[1])+'\n'+str(showList[2])+'\n'+str(showList[3])+'\n'+str(showList[4])+"```")
        return     

client.run(os.environ['token'])