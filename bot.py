import discord
import os
from random import *
from discord.ext.commands import Bot
from discord.utils import get
from urllib import request
from bs4 import BeautifulSoup

intents=discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents, help_command=None)
userList = {}

@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다!')





@bot.event
async def on_message(message):
    if message.author.bot: 
        return

    await message.channel.send('.')


@bot.command()
async def 설명(ctx):
    print('used help cmd')
    await ctx.send("-도박장에 오신걸 환영합니다!:D-\n" + "\n"
                    +"참가한 이후 나갈 수 없으며 봇이 업뎃되면 잔액이 초기화 됩니다. 일정 시기마다 봇이 초기화 되므로 주의해 주시길 바랍니다.\n잔액이 매우 부족할경우"
                    +" 한강물 온도 체크후 입수하시면 됩니다.\n" + "\n"
					+ "-게임 룰-\n" + "\n" + "-홀짝 게임 : 홀 또는 짝을 선택하여 참가합니다.(승리시 잔액의 50% 추가 획득, 패배시 잔액의 20%손실)\n" + "\n" + "*-명령어 목록-*\n"
					+ "\n" + "!도박참여 : 도박에 참가합니다. 이 명령어를 사용해야 게임을 즐길 수 있습니다.\n"
					+ "!잔액 : 현재 남은 잔액을 확인합니다. 잔액이 높을수록 게임의 부담이 높아지지만 랭킹에 오를 수 있습니다.\n" + "!홀 : 홀짝게임에 홀을 걸고 참가합니다.\n"
					+ "!짝 : 홀짝게임에 짝을 걸고 참가합니다.\n" + "!랭킹 : 랭킹을 확인합니다.")
		   
		   
@bot.command()
async def help(ctx):
    await ctx.send("-도박장에 오신걸 환영합니다!:D-\n" + "\n"
                    +"참가한 이후 나갈 수 없으며 봇이 업뎃되면 잔액이 초기화 됩니다. 일정 시기마다 봇이 초기화 되므로 주의해 주시길 바랍니다.\n잔액이 매우 부족할경우"
                    +" 한강물 온도 체크후 입수하시면 됩니다.\n" + "\n"
					+ "-게임 룰-\n" + "\n" + "-홀짝 게임 : 홀 또는 짝을 선택하여 참가합니다.(승리시 잔액의 50% 추가 획득, 패배시 잔액의 20%손실)\n" + "\n" + "*-명령어 목록-*\n"
					+ "\n" + "!도박참여 : 도박에 참가합니다. 이 명령어를 사용해야 게임을 즐길 수 있습니다.\n"
					+ "!잔액 : 현재 남은 잔액을 확인합니다. 잔액이 높을수록 게임의 부담이 높아지지만 랭킹에 오를 수 있습니다.\n" + "!홀 : 홀짝게임에 홀을 걸고 참가합니다.\n"
					+ "!짝 : 홀짝게임에 짝을 걸고 참가합니다.\n" + "!랭킹 : 랭킹을 확인합니다.")
		   
		   
@bot.command()
async def 도박참여(ctx):
    if not userList:
        userList[str(ctx.author)] = 100000
        await ctx.send(ctx.author.mention + "님이 게임에 참가하셨습니다.  (잔액:100000원)")
        return
        
    
    for name in userList:
        if name == str(ctx.author) :
            await ctx.send(ctx.author.mention + "님은 이미 게임에 참가하셨습니다.")        
            return

    userList[str(ctx.author)] = 100000

    await ctx.send(ctx.author.mention + "님이 게임에 참가하셨습니다.  (잔액:100000원)")
    
@bot.command()
async def 잔액(ctx):
    for name in userList:
        if name == str(ctx.author) :
            await ctx.send(ctx.author.mention + "님의 잔액은 " + str(userList[name]) + "원 입니다.")
            return

@bot.command()
async def 홀(ctx):
    for name in userList:
        if not name:
            return

        if name == str(ctx.author):
            rand = randint(0, 2)

            if rand == 0:
                if userList[name] <= 0:
                    userList[name] += 1000
                    await ctx.send(ctx.author.mention + "\n*\"홀\"이 나왔습니다. 빚이 있으므로 1000원을 얻습니다.*  (잔액:" + str(userList[name]) + "원)")
                    break
                else:
                    userList[name] += int(userList[name] / 2)
                    await ctx.send(ctx.author.mention + "\n*\"홀\"이 나왔습니다. 잔액의 50%를 얻습니다.*  (잔액:" + str(userList[name]) + "원)")
                    break
            else:
                if userList[name] <= 0:
                    userList[name] -= 1000
                    await ctx.send(ctx.author.mention + "\n*\"짝\"이 나왔습니다. 빚이 있으므로 1000원을 잃습니다.*  (잔액:" + str(userList[name]) + "원)")
                    break
                else:
                    userList[name] -= int(userList[name] * 0.2)
                    await ctx.send(ctx.author.mention + "\n*\"짝\"이 나왔습니다. 잔액의 20%를 잃습니다.*  (잔액:" + str(userList[name]) + "원)")
                    break


@bot.command()
async def 짝(ctx):
     for name in userList:
        if not name:
            return

        if name == str(ctx.author):
            rand = randint(0, 2)

            if rand == 0:
                if userList[name] <= 0:
                    userList[name] += 1000
                    await ctx.send(ctx.author.mention + "\n*\"짝\"이 나왔습니다. 빚이 있으므로 1000원을 얻습니다.*  (잔액:" + str(userList[name]) + "원)")
                    break
                else:
                    userList[name] += int(userList[name] / 2)
                    await ctx.send(ctx.author.mention + "\n*\"짝\"이 나왔습니다. 잔액의 50%를 얻습니다.*  (잔액:" + str(userList[name]) + "원)")
                    break
            else:
                if userList[name] <= 0:
                    userList[name] -= 1000
                    await ctx.send(ctx.author.mention + "\n*\"홀\"이 나왔습니다. 빚이 있으므로 1000원을 잃습니다.*  (잔액:" + str(userList[name]) + "원)")
                    break
                else:
                    userList[name] -= int(userList[name] * 0.2)
                    await ctx.send(ctx.author.mention + "\n*\"홀\"이 나왔습니다. 잔액의 20%를 잃습니다.*  (잔액:" + str(userList[name]) + "원)")
                    break

@bot.command()
async def 랭킹(ctx):
    rankMap = {

    }

    for name in userList:
        if not name :
            break

        rankMap[name.split("#")[0]] = str(userList[name])

    sdict= sorted(rankMap.items(), key=lambda x: x[1], reverse=True)

    rankingMsg = "-랭킹-\n\n"

    i = 1

    for inf in sdict:
        rankingMsg += str(i) + "위:" + inf[0] + "  (잔액:" + str(inf[1]) + "원)\n"
        i += 1

    if rankingMsg == "-랭킹-\n\n":
        await ctx.send('참가자 없음.')    
        return

    await ctx.send(rankingMsg)

    

bot.run(os.environ['token'])
