import time, re
from config import BOT_USERNAME
from pyrogram.enums import MessageEntityType
from pyrogram import filters
from pyrogram.types import Message
from CUTEXMUSIC import app
import random 
from unidecode import unidecode 
from PIL import Image, ImageDraw, ImageFont
from pyrogram import *
from pyrogram.types import *
from CUTEXMUSIC.utils.database.readable_time import get_readable_time
from CUTEXMUSIC.utils.database.afkdb import add_afk, is_afk, remove_afk

button = [
       [
            InlineKeyboardButton(
                text="Sᴜᴍᴍᴏɴ ᴍᴇ ✨",     url=f"https://t.me/CuteXMusicBot?startgroup=new",
            ),
            InlineKeyboardButton(
                   text="〆 ᴄʟᴏsᴇ 〆", callback_data=f"close",
            ),
        ]
    ]

async def cute_download_pic(user_id):
    user = await app.get_users(user_id)
    if user.photo:
        file_path = await app.download_media(user.photo.big_file_id)
        return file_path
    else:
        return "assets/NODP.PNG"

async def cute_afk_img(user_id, username, first_name):
    photo_path = await cute_download_pic(user_id)
    background = Image.open("assets/AFK.PNG")
    user_photo = Image.open(photo_path)
    user_photo = user_photo.resize((1205, 1205))
# photo phitto ko circle 
    mask = Image.new("L", (1205, 1205), 0) 
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 1205, 1205), fill=255)
    user_photo.putalpha(mask.resize(user_photo.size))  
    background.paste(user_photo, (303, 700), user_photo)
    first_name = unidecode(first_name)
    if username is not None:
        username = unidecode(username)
    else:
        username = "None"
# drawwwwwww 
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('assets/font.ttf', size=175)  
    draw.text((1700, 800), f"Name : {first_name}", font=font, fill=(255, 255, 255))
    draw.text((1700, 1160), f"ID : {user_id}", font=font, fill=(255, 255, 255))
    draw.text((1700, 1510), f"Username : {username}", font=font, fill=(255, 255, 255))

    afk_path = f"afk_{user_id}.png"
    background.save(afk_path)
    
    return afk_path


AFKPHOTO = [
"https://telegra.ph/file/693c9e2f2f7440f52fca5.jpg"
"https://telegra.ph/file/ff97ddfc83e155a9a153a.jpg",
"https://telegra.ph/file/5b7698733583fd0348704.jpg",
"https://telegra.ph/file/c365b6a90f135c2d6fc50.jpg",
"https://telegra.ph/file/77b43f09c5b2cc4be72c7.jpg",
"https://telegra.ph/file/e10bdc982ece5dce0fe7d.jpg",
"https://telegra.ph/file/e10bdc982ece5dce0fe7d.jpg",
"https://telegra.ph/file/41102e5854d9b05252546.jpg",
]

