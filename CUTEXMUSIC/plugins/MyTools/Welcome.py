import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import random
from CUTEXMUSIC import app

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
    font2 = ImageFont.truetype('assets/font/Sofia-Regular.otf', size=50)
    draw.text((48, 37), f"CUTE X MUSIC", fill="orange", font=font2)
    pfp_position = (223, 317)  
    background.paste(pfp, pfp_position, pfp)  
    background.save(
        f"downloads/welcome#{id}.png"
    )
    return f"downloads/welcome#{id}.png"



@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
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
    except Exception as e:
        pic = "assets/NODP.PNG"
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username, Thumbnail
        )
        await app.send_photo(
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
        print(str(e))
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass









