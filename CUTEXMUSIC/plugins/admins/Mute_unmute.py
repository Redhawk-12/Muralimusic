import random
from pyrogram import filters, enums
from pyrogram.types import *
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)
from CUTEXMUSIC import app
from config import *
from pyrogram.errors import RPCError

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



async def mute_user(user_id, first_name, admin_id, admin_name, chat_id, message, time=None):
    if user_id == 6844821478:
        msg_text = "ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ᴍʏ ᴏᴡɴᴇʀ"
        return msg_text, False
    try:
        member = await app.get_chat_member(chat_id, user_id)
        if member.status == enums.ChatMemberStatus.RESTRICTED:
            return "ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴍᴜᴛᴇᴅ.", False
    except Exception as e:
        return f"Error occurred while checking user status: {e}", False
    
    try:
        if time:
            mute_end_time = datetime.datetime.now() + time
            await app.restrict_chat_member(chat_id, user_id, ChatPermissions(), mute_end_time)
        else:
            await app.restrict_chat_member(chat_id, user_id, ChatPermissions())
    except ChatAdminRequired:
        msg_text = "ꜰɪʀꜱᴛ ɢɪᴠᴇ ᴍᴇ ᴍᴜᴛᴇ ʀɪɢʜᴛꜱ ᴛʜᴇɴ ᴜꜱᴇ ɪᴛ 😠"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ᴀɴ ᴀᴅᴍɪɴ 🌋"
        return msg_text, False
    except Exception as e:
        msg_text = f"Oops!!\n{e}"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    button = [
        [
            InlineKeyboardButton(
                text="• ᴜɴᴍᴜᴛᴇ •",
                callback_data=f"unmute_={user_id}",
            ),
            InlineKeyboardButton(
                text="• ᴅᴇʟᴇᴛᴇ •",
                callback_data=f"close",
            ),
        ]
    ]
    await app.send_message(LOG_GROUP_ID, f"{user_mention} was muted by {admin_mention} in {message.chat.title}")
    MUTEE = await message.reply_photo(
        photo=random.choice(MUTEIMG),
        caption=f"<u>{message.chat.title} Mᴜᴛᴇ Eᴠᴇɴᴛ 🔇</u>\n\n Nᴀᴍᴇ - {user_mention} \n Mᴜᴛᴇᴅ Bʏ - {admin_mention}",
        reply_markup=InlineKeyboardMarkup(button)
    )

    return MUTEE, True

async def unmute_user(user_id, first_name, admin_id, admin_name, chat_id, message):
    try:
        member = await app.get_chat_member(chat_id, user_id)
        if member.status != enums.ChatMemberStatus.RESTRICTED:
            return "ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ɴᴏᴛ ᴍᴜᴛᴇᴅ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ 🌾.", False
    except Exception as e:
        return f"Error occurred while checking user status: {e}", False

    try:
        await app.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
                can_send_media_messages=True,
                can_send_messages=True,
                can_invite_users=True
            )
        )
    except ChatAdminRequired:
        msg_text = "ꜰɪʀꜱᴛ ɢɪᴠᴇ ᴍᴇ ᴍᴜᴛᴇ ʀɪɢʜᴛꜱ ᴛʜᴇɴ ᴜꜱᴇ ɪᴛ 🥺"
        return msg_text, False
    except Exception as e:
        msg_text = f"Oops!!\n{e}"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    button = [
        [
            InlineKeyboardButton(
                text="• Sᴜᴍᴍᴏɴ ᴍᴇ •",
                url=f"https://t.me/CuteXMusicBot?startgroup=new",
            ),
            InlineKeyboardButton(
                text="• ᴅᴇʟᴇᴛᴇ •",
                callback_data=f"close",
            ),
        ]
    ]
    
    UNMUTEE = await message.reply_photo(
        photo=random.choice(MUTEIMG),
        caption=f"<u>Uɴᴍᴜᴛᴇ Eᴠᴇɴᴛ </u>\n\n Nᴀᴍᴇ - {user_mention} \n Uɴᴍᴜᴛᴇᴅ Bʏ - {admin_mention}",
        reply_markup=InlineKeyboardMarkup(button),
    )
    return UNMUTEE, True

@app.on_message(filters.command(["mute"]))
async def mute_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "ᴍʏ ᴄᴜᴛᴇ ᴍᴀꜱᴛᴇʀ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴍᴜᴛᴇ ꜱᴏᴍᴇᴏɴᴇ 👀"
            return await message.reply_text(msg_text)
    else:
        msg_text = "ᴍʏ ᴄᴜᴛᴇ ᴍᴀꜱᴛᴇʀ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴍᴜᴛᴇ ꜱᴏᴍᴇᴏɴᴇ 🥀"
        return await message.reply_text(msg_text)

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

            try:
                reason = message.text.partition(message.command[1])[2]
            except:
                reason = None

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("Please specify a valid user or reply to that user's message")
        return

    result, success = await mute_user(user_id, first_name, admin_id, admin_name, chat_id, message)
    if not success:
        return await message.reply_text(result)

@app.on_callback_query(filters.regex("^unmute_"))
async def unmutebutton(c: app, q: CallbackQuery):
    splitter = (str(q.data).replace("unmute_", "")).split("=")
    user_id = int(splitter[1])
    user = await q.message.chat.get_member(q.from_user.id)

    if not user:
        await q.answer(
            "You don't have enough permission to do this!\nStay in your limits!",
            show_alert=True,
        )
        return

    if not user.privileges.can_restrict_members and user.id != OWNER_ID:
        await q.answer(
            "You don't have enough permission to do this!\nStay in your limits!",
            show_alert=True,
        )
        return
    
    whoo = await c.get_users(user_id)
    
    try:
        await q.message.chat.unban_member(user_id)
    except RPCError as e:
        await q.message.edit_text(f"Error: {e}")
        return
    
    await q.message.edit_text(f"ᴜɴᴍᴜᴛᴇ ᴇᴠᴇɴᴛ \n\n ɴᴀᴍᴇ - {whoo.mention}! \n Uɴᴍᴜᴛᴇᴅ Bʏ {q.from_user.mention}")
    return

@app.on_message(filters.command(["unmute"]))
async def unmute_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "You don't have permission to unmute someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You don't have permission to unmute someone"
        return await message.reply_text(msg_text)

    if len(message.command) > 1:
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
    else:
        await message.reply_text("Please specify a valid user or reply to that user's message")
        return

    msg_text, success = await unmute_user(user_id, first_name, admin_id, admin_name, chat_id, message)
    if not success:
        return await message.reply_text(msg_text)