@app.on_message(filters.command(["afk", "brb"], prefixes=["/", "!", ""]))
async def active_afk(_, message: Message):
    if message.sender_chat:
        return
    user_id = message.from_user.id
    username= message.from_user.username
    name = message.from_user.first_name
    verifier, reasondb = await is_afk(user_id)
    afkkphoto = await cute_afk_img(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
    )
    if verifier:
        await remove_afk(user_id)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeafk)))
            if afktype == "text":
                send = await message.reply_photo(
                photo=afkkphoto,
                caption=f"**{message.from_user.mention}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}",
reply_markup=InlineKeyboardMarkup(button),
                  #  disable_web_page_preview=True,
                )
            if afktype == "text_reason":
                send = await message.reply_photo(
data,
                photo=afkkphoto,
                caption=f" {message.from_user.mention} ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`",
reply_markup=InlineKeyboardMarkup(button),
                   # disable_web_page_preview=True,
                )
            if afktype == "animation":
                if str(reasonafk) == "None":
                   send = await message.reply_photo(
                photo=afkkphoto,
                caption=f"**{message.from_user.mention}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}",
reply_markup=InlineKeyboardMarkup(button),
                    )
                else:
                    send = await message.reply_photo(
                        data,
photo=afkkphoto, caption=f"**{message.from_user.mention}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`",
reply_markup=InlineKeyboardMarkup(button),
                    )
            if afktype == "photo":
                if str(reasonafk) == "None":
                    send = await message.reply_photo(
                        photo=afkkphoto,
                        caption=f"**{message.from_user.mention}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}",
reply_markup=InlineKeyboardMarkup(button),
                    )
                else:
                    send = await message.reply_photo(
data,
                        photo=afkkphoto,
                      caption=f"**{message.from_user.mention}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`",
reply_markup=InlineKeyboardMarkup(button),
                    )
        except Exception:
            send = await message.reply_photo(
                   photo=afkkphoto,
               caption=f"**{message.from_user.mention}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ",
                   reply_markup=InlineKeyboardMarkup(button),
               # disable_web_page_preview=True,
            )

    if len(message.command) == 1 and not message.reply_to_message:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and not message.reply_to_message:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "text_reason",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        _reason = message.text.split(None, 1)[1].strip()
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.sticker:
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
    elif len(message.command) > 1 and message.reply_to_message.sticker:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text_reason",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
    else:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }

    await add_afk(user_id, details)    
    await message.reply_photo(
    photo=afkkphoto,
    caption=f"{message.from_user.mention} ɪs ɴᴏᴡ ᴀғᴋ!",
    reply_markup=InlineKeyboardMarkup(button),
    )




chat_watcher_group = 1


