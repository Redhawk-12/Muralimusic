from pyrogram import filters, enums
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)
from config import LOG_GROUP_ID, OWNER_ID
from CUTEXMUSIC import app
from pyrogram.types import *



button = [
       [
            InlineKeyboardButton(
                text="Sᴜᴍᴍᴏɴ ᴍᴇ ✨",     url=f"https://t.me/CuteXMusicBot?startgroup=true",
            ),
           InlineKeyboardButton(
               text="• Dᴇʟᴇᴛᴇ •",
               callback_data=f"close",
           ),
        ]
]

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

async def zkick_user(user_id, first_name, admin_id, admin_name, chat_id, message):
    if user_id == 6844821478:
            msg_text = "Why should I ban myself? Sorry, but I'm not stupid like you"
            return msg_text, False
    try:
        await app.ban_chat_member(chat_id, user_id)
        await app.unban_chat_member(chat_id, user_id)
    except ChatAdminRequired:
        msg_text = "Give Me Ban Rights Then use it 🥺"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I won't ban an admin!!"
        return msg_text, False
    except Exception as e:
        msg_text = f"Oops!!\n{e}"
        return msg_text, False
    
    url = f"https://api.waifu.pics/sfw/kick"
    response = requests.get(url).json()
    up = response['url']
    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    await app.send_message(LOG_GROUP_ID, f"{user_mention} was kicked by {admin_mention} in {message.chat.title}")

    
        
        
    ZYEAHHHH = await message.reply_video(up,
        caption=f"<u>{message.chat.title} Kɪᴄᴋ Eᴠᴇɴᴛ</u>\n\nName - {user_mention}\nKicked by {admin_mention}\n",
        reply_markup=InlineKeyboardMarkup(button)
    )
    return ZYEAHHHH, True



@app.on_message(filters.command("kick"))
async def kickk_user(client, message):
    chat = message.chat
    reply = message.reply_to_message
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "Sᴏʀʀʏ ʙᴜᴛ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ʙᴀɴ sᴏᴍᴇᴏɴᴇ"
            return await message.reply_text(msg_text)
    else:
        msg_text = "Sᴏʀʀʏ ʙᴜᴛ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ʙᴀɴ sᴏᴍᴇᴏɴᴇ"
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

    msg_text, result = await zkick_user(user_id, first_name, admin_id, admin_name, chat_id, message)
    if result == False:
        await message.reply_text(msg_text)

@app.on_message(filters.command("kickme") & filters.group)
async def kickme_command(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chat_id = message.chat.id
    url = f"https://api.waifu.pics/sfw/kick"
    response = requests.get(url).json()
    up = response['url']

    try:
        # kick him
        await app.ban_chat_member(chat_id, user_id)
        # Mention the kicked member in the group
        await message.reply_video(
            up,
            caption=f"Lᴏʟ ! {user_name} ʜᴀs ʙᴇᴇɴ sᴇʟғ ᴋɪᴄᴋᴇᴅ ᴏᴜᴛ ᴏғ ᴛʜɪs ɢʀᴏᴜᴘ 🤣 .",
            reply_markup=InlineKeyboardMarkup(button),
        )
        await app.send_message(LOG_GROUP_ID, f"{user_name} used kickme command from {message.chat.title}")
    except Exception as e:
        # Handle any errors that may occur during the kicking process
        await message.reply_text(f"An error occurred: {str(e)}")
