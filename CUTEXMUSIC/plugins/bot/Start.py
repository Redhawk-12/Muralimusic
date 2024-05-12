import asyncio
import random
import requests 
from pyrogram import filters
from pyrogram import enums, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from pyrogram.enums import *
from config import BOT_USERNAME
from strings import get_command, get_string
from CUTEXMUSIC import Telegram, YouTube, app
from CUTEXMUSIC.misc import SUDOERS
from CUTEXMUSIC.plugins.play.playlist import del_plist_msg
from CUTEXMUSIC.plugins.Sudo.sudoers import sudoers_list
from CUTEXMUSIC.utils.database import (
    add_served_chat,
    is_served_user,
    add_served_user,
    blacklisted_chats,
    get_assistant,
    get_lang,
    get_userss,
    is_on_off,
    is_served_private_chat,
)
from nekos import img
from CUTEXMUSIC.utils.decorators.language import LanguageStart
from CUTEXMUSIC.utils.inline import help_pannel, private_panel, start_pannel
from CUTEXMUSIC.utils.inline.start import START_BUT


loop = asyncio.get_running_loop()


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🎋",
    "✨",
    "🦹",
    "🌺",
    "🍀",
    "💞",
    "🎁",
    "💌",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
    "🍭",
    "🐻",
    "🦄",
    "🐼",
    "🐰",
    "🌸",
    "🌈",
    "🌟",
    "🌼",
    "🐱",
    "🐶",
    "🐨",
    "🐥",
    "🎮",
    "🎵",
    "📚",
    "🎨",
    "☕",
    "🍕",
    "🍦",
    "🍰",
    "🎈",
    "🎉",
    "🐤",
    "🍬",
]


STICKER = [
"CAACAgUAAx0CfAEyWgAClxdl9Gg4N-HyCImjGFXOQSHz50MD9wACzgoAAgrrYVWxPZWXGNr8SjQE",
"CAACAgUAAx0CfAEyWgAClx1l9Gh9PHZKDIw8qbacmxzRD1QNAAOcDQAC0YVxVQijiuf_CF8_NAQ",
"CAACAgUAAx0CfAEyWgAClyJl9Giplzk45LHa3SWbl30VQud5sgACJAgAAkemgVWsjZK8lbezvDQE",
"CAACAgUAAx0CfAEyWgACmzZl-DHnr2MOLOPp34onib6dzUFjZgACQAgAApt6iFXzn_VE52urQDQE",
"CAACAgUAAx0CfAEyWgAClydl9GjEpP5YDBYtPn-g8aC55Mmw_wACyQwAApDeqFbZJHowNnvidjQE",
"CAACAgUAAx0CbEz78AABAQsvZfP2vNspUQkhtlqbZvDVUTvtIeIAApwNAALRhXFVCKOK5_8IXz8eBA",
"CAACAgUAAx0CffjZyQACKoZmInOTHCv5lfpO580Y_UPEeUveYAAClAgAAspLwVT1oL4z_bhK7x4E",
"CAACAgUAAx0CffjZyQACKo5mInRgNfyhH-Y3tKwKyj4_RoKu9gACsgYAAtAF2VYY6HZG8DUiyh4E",
"CAACAgUAAx0CffjZyQACKoVmInNNz2YqgVIOm0b_XNASdarg0QAC9QkAAlTOgFSpIzlJ8dofZR4E",
"CAACAgUAAx0CffjZyQACKohmInOZTlDo3YUTGWNdt1-8QFvrhQACqgwAArC9oFRVcuyU8PCqFR4E",
"CAACAgUAAx0CffjZyQACKopmInPJwawFfy9z96S23cRxc5iI3QACegsAAtFEoVSKNlWkZeVvBh4E",
"CAACAgUAAx0CffjZyQACKodmInOY37YoG7I-Mn9VbHbcE1VkYgACWAcAAmF4oFRci8T1o_XfEh4E",
"CAACAgUAAx0CffjZyQACKotmInP5P_GvgKU67nB3ZXDU5UHdwQACBAkAAmGTqFTyMEUMwHr2WB4E",
"CAACAgUAAx0CfAEyWgAClyxl9GkdhdvG8gmelpuDDXW43GdyYgACDAkAAgYmmVWwda82o5ssVx4E",
"CAACAgUAAx0CffjZyQACKoZmInOTHCv5lfpO580Y_UPEeUveYAAClAgAAspLwVT1oL4z_bhK7x4E",
"CAACAgQAAx0CfAEyWgACly9l9GoPSnyCro7QrrIPDIMl0VJNvAACKAwAArq5EFDBJa4kfYMtSB4E",
"CAACAgUAAx0CfAEyWgAClzJl9Gphz8y2LOZXS_g4SBfUPQwAAeIAAs0EAAISTXlWi28Xpyv5nuUeBA",
]