@app.on_message(
    ~filters.me & ~filters.bot & ~filters.via_bot,
    group=chat_watcher_group,
)
async def chat_watcher_func(_, message):
    if message.sender_chat:
        return
    userid = message.from_user.id
    user_name = message.from_user.first_name
    name = message.from_user.first_name
    afkkphoto = await cute_afk_img(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
    )
    if message.entities:
        possible = ["/afk", f"/afk@{BOT_USERNAME}"]
        message_text = message.text or message.caption
        for entity in message.entities:
            if entity.type == MessageEntityType.BOT_COMMAND:
                if (message_text[0 : 0 + entity.length]).lower() in possible:
                    return

    msg = ""
    replied_user_id = 0



    verifier, reasondb = await is_afk(userid)
    if verifier:
        await remove_afk(userid)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeafk)))
            if afktype == "text":
                 await message.reply_photo(
                       photo=afkkphoto,
                       caption=f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n",
                       reply_markup=InlineKeyboardMarkup(button),
                )
            if afktype == "text_reason":
                await message.reply_photo(
                       photo=afkkphoto,
                       caption=f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`\n\n",
                       reply_markup=InlineKeyboardMarkup(button),
                )
            if afktype == "animation":
                if str(reasonafk) == "None":
                    await message.reply_photo(
                        data,
photo=afkkphoto,
                        caption=f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n",
reply_markup=InlineKeyboardMarkup(button),
                    )
                else:
                     await message.reply_photo(
                        data,
photo=afkkphoto,
                        caption=f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`\n\n",
reply_markup=InlineKeyboardMarkup(button),
                    )
            if afktype == "photo":
                if str(reasonafk) == "None":
                    await message.reply_photo(
                        photo=afkkphoto,
                        caption=f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n",
                        reply_markup=InlineKeyboardMarkup(button),
                    )
                else:
                     await message.reply_photo(
                       photo=afkkphoto,
                        caption=f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`\n\n",
                            reply_markup=InlineKeyboardMarkup(button),
                    )
        except:
            msg += f"**{user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ\n\n"


    if message.reply_to_message:
        try:
            replied_first_name = message.reply_to_message.from_user.first_name
            replied_user_id = message.reply_to_message.from_user.id
            verifier, reasondb = await is_afk(replied_user_id)
            if verifier:
                try:
                    afktype = reasondb["type"]
                    timeafk = reasondb["time"]
                    data = reasondb["data"]
                    reasonafk = reasondb["reason"]
                    seenago = get_readable_time((int(time.time() - timeafk)))
                    if afktype == "text":
                        await message.reply_photo(
                           photo=afkkphoto,
                            caption=f"**{replied_first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",
                                reply_markup=InlineKeyboardMarkup(button),
                        )
                    if afktype == "text_reason":
                      await message.reply_photo(
                      photo=afkkphoto,
                      caption=f"**{replied_first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`\n\n",
                          reply_markup=InlineKeyboardMarkup(button),
                          )
                    if afktype == "animation":
                      await message.reply_photo(
                      photo=afkkphoto,
                      caption=f"**{replied_first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",
                      reply_markup=InlineKeyboardMarkup(button),
                        )
                except Exception:
                    msg += f"**{replied_first_name}** ɪs ᴀғk"
        except:
            pass

    if message.entities:
        entity = message.entities
        j = 0
        for x in range(len(entity)):
            if (entity[j].type) == MessageEntityType.MENTION:
                found = re.findall("@([_0-9a-zA-Z]+)", message.text)
                try:
                    get_user = found[j]
                    user = await app.get_users(get_user)
                    if user.id == replied_user_id:
                        j += 1
                        continue
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_afk(user.id)
                if verifier:
                    try:
                        afktype = reasondb["type"]
                        timeafk = reasondb["time"]
                        data = reasondb["data"]
                        reasonafk = reasondb["reason"]
                        seenago = get_readable_time((int(time.time() - timeafk)))
                        if afktype == "text":
                            await message.reply_photo(
                            photo=afkkphoto,
                               caption=f"**{user.first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",
reply_markup=InlineKeyboardMarkup(button),
                            )
                        if afktype == "text_reason":
                            msg += f"**{user.first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`\n\n"
                        if afktype == "animation":
                            if str(reasonafk) == "None":
                                 await message.reply_photo(
                                    data,
                                    photo=afkkphoto,
                                    caption=f"**{user.first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",
reply_markup=InlineKeyboardMarkup(button),
                                )
                            else:
                                await message.reply_animation(
                                    data,
                                    caption=f"**{user.first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`\n\n",
reply_markup=InlineKeyboardMarkup(button),
                                )
                        if afktype == "photo":
                            if str(reasonafk) == "None":
                                 await message.reply_photo(
                                    data,
                                    photo=afkkphoto,
                                    caption=f"**{user.first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",
reply_markup=InlineKeyboardMarkup(button),
                                )
                    except:
                        msg += f"**{user.first_name}** ɪs ᴀғᴋ\n\n"
            elif (entity[j].type) == MessageEntityType.TEXT_MENTION:
                try:
                    user_id = entity[j].user.id
                    if user_id == replied_user_id:
                        j += 1
                        continue
                    first_name = entity[j].user.first_name
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_afk(user_id)
                if verifier:
                    try:
                        afktype = reasondb["type"]
                        timeafk = reasondb["time"]
                        data = reasondb["data"]
                        reasonafk = reasondb["reason"]
                        seenago = get_readable_time((int(time.time() - timeafk)))
                        if afktype == "text":
                            msg += f"**{first_name}** is ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n"
                        if afktype == "text_reason":
                            msg += f"**{first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`\n\n"
                        if afktype == "animation":
                            if str(reasonafk) == "None":
                                await message.reply_photo(
                                    data,
photo=afkkphoto,
                                    caption=f"**{first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",
                                )
                        if afktype == "photo":
                            if str(reasonafk) == "None":
                                 await message.reply_photo(
                                    data,
                                    photo=afkkphoto,
                                    caption=f"**{user.first_name}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n",
reply_markup=InlineKeyboardMarkup(button),
                                 )
                    except:
                        msg += f"**{first_name}** ɪs ᴀғᴋ\n\n"
            j += 1
    if msg != "":
        try:
            send = await message.reply_text(msg, disable_web_page_preview=True)
        except:
            return

