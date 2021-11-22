print("[INFO]: Importing Your API_ID, API_HASH, BOT_TOKEN")
import re
from asyncio import (gather, get_event_loop, sleep)

from aiohttp import ClientSession
from pyrogram import (Client, filters, idle)
from Python_ARQ import ARQ

from config import bot, BOT_TOKEN, ARQ_API_KEY, ARQ_API_BASE_URL, LANGUAGE
bot_token= BOT_TOKEN

print("[INFO]: Checking... Your Details")

bot_id = int(bot_token.split(":")[0])
print("[INFO]: Code running by master Poison")
arq = None


async def lunaQuery(query: str, user_id: int):
    query = (
        query
        if LANGUAGE == "en"
        else (await arq.translate(query, "en")).result.translatedText
    )
    resp = (await arq.luna(query, user_id)).result
    return (
        resp
        if LANGUAGE == "en"
        else (
            await arq.translate(resp, LANGUAGE)
        ).result.translatedText
    )


async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    if "support" in response:
        responsee = response.replace("@team_𝚔𝚊𝚛𝚖𝚊", "@𝚔𝚒𝚝𝚝𝚞_𝚋𝚛𝚘𝚔𝚎𝚗_𝚑𝚎𝚊𝚛𝚝")

async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    if "Luna" in response:
        responsee = response.replace("𝚔𝚒𝚝𝚝𝚞", "Chat Bot")
    else:
        responsee = response
    if "Aco" in responsee:
        responsess = responsee.replace("Aco", "Chat Bot")
    else:
        responsess = responsee
    if "Who is ChatBot" in responsess:
        responsess2 = responsess.replace("Who is ChatBot", "Me 😅")
    else:
        responsess2 = responsess
    await message.reply_text(responsess2)
    await message._client.send_chat_action(chat_id, "cancel")


@bot.on_message(
    ~filters.private
    & filters.text
    & ~filters.command("start")
    & ~filters.edited,
    group=69,
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}iris[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await type_and_send(message)


@bot.on_message(
    filters.private
    & ~filters.command("start")
    & ~filters.edited
)
async def chatpm(_, message):
    if not message.text:
        await message.reply_text("Ufffff Avoiding....")
        return
    await type_and_send(message)


@bot.on_message(filters.command("start") & ~filters.edited)
async def startt(_, message):
    await message.reply_text("𝚒𝚊𝚖 𝚘𝚗𝚕𝚒𝚗𝚎 𝚗𝚘𝚠❤️❤️ 𝚋𝚢 @Kittu_broken_heart ")


async def main():
    global arq
    session = ClientSession()
    arq = ARQ(ARQ_API_BASE_URL, ARQ_API_KEY, session)

    await bot.start()
    print(
        """
Your kittuchatbot Is Deployed Successfully.
"""
    )
    await idle()


loop = get_event_loop()
loop.run_until_complete(main())
