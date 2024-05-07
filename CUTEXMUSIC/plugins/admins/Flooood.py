import time
import requests
from traceback import format_exc
from pyrogram import filters, client, enums
import nekos
from CUTEXMUSIC.misc import SUDOERS
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ChatType
from pyrogram.errors import RPCError, UserAdminInvalid
from pyrogram.types import (CallbackQuery, ChatPermissions,
                            InlineKeyboardButton, InlineKeyboardMarkup,
                            Message)
from CUTEXMUSIC import app 
from CUTEXMUSIC.utils.database.flood_db import Floods
import config 



on_key = ["on", "start", "disable"]
off_key = ["off", "end", "enable", "stop"]



within_kb = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "5",
                callback_data="f_f_5"
            ),
            InlineKeyboardButton(
                "10",
                callback_data="f_f_10"
            ),
            InlineKeyboardButton(
                "15",
                callback_data="f_f_15"
            )
        ],
        [
            InlineKeyboardButton(
                "Skip",
                callback_data="f_f_skip"
            )
        ]
    ]
)

limit_kb = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "5",
                callback_data="f_5"
            ),
            InlineKeyboardButton(
                "10",
                callback_data="f_10"
            ),
            InlineKeyboardButton(
                "15",
                callback_data="f_15"
            )
        ],
        [
            InlineKeyboardButton(
                "Skip",
                callback_data="f_f_f_skip"
            )
        ]
    ]
)

@app.on_message(filters.command(["floodaction","actionflood"]))
async def flood_action(cute: app, m: Message):
    Flood = Floods()
    admin_id = m.from_user.id
    chat = m.chat
    if m.chat.type == ChatType.PRIVATE:
        await m.reply_text("Use this command in group")
        return
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
      pass
    else:
      await m.reply_text("you are not an admin ")
      return 
        
    c_id = m.chat.id
    is_flood = await Flood.is_chat(c_id)
    if is_flood:
        saction = is_flood[2]
        await m.reply_text(
            f"Choose a action given bellow to do when flood happens.\n **CURRENT ACTION** is {saction}",
            reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Mute 🔇",
                callback_data="f_mute"
            ),
            InlineKeyboardButton(
                "Ban 🚷",
                callback_data="f_ban"
            ),
            InlineKeyboardButton(
                "Kick 🦿",
                callback_data="f_kick"
            )
        ],
        [
            InlineKeyboardButton(
                "➡️ Skip",
                callback_data="f_skip"
            )
        ]
    ]
            )
        )
        return
    await m.reply_text("Switch on the flood protection first.")
    return

@app.on_message(filters.command(["isflood", "flood"]) & ~filters.bot)
async def flood_on_off(cute: app, m: Message):
    if m.chat.type == ChatType.PRIVATE:   
      return await m.reply_text("This command is ment to be used in groups.")
    Flood = Floods()
    c_id = m.chat.id
    is_flood = await Flood.is_chat(c_id)
    c_id = m.chat.id
    if is_flood:
      saction = is_flood[2]
      slimit = is_flood[0]
      swithin = is_flood[1]
      return await m.reply_text(f"Flood is on for this chat\n**Action**: {saction}\n**Messages**: {slimit} within {swithin} sec")
    return await m.reply_text("Flood protection is off for this chat.")

@app.on_message(filters.command(["setflood"]) & ~filters.bot)
async def flood_set(cute: app, m: Message):
    admin_id = m.from_user.id
    chat = m.chat
    member = await chat.get_member(admin_id)
    Flood = Floods()
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        pass
    else:
        await m.reply_text("You are not an admin.")
        return

    if m.chat.type == ChatType.PRIVATE:
        return await m.reply_text("This command is meant to be used in groups.")

    split = m.text.split(None, 1)
    c_id = m.chat.id
    is_flood = await Flood.is_chat(c_id)

    if len(split) == 1:
        if is_flood: 
            saction = is_flood[2]
            slimit = is_flood[0]
            swithin = is_flood[1]   
            return await m.reply_text(f"Flood is on for this chat\n**Action**:{saction}\n**Messages**:{slimit} within {swithin} sec")
        return await m.reply_text("Flood protection is off for this chat.")

    if len(split) == 2:
        if split[1].lower() in on_key:
            if is_flood:    
                return await m.reply_text(f"Flood is on for this chat\n**Action**:{is_flood[2]}\n**Messages**:{is_flood[0]} within {is_flood[1]} sec")
            await Flood.save_flood(m.chat.id, 5, 5, 'mute')
            await m.reply_text("Flood protection has been started for this group.")
            return
        if split[1].lower() in off_key:
            x = await Flood.rm_flood(c_id)
            if x:
                await m.reply_text("Flood protection has been stopped for this chat")
                return
            await m.reply_text("Failed to stop flood protection")
            return
    await m.reply_text("**Usage:**\n `/setflood on/off`")
    return


