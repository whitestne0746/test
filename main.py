import discord
import survivor
import os
from discord.ext import commands

client = discord.Client()

TOKEN = os.environ["TOKEN"]

@client.event
async def on_ready():
    print('Logged in as: {}'.format(client.user.name))
    print('ID: {}'.format(client.user.id))
    print('------')

'''
@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)
'''

count = 0
question_state = ""
@client.event
async def on_message(message):
    global count, question_state
    if count == 0:
        count += 1
        text = "やあ, " + message.author.name + "! 何について調べる？\n" + "生存者　殺人鬼　パーク の中から一つ入力してね"
        return await client.send_message(message.channel, text)
    if client.user != message.author:
        if message.content.startswith("ドワイト") or message.content.startswith("どわいと"):
            character = "DWIGHT FAIRFIELD"
        elif message.content.startswith("メグ") or message.content.startswith("めぐ"):
            character = "MEG THOMAS"
        elif message.content.startswith("ジェイク") or message.content.startswith("じぇいく"):
            character = "JAKE PARK"
        elif message.content.startswith("クローデット") or message.content.startswith("くろーでっと"):
            character = "CLAUDETTE MOREL"
        elif message.content.startswith("ネア") or message.content.startswith("ねあ"):
            character = "NEA KARLSSON"
        elif message.content.startswith("ローリー") or message.content.startswith("ろーりー"):
            character = "LAURIE STRODE"
        elif message.content.startswith("エース") or message.content.startswith("えーす"):
            character = "ACE VISCONTI"
        elif message.content.startswith("ウィリアム") or message.content.startswith("うぃりあむ"):
            character = "WILLIAM OVERBECK"
        elif message.content.startswith("フェンミン") or message.content.startswith("ふぇんみん") or message.content.startswith("ミンちゃん"):
            character = "FENG MIN"
        elif message.content.startswith("キング") or message.content.startswith("きんぐ"):
            character = "DAVID KING"
        elif message.content.startswith("クウェンティン") or message.content.startswith("くうぇんてぃん"):
            character = "QUENTIN SMITH"
        elif message.content.startswith("タップ") or message.content.startswith("たっぷ"):
            character = "DAVID TAPP"
        else:
            return await client.send_message(message.channel, "すみません、わかりません。")

        data = survivor.Survivor().charaData(character)
        name = "名前: " + data["name"] + "\n"
        perks = "固有パーク:\n" + data["perks"][0] + ", " + data["perks"][1] + ", " + data["perks"][2]
        await client.send_message(message.channel, name + perks)

client.run(TOKEN)
