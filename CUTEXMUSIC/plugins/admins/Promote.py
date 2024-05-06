import random
from pyrogram import filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPermissions
)
from CUTEXMUSIC.utils.database.shalu_ban import admin_filter
from CUTEXMUSIC import LOGGER
from pyrogram.types import *
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)
from logging import getLogger
import random 
import datetime
from CUTEXMUSIC import app, userbot
import requests
from CUTEXMUSIC.misc import SUDOERS
from config import LOG_GROUP_ID
from config import OWNER_ID

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

async def promote_user(user_id, first_name, admin_id, admin_name, chat_id, message, time=None):
    try:
        # if already admin chk
        user_status = await app.get_chat_member(chat_id, user_id)
        if user_status.status == enums.ChatMemberStatus.ADMINISTRATOR or user_status.status == enums.ChatMemberStatus.OWNER:
            msg_text = "User is already an admin."
            return msg_text, False
        
        await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=True,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=True,
                       )
                     ) 
    except ChatAdminRequired:
        msg_text = "Give me promote wala rights"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I wont promote an admin bruh!!"
        return msg_text, False
    except BadRequest as e:
        if "[400 USER_CREATOR]" in str(e):
            msg_text = "User is already an admin."
            return msg_text, False
        else:
            await message.reply_text(f"Oh An Error Occurred Please Report it at support chat \n\n Error Type: {e} ")
            
    url = "https://api.waifu.pics/sfw/happy"
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
    await app.send_message(LOG_GROUP_ID, f"{user_mention} promote Bʏ {admin_mention} in {message.chat.title}")
    promoteee = await message.reply_video(
        video=pimg,
        caption=f"<u>{message.chat.title} promote Eᴠᴇɴᴛ🚫 </u> \n\n ɴᴀᴍᴇ - {user_mention}\n promote Bʏ - {admin_mention}\n",
        reply_markup=InlineKeyboardMarkup(button)
    )

    return promoteee, True



@app.on_message(filters.command(["Promote"]))
async def cutexpromote(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    
  
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_promote_members:
            pass
        else:
            msg_text = "You dont have permission to promote someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to promote someone"
        return await message.reply_text(msg_text)
    
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("I can't find that user")
                user_id = user_obj[0]
                first_name = user_obj[1]
                
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("Please specify a valid user or reply to that user's message")
        return

    msg_text, result = await promote_user(user_id, first_name, admin_id, admin_name, chat_id, message)

    if result == False:
        await message.reply_text(msg_text)




async def lowpromote_user(user_id, first_name, admin_id, admin_name, chat_id, message, time=None):
    try:
        # if already admin chk
        user_status = await app.get_chat_member(chat_id, user_id)
        if user_status.status == enums.ChatMemberStatus.ADMINISTRATOR or user_status.status == enums.ChatMemberStatus.OWNER:
            msg_text = "User is already an admin."
            return msg_text, False
        
        await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                       )
                     ) 
    except ChatAdminRequired:
        msg_text = "Give me promote wala rights"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I wont promote an admin bruh!!"
        return msg_text, False
    except BadRequest as e:
        if "[400 USER_CREATOR]" in str(e):
            msg_text = "User is already an admin."
            return msg_text, False
        else:
            await message.reply_text(f"Oh An Error Occurred Please Report it at support chat \n\n Error Type: {e} ")
            
    url = "https://api.waifu.pics/sfw/happy"
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
    await app.send_message(LOG_GROUP_ID, f"{user_mention} ʟᴏᴡ ᴘʀᴏᴍᴏᴛᴇ  Bʏ {admin_mention} in {message.chat.title}")
    promoteee = await message.reply_video(
        video=pimg,
        caption=f"<u>{message.chat.title} ʟᴏᴡ ᴘʀᴏᴍᴏᴛᴇ  Eᴠᴇɴᴛ🚫 </u> \n\n ɴᴀᴍᴇ - {user_mention}\n ᴘʀᴏᴍᴏᴛᴇ Bʏ - {admin_mention}\n",
        reply_markup=InlineKeyboardMarkup(button)
    )

    return promoteee, True



@app.on_message(filters.command(["lowPromote"]))
async def cutexlowpromote(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    
  
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_promote_members:
            pass
        else:
            msg_text = "You dont have permission to promote someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to promote someone"
        return await message.reply_text(msg_text)
    
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("I can't find that user")
                user_id = user_obj[0]
                first_name = user_obj[1]
                
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("Please specify a valid user or reply to that user's message")
        return

    msg_text, result = await lowpromote_user(user_id, first_name, admin_id, admin_name, chat_id, message)

    if result == False:
        await message.reply_text(msg_text)




async def fullpromote_user(user_id, first_name, admin_id, admin_name, chat_id, message, time=None):
    try:
        # if already admin chk
        user_status = await app.get_chat_member(chat_id, user_id)
        if user_status.status == enums.ChatMemberStatus.ADMINISTRATOR or user_status.status == enums.ChatMemberStatus.OWNER:
            msg_text = "User is already an admin."
            return msg_text, False
        
        await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=True,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                       )
                     ) 
    except ChatAdminRequired:
        msg_text = "Give me promote wala rights"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I wont promote an admin bruh!!"
        return msg_text, False
    except BadRequest as e:
        if "[400 USER_CREATOR]" in str(e):
            msg_text = "User is already an admin."
            return msg_text, False
        else:
            await message.reply_text(f"Oh An Error Occurred Please Report it at support chat \n\n Error Type: {e} ")
            
    url = "https://api.waifu.pics/sfw/happy"
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
    await app.send_message(LOG_GROUP_ID, f"{user_mention} ꜰᴜʟʟ ᴘʀᴏᴍᴏᴛᴇ  Bʏ {admin_mention} in {message.chat.title}")
    promoteee = await message.reply_video(
        video=pimg,
        caption=f"<u>{message.chat.title} ꜰᴜʟʟ ᴘʀᴏᴍᴏᴛᴇ  Eᴠᴇɴᴛ🥀 </u> \n\n ɴᴀᴍᴇ - {user_mention}\n promote Bʏ - {admin_mention}\n",
        reply_markup=InlineKeyboardMarkup(button)
    )

    return promoteee, True



@app.on_message(filters.command(["fullPromote"]))
async def cutexfullpromote(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    
  
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_promote_members:
            pass
        else:
            msg_text = "You dont have permission to promote someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to promote someone"
        return await message.reply_text(msg_text)
    
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("I can't find that user")
                user_id = user_obj[0]
                first_name = user_obj[1]
                
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("Please specify a valid user or reply to that user's message")
        return

    msg_text, result = await fullpromote_user(user_id, first_name, admin_id, admin_name, chat_id, message)

    if result == False:
        await message.reply_text(msg_text)