@app.on_callback_query(filters.regex("^f_"))
async def callbacks(cute: app, q: CallbackQuery):
    data = q.data
    if data == "f_close":
        await q.answer("Closed")
        await q.message.delete()
        return
    c_id = q.message.chat.id
    Flood = Floods()
    is_flood = await Flood.is_chat(c_id)
    if is_flood:
        saction = is_flood[2]
        slimit = is_flood[0]
        swithin = is_flood[1]
    user = q.from_user.id
    user_status = (await q.message.chat.get_member(q.from_user.id)).status
    if user in SUDOERS or user_status in [enums.ChatMemberStatus.OWNER or enums.ChatMemberStatus.ADMINISTRATOR]:
        if data in ["f_mute", "f_ban", "f_kick", "f_skip"]:
            change = data.split("_")[1]
            if not change == saction:
                await Flood.save_flood(c_id, slimit, swithin, change)
                await q.answer("Updated action", show_alert=True)
                await q.edit_message_text(
                    f"Set the limit of message after the flood protection will be activated\n **CURRENT LIMIT** {slimit} messages",
                    reply_markup=limit_kb
                )
                return
            elif change == "skip":
                await q.answer("Skip", show_alert=True)
                await q.edit_message_text(
                    f"Set the limit of message after the flood protection will be activated\n **CURRENT LIMIT** {slimit} messages",
                    reply_markup=limit_kb
                )
            else:
                await q.answer("Updated action", show_alert=True)
                await q.edit_message_text(
                    f"Set the limit of message after the flood protection will be activated\n **CURRENT LIMIT** {slimit} messages",
                    reply_markup=limit_kb
                )
        elif data in ["f_5", "f_10", "f_15", "f_f_f_skip"]:
            try:
                change = int(data.split("_")[-1])
            except ValueError:
                await q.answer("skip")
                await q.edit_message_text(
                    f"Set the time with the number of message recived treated as flood\n **CUURENT TIME** {swithin}",
                    reply_markup=within_kb
                )
                return
            if not change == slimit:
                await Flood.save_flood(c_id, change, swithin, saction)
                await q.answer("Updated limit", show_alert=True)
                await q.edit_message_text(
                    f"Set the time with the number of message recived treated as flood\n **CUURENT TIME** {swithin}",
                    reply_markup=within_kb
                )
                return
            else:
                await q.answer("Updated action", show_alert=True)
                await q.edit_message_text(
                    f"Set the time with the number of message recived treated as flood\n **CUURENT TIME** {swithin}",
                    reply_markup=within_kb
                )
                return
        elif data in ["f_f_5", "f_f_10", "f_f_15", "f_f_skip"]:
            data = data.split("_")[-1]
            try:
                change = int(data)
            except ValueError:
                await q.edit_message_text(
                    "Flood protection setting has been updated",
                    reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Close ❌",
                callback_data="f_close"
            )
        ]
    ]
                    )
                )
                return
                await q.answer("skip")
            if not change == swithin:
                await Flood.save_flood(c_id, slimit, change, saction)
                await q.answer("Updated", show_alert=True)
                await q.edit_message_text(
                    "Flood protection setting has been updated",
                    reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Close ❌",
                callback_data="f_close"
            )
        ]
    ]
                    )
                )
                
                return
            else:
                await q.answer("Updated action", show_alert=True)
                await q.edit_message_text(
                    f"Set the limit of message after the flood protection will be activated\n **CURRENT LIMIT** {slimit} messages",
                    reply_markup=limit_kb
                )
    else:
        await q.answer(
            "You don't have enough permission to do this!\nStay in your limits!",
            show_alert=True,
            )
        return

@app.on_callback_query(filters.regex("^un_"))
async def reverse_callbacks(c: app, q: CallbackQuery):
    data = q.data.split("=")  # Split by '=' to get user_id
    action = data[0].split("_")[1]  # Extract the action from the callback data
    user_id = int(data[1])  # Corrected index to get user_id
    if not q.from_user:
        return await q.answer("Looks like you are not a user 👀")

    if action == "ban":
        user = await q.message.chat.get_member(q.from_user.id)
        if user.status not in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
            return await q.answer("You don't have enough permission to do this!\nStay in your limits!", show_alert=True)
        try:
            await q.message.chat.unban_member(user_id)
            user_info = await c.get_users(user_id)
            admin_info = await c.get_users(q.from_user.id)
            await q.message.edit_text(f"{admin_info.mention} unbanned {user_info.mention}!")
        except RPCError as e:
            await q.message.edit_text(f"Error: {e}")
            return
    elif action == "mute":
        user = await q.message.chat.get_member(q.from_user.id)
        if user.status not in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
            return await q.answer("You don't have enough permission to do this!\nStay in your limits!", show_alert=True)
        try:
            await q.message.chat.restrict_member(user_id, ChatPermissions())
            user_info = await c.get_users(user_id)
            admin_info = await c.get_users(q.from_user.id)
            await q.message.edit_text(f"{admin_info.mention} unmuted {user_info.mention}!")
        except RPCError as e:
            await q.message.edit_text(f"Error: {e}")
            return


