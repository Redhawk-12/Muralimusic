import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from CUTEXMUSIC import LOGGER
from pyrogram.types import Message
import random
from config import OWNER_ID
from CUTEXMUSIC.misc import SUDOERS
from CUTEXMUSIC import app, userbot
from CUTEXMUSIC.utils.database.Welcomedb import *
from config import LOG_GROUP_ID


LOGGER = getLogger(__name__)

Zthumb = [
"Wel1",
"Wel2",
"Wel3",
"Wel4",
"Wel5",
"Wel6",
"Wel7",
"Wel8",
"Wel9",
"Wel10",
]



class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(450, 450)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chat, id, uname, Thumbnail):
    background = Image.open(f"assets/Wel/{Thumbnail}.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize(
        (900, 900)
    ) 
    draw = ImageDraw.Draw(background)
   # font = ImageFont.truetype('assets/font.ttf', size=160)
    font2 = ImageFont.truetype('assets/font.ttf', size=50)
    draw.text((48, 37), f"CUTEXMUSIC", fill=(255, 255, 255), font=font2)
   # draw.text((1680, 1120), f'ID: {id}', fill=(255, 255, 255), font=font)
  #  draw.text((1680, 1380), f"USERNAME : {uname}", fill=(255,255,255),font=font)
    pfp_position = (170, 330)  
    background.paste(pfp, pfp_position, pfp)  
    background.save(
        f"downloads/welcome#{id}.png"
    )
    return f"downloads/welcome#{id}.png"

SPECIAL_WELCOME_USER_IDS = {6761639198, 6844821478}

@app.on_message(filters.command(["zwel", "zswel", "zWelcome"]) & ~filters.private)
async def auto_state(_, message):
    usage = "**Usage:**\n/wel [ENABLE|DISABLE]"
    if len(message.command) == 1:
        return await message.reply_text(usage)

    chat_id = message.chat.id
    user_id = message.from_user.id

    if user_id in SPECIAL_WELCOME_USER_IDS:
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "enable":
            await add_wlcm(chat_id)
            await message.reply_text(f"Enabled Special Welcome in {message.chat.title}")
        elif state == "disable":
            await rm_wlcm(chat_id)
            await message.reply_text(f"Disabled Special Welcome in {message.chat.title}")
        else:
            await message.reply_text(usage)

    else:
        user = await app.get_chat_member(chat_id, user_id)
        if user.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
            A = await wlcm.find_one({"chat_id": chat_id})
            state = message.text.split(None, 1)[1].strip().lower()
            if state == "enable":
                if A:
                    return await message.reply_text("Special Welcome Already Enabled")
                else:
                    await add_wlcm(chat_id)
                    await message.reply_text(f"Enabled Special Welcome in {message.chat.title}")
            elif state == "disable":
                if not A:
                    return await message.reply_text("Special Welcome Already Disabled")
                else:
                    await rm_wlcm(chat_id)
                    await message.reply_text(f"Disabled Special Welcome in {message.chat.title}")
            else:
                await message.reply_text(usage)
        else:
            await message.reply("Only Admins Can Use This Command")


#bhag 

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one({"chat_id" : chat_id})
    if not A:
       return
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    Thumbnail = random.choice(Zthumb)
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "assets/NODP.PNG"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username, Thumbnail
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption= f"""
**


 ❅𝐍𝐚𝐦𝐞 ➳  {user.mention}
 ❅𝐔𝐬𝐞𝐫 𝐍𝐚𝐦𝐞 ➳ @{user.username}
 ❅𝐔𝐬𝐞𝐫 𝐈𝐝  ➳ {user.id}


**
""",
reply_markup=InlineKeyboardMarkup(
[
[InlineKeyboardButton(f"๏ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ!", url=f"https://t.me/CuteXMusicBot?startgroup=new"),
InlineKeyboardButton(f"๏ ᴏᴡɴᴇʀ !",
url=f"tg://openmessage?user_id=6844821478"),
]
]
))

    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass









