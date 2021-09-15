from collections import UserList
import discord
import json
from discord import channel
import requests
from requests.api import request
from requests.sessions import Request
import os
import random


url = 'https://script.google.com/macros/s/AKfycbwIGjc6merW4KOIh_fQ1hTOLw28nB_B0iRHiWDJG103gBskGHLVIVjb_s_YZIiPfSUW6w/exec?sheetName=requestList'
patchNote = 'http://arkdedicated.com/dynamicconfig.ini'

global passNum
global j


platform = "Discord / Wechat"
plat_id = "Discord ID or WeChat ID"
ingame = "INGAME NAME"


arthro = " [Arthro/古马陆]"



def checkList(output,dino) :
    global show
    global howmany
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
            req[str(output["data"][i][ingame])] = howmany[i-passNum]
            platInfo[i-passNum] = str(output["data"][i][platform])
            idInfo[i-passNum] = str(output["data"][i][plat_id])



    for key, val in req.items():
        show[j] = str(platInfo[j])+" : "+str(idInfo[j])+"\n"+"Name: "+key+"\n"+"Quantity: "+val+"\n\n"
        print("this is output :  "+str(show[j])+"\n")
        j=j+1



client = discord.Client()

@client.event
async def on_ready():

    
    await client.change_presence(status=discord.Status.online, activity=discord.Game("곰젤리 먹방"))

    print('We have logged in as {0.user}'.format(client)) #실행 콘솔로그

@client.event
async def on_message(message):

    foodList = ['사탕','초콜릿','물','짜장면','블루베리','짬뽕','치킨','족발','라면','피자','파스타','돈까스','김치볶음밥','양꼬치','돼지국밥','마라탕','순대국밥','떡볶이','갈비탕','냉면','밀면','쌀국수','볶음밥','삼겹살','소고기','회','초밥','우동','쫄면','육회','찜닭','감자탕','커피','햄버거','김밥','보쌈','라멘','비빔밥','아무거나','곰젤리','콜라','사이다','맥주','쭈꾸미','곱창','갈비찜','소바','부대찌개','김치찌개','된장찌개','스테이크','빵','츄러스','치즈케이크','샐러드','요거트','죽','덮밥','샤브샤브','월남쌈','전골']
    menu = random.choice(foodList) 
    output = requests.get(url).json()
    patchOut = requests.get(patchNote)
    print(patchOut)

    if message.author == client.user: # 봇 메시지 무시
        return

    if message.content == ';밥':
        await message.channel.send(menu+"ㄱㄱㄱ")

    ch = client.get_channel(channel)
    await ch.delete()
    await ch.send ('on test...\n'+patchOut)

    # if message.content.startswith(';arthro'):
    #     checkList(output,arthro)
    #     if message.content == ';arthro':
    #         await message.channel.send("```"+str(show[0])+str(show[1])+str(show[2])+str(show[3])+str(show[4])+"```")
    #         return
    #     # if message.content[:-2] == '-a':
    #     #     await message.channel.send("it's about all list")
    #     #     return


client.run(os.environ['token'])
#"```"+arthroShow[0]+'\n'+arthroShow[1]+'\n'+arthroShow[2]+'\n'+arthroShow[3]+'\n'+arthroShow[4]+"```"