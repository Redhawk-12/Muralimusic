from pyrogram import Client, filters, types
import requests
import os
import nekos
import time 
import random
from pyrogram.enums import ChatType
from pyrogram.errors import MessageNotModified
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto)
from typing import Union
from CUTEXMUSIC import app
from config import OWNER_ID, LOG_GROUP_ID

# WRITTEN BY - MURALI-BOTS

phtotlist = ["neko", "waifu"]
cutee = random.choice(phtotlist)
url = f"https://api.waifu.pics/sfw/{cutee}"

@app.on_message(filters.command(["anime", "animepfp"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def animenekoimages(client, message):      
    await message.reply_photo(photo="https://telegra.ph/file/a36413c838b31caee7eb9.jpg",
                              caption=f"Choose what you want:",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                  InlineKeyboardButton(text="ɴᴇᴋᴏ ᴀɴɪᴍᴇ [ V1 ]", callback_data="animev1"),
                  InlineKeyboardButton(text="ɴᴇᴋᴏ ᴀɴɪᴍᴇ [ V2 ]", callback_data="animev2"),
                ],
                 [
                   InlineKeyboardButton(text="ɴᴇᴋᴏ ᴀɴɪᴍᴇ [ᴠ𝟹]", callback_data="nekov3"),
                   InlineKeyboardButton(text="ɴᴇᴋᴏ ᴀɴɪᴍᴇ [ᴠ4]", callback_data="nekov4"),
                 ],
                [
                  InlineKeyboardButton(text="Bᴏʏs", callback_data="animeboyspfp"),
                  InlineKeyboardButton(text="ғᴏx ɢɪʀʟ", callback_data="foxgirlz"),
                ],
                [ 
                InlineKeyboardButton(text="ᴋɪᴛsᴜɴᴇ ", callback_data="kitsunepfp"),
                InlineKeyboardButton(text="Wᴀɪғᴜ", callback_data="waifupfp"),
                ],
              [
                InlineKeyboardButton(text="Cᴀᴛs ", callback_data="catsimg"),
              ],
           ]
        )
    )

# anime v1 callback 
@app.on_callback_query(filters.regex("animev1"))
async def animev1callback(client: app, update: Union[types.Message, types.CallbackQuery]):
    response = requests.get(url).json()
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
    try:
        up = response['url']
        but = [
            [InlineKeyboardButton("ᴋɪᴅɴᴀᴘ Mᴇ ✨", url=f"https://t.me/CuteXMusicBot?startgroup=true")],
            [
                InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ 🕊️", callback_data="animev1"),
                InlineKeyboardButton("ᴏᴡɴᴇʀ 💕", user_id=OWNER),
            ],
            [
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data=f"close"),
            ],
        ]
        is_callback = isinstance(update, types.CallbackQuery)
        if is_callback:
            try:
                await update.answer()
            except:
                pass
            chat_id = update.message.chat.id
            await update.message.edit_media(
                media=InputMediaPhoto(up),
            )
            await update.message.edit_caption(
                caption=f"ʟᴀsᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ: {update.from_user.mention}",
                reply_markup=InlineKeyboardMarkup(but)
            )
    except FloodWait as e:
        await update.message.reply(f"<u>ᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ʙʟᴏᴄᴋᴇᴅ ʙʏ ʙᴏᴛ</u>\n\n<u>ʀᴇᴀꜱᴏɴ :</u> ᴜꜱɪɴɢ ᴍᴇ ᴠᴇʀʏ ꜰᴀꜱᴛ \nᴛʀʏ ᴀɢᴀɪɴ ᴀꜰᴛᴇʀ 20 ꜱᴇᴄᴏɴᴅꜱ ")
    except Exception as e:
        await app.send_messsage(LOG_GROUP_ID, f"An error occurred while editing the message in anime v1: {e}")
  
      
