import discord
import os
from random import *
from discord.ext.commands import Bot
from discord.utils import get
from urllib import request
from bs4 import BeautifulSoup

intents=discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다!')
    #file = open("playerInfo.txt", "a")
    #file.write("")
    #file.close()

@bot.command()
async def 씨발(ctx):
    await ctx.send(ctx.author.mention + "님 인생은 원래 ㅈ같은거에요^^")

@bot.command()
async def 설명(ctx):
    await ctx.send("-도박장에 오신걸 환영합니다!:D-\n" + "\n" + "이 봇은 현재 테스트중에 있으며 게임은 차차 추가 될 예정입니다."
                    +"참가한 이후 나갈 수 없으며 잔액은 봇이 종료되어도 유지됩니다.잔액이 매우 부족할경우"
                    +"개발자 샛끼한테 빌거나 한강물 온도 체크후 입수하시면 됩니다.\n (버그리폿:방장샛끼한테 DM)\n" + "\n"
					+ "-게임 룰-\n" + "\n" + "-홀짝 게임:홀 또는 짝을 선택하여 참가합니다.(승리시 잔액의 50% 추가 획득, 패배시 잔액의 20%손실)\n" + "\n" + "*-명령어 목록-*\n"
					+ "\n" + "!도박참여:도박에 참가합니다. 이 명령어를 사용해야 게임을 즐길 수 있습니다.\n"
					+ "!잔액:현재 남은 잔액을 확인합니다. 잔액이 높을수록 게임의 부담이 높아지지만 랭킹에 오를 수 있습니다.\n" + "!홀:홀짝게임에 홀을 걸고 참가합니다.\n"
					+ "!짝:홀짝게임에 짝을 걸고 참가합니다.\n" + "!랭킹:랭킹을 확인합니다.\n" + "!한강물:수질정보원에서 한강물 온도를 알아옵니다.")

@bot.command()
async def 도박참여(ctx):
    file = open("playerInfo.txt", "r")
    if not file.read():
        file.close()
        file = open("playerInfo.txt", "w")
        file.write(str(ctx.author) + " " + "100000\'")
        file.close()
        await ctx.send(ctx.author.mention + "님이 게임에 참가하셨습니다.  (잔액:100000원)")
        return
        
    
    file.close()
    file = open("playerInfo.txt", "r")
    infos = file.read().split("\'")
    for info in infos:
        if not info:
            break
        name = info.split(" ")

        if name[0] == str(ctx.author) :
            await ctx.send(ctx.author.mention + "님은 이미 게임에 참가하셨습니다.")        
            return

    
    file.close()
    file = open("playerInfo.txt", "a")
    file.write(str(ctx.author) + " " + "100000\'")
    
    file.close()

    await ctx.send(ctx.author.mention + "님이 게임에 참가하셨습니다.  (잔액:100000원)")
    
@bot.command()
async def 잔액(ctx):
    file = open("playerInfo.txt", "r")
    infos = file.read().split("\'")
    for info1 in infos:
        if not info1:
            break
        info = info1.split(" ")

        if info[0] == str(ctx.author) :
            await ctx.send(ctx.author.mention + "님의 잔액은 " + info[1] + "원 입니다.")
            file.close()
            return

    file.close()

@bot.command()
async def 홀(ctx):
    file = open("playerInfo.txt", "r")

    infos = file.read().split("\'")
    newMoney = ""
    cnt = 0

    for info1 in infos:
        cnt += 1
        if not info1:
            break
        info = info1.split(" ")

        if info[0] == str(ctx.author) :
            rand = randint(0, 3)

            if rand == 0:
                file.close()
                file = open("playerInfo.txt", "r")
                infoMsg = file.read()
                newInfoMsg = ""
                m = infoMsg.split("\'")

                for n in range(0, len(m) + 1):
                    if not m[n] :
                        break
                    m1 = m[n].split(" ")

                    if m1[0] == info[0]:
                        m1[1] = str(int(m1[1]) + int(int(m1[1]) / 2))
                        newMoney = m1[1]
                        newInfoMsg += m1[0] + " " + m1[1] + "\'"
                    else:
                        newInfoMsg += m[n] + "\'"

                file.close()
                file = open("playerInfo.txt", "w")
                file.write(newInfoMsg)
                file.close()

                await ctx.send(ctx.author.mention + "\n*\"홀\"이 나왔습니다. 잔액의 50%를 얻습니다.*  (잔액:" + newMoney + "원)")
                return
            else:
                file.close()
                file = open("playerInfo.txt", "r")
                infoMsg = file.read()
                newInfoMsg = ""
                m = infoMsg.split("\'")
                for n in range(0, len(m) + 1):
                    if not m[n]:
                        break

                    m1 = m[n].split(" ")

                    if m1[0] == info[0]:
                        m1[1] = str(int(m1[1]) - int(int(m1[1]) * 0.2))
                        newMoney = m1[1]
                        newInfoMsg += m1[0] + " " + m1[1] + "\'"
                    else:
                        newInfoMsg += m[n] + "\'"

                file.close()
                file = open("playerInfo.txt", "w")
                file.write(newInfoMsg)
                file.close()
                await ctx.send(ctx.author.mention + "\n*\"짝\"이 나왔습니다. 잔액의 20%를 잃습니다.*  (잔액:" + newMoney + "원)")
                return

