from pyrogram import Client, filters, enums
from CUTEXMUSIC import app 
import datetime
import asyncio
import re
from config import LOG_GROUP_ID, OWNER_ID
from pyrogram.types.user_and_chats import ChatPermissions

link_filter = filters.regex(r"(https?://|www\.|t\.me/)\S+\.\S+|\.com")

# EDITS BY - ZeroXCoderZ

@app.on_message(filters.group & link_filter)
async def delete_links(client, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id

        if message.from_user.id == OWNER_ID:
            return

        member = await message.chat.get_member(message.from_user.id)
        if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
            return
        
        await message.delete()
        cute = await message.reply_text(f"Hey {message.from_user.mention} \n You sent a link, so you are muted for 2 minutes")
        mute_time = datetime.datetime.now() + datetime.timedelta(minutes=2)
        await app.restrict_chat_member(chat_id, user_id, ChatPermissions(), until_date=mute_time)
        await asyncio.sleep(120)
        await cute.delete()
    except Exception as e:
        await app.send_message(LOG_GROUP_ID, f" {e} ")


BAD_WORDS = ["fuck", "fukk", "bsdk", "bhosdike", "porn", "xxx", "sex", "gali", "galiya", "bc", "mc", "lode", "loda", "maki", "sale", "bhosda", "bhosdike", "bsdk", "bhosdiwale", "fuckk", "fuck", "fucking", "maaki"]

bad_words_pattern = r"\b(" + "|".join(re.escape(word) for word in BAD_WORDS) + r")\b"


@app.on_message(filters.regex(bad_words_pattern))
async def handle_bad_words(client, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id

        if message.from_user.id == 6761639198:
            return

        member = await message.chat.get_member(message.from_user.id)
        if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
            return
        else: 
            await message.delete()
            cute= await message.reply_text(f"Hey {message.from_user.mention}, you sent a bad word, so you are muted for 2 minutes")
            mute_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
            await app.restrict_chat_member(chat_id, user_id, ChatPermissions(), until_date=mute_time)
            await app.send_message(LOG_GROUP_ID, f"{message.from_user.mention} used a bad word in {message.chat.title}")
            await asyncio.sleep(120)
            await cute.delete() 
    except Exception as e:
        await app.send_message(LOG_GROUP_ID, f" {e} ")