# anime v2 callback
@app.on_callback_query(filters.regex("animev2"))
async def animev2callback(client, callback_query: CallbackQuery):
    response = requests.get("https://nekos.best/api/v2/neko").json()
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
    try:
        button = [
            [InlineKeyboardButton("ᴋɪᴅɴᴀᴘ Mᴇ ✨", url=f"https://t.me/CuteXMusicBot?startgroup=true")],
            [
                InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ 🕊️", callback_data="animev2"),
                InlineKeyboardButton("ᴏᴡɴᴇʀ 💕", user_id=OWNER),
            ],
            [     
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data=f"close"),
            ],
        ]
        image_url = response["results"][0]["url"]
        await callback_query.edit_message_media(
            media=InputMediaPhoto(image_url),
        )
        await callback_query.message.edit_caption(
                caption=f"ʟᴀsᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ: {callback_query.from_user.mention}", reply_markup=InlineKeyboardMarkup(button),
       )
    except FloodWait as e:
        await callback_query.message.reply(f"<u>ᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ʙʟᴏᴄᴋᴇᴅ ʙʏ ʙᴏᴛ</u>\n\n<u>ʀᴇᴀꜱᴏɴ :</u> ᴜꜱɪɴɢ ᴍᴇ ᴠᴇʀʏ ꜰᴀꜱᴛ \nᴛʀʏ ᴀɢᴀɪɴ ᴀꜰᴛᴇʀ 20 ꜱᴇᴄᴏɴᴅꜱ ")
    except Exception as e:
        await app.send_messsage(LOG_GROUP_ID, f"An error occurred while editing the message in anime v2: {e}")
  
# anime boys 
@app.on_callback_query(filters.regex("animeboyspfp"))
async def animeboyspfp(client, callback_query: CallbackQuery):
    response = requests.get("https://nekos.best/api/v2/husbando").json()
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
    try:
        button = [
            [InlineKeyboardButton("ᴋɪᴅɴᴀᴘ Mᴇ ✨", url=f"https://t.me/CuteXMusicBot?startgroup=true")],
            [
                InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ 🕊️", callback_data="animeboyspfp"),
                InlineKeyboardButton("ᴏᴡɴᴇʀ 💕", user_id=OWNER),
            ],
            [
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data=f"close"),
            ],
        ]
        image_url = response["results"][0]["url"]
        await callback_query.edit_message_media(
            media=InputMediaPhoto(image_url),
        )
        await callback_query.message.edit_caption(
                caption=f"ʟᴀsᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ: {callback_query.from_user.mention}", reply_markup=InlineKeyboardMarkup(button),
       )
    except FloodWait as e:
        await callback_query.message.reply(f"<u>ᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ʙʟᴏᴄᴋᴇᴅ ʙʏ ʙᴏᴛ</u>\n\n<u>ʀᴇᴀꜱᴏɴ :</u> ᴜꜱɪɴɢ ᴍᴇ ᴠᴇʀʏ ꜰᴀꜱᴛ \nᴛʀʏ ᴀɢᴀɪɴ ᴀꜰᴛᴇʀ 20 ꜱᴇᴄᴏɴᴅꜱ ")
    except Exception as e:
        await app.send_messsage(LOG_GROUP_ID, f"An error occurred while editing the message in anime boys: {e}")
  

# kitsune anime pfp
@app.on_callback_query(filters.regex("kitsunepfp"))
async def animev2callback(client, callback_query: CallbackQuery):
    response = requests.get("https://nekos.best/api/v2/neko").json()
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
    try:
        button = [
            [InlineKeyboardButton("ᴋɪᴅɴᴀᴘ Mᴇ ✨", url=f"https://t.me/CuteXMusicBot?startgroup=true")],
            [
                InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ 🕊️", callback_data="kitsunepfp"),
                InlineKeyboardButton("ᴏᴡɴᴇʀ 💕", user_id=OWNER),
            ],
            [      
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data=f"close"),
            ],
        ]
        image_url = response["results"][0]["url"]
        await callback_query.edit_message_media(
            media=InputMediaPhoto(image_url),
        )
        await callback_query.message.edit_caption(
                caption=f"ʟᴀsᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ: {callback_query.from_user.mention}", reply_markup=InlineKeyboardMarkup(button),
        )
    except FloodWait as e:
        await callback_query.message.reply(f"<u>ᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ʙʟᴏᴄᴋᴇᴅ ʙʏ ʙᴏᴛ</u>\n\n<u>ʀᴇᴀꜱᴏɴ :</u> ᴜꜱɪɴɢ ᴍᴇ ᴠᴇʀʏ ꜰᴀꜱᴛ \nᴛʀʏ ᴀɢᴀɪɴ ᴀꜰᴛᴇʀ 20 ꜱᴇᴄᴏɴᴅꜱ ")
    except Exception as e:
        await app.send_messsage(LOG_GROUP_ID, f"An error occurred while editing the message in anime kitsune: {e}")
  

