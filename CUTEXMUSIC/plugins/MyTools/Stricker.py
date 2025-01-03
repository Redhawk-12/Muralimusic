from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import (
    PeerIdInvalid,
    ShortnameOccupyFailed,
    StickerEmojiInvalid,
    StickerPngDimensions,
    StickerPngNopng,
    UserIsBlocked,
)
import os
import config
import pyrogram
from uuid import uuid4
from config import BOT_USERNAME
from CUTEXMUSIC import app


@app.on_message(filters.command(["stickerid", "stid"]))
async def sticker_id(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.sticker:
        await message.reply_text("Reply to a sticker.")
        return
    sticker = message.reply_to_message.sticker
    await message.reply_text(f"**Sticker ID:** `{sticker.file_id}`\n**Unique ID:** `{sticker.file_unique_id}`")


@app.on_message(filters.command(["packkang", "kang"]))
async def _packkang(app, message):
    txt = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ....**")
    if not message.reply_to_message:
        await txt.edit('ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ')
        return
    if not message.reply_to_message.sticker:
        await txt.edit('ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ')
        return
    if message.reply_to_message.sticker.is_animated or message.reply_to_message.sticker.is_video:
        await txt.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ɴᴏɴ-ᴀɴɪᴍᴀᴛᴇᴅ sᴛɪᴄᴋᴇʀ")
        return
    short_name = message.reply_to_message.sticker.set_name
    if short_name is None:
        await txt.edit("This sticker does not belong to any pack.")
        return
    
    if len(message.command) < 2:
        pack_name = f'{message.from_user.first_name}_sticker_pack_by_@CutieXmusicBot'
    else:
        pack_name = message.text.split(maxsplit=1)[1]

    try:
        stickers = await app.invoke(
            pyrogram.raw.functions.messages.GetStickerSet(
                stickerset=pyrogram.raw.types.InputStickerSetShortName(short_name=short_name),
                hash=0
            )
        )
    except Exception as e:
        await txt.edit(f"Failed to fetch sticker set: {str(e)}")
        return

    shits = stickers.documents
    sticks = []

    for i in shits:
        sex = pyrogram.raw.types.InputDocument(
            id=i.id,
            access_hash=i.access_hash,
            file_reference=i.thumbs[0].bytes
        )

        sticks.append(
            pyrogram.raw.types.InputStickerSetItem(
                document=sex,
                emoji=i.attributes[1].alt
            )
        )

    try:
        new_short_name = f'sticker_pack_{str(uuid4()).replace("-","")}_by_{app.me.username}'
        user_id = await app.resolve_peer(message.from_user.id)
        await app.invoke(
            pyrogram.raw.functions.stickers.CreateStickerSet(
                user_id=user_id,
                title=pack_name,
                short_name=new_short_name,
                stickers=sticks,
            )
        )
        await txt.edit(f"**๏ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴋᴀɴɢᴇᴅ ʟɪɴᴋ**!\n**๏ ᴛᴏᴛᴀʟ sᴛɪᴄᴋᴇʀ** : {len(sticks)}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴘᴀᴄᴋ ʟɪɴᴋ", url=f"http://t.me/addstickers/{new_short_name}")]]))
    except Exception as e:
        await txt.edit(f"Failed to create sticker pack: {str(e)}")


@app.on_message(filters.command("stkrfind"))
async def generate_sticker(client, message):
    if len(message.command) == 2:
        sticker_id = message.command[1]
        try:
            await message.reply_sticker(sticker=sticker_id)
        except Exception as e:
            await message.reply_text(f"Error: {e}")
    else:
        await message.reply_text("Please provide a sticker ID after /stkrfind command.")
