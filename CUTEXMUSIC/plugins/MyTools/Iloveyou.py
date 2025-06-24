from pyrogram import Client, filters
from CUTEXMUSIC import app 
import asyncio
import random
import re

# MADE BY - MURALI-BOTS 

STICKERS = [
"CAACAgUAAx0CfRCYvwACIVBmAAEK5xfOsbAKwRLnE1aP6mLVwJYAAmIMAALQZylWJYHrI3fMSeceBA",
"CAACAgUAAx0EfRCYvwACIWBmAAELpZyrhFxDt2e5jRFE6h64gWEAAisNAAIdy2BWsURsfjszemceBA",
"CAACAgEAAx0CfRCYvwACIWZmAAEOP5kD-y8AAZnYWdKwYCC9XptAAAK_AwACbk1BR8zW1v4rtxNgHgQ",
"CAACAgUAAx0CfRCYvwACIWlmAAEOZCaVd3n6mFnNxq4Zl_IttxMAAkMNAAJR6hlXgMC_JLF6vqMeBA",
"CAACAgUAAx0CfRCYvwACIWxmAAEOhS8sw5tx92k3QIKTZ1i0IDIAAoEGAAKBttFXzTHb7JwBiuUeBA",
"CAACAgUAAx0CfRCYvwACIW5mAAEOicSAShNNgVJUCnbMTyIPNHAAAhQGAAJN-9FXu1E-Iq9qrbceBA"
"CAACAgUAAx0CfRCYvwACIW1mAAEOhknSqm3Dc1IT1lCjh-JnHK4AAowGAAIky8lXi7X6Vd5XduEeBA"
]

@app.on_message(filters.text & filters.regex(r'^I love you$', flags=re.IGNORECASE))
async def reply_to_love_you(client, message):
    A = await message.reply_sticker("CAACAgEAAx0CfRCYvwACG1xl_t41Ncb8rG0p89bTP6maqzP9oQACAwMAAhReeUTTVv1oa77jZh4E")
    await asyncio.sleep(0.1)
    B = await message.reply_text(f"❤️")
    await asyncio.sleep(0.3)
    await A.delete()
    await B.edit(f"hey {message.from_user.mention} \n\n I love you too Baby")
    await asyncio.sleep(0.2)
    Zz = await message.reply_sticker("CAACAgUAAx0CfRCYvwACIrxmAAFogz1Jw0LRwmSrp0J0Lu5B7U8AAm0KAALhnGhWzoDsWIAGsWMeBA")
    await asyncio.sleep(0.2)
    ZZZ = await message.reply_sticker("CAACAgUAAx0CfRCYvwACIr1mAAFot2Rn832U1yqBXQMm7SRDevAAAg8LAAKLQ2hWkgxtXTRlh-8eBA")
    await Zz.delete()
    await asyncio.sleep(0.2)
    ccc = await message.reply_sticker("CAACAgUAAx0CfRCYvwACIr5mAAFovCRMrggdMb54wyBlpGzyaTwAAigLAAKvDGBWhi8pQl1m6-YeBA")
    await asyncio.sleep(0.2)
    await ZZZ.delete()
    E = await message.reply_sticker("CAACAgUAAx0CfRCYvwACHvZl_uQTCBstNPh4e_ZZvRNxnRS_eQACKw0AAh3LYFaxRGx-OzN6Zx4E")
    await asyncio.sleep(0.2)
    await E.delete()
    await B.edit(f"{message.from_user.mention} I Love You Soo Much Baby ")
    await asyncio.sleep(0.2)
    x = await message.reply_sticker("CAACAgUAAx0CfRCYvwACIWFmAAEMvLYcRtZa4gwjm5DiX3FlSfQAAqoHAAKKSthU375Zyf-y_BYeBA")
    await asyncio.sleep(0.1)
    await ccc.delete()
    lol = await message.reply_sticker(sticker=random.choice(STICKERS))
    await x.delete()
    await asyncio.sleep(0.1)
    z = await message.reply_sticker("CAACAgUAAx0CfRCYvwACIrtmAAFobzXv4q50EREaglzAuqF14UEAAjQOAAIcQmhWRE-82MpUtooeBA")
    await message.delete()
    await asyncio.sleep(0.1)
    await z.delete()
    await B.delete()
    await asyncio.sleep(0.2)
    await lol.delete()
    await message.reply_text(f" {message.from_user.mention} 𝙄 𝙇𝙊𝙑𝙀 𝙔𝙊𝙐 𝙏𝙊𝙊 𝘽𝘼𝘽𝙔 😍❤️‍🩹 ")
    await message.delete()
  