@app.on_callback_query(filters.regex("waifupfp"))
async def animev2callback(client, callback_query: CallbackQuery):
    response = requests.get("https://nekos.best/api/v2/neko").json()
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
    try:
        button = [
            [InlineKeyboardButton("ᴋɪᴅɴᴀᴘ Mᴇ ✨", url=f"https://t.me/CuteXMusicBot?startgroup=true")],
            [
                InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ 🕊️", callback_data="waifupfp"),
                InlineKeyboardButton("ᴏᴡɴᴇʀ 💕", user_id=OWNER),
            ],
            [
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data=f"close"),
            ],
        ]
        image_url = response["results"][0]["url"]
        await callback_query.edit_message_media(
            media=InputMediaPhoto(image_url),
        )
        await callback_query.message.edit_caption(
                caption=f"ʟᴀsᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ: {callback_query.from_user.mention}", reply_markup=InlineKeyboardMarkup(button),
        )
    except FloodWait as e:
        await callback_query.message.reply(f"<u>ᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ʙʟᴏᴄᴋᴇᴅ ʙʏ ʙᴏᴛ</u>\n\n<u>ʀᴇᴀꜱᴏɴ :</u> ᴜꜱɪɴɢ ᴍᴇ ᴠᴇʀʏ ꜰᴀꜱᴛ \nᴛʀʏ ᴀɢᴀɪɴ ᴀꜰᴛᴇʀ 20 ꜱᴇᴄᴏɴᴅꜱ ")
    except Exception as e:
        await app.send_messsage(LOG_GROUP_ID, f"An error occurred while editing the message in anime waifu : {e}")
  
#fox girl pfp
@app.on_callback_query(filters.regex("foxgirlz"))
async def foxgirlcallback(client, callback_query: CallbackQuery):
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
    try:
        button = [
            [InlineKeyboardButton("ᴋɪᴅɴᴀᴘ Mᴇ ✨", url="https://t.me/CuteXMusicBot?startgroup=true")],
            [
                InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ 🕊️", callback_data="foxgirlz"),
                InlineKeyboardButton("ᴏᴡɴᴇʀ 💕", user_id=OWNER),
            ],
            [
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close"),
            ],
        ]
        await callback_query.edit_message_media(
            media=InputMediaPhoto(media=nekos.img("fox_girl")),
            
        )
        await callback_query.message.edit_caption(
                caption=f"ʟᴀsᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ: {callback_query.from_user.mention}", reply_markup=InlineKeyboardMarkup(button),
        )
    except FloodWait as e:
        await callback_query.message.reply(f"<u>ᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ʙʟᴏᴄᴋᴇᴅ ʙʏ ʙᴏᴛ</u>\n\n<u>ʀᴇᴀꜱᴏɴ :</u> ᴜꜱɪɴɢ ᴍᴇ ᴠᴇʀʏ ꜰᴀꜱᴛ \nᴛʀʏ ᴀɢᴀɪɴ ᴀꜰᴛᴇʀ 20 ꜱᴇᴄᴏɴᴅꜱ ")
    except Exception as e:
        await app.send_messsage(LOG_GROUP_ID, f"An error occurred while editing the message in anime fox girlz: {e}")
  
