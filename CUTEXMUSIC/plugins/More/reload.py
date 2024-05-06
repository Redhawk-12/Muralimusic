import asyncio
from pyrogram.types import *
from pyrogram import filters, client
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus
from pyrogram.types import CallbackQuery, Message
from config import BANNED_USERS, MUSIC_BOT_NAME, adminlist, lyrical
from strings import get_command
from CUTEXMUSIC import app
from CUTEXMUSIC.core.call import CUTE
from logging import getLogger
from CUTEXMUSIC import LOGGER
from config import LOG_GROUP_ID
from CUTEXMUSIC.misc import db
from CUTEXMUSIC.utils.database import get_authuser_names, get_cmode
from CUTEXMUSIC.utils.decorators import ActualAdminCB, AdminActual, language
from CUTEXMUSIC.utils.formatters import alpha_to_int

### Multi-Lang Commands
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")


@app.on_message(filters.command(RELOAD_COMMAND) & filters.group & ~BANNED_USERS)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        chat_id = message.chat.id
        admins = app.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS)
        authusers = await get_authuser_names(chat_id)
        adminlist[chat_id] = []
        async for user in admins:
            if user.status == ChatMemberStatus.ADMINISTRATOR:
                adminlist[chat_id].append(user.user.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[chat_id].append(user_id)
        await message.reply_text(_["admin_20"])
    except:
        await message.reply_text(
            "ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇғʀᴇsʜ ᴀᴅᴍɪɴs ʟɪsᴛ, ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ᴩʀᴏᴍᴏᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ."
        )


@app.on_message(filters.command(RESTART_COMMAND) & filters.group & ~BANNED_USERS)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ ʀᴇʙᴏᴏᴛɪɴɢ ༄𝐂𝐔𝐓𝐄 ✘ 𝐌𝐔𝐒𝐈𝐂 ࿐𝄟͢  ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await CUTE.stop_stream(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            await app.get_chat(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await CUTE.stop_stream(chat_id)
        except:
            pass
    return await mystic.edit_text(
        "sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇʙᴏᴏᴛᴇᴅ ༄𝐂𝐔𝐓𝐄 ✘ 𝐌𝐔𝐒𝐈𝐂 ࿐𝄟͢ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ, ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ sᴛᴀʀᴛ ᴩʟᴀʏɪɴɢ ᴀɢᴀɪɴ..."
    )


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("stop_downloading") & ~BANNED_USERS)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(
            "ᴅᴏᴡɴʟᴏᴀᴅ ᴀʟʀᴇᴀᴅʏ ᴄᴏᴍᴩʟᴇᴛᴇᴅ.", show_alert=True
        )
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(
            "ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴀʟʀᴇᴀᴅʏ ᴄᴏᴍᴩʟᴇᴛᴇᴅ ᴏʀ ᴄᴀɴᴄᴇʟʟᴇᴅ.",
            show_alert=True,
        )
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer("ᴅᴏᴡɴʟᴏᴀᴅɪɢ ᴄᴀɴᴄᴇʟʟᴇᴅ.", show_alert=True)
            return await CallbackQuery.edit_message_text(
                f"ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴩʀᴏᴄᴇss ᴄᴀɴᴄᴇʟʟᴇᴅ ʙʏ {CallbackQuery.from_user.mention}"
            )
        except:
            return await CallbackQuery.answer(
                "ғᴀɪʟᴇᴅ ᴛᴏ ᴄᴀɴᴄᴇʟ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...", show_alert=True
            )
    await CallbackQuery.answer("ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴄᴏɢɴɪᴢᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴛᴀsᴋ.", show_alert=True)



@app.on_message(filters.command(["repo", "source"]))
async def newrepomsg(client, message):
    tez = await message.reply_sticker("CAACAgUAAx0CfRCYvwACGpNl-pfSW0bbkGCXA87GopOwTaUEwgACwwwAAneHKVbnz2JiHs1iRB4E")
    await asyncio.sleep(0.2)
    te = await message.reply_sticker("CAACAgUAAx0CfRCYvwACGpFl-paewkn8CmDRNX2pGCK2v0zxcgACTAYAArduiVRsZfI-WCQWox4E")
    await asyncio.sleep(0.3)
    await tez.delete()
    ss = await message.reply_text(f"ᴜ ᴡᴀɴᴛ ᴍʏ ʀᴇᴘᴏ ??\n{message.from_user.mention}")
    await asyncio.sleep(0.6)
    await ss.edit("Jᴜsᴛ ᴀ ᴍɪɴ")
    await asyncio.sleep(0.4)
    sha = await message.reply_sticker("CAACAgUAAx0CfAEyWgACoKVl-rEYhItcr15JUuS26ZtB5lopSAACbQoAAuGcaFbOgOxYgAaxYx4E")
    await te.delete()
    await asyncio.sleep(0.5)
    await message.reply_photo(
        photo="https://telegra.ph/file/0c6d683afa687143788b8.jpg",
        caption=f"ʜᴇʏ {message.from_user.mention}\n\nCʟɪᴄᴋ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ Fᴏʀ Rᴇᴘᴏ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴄʟɪᴄᴋ ʜᴇʀᴇ",
                        callback_data="repppo",
                    )
                ]
            ]
        )
    )
    await sha.delete()
    await ss.delete()
    await app.send_message(LOG_GROUP_ID, f"{message.from_user.mention} used /repo")

@app.on_callback_query(filters.regex("repppo"))
async def gib_repository_callback(_, callback_query):
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://te.legra.ph/file/11b8f5140824cb5f6d5f6.mp4", caption="🤣🤣🤣"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Cʟᴏsᴇ",
                        callback_data="close",
                    )
                ]
            ]
        )
    )