dic = {}
@app.on_message(filters.all & ~filters.bot | ~filters.private, 10)
async def flood_watcher(cute: app, m: Message):
    c_id = m.chat.id
    
    if not m.chat:
        return
    
    Flood = Floods()
    
    try:
        u_id = m.from_user.id
    except AttributeError:
        return # Get this error when the message received is not by an user and return
    
    is_flood = await Flood.is_chat(c_id)
    
    if not is_flood:
        return 

    if u_id == 6844821478:
        return
        
    
    if not is_flood or u_id in SUDOERS:
        return #return if the user is in support_staff
    
    try:
        user_status = (await m.chat.get_member(m.from_user.id)).status
    except Exception:
        return
    
    if user_status in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
        return #return if the user is owner or admin
    
    action = is_flood[2]
    limit = int(is_flood[0])
    within = int(is_flood[1])
    
    if not len(dic):
        z = {c_id : {u_id : [[],[]]}}
        dic.update(z)
    
    try:
      dic[c_id] # access and check weather the c_id present or not
    except KeyError:
      z = {c_id : {u_id : [[],[]]}}
      dic.update(z)

    try:
      dic[c_id][u_id]
    except KeyError:
      z = {u_id : [[],[]]}
      dic[c_id].update(z) # make the dic something like {c_id : {u_id : [[for time],[for msg]]}}
    
    sec = round(time.time())
    
    try:
        dic[c_id][u_id][0].append(sec)
        dic[c_id][u_id][1].append("x")
    except KeyError:
        dic[c_id].update({u_id : [[sec], ["x"]]})
    
    x = int(dic[c_id][u_id][0][0])
    y = int(dic[c_id][u_id][0][-1])
    
    if len(dic[c_id][u_id][1]) == limit:
        if y-x <= within:
            if action == "ban":
                try:
                    await m.chat.ban_member(u_id)
                    keyboard = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Unban",
                                    callback_data=f"un_ban_={u_id}",
                                ),
                            ],
                        ],
                    )
                    txt = "Don't dare to spam here if I am around! Nothing can escape my 6 eyes\nAction: Baned\nReason: Spaming"
                    await m.reply_photo(
                        photo=nekos.img("neko"),
                        caption=txt,
                        reply_markup=keyboard,
                    )
                    dic[c_id][u_id][1].clear()
                    dic[c_id][u_id][0].clear()
                    return

                except UserAdminInvalid:
                    await m.reply_text(
                        "I can't protect this chat from this user",
                        )
                    dic[c_id][u_id][1].clear()
                    dic[c_id][u_id][0].clear()
                    return
                except RPCError as ef:
                    await m.reply_text(
                        text=f"""Some error occured, report it using 

                        <b>Error:</b> <code>{ef}</code>"""
                        )
                    LOGGER.error(ef)
                    LOGGER.error(format_exc())
                    dic[c_id][u_id][1].clear()
                    dic[c_id][u_id][0].clear()
                    return
                
            elif action == "kick":
                try:
                    await m.chat.ban_member(u_id)
                    txt = "Don't dare to spam here if I am around! Nothing can escape my 6 eyes\nAction: kicked\nReason: Spaming"
                    await m.reply_photo(
                        photo=nekos.img("neko"),
                        caption=txt,
                    )
                    await m.chat.unban_member(u_id)
                    dic[c_id][u_id][1].clear()
                    dic[c_id][u_id][0].clear()
                    return
                except UserAdminInvalid:
                    await m.reply_text(
                        "I can't protect this chat from this user",
                    )
                    dic[c_id][u_id][1].clear()
                    dic[c_id][u_id][0].clear()
                    return
                except RPCError as ef:
                    await m.reply_text(
                        text=f"""Some error occured, report it using `/bug`

                        <b>Error:</b> <code>{ef}</code>"""
                    )
                    LOGGER.error(ef)
                    LOGGER.error(format_exc())
                    dic[c_id][u_id][1].clear()
                    dic[c_id][u_id][0].clear()
                    return
            elif action == "mute":
                try:
                    await m.chat.restrict_member(
                        u_id,
                        ChatPermissions(),
                    )
                    keyboard = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Unmute",
                                    callback_data=f"un_mute_={u_id}",
                                ),
                            ],
                        ],
                    )
                    txt = "Don't dare to spam here if I am around! Nothing can escape my 6 eyes\nAction: Muted\nReason: Spaming"
                    await m.reply_photo(
                        photo=nekos.img("neko"),
                        caption=txt,
                        reply_markup=keyboard,
                    )
                    dic[c_id][u_id][1].clear()
                    dic[c_id][u_id][0].clear()
                    return
                except UserAdminInvalid:
                    await m.reply_text(
                        "I can't protect this chat from this user",
                    )
                    dic[c_id][u_id][1].clear()
                    dic[c_id][u_id][0].clear()
                    return
                except RPCError as ef:
                    await m.reply_text(
                        text=f"""Some error occured

                        <b>Error:</b> <code>{ef}</code>"""
                    )
                    LOGGER.error(ef)
                    LOGGER.error(format_exc())
                    dic[c_id][u_id][1].clear()
                    dic[c_id][u_id][0].clear()
                    return
    elif y-x > within:
      try:
        dic[c_id][u_id][1].clear()
        dic[c_id][u_id][0].clear()
        return
      except Exception:
        pass
    else:
        return