CUTE_PICS = [
"https://telegra.ph/file/018d6002a0ad3aee739f4.jpg",
"https://telegra.ph/file/9d1b413d24ef703e931e3.jpg",
"https://telegra.ph/file/035f1b9835c47f45952f7.jpg",
"https://telegra.ph/file/ca93aeef2e7b45918b668.jpg",
"https://telegra.ph/file/be64889b9a092f05bb51e.jpg",
"https://telegra.ph/file/b75e6977d0fa2d5d78b0f.jpg",
"https://telegra.ph/file/7a07ef4fd40ad2eb20c35.jpg",
"https://telegra.ph/file/cc7adb01901d0e3d2ed3c.jpg",
"https://telegra.ph/file/38e76bbfb4666757186f1.jpg",
"https://telegra.ph/file/602b29a89fca3129194be.jpg",
"https://telegra.ph/file/71d6213be9255750453a6.jpg",
"https://telegra.ph/file/7576d27e926a634add7f4.jpg",
"https://telegra.ph/file/c15485da3d83eb47ad0ff.jpg",
"https://telegra.ph/file/2c46895723d637de84918.jpg",
"https://telegra.ph/file/148858c4837e90c9cae49.jpg",
"https://telegra.ph/file/aa5556e11d949e5f095c5.jpg",
"https://telegra.ph/file/dd4479290dc8aecd5ed26.jpg",
"https://telegra.ph/file/7226a80d33f1d9e9051a4.jpg",
"https://telegra.ph/file/903078ebee2327f8a433c.jpg",
"https://telegra.ph/file/f5e17db4530f3afb7df29.jpg",
"https://telegra.ph/file/d104ea00a4f5d5a2bd6bd.jpg",
"https://telegra.ph/file/e30c70f101f19dac328c6.jpg",
"https://telegra.ph/file/9dbab97d92fefb83ffb83.jpg",
"https://telegra.ph/file/574377193d0ac413757a4.jpg",
"https://telegra.ph/file/704ef3c97af1163689206.jpg",
"https://telegra.ph/file/18bb7adf017c4566f17bf.jpg",
"https://telegra.ph/file/eeb95340c7f1b6548f4e2.jpg",
"https://telegra.ph/file/b6c7cee4bb3767c59ab54.jpg",
"https://telegra.ph/file/e8d502afc144e77d81c48.jpg",
]

@app.on_message(
    filters.command(get_command("START_COMMAND")) & filters.private & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_text(_["help_1"], reply_markup=keyboard)
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                "🥱 ɢᴇᴛᴛɪɴɢ ʏᴏᴜʀ ᴩᴇʀsᴏɴᴀʟ sᴛᴀᴛs ғʀᴏᴍ {config.MUSIC_BOT_NAME} sᴇʀᴠᴇʀ."
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ](https://t.me/ZeroXCoderZChat) ** ᴩʟᴀʏᴇᴅ {count} ᴛɪᴍᴇs**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(None, get_stats)
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <code>sᴜᴅᴏʟɪsᴛ</code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ʟʏʀɪᴄs.")
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
😲**ᴛʀᴀᴄᴋ ɪɴғᴏʀɴᴀᴛɪᴏɴ**😲

📌**ᴛɪᴛʟᴇ:** {title}

⏳**ᴅᴜʀᴀᴛɪᴏɴ:** {duration} ᴍɪɴᴜᴛᴇs
👀**ᴠɪᴇᴡs:** `{views}`
⏰**ᴩᴜʙʟɪsʜᴇᴅ ᴏɴ:** {published}
🎥**ᴄʜᴀɴɴᴇʟ:** {channel}
📎**ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ:** [ᴠɪsɪᴛ ᴄʜᴀɴɴᴇʟ]({channellink})
🔗**ʟɪɴᴋ:** [ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})

