from pyrogram import Client, filters
from CUTEXMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="ᴄʟᴏꜱᴇ",
                callback_data="close",
            )
        ]
    ]
)

# vc on
@app.on_message(filters.video_chat_started)
async def VCSTART(_, message):
    await message.reply_text("**😍 νσιςε ςнɑт нɑѕ ѕтɑятε∂ 😽 **", reply_markup=BUTTON)

# vc off
@app.on_message(filters.video_chat_ended)
async def VCEND(_, message):
    await message.reply_text("**🥲 νσιςε ςнɑт нɑѕ εи∂ε∂ 💔**", reply_markup=BUTTON)

# invite members on vc
@app.on_message(filters.video_chat_members_invited)
async def vvcinvite(_, message):
    if message.from_user:
        text = f"{message.from_user.mention} ɪɴᴠɪᴛᴇᴅ "
        x = 0
        for user in message.video_chat_members_invited.users:
            try:
                text += f"[{user.first_name}](tg://user?id={user.id}) "
                x += 1
            except Exception:
                pass
        try:
            await message.reply(f"{text} 💞", reply_markup=BUTTON)
        except:
            pass
               
