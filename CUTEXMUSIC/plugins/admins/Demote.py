import random
from pyrogram import filters, enums
from pyrogram.types import *
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)
from CUTEXMUSIC import app
import requests
from config import OWNER_ID, LOG_GROUP_ID

def mention(user, name, mention=True):
    if mention == True:
        link = f"[{name}](tg://openmessage?user_id={user})"
    else:
        link = f"[{name}](https://t.me/{user})"
    return link

async def get_userid_from_username(username):
    try:
        user = await app.get_users(username)
    except:
        return None

    user_obj = [user.id, user.first_name]
    return user_obj


async def demote_user(user_id, first_name, admin_id, admin_name, chat_id, message, time=None):
    if user_id == 6844821478:
        msg_text = "ᴏʜ ᴍʏ ᴅᴏɢ ! "
        return msg_text, False
    try:
        # if owner check
        user_status = await app.get_chat_member(chat_id, user_id)
        if user_status.status == enums.ChatMemberStatus.OWNER:
            msg_text = "ᴍʏ ᴄᴜᴛᴇ ᴍᴀꜱᴛᴇʀ ɪ ᴄᴀɴ'ᴛ ᴅᴇᴍᴏᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ 😁"
            return msg_text, False
        if user_status.status not in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
            msg_text = "ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ 🌋"
            return msg_text, False
        
        await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_video_chats=False,
        ))
    except ChatAdminRequired as e:
        if "[400 CHAT_ADMIN_REQUIRED]" in str(e):
            msg_text = "Tᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ✨."
            return msg_text, False
        else:
            msg_text = "ꜰɪʀꜱᴛ ɢɪᴠᴇ ᴍᴇ ʀɪɢʜᴛꜱ ᴛʜᴇɴ ᴜꜱᴇ ɪᴛ 🥺"
            return msg_text, False
    except BadRequest as e:
        if "[400 USER_CREATOR]" in str(e):
            msg_text = "ᴍʏ ᴄᴜᴛᴇ ᴍᴀꜱᴛᴇʀ ɪ ᴄᴀɴ'ᴛ ᴅᴇᴍᴏᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ 😠"
            return msg_text, False
        else:
            await message.reply_text(f"Oh An Error Occurred Please Report it at support chat \n\n Error Type: {e} ")

    url = "https://api.waifu.pics/sfw/dance"
    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)

    button = [
       [
           InlineKeyboardButton(
               text="• ᴅᴇʟᴇᴛᴇ •",
               callback_data=f"close",
           ),
        ]
    ]
    response = requests.get(url).json()
    pimg = response['url']
    await app.send_message(LOG_GROUP_ID, f"{user_mention} ᴅᴇᴍᴏᴛᴇ Bʏ {admin_mention} in {message.chat.title}")
    promoteee = await message.reply_video(
        video=pimg,
        caption=f"<u>{message.chat.title} ᴅᴇᴍᴏᴛᴇ Eᴠᴇɴᴛ🚫</u> \n\n ɴᴀᴍᴇ - {user_mention}\n ᴅᴇᴍᴏᴛᴇ Bʏ - {admin_mention}\n",
        reply_markup=InlineKeyboardMarkup(button)
    )

    return promoteee, True



@app.on_message(filters.command(["Demote"]))
async def cutexdemotes(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_promote_members:
            pass
        else:
            msg_text = "ᴍʏ ᴄᴜᴛᴇ ᴍᴀꜱᴛᴇʀ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴅᴇᴍᴏᴛᴇ ꜱᴏᴍᴇᴏɴᴇ 🇮🇳"
            return await message.reply_text(msg_text)
    else:
        msg_text = "ᴍʏ ᴄᴜᴛᴇ ᴍᴀꜱᴛᴇʀ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴅᴇᴍᴏᴛᴇ ꜱᴏᴍᴇᴏɴᴇ ❣️"
        return await message.reply_text(msg_text)
    
    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            reason = message.text.split(None, 1)[1]
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("ɪ ᴅɪᴅɴ'ᴛ ꜰɪɴᴅ ᴛʜᴀᴛ ᴜꜱᴇʀ 👀")
                user_id = user_obj[0]
                first_name = user_obj[1]
                
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("ᴍʏ ᴄᴜᴛᴇ ᴍᴀꜱᴛᴇʀ ꜱᴘᴇᴄɪꜰʏ ᴀ ᴠᴀʟɪᴅ ᴜꜱᴇʀ ᴏʀ ʀᴇᴘʟʏ ᴡɪᴛʜ ʜᴇʀ ᴍᴇꜱꜱᴀɢᴇ 🥺")
        return

    msg_text, result = await demote_user(user_id, first_name, admin_id, admin_name, chat_id, message)

    if result == False:
        await message.reply_text(msg_text)

