import discord
import asyncio
import random
import os

from discord.utils import get


client = discord.Client()


@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('디코니 도움말 이라고 하시면 지금 만들어져있는 명령어가 나와요') # ~~ 하는중
    await client.change_presence(status=discord.Status.online, activity=game)
    ch = client.get_channel(931950571848601631)
    await ch.send (f"✅ **디코니가 시작하였습니다**")
@client.event
async def on_message(message):
    if message.content == "디코니 안녕": # 내가 '안녕'이라고 말하면
        await message.channel.send (f"안녕하세요!") # 봇이 '안녕하세요'라고 대답
    if message.content == "디코니 예뻐": # 내가 '안녕'이라고 말하면
        await message.channel.send (f"에헤헤...❤") # 봇이 '안녕하세요'라고 대답
    if message.content == "디코니 디스커": # 내가 '안녕'이라고 말하면
        message = await message.channel.send (f"맨날 이상한거 알려주는 개새끼") # 봇이 '안녕하세요'라고 대답
        await asyncio.sleep(0.2) # 0.2 초후
        await message.edit(content="저의 주인님이에요 ^^")
    if message.content == "디코니 바보": # 내가 '안녕'이라고 말하면
        await message.channel.send (f"너님이 더 바보인걸요? ^^") # 봇이 '안녕하세요'라고 대답
        await message.author.dm_channel.send(f"너님이 더 바보입니당!!")
    if message.content == "디코니 무": # 내가 '안녕'이라고 말하면
        await message.channel.send (f"야호") # 봇이 '안녕하세요'라고 대답
        msg = await message.channel.send (f"보단 우영우")
        await asyncio.sleep(0.3) # 숫자는 몇초후를 의미함
        await msg.delete() # 메세지 삭제를 의미
    if message.content == "디코니 도움말": # 내가 '안녕'이라고 말하면
        await message.channel.send (f"지금까지 만들어 진건 디코니 목이버섯/디코니 뇌절/디코니 임베드 내용/디코니 고양이/디코니/ 디코니 안녕/디코니 예뻐/디코니 성별/디코니 디스커/디코니 바보/디코니 무/디코니 디코디코니/디코니 디뉴비/디코니 어쩔티비/디코니 욕/디코니 크시/디코니 우 투더 입니다아아") # 봇이 '안녕하세요'라고 대답
    if message.content == "디코니 디코디코니": # 내가 '안녕'이라고 말하면
        await message.channel.send (f"최초의 이름입니다") # 봇이 '안녕하세요'라고 대답
    if message.content == "디코니 디뉴비": # 내가 '안녕'이라고 말하면
        await message.channel.send (f"저의 후배에요") # 봇이 '안녕하세요'라고 대답
    if message.content == "디코니 어쩔티비": # 내가 '안녕'이라고 말하면
        await message.channel.send (f"저쩔티비")
        await message.channel.send (f"안물티비")
        await message.channel.send (f"안궁티비")
        await message.channel.send (f"뇌절티비")
        await message.channel.send (f"우짤래미")
        await message.channel.send (f"저짤래미")
        await message.channel.send (f"크크루삥뽕!")
    if message.content == "디코니 욕":
        await message.channel.send (f"은 나빠여")
    if message.content == "디코니":
        await message.channel.send (f"넹?")
    if message.content == "디코니 크시":
        await message.channel.send (f"대대대대대대대대대누님이신 봇이에요!")
    if message.content == "디코니 우 투더":
        await message.channel.send (f"영 투더 우!")
        await message.channel.send (f"동 투더 그 투더 롸미")
    if message.content == "디코니 성별":
        await message.channel.send (f"맞춰보세여 히히")
    if message.content == "디코니 고양이":
        await message.channel.send (f"야옹!")
    if message.content == "착한척 하는 나쁜ㄴ":
        await message.channel.send (f"뭐라고..? 잘못 본건가..")
    if message.content == "디코니 뇌절":
        await message.channel.send (f"1절 2절 3절 뇌절")
    if message.content == "디코니 목이버섯":
        await message.channel.send (f"마시쪄")
    if message.content.startswith(":청소 "):   # 명령어를 적고 한칸 띄워주세요
        purge_number = message.content.replace(":청소 ", "")   # 윗줄 명령어와 똑같이 해주세요
        check_purge_number = purge_number.isdigit()

        if check_purge_number == True:
            await message.channel.purge(limit=int(purge_number) + 1)
            msg = await message.channel.send(f"**{purge_number}개**의 메시지를 삭제했어요!")
            await asyncio.sleep(4)   # ←초후에 ~개의 메시지를 삭제했습니다도 지워집니다
            await msg.delete()
        else:
            await message.channel.send("올바른 값을 입력해주세요.")  # 숫자를 입력하지 않았을때

    if message.content == "디코니 임베드 내용": #입력할 메시지
        embed = discord.Embed(title="임베드 내용", description="내용", color=0x4000FF) #큰 제목과 작은 제목을 보여준다
        embed.add_field(name="뉴비의 어드민 점프맵 탄생", value="디뉴비 디코니봇 업데이트", inline=False) #작은 제목과 작은제목의 설명
        await message.channel.send(embed=embed)







access_token - os.environ['BOT_TOKEN']
client.run("access_token") # 토큰 적는곳
