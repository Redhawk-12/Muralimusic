from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import asyncio
import requests 
import nekos
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from CUTEXMUSIC import app
from CUTEXMUSIC.core.call import CUTE
from CUTEXMUSIC.utils import bot_sys_stats
from CUTEXMUSIC.utils.decorators.language import language

button = [
       [
            InlineKeyboardButton(
                text="Sᴜᴍᴍᴏɴ ᴍᴇ ✨",     url=f"https://t.me/HawkMusic_Robot?startgroup=new",
            ),
            InlineKeyboardButton(
                   text="〆 ᴄʟᴏsᴇ 〆", callback_data=f"close",
            ),
        ]
]

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(filters.command(PING_COMMAND) & filters.group & ~BANNED_USERS)
@language
async def ping_com(client, message, _):
    em = await message.reply_text(f"🚀")
    await asyncio.sleep(0.1)
    await em.edit(f"ʜᴇʟʟᴏ {message.from_user.mention} ")
    st = await message.reply_sticker("CAACAgUAAx0CfRCYvwACGKhl9wpHYaXxQD8OSnKUx6gh9UgAAX4AAkAIAAKbeohV85_1ROdrq0AeBA")
    await asyncio.sleep(0.3)
    await em.delete()

    
    api_response = requests.get("https://nekos.best/api/v2/neko").json()
    image_url = api_response["results"][0]["url"]
    response_message = await message.reply_photo(
        photo=image_url,
        caption=_["ping_1"],
    )
    start = datetime.now()
    
    pytgping = await CUTE.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await st.delete()

    await response_message.edit_media(
        media=InputMediaPhoto(image_url),
        reply_markup=InlineKeyboardMarkup(button)
    )
    await response_message.edit_caption(
        caption=_["ping_2"].format(resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping)
    )

