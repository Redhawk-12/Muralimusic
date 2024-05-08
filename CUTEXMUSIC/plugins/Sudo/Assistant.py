import os
from pyrogram import filters, Client
from pyrogram.types import Message
from CUTEXMUSIC import app, userbot
from CUTEXMUSIC.misc import SUDOERS
from CUTEXMUSIC.utils.database import get_client
import asyncio
from pyrogram.errors import FloodWait
import nekos
from config import OWNER_ID, SUPPORT_GROUP
from CUTEXMUSIC.core.userbot import assistants


@app.on_message(filters.command("setpfp") & SUDOERS)
async def set_pfp(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply_text("Reply to a photo.")
    for num in assistants:
        client = await get_client(num)
        photo = await message.reply_to_message.download()
        try:
            await client.set_profile_photo(photo=photo)
            await message.reply_text("Successfully Changed PFP.")
            os.remove(photo)
        except Exception as e:
            await message.reply_text(f"{e}")


@app.on_message(filters.command("setbio") & SUDOERS)
async def set_bio(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Give some text to set as bio.")
    bio = message.text.split(None, 1)[1]
    for num in assistants:
        client = await get_client(num)
        try:
            await client.update_profile(bio=bio)
            await message.reply_text("Successfully Changed Bio.")
        except Exception as e:
            await message.reply_text(f"{e}")


@app.on_message(filters.command("setname") & SUDOERS)
async def set_name(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Give some text to set as name.")
    name = message.text.split(None, 1)[1]
    for num in assistants:
        client = await get_client(num)
        try:
            await client.update_profile(first_name=name)
            await message.reply_text(f"Name Changed to {name}.")
        except Exception as e:
            await message.reply_text(f"{e}")


@app.on_message(filters.command("delpfp") & SUDOERS)
async def del_pfp(client: Client, message: Message):
    for num in assistants:
        client = await get_client(num)
        photos = [p async for p in client.get_chat_photos("me")]
        try:
            if photos:
                await client.delete_profile_photos(photos[0].file_id)
                await message.reply_text("Successfully deleted photo.")
            else:
                await message.reply_text("No profile photos found.")
        except Exception as e:
            await message.reply_text(f"{e}")


@app.on_message(filters.command("delallpfp") & SUDOERS)
async def delall_pfp(client: Client, message: Message):
    for num in assistants:
        client = await get_client(num)
        photos = [p async for p in client.get_chat_photos("me")]
        try:
            if photos:
                await client.delete_profile_photos([p.file_id for p in photos])
                await message.reply_text("Successfully deleted all photos.")
            else:
                await message.reply_text("No profile photos found.")
        except Exception as e:
            await message.reply_text(f"{e}")






profile_picture_update_enabled = False


async def update_profile_picture(client):
    global profile_picture_update_enabled
    while profile_picture_update_enabled:
        try:
            image_url = nekos.img("neko")
            photo_path = await client.download_media(image_url)
            await client.set_profile_photo(photo=photo_path)
            
            os.remove(photo_path)
            
            await asyncio.sleep(1200)
        except Exception as e:
            print(f"Error updating profile picture: {e}")
            await asyncio.sleep(60)



@app.on_message(filters.command("pfps") & SUDOERS)
async def pfp_toggle_on(client: Client, message: Message):
    global profile_picture_update_enabled
    if len(message.command) < 2:
        return await message.reply_text("Please provide 'on' or 'off' as arguments.")
    if message.command[1] == "on":
        profile_picture_update_enabled = True
        await message.reply_text("Profile picture updating is now enabled.")
        asyncio.create_task(update_profile_picture(client))
    elif message.command[1] == "off":
        profile_picture_update_enabled = False
        await message.reply_text("Profile picture updating is now disabled.")
        
