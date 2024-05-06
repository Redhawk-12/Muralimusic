from CUTEXMUSIC import app
import asyncio
import requests
from pyrogram import client, filters
import nekos

# All Done

@app.on_message(filters.command("neko"))
async def nekoimgg(client, message):
  await message.reply_photo(nekos.img("neko"))

@app.on_message(filters.command("slap"))
async def slappp(client, message):
    try:
        if message.reply_to_message:
            await message.reply_video(nekos.img("slap"), caption=f"{message.from_user.mention} slapped {message.reply_to_message.from_user.mention}")
        else:
            await message.reply_video(nekos.img("slap"))
    except Exception as e:
        await message.reply_text(f"Error: {e}")


@app.on_message(filters.command("tickle"))
async def tickleee(client, message):
    try:
        if message.reply_to_message:
            await message.reply_video(nekos.img("tickle"), caption=f"{message.from_user.mention} tickle {message.reply_to_message.from_user.mention}")
        else:
            await message.reply_video(nekos.img("tickle"))
    except Exception as e:
        await message.reply_text(f"Error: {e}")


@app.on_message(filters.command("feed"))
async def feedd(client, message):
  await message.reply_video(nekos.img("feed"))

@app.on_message(filters.command("lizard"))
async def lizard(client, message):
  a = await message.reply_text(f"🦎")
  await asyncio.sleep(0.7)
  await message.reply_photo(nekos.img("lizard"))
  await a.delete()
  
@app.on_message(filters.command("pat"))
async def feedd(client, message):
  await message.reply_photo(nekos.img("pat"))



@app.on_message(filters.command("kiss"))
async def kisss(client, message):
    try:
        if message.reply_to_message:
            await message.reply_video(nekos.img("kiss"), caption=f"{message.from_user.mention} kissed {message.reply_to_message.from_user.mention}")
        else:
            await message.reply_video(nekos.img("kiss"))
    except Exception as e:
        await message.reply_text(f"Error: {e}")


@app.on_message(filters.command("hug"))
async def kisss(client, message):
    try:
        if message.reply_to_message:
            await message.reply_video(nekos.img("hug"), caption=f"{message.from_user.mention} hugged {message.reply_to_message.from_user.mention}")
        else:
            await message.reply_video(nekos.img("hug"))
    except Exception as e:
        await message.reply_text(f"Error: {e}")
                                      
