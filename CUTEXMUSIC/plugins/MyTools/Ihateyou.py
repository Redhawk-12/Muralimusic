from pyrogram import Client, filters
from CUTEXMUSIC import app 
import asyncio
import random
import re

# MADE BY - MURALI-BOTS 

STICKERS = [
"CAACAgUAAxkBAAEMNTBmVJEXmduquwcLrHjRLqNLmJlg0wACoxAAAnFoAVd6B8ULiKD8iTUE",
"CAACAgQAAxkBAAEMNTJmVJFna5Dvl4tgnqUmGugaJ17q8QAChAoAAhcOmVKwScr_MavWYjUE",
"CAACAgUAAxkBAAEMNTRmVJGH3QrEDs4au2GbZ1DWdzdLzgACFQcAAq5BIFd0frZYOk3W2jUE",
"CAACAgUAAxkBAAEMNTZmVJGkjJ_EC3IovqqmKRKKT0U7iwAC-wUAAt_piFR_eTfPi25S8zUE",
"CAACAgUAAxkBAAEMNTxmVJHRIx68paAjiCmIfoqy8BGbwQACRAYAAlcTWFc2CnG1RGg1VjUE",
"CAACAgIAAxkBAAEMNTpmVJHIAu4BJ56DqvdFnzTiyZSWxgAC3xkAAn9qgEhKd15t6hdRzDUE"
"CAACAgQAAxkBAAEMNThmVJG-dRGTkPUTYQOChO5mDNPD-QACzRIAAsjMyVCnolYbjU-orjUE"
]

@app.on_message(filters.text & filters.regex(r'^I hate you$', flags=re.IGNORECASE))
async def reply_to_love_you(client, message):
    A = await message.reply_sticker("CAACAgUAAxkBAAEMNTBmVJEXmduquwcLrHjRLqNLmJlg0wACoxAAAnFoAVd6B8ULiKD8iTUE")
    await asyncio.sleep(0.1)
    B = await message.reply_text(f"💔")
    await asyncio.sleep(0.3)
    await A.delete()
    await B.edit(f"hey {message.from_user.mention} \n\n 𝙄 𝙃𝘼𝙏𝙀 𝙔𝙊𝙐 𝙏𝙊𝙊 😔🥺")
    await asyncio.sleep(0.2)
    Zz = await message.reply_sticker("CAACAgQAAxkBAAEMNTJmVJFna5Dvl4tgnqUmGugaJ17q8QAChAoAAhcOmVKwScr_MavWYjUE")
    await asyncio.sleep(0.2)
    ZZZ = await message.reply_sticker("CAACAgUAAxkBAAEMNTRmVJGH3QrEDs4au2GbZ1DWdzdLzgACFQcAAq5BIFd0frZYOk3W2jUE")
    await Zz.delete()
    await asyncio.sleep(0.2)
    ccc = await message.reply_sticker("CAACAgQAAxkBAAEMNThmVJG-dRGTkPUTYQOChO5mDNPD-QACzRIAAsjMyVCnolYbjU-orjUE")
    await asyncio.sleep(0.2)
    await ZZZ.delete()
    E = await message.reply_sticker("CAACAgUAAxkBAAEMNTZmVJGkjJ_EC3IovqqmKRKKT0U7iwAC-wUAAt_piFR_eTfPi25S8zUE")
    await asyncio.sleep(0.2)
    await E.delete()
    await B.edit(f"{message.from_user.mention} 𝙄 𝙃𝘼𝙏𝙀 𝙔𝙊𝙐 𝙎𝙊𝙊 𝙈𝙐𝘾𝙃 🧸💔🥺 ")
    await asyncio.sleep(0.2)
    x = await message.reply_sticker("CAACAgIAAxkBAAEMNTpmVJHIAu4BJ56DqvdFnzTiyZSWxgAC3xkAAn9qgEhKd15t6hdRzDUE")
    await asyncio.sleep(0.1)
    await ccc.delete()
    lol = await message.reply_sticker(sticker=random.choice(STICKERS))
    await x.delete()
    await asyncio.sleep(0.1)
    z = await message.reply_sticker("CAACAgUAAxkBAAEMNTxmVJHRIx68paAjiCmIfoqy8BGbwQACRAYAAlcTWFc2CnG1RGg1VjUE")
    await message.delete()
    await asyncio.sleep(0.1)
    await z.delete()
    await B.delete()
    await asyncio.sleep(0.2)
    await lol.delete()
    await message.reply_text(f" {message.from_user.mention} 𝙄 𝙃𝘼𝙏𝙀 𝙔𝙊𝙐 2 🥺🧸💔 ")
    await message.delete()
  