@bot.command()
async def 짝(ctx):
    file = open("playerInfo.txt", "r")

    infos = file.read().split("\'")
    newMoney = ""
    cnt = 0

    for info1 in infos:
        cnt += 1
        if not info1:
            break


        info = info1.split(" ")

        if info[0] == str(ctx.author) :
            rand = randint(0, 3)

            if rand == 0:
                file.close()
                file = open("playerInfo.txt", "r")
                infoMsg = file.read()
                newInfoMsg = ""
                m = infoMsg.split("\'")
                for n in range(0, len(m) + 1):
                    if not m[n]:
                        break
                    m1 = m[n].split(" ")

                    if m1[0] == info[0]:
                        m1[1] = str(int(m1[1]) + int(int(m1[1]) / 2))
                        newMoney = m1[1]
                        newInfoMsg += m1[0] + " " + m1[1] + "\'"
                    else:
                        newInfoMsg += m[n] + "\'"

                file.close()
                file = open("playerInfo.txt", "w")
                file.write(newInfoMsg)
                file.close()
                await ctx.send(ctx.author.mention + "\n*\"짝\"이 나왔습니다. 잔액의 50%를 얻습니다.*  (잔액:" + newMoney + "원)")
                return
            else:
                file.close()
                file = open("playerInfo.txt", "r")
                infoMsg = file.read()
                newInfoMsg = ""
                m = infoMsg.split("\'")
                for n in range(0, len(m) + 1):
                    if not m[n]:
                        break

                    m1 = m[n].split(" ")

                    if m1[0] == info[0]:
                        m1[1] = str(int(m1[1]) - int(int(m1[1]) * 0.2))
                        newMoney = m1[1]
                        newInfoMsg += m1[0] + " " + m1[1] + "\'"
                    else:
                        newInfoMsg += m[n] + "\'"

                file.close()
                file = open("playerInfo.txt", "w")
                file.write(newInfoMsg)
                file.close()
                await ctx.send(ctx.author.mention + "\n*\"홀\"이 나왔습니다. 잔액의 20%를 잃습니다.*  (잔액:" + newMoney + "원)")
                return

@bot.command()
async def 랭킹(ctx):
    rankMap = {

    }

    file = open("playerInfo.txt", "r")
    infos = file.read().split("\'")

    for info1 in infos:
        if not info1 :
            break
        name = info1.split(" ")
        rankMap[name[0].split("#")[0]] = int(name[1])

    sdict= sorted(rankMap.items(), key=lambda x: x[1], reverse=True)

    rankingMsg = "-랭킹-\n\n"

    i = 1

    for inf in sdict:
        rankingMsg += str(i) + "위:" + inf[0] + "  (잔액:" + str(inf[1]) + "원)\n"
        i += 1

    if rankingMsg == "-랭킹-\n\n":
        return

    await ctx.send(rankingMsg)

@bot.command()
async def 한강물(ctx):
    target = request.urlopen('http://www.koreawqi.go.kr/wQSCHomeLayout_D.wq?action_type=T#')

    soup = BeautifulSoup(target,'html.parser')

    msg = soup.find('tr', class_='site_S01001').find_next_sibling("tr").text

    str1 = str(msg)

    str1 = str1.split('\n')
    str1 = str1[4].split('\t')
    str1 = str1[13].split('\r')
    msg = str1[0]

    await ctx.send('현재 한강물의 온도는 ' + msg + '도 입니다.' + ctx.author.mention + '님께서 뛰어내리기 딱 좋은 온도네요^^')
    

bot.run(os.environ['token'])