@app.on_callback_query(filters.regex("nekov3"))
async def foxgirlcallback(client, callback_query: CallbackQuery):
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
    try:
        button = [
            [InlineKeyboardButton("ᴋɪᴅɴᴀᴘ Mᴇ ✨", url="https://t.me/CuteXMusicBot?startgroup=true")],
            [
                InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ 🕊️", callback_data="nekov3"),
                InlineKeyboardButton("ᴏᴡɴᴇʀ 💕", user_id=OWNER),
            ],
            [
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close"),
            ],
        ]
        await callback_query.edit_message_media(
            media=InputMediaPhoto(media=nekos.img("neko")),
            
        )
        await callback_query.message.edit_caption(
                caption=f"ʟᴀsᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ: {callback_query.from_user.mention}", reply_markup=InlineKeyboardMarkup(button),
        )
       
    except FloodWait as e:
        await callback_query.message.reply(f"<u>ᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ʙʟᴏᴄᴋᴇᴅ ʙʏ ʙᴏᴛ</u>\n\n<u>ʀᴇᴀꜱᴏɴ :</u> ᴜꜱɪɴɢ ᴍᴇ ᴠᴇʀʏ ꜰᴀꜱᴛ \nᴛʀʏ ᴀɢᴀɪɴ ᴀꜰᴛᴇʀ 20 ꜱᴇᴄᴏɴᴅꜱ ")
    except Exception as e:
        await app.send_messsage(LOG_GROUP_ID, f"An error occurred while editing the message in anime v3: {e}")
  
# finnaly neko v4 pfps 
@app.on_callback_query(filters.regex("nekov4"))
async def foxgirlcallback(client, callback_query: CallbackQuery):
    response = requests.get("https://nekos.life/api/v2/img/neko")
    data = response.json()
    neko_image_url = data["url"]
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
    try:
        button = [
            [InlineKeyboardButton("ᴋɪᴅɴᴀᴘ Mᴇ ✨", url="https://t.me/CuteXMusicBot?startgroup=true")],
            [
                InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ 🕊️", callback_data="nekov3"),
                InlineKeyboardButton("ᴏᴡɴᴇʀ 💕", user_id=OWNER),
            ],
            [
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close"),
            ],
        ]
        await callback_query.edit_message_media(
            media=InputMediaPhoto(media=neko_image_url),
        )
        await callback_query.message.edit_caption(
                caption=f"ʟᴀsᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ: {callback_query.from_user.mention}", reply_markup=InlineKeyboardMarkup(button),
        )
    except FloodWait as e:
        await callback_query.message.reply(f"<u>ᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ʙʟᴏᴄᴋᴇᴅ ʙʏ ʙᴏᴛ</u>\n\n<u>ʀᴇᴀꜱᴏɴ :</u> ᴜꜱɪɴɢ ᴍᴇ ᴠᴇʀʏ ꜰᴀꜱᴛ \nᴛʀʏ ᴀɢᴀɪɴ ᴀꜰᴛᴇʀ 20 ꜱᴇᴄᴏɴᴅꜱ ")
    except Exception as e:
        await app.send_messsage(LOG_GROUP_ID, f"An error occurred while editing the message in anime v4: {e}")
  

# Cats

@app.on_callback_query(filters.regex("catsimg"))
async def foxgirlcallback(client, callback_query: CallbackQuery):
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
    try:
        button = [
            [InlineKeyboardButton("ᴋɪᴅɴᴀᴘ Mᴇ ✨", url="https://t.me/CuteXMusicBot?startgroup=true")],
            [
                InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ 🕊️", callback_data="catsimg"),
                InlineKeyboardButton("ᴏᴡɴᴇʀ 💕", user_id=OWNER),
            ],
            [
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close"),
            ],
        ]
        await callback_query.edit_message_media(
            media=InputMediaPhoto(media=(nekos.cat())),
        )
        await callback_query.message.edit_caption(
                caption=f"ʟᴀsᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ: {callback_query.from_user.mention}", reply_markup=InlineKeyboardMarkup(button),
        )
    except FloodWait as e:
        await callback_query.message.reply(f"<u>ᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ʙʟᴏᴄᴋᴇᴅ ʙʏ ʙᴏᴛ</u>\n\n<u>ʀᴇᴀꜱᴏɴ :</u> ᴜꜱɪɴɢ ᴍᴇ ᴠᴇʀʏ ꜰᴀꜱᴛ \nᴛʀʏ ᴀɢᴀɪɴ ᴀꜰᴛᴇʀ 20 ꜱᴇᴄᴏɴᴅꜱ ")
    except Exception as e:
        await app.send_messsage(LOG_GROUP_ID, f"An error occurred while editing the message in cats img: {e}")
  