💖 sᴇᴀʀᴄʜ ᴩᴏᴡᴇʀᴇᴅ ʙʏ {config.MUSIC_BOT_NAME}"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                text="Sᴜᴍᴍᴏɴ ᴍᴇ ✨",     url=f"https://t.me/CutieXmusicBot?startgroup=new",
                  ),
                    ],
                    [
                        InlineKeyboardButton(text="• ʏᴏᴜᴛᴜʙᴇ •", url=f"{link}"),
                        InlineKeyboardButton(text="〆 ᴄʟᴏsᴇ 〆 ", callback_data="close"),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode=enums.ParseMode.MARKDOWN,
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <code>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = f"tg://openmessage?user_id=6844821478"

        out = private_panel(_, BOT_USERNAME, OWNER)
        response = requests.get("https://nekos.best/api/v2/neko").json()
        image_url = response["results"][0]["url"]
        startmsg = await message.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(0.1)
        b = await message.reply_text(f" Hᴇʟʟᴏ {message.from_user.mention}")
        c = await message.reply_text(f"ᴍʏ ɴᴀᴍᴇ ɪs {app.mention} ")
        await b.delete()
        d = await message.reply_text(f"ᴍᴀᴅᴇ ʙʏ 𝑴𝑼𝑹𝜦𝑳𝛪...")
        await c.delete()
        await d.delete()
        Ahh = await message.reply_text(text=random.choice(EMOJIOS))
        await asyncio.sleep(0.1)
        await Ahh.delete()
        jj = await message.reply_sticker(random.choice(STICKER))
        await asyncio.sleep(0.04)
        await jj.delete()
        let = await message.reply_text("ʟᴇᴛ ᴍᴇ sᴛᴀʀᴛ")
        await asyncio.sleep(0.002)
        await startmsg.delete()
        await let.edit("ʟᴇᴛ ᴍᴇ sᴛᴀʀᴛ....")
        STT = await message.reply_sticker(random.choice(STICKER))
        fff = await message.reply_sticker(random.choice(STICKER))
        await STT.delete()
        await asyncio.sleep(0.007)
        await let.delete()
        Hlo = await message.reply_sticker(random.choice(STICKER))
        Rrr = await message.reply_sticker(random.choice(STICKER))
        await asyncio.sleep(0.02)
        await Hlo.delete()
        await message.reply_photo(
                    photo=image_url,
                    caption=_["start_2"].format(message.from_user.mention, app.mention),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        await Rrr.delete()
        await fff.delete()
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.username
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** @{sender_name}",
            )


@app.on_message(
    filters.command(get_command("START_COMMAND")) & filters.group & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    out = start_pannel(_)
    return await message.reply_text(
        _["start_1"].format(message.chat.title, config.MUSIC_BOT_NAME),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**ᴩʀɪᴠᴀᴛᴇ ᴍᴜsɪᴄ ʙᴏᴛ**\n\nᴏɴʟʏ ғᴏʀ ᴛʜᴇ ᴄʜᴀᴛs ᴀᴜᴛʜᴏʀɪsᴇᴅ ʙʏ ᴍʏ ᴏᴡɴᴇʀ, ʀᴇǫᴜᴇsᴛ ɪɴ ᴍʏ ᴏᴡɴᴇʀ's ᴩᴍ ᴛᴏ ᴀᴜᴛʜᴏʀɪsᴇ ʏᴏᴜʀ ᴄʜᴀᴛ ᴀɴᴅ ɪғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴡᴀɴᴛ ᴛᴏ ᴅᴏ sᴏ ᴛʜᴇɴ ғᴜ*ᴋ ᴏғғ ʙᴇᴄᴀᴜsᴇ ɪ'ᴍ ʟᴇᴀᴠɪɴɢ."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != enums.ChatType.SUPERGROUP:
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                await message.reply_text(
                    _["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id == 6844821478:
                await message.reply_text(
                    _["start_4"].format(member.mention)
                )
                await app.promote_chat_member(chat_id, merber.id, privileges=ChatPrivileges(
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
            if member.id in SUDOERS:
                await message.reply_text(
                    _["start_5"].format(member.mention)
                )
                await app.promote_chat_member(chat_id, merber.id, privileges=ChatPrivileges(
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
            return
        except:
            return

