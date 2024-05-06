from pyrogram import filters
from pyrogram.types import Message
from config import BANNED_USERS
from strings import get_command
from CUTEXMUSIC import app
from CUTEXMUSIC.core.call import CUTE
from CUTEXMUSIC.utils.database import is_music_playing, music_off, music_on
from CUTEXMUSIC.utils.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")

@app.on_message(filters.command(PAUSE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"], disable_web_page_preview=True)
    await music_off(chat_id)
    await CUTE.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), disable_web_page_preview=True
  )



@app.on_message(filters.command(RESUME_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"], disable_web_page_preview=True)
    await music_on(chat_id)
    await CUTE.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), disable_web_page_preview=True
    )
