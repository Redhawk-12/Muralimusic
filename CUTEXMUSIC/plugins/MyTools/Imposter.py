import os
from PIL import Image, ImageDraw, ImageFont
import requests
import random 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from CUTEXMUSIC.utils.database.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from CUTEXMUSIC import app


BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="ᴋɪᴅɴᴀᴘ ᴍᴇ",
                url="https://t.me/CuteXMusicBot?startgroup=new",
            ),
            InlineKeyboardButton(
                text="〆 ᴄʟᴏsᴇ 〆",
                callback_data="close",
            )
        ]
    ]
)


async def cute_download_pic(user_id):
    user = await app.get_users(user_id)
    if user.photo:
        file_path = await app.download_media(user.photo.big_file_id)
        return file_path
    else:
        return "assets/NODP.PNG"
# IMPOSTER IMAGE 
# CREATED BY MURALI - BOTS
async def cute_imp_img(user_id, username, first_name):
    photo_path = await cute_download_pic(user_id)
    background = Image.open("assets/lMPOSTER.png")
    user_photo = Image.open(photo_path)
    user_photo = user_photo.resize((1400, 1400))
# photo phitto ko circle 
    mask = Image.new("L", (1400, 1400), 0) 
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 1400, 1400), fill=255)
    user_photo.putalpha(mask.resize(user_photo.size))  
    background.paste(user_photo, (125, 352), user_photo)
# drawwwwwww 
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('assets/font.ttf', size=175)  
    draw.text((1700, 600), f"Name : {first_name}", font=font, fill=(255, 255, 255))
    draw.text((1700, 1000), f"ID : {user_id}", font=font, fill=(255, 255, 255))
    draw.text((1700, 1400), f"Username : {username}", font=font, fill=(255, 255, 255))

    impostor_path = f"impostor_{user_id}.png"
    background.save(impostor_path)
    
    return impostor_path



@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**❄️ ᴜsᴇʀ sʜᴏʀᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ❄️**

**๏ ɴᴀᴍᴇ** ➛ {message.from_user.mention}
**๏ ᴜsᴇʀ ɪᴅ** ➛ {message.from_user.id}
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**❄️ ᴄʜᴀɴɢᴇᴅ ᴜsᴇʀɴᴀᴍᴇ ❄️**

**๏ ᴡɪᴛʜᴏᴜᴛ ᴄʜᴀɴɢᴇ ᴜsᴇʀɴᴀᴍᴇ** ➛ {bef}
**๏ ᴀғᴛᴇʀ ᴄʜᴀɴɢᴇ ᴜsᴇʀɴᴀᴍᴇ** ➛ {aft}
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**❄️ ᴄʜᴀɴɢᴇs ғɪʀsᴛ ɴᴀᴍᴇ ❄️**

**๏ ᴡɪᴛʜᴏᴜᴛ ᴄʜᴀɴɢᴇ ғʀɪsᴛ ɴᴀᴍᴇ** ➛ {bef}
**๏ ᴀғᴛᴇʀ ᴄʜᴀɴɢᴇ ғʀɪsᴛ ɴᴀᴍᴇ** ➛ {aft}
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**❄️ ᴄʜᴀɴɢᴇs ʟᴀsᴛ ɴᴀᴍᴇ ❄️**

**๏ ᴡɪᴛʜᴏᴜᴛ ᴄʜᴀɴɢᴇ ʟᴀsᴛ ɴᴀᴍᴇ** ➛ {bef}
**๏ ᴀғᴛᴇʀ ᴄʜᴀɴɢᴇ ʟᴀsᴛ ɴᴀᴍᴇ** ➛ {aft}
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        CUTE_IMP_image = await cute_imp_img(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
        )
        await message.reply_photo(CUTE_IMP_image, caption=msg, reply_markup=BUTTON)

# HEHE
@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ ** \n /imposter enable or disable")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    else:
        await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")


