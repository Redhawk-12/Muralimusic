import config
import random 
import requests
import nekos
from pyrogram.errors.exceptions.flood_420 import FloodWait
from CUTEXMUSIC.utils.decorators.language import LanguageStart
from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InputMediaVideo,
    InputMediaPhoto,
    InlineKeyboardMarkup,
    Message,
)
from pyrogram import filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPermissions
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)

import datetime
import random 
from logging import getLogger
from CUTEXMUSIC import LOGGER
from config import LOG_GROUP_ID, OWNER_ID, BOT_USERNAME

from pyrogram.types import *
from pyrogram.enums import ChatType
from pyrogram.errors import MessageNotModified
from config import BANNED_USERS, CLEANMODE_DELETE_MINS, MUSIC_BOT_NAME, OWNER_ID
from strings import get_command
from CUTEXMUSIC import app
from config import SUPPORT_GROUP as SUPPORT_CHAT
from pyrogram.enums import ChatType
from CUTEXMUSIC.utils.database import (
    add_nonadmin_chat,
    cleanmode_off,
    cleanmode_on,
    commanddelete_off,
    commanddelete_on,
    get_aud_bit_name,
    get_authuser,
    get_authuser_names,
    get_playmode,
    get_playtype,
    get_vid_bit_name,
    is_cleanmode_on,
    is_commanddelete_on,
    is_nonadmin_chat,
    is_suggestion,
    remove_nonadmin_chat,
    save_audio_bitrate,
    save_video_bitrate,
    set_playmode,
    set_playtype,
    suggestion_off,
    suggestion_on,
)
from CUTEXMUSIC.utils.decorators.admins import ActualAdminCB
from CUTEXMUSIC.utils.decorators.language import language, languageCB
from CUTEXMUSIC.utils.inline.settings import (
    audio_quality_markup,
    auth_users_markup,
    cleanmode_settings_markup,
    playmode_users_markup,
    setting_markup,
    video_quality_markup,
)
from CUTEXMUSIC.utils.inline.start import private_panel
from CUTEXMUSIC.utils.inline.help import twohelp_pannel
from CUTEXMUSIC.utils.inline.help import threehelp_pannel
from CUTEXMUSIC.utils.inline.help import fourhelp_pannel



LOGGER = getLogger(__name__)

VIDEO_URL = [
"https://telegra.ph/file/994be8612ef77a7f58a28.mp4",
"https://telegra.ph/file/192e3530d0825cb34f8e0.mp4",
"https://telegra.ph/file/bbe808e82960f66a32a33.mp4",
"https://telegra.ph/file/60984b88fceb89a2e4c43.mp4",
"https://telegra.ph/file/ef34cfb6939a318b73945.mp4",
"https://telegra.ph/file/3f5602d66591fbd5793ec.mp4",
]

SHALU_PICS = [
"https://telegra.ph/file/4b637281b81d3f637f643.jpg",
"https://telegra.ph/file/02fa944693f8fbcddbdde.jpg",
"https://telegra.ph/file/393d12eb83a47a0499312.jpg",
"https://telegra.ph/file/4899608b9d4efeb30ab3d.jpg",
"https://telegra.ph/file/3992f6c841bbeadad51c2.jpg",
"https://telegra.ph/file/31c70758a9f35665ee769.jpg",
"https://telegra.ph/file/d1a1932b2d0d3085c3e8c.jpg",
"https://telegra.ph/file/cb13f1b053b99afde7b6e.jpg",
"https://telegra.ph/file/21bc78f527468bc17974f.jpg",
"https://telegra.ph/file/4db7502007aeeced8ba6f.jpg",
"https://telegra.ph/file/616dcf138c736cde4e3e6.jpg",
"https://telegra.ph/file/4ba0f55315b322b77ed17.jpg",
"https://telegra.ph/file/c26dafda0eaa0e9eb6535.jpg",
"https://telegra.ph/file/ac895ede3b122f7c34129.jpg",
"https://telegra.ph/file/54e4428eb161f2198e328.jpg",
"https://telegra.ph/file/5084957be8730f10d8e18.jpg",
"https://telegra.ph/file/e1b2272788148fc8f7dba.jpg",
"https://telegra.ph/file/6cd7dde536d6202f03445.jpg",
]

Bhsvid = [
"https://te.legra.ph/file/11b8f5140824cb5f6d5f6.mp4",
"https://telegra.ph/file/1187734cafc2f69e4622c.mp4",
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


### Command
SETTINGS_COMMAND = get_command("SETTINGS_COMMAND")

@app.on_callback_query(filters.regex("source_codeprank"))
async def gib_repo_callback(_, callback_query):
    try:
        await callback_query.edit_message_media(
            media=InputMediaVideo("https://telegra.ph/file/4724cd4ad751b7b94269d.mp4", has_spoiler=True),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data=f"zsettingsback_helper"),
                 InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data=f"close"),
                 ]]
            ),
        )
    except Exception as e:
        print(f"Error sending media: {e}")

##########

@app.on_callback_query(filters.regex("REPOSITORYKA"))
async def gib_repository_callback(_, callback_query):
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://telegra.ph/file/4b64a63d31b4f2e48efa1.mp4", has_spoiler=True),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ʙᴀᴄᴋ",
                        callback_data="repo_backk",
                    ),
                    InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data=f"close"),
                ]
            ]
        )
    )
    
@app.on_callback_query(filters.regex("repo_backk") & ~BANNED_USERS)
@languageCB
async def repoback_back_mcarkup(client, CallbackQuery: CallbackQuery, _):
    buttons = threehelp_pannel(_, True)
    await CallbackQuery.edit_message_media(
        InputMediaPhoto(media=nekos.img("neko"), caption=_["help_1"].format(SUPPORT_CHAT))
    )
    await CallbackQuery.edit_message_reply_markup(reply_markup=buttons)


@app.on_callback_query(filters.regex("zsettingsback_helper") & ~BANNED_USERS)
@languageCB
async def repoback_back_markup(client, CallbackQuery: CallbackQuery, _):
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
            
        
    out = private_panel(_, BOT_USERNAME, OWNER)
    await CallbackQuery.edit_message_media(
        InputMediaPhoto(media=nekos.img("neko"), caption=_["start_2"].format(CallbackQuery.from_user.mention, app.mention))
    )
    
    # Edit the message reply markup
    await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(out))

# pages of help inline

@app.on_callback_query(filters.regex("SECONDPAGE") & ~BANNED_USERS)
@languageCB
async def second_help_panel(client, callback_query: CallbackQuery, _):
    try:
        await callback_query.answer()
    except FloodWait as e:
        # Handle flood wait error when answering the callback query
        await callback_query.message.reply_text(f"Slow down! Please wait {e.x} seconds before trying again.")
        return
    except Exception as e:
        # Handle other exceptions if needed
        print(f"An error occurred: {e}")
        return
    
    try:
        # Attempt to edit the message
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            buttons = twohelp_pannel(_, True)  
            await callback_query.edit_message_text(
                _["help_1"].format(SUPPORT_CHAT),  
                reply_markup=buttons
            )
    except FloodWait as e:
        # Handle flood wait error when editing the message
        await callback_query.message.reply_text(f"Slow down! Please wait {e.x} seconds before trying again.")
    except Exception as e:
        # Handle other exceptions if needed
        print(f"An error occurred while editing the message: {e}")

    
        

@app.on_callback_query(filters.regex("THREEPAGE") & ~BANNED_USERS)
@languageCB
async def thirdhelp_pannel(client, callback_query: CallbackQuery, _):
    try:
        await callback_query.answer()
    except:
        pass
    if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
        buttons = threehelp_pannel(_, True)
        await callback_query.edit_message_text(
                _["help_1"].format(SUPPORT_CHAT),
            reply_markup=buttons
        )
    
# four page 

@app.on_callback_query(filters.regex("FOURPAGE") & ~BANNED_USERS)
@languageCB
async def thirdhelp_pannel(client, callback_query: CallbackQuery, _):
    try:
        await callback_query.answer()
    except:
        pass
    if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
        buttons = fourhelp_pannel(_, True)
        await callback_query.edit_message_text(
                _["help_1"].format(SUPPORT_CHAT),
            reply_markup=buttons
        )
    

@app.on_message(filters.command(SETTINGS_COMMAND) & filters.group & ~BANNED_USERS)
@language
async def settings_mar(client, message: Message, _):
    buttons = setting_markup(_)
    await message.reply_text(
        _["setting_1"].format(message.chat.title, message.chat.id),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("settings_helper") & ~BANNED_USERS)
@languageCB
async def settings_cb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer(_["set_cb_5"])
    except:
        pass
    buttons = setting_markup(_)
    return await CallbackQuery.edit_message_text(
        _["setting_1"].format(
            CallbackQuery.message.chat.title,
            CallbackQuery.message.chat.id,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(
    filters.regex("help_back") & ~BANNED_USERS
)
@languageCB
async def settings_back_markup(
    client, callback_query: CallbackQuery, _
):
    try:
        await app.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = f"tg://openmessage?user_id=6844821478"
        
    out = private_panel(_, BOT_USERNAME, OWNER)
    if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
        await callback_query.edit_message_text(
            _["start_2"].format(callback_query.from_user.mention, app.mention),
        )
        await callback_query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(out)
        )


@app.on_callback_query(
    filters.regex("settingsback_helper") & ~BANNED_USERS
)
@languageCB
async def settings_back_markup(
   Message, client, CallbackQuery: CallbackQuery, _
):
    try:
        await CallbackQuery.answer()
    except Exception as e:
        print(f"An error occurred: {e}")

    if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        buttons = private_panel(_, app.username, OWNER)
        try:
            await CallbackQuery.edit_message_media(
                InputMediaPhoto(media=random.choice(SHALU_PICS),                   caption=_["start_2"].format(message.from_user.mention, app.mention ),
                )
            )
            await CallbackQuery.edit_message_reply_markup(
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        except MessageNotModified:
            pass
        except Exception as e:
            print("An error occurred:", e)
    else:
        buttons = setting_markup(_)
        try:
            await CallbackQuery.edit_message_reply_markup(
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        except MessageNotModified:
            pass







## Audio and Video Quality
async def gen_buttons_aud(_, aud):
    if aud == "STUDIO":
        buttons = audio_quality_markup(_, STUDIO=True)
    elif aud == "HIGH":
        buttons = audio_quality_markup(_, HIGH=True)
    elif aud == "MEDIUM":
        buttons = audio_quality_markup(_, MEDIUM=True)
    elif aud == "LOW":
        buttons = audio_quality_markup(_, LOW=True)
    return buttons


async def gen_buttons_vid(_, aud):
    if aud == "QHD_2K":
        buttons = video_quality_markup(_, QHD_2K=True)
    elif aud == "FHD_1080p":
        buttons = video_quality_markup(_, FHD_1080p=True)
    elif aud == "HD_720p":
        buttons = video_quality_markup(_, HD_720p=True)
    elif aud == "SD_480p":
        buttons = video_quality_markup(_, SD_480p=True)
    elif aud == "SD_360p":
        buttons = video_quality_markup(_, SD_360p=True)
    return buttons


# without admin rights


@app.on_callback_query(
    filters.regex(
        pattern=r"^(SEARCHANSWER|PLAYMODEANSWER|PLAYTYPEANSWER|AUTHANSWER|CMANSWER|COMMANDANSWER|SUGGANSWER|CM|AQ|VQ|PM|AU)$"
    )
    & ~BANNED_USERS
)
@languageCB
async def without_Admin_rights(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "SEARCHANSWER":
        try:
            return await CallbackQuery.answer(_["setting_3"], show_alert=True)
        except:
            return
    if command == "PLAYMODEANSWER":
        try:
            return await CallbackQuery.answer(_["setting_10"], show_alert=True)
        except:
            return
    if command == "PLAYTYPEANSWER":
        try:
            return await CallbackQuery.answer(_["setting_11"], show_alert=True)
        except:
            return
    if command == "AUTHANSWER":
        try:
            return await CallbackQuery.answer(_["setting_4"], show_alert=True)
        except:
            return
    if command == "CMANSWER":
        try:
            return await CallbackQuery.answer(
                _["setting_9"].format(CLEANMODE_DELETE_MINS),
                show_alert=True,
            )
        except:
            return
    if command == "COMMANDANSWER":
        try:
            return await CallbackQuery.answer(_["setting_14"], show_alert=True)
        except:
            return
    if command == "SUGGANSWER":
        try:
            return await CallbackQuery.answer(_["setting_16"], show_alert=True)
        except:
            return
    if command == "CM":
        try:
            await CallbackQuery.answer(_["set_cb_5"], show_alert=True)
        except:
            pass
        sta = None
        cle = None
        if await is_cleanmode_on(CallbackQuery.message.chat.id):
            cle = True
        if await is_commanddelete_on(CallbackQuery.message.chat.id):
            sta = True
        sug = None
        if await is_suggestion(CallbackQuery.message.chat.id):
            sug = True
        buttons = cleanmode_settings_markup(_, status=cle, dels=sta, sug=sug)
    if command == "AQ":
        try:
            await CallbackQuery.answer(_["set_cb_1"], show_alert=True)
        except:
            pass
        aud = await get_aud_bit_name(CallbackQuery.message.chat.id)
        buttons = await gen_buttons_aud(_, aud)
    if command == "VQ":
        try:
            await CallbackQuery.answer(_["set_cb_2"], show_alert=True)
        except:
            pass
        aud = await get_vid_bit_name(CallbackQuery.message.chat.id)
        buttons = await gen_buttons_vid(_, aud)
    if command == "PM":
        try:
            await CallbackQuery.answer(_["set_cb_4"], show_alert=True)
        except:
            pass
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            Group = True
        else:
            Group = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = None
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "AU":
        try:
            await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
        except:
            pass
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            buttons = auth_users_markup(_, True)
        else:
            buttons = auth_users_markup(_)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


# Audio Video Quality


@app.on_callback_query(
    filters.regex(
        pattern=r"^(LOW|MEDIUM|HIGH|STUDIO|SD_360p|SD_480p|HD_720p|FHD_1080p|QHD_2K)$"
    )
    & ~BANNED_USERS
)
@ActualAdminCB
async def aud_vid_cb(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    try:
        await CallbackQuery.answer(_["set_cb_6"], show_alert=True)
    except:
        pass
    if command == "LOW":
        await save_audio_bitrate(CallbackQuery.message.chat.id, "LOW")
        buttons = audio_quality_markup(_, LOW=True)
    if command == "MEDIUM":
        await save_audio_bitrate(CallbackQuery.message.chat.id, "MEDIUM")
        buttons = audio_quality_markup(_, MEDIUM=True)
    if command == "HIGH":
        await save_audio_bitrate(CallbackQuery.message.chat.id, "HIGH")
        buttons = audio_quality_markup(_, HIGH=True)
    if command == "STUDIO":
        await save_audio_bitrate(CallbackQuery.message.chat.id, "STUDIO")
        buttons = audio_quality_markup(_, STUDIO=True)
    if command == "SD_360p":
        await save_video_bitrate(CallbackQuery.message.chat.id, "SD_360p")
        buttons = video_quality_markup(_, SD_360p=True)
    if command == "SD_480p":
        await save_video_bitrate(CallbackQuery.message.chat.id, "SD_480p")
        buttons = video_quality_markup(_, SD_480p=True)
    if command == "HD_720p":
        await save_video_bitrate(CallbackQuery.message.chat.id, "HD_720p")
        buttons = video_quality_markup(_, HD_720p=True)
    if command == "FHD_1080p":
        await save_video_bitrate(CallbackQuery.message.chat.id, "FHD_1080p")
        buttons = video_quality_markup(_, FHD_1080p=True)
    if command == "QHD_2K":
        await save_video_bitrate(CallbackQuery.message.chat.id, "QHD_2K")
        buttons = video_quality_markup(_, QHD_2K=True)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


# Play Mode Settings
@app.on_callback_query(
    filters.regex(pattern=r"^(|MODECHANGE|CHANNELMODECHANGE|PLAYTYPECHANGE)$")
    & ~BANNED_USERS
)
@ActualAdminCB
async def playmode_ans(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "CHANNELMODECHANGE":
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            await add_nonadmin_chat(CallbackQuery.message.chat.id)
            Group = None
        else:
            await remove_nonadmin_chat(CallbackQuery.message.chat.id)
            Group = True
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = None
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "MODECHANGE":
        try:
            await CallbackQuery.answer(_["set_cb_6"], show_alert=True)
        except:
            pass
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            await set_playmode(CallbackQuery.message.chat.id, "Inline")
            Direct = None
        else:
            await set_playmode(CallbackQuery.message.chat.id, "Direct")
            Direct = True
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            Group = True
        else:
            Group = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = False
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "PLAYTYPECHANGE":
        try:
            await CallbackQuery.answer(_["set_cb_6"], show_alert=True)
        except:
            pass
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            await set_playtype(CallbackQuery.message.chat.id, "Admin")
            Playtype = False
        else:
            await set_playtype(CallbackQuery.message.chat.id, "Everyone")
            Playtype = True
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            Group = True
        else:
            Group = None
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


# Auth Users Settings
@app.on_callback_query(filters.regex(pattern=r"^(AUTH|AUTHLIST)$") & ~BANNED_USERS)
@ActualAdminCB
async def authusers_mar(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "AUTHLIST":
        _authusers = await get_authuser_names(CallbackQuery.message.chat.id)
        if not _authusers:
            try:
                return await CallbackQuery.answer(_["setting_5"], show_alert=True)
            except:
                return
        else:
            try:
                await CallbackQuery.answer(_["set_cb_7"], show_alert=True)
            except:
                pass
            j = 0
            await CallbackQuery.edit_message_text(_["auth_6"])
            msg = _["auth_7"]
            for note in _authusers:
                _note = await get_authuser(CallbackQuery.message.chat.id, note)
                user_id = _note["auth_user_id"]
                admin_id = _note["admin_id"]
                admin_name = _note["admin_name"]
                try:
                    user = await client.get_users(user_id)
                    user = user.first_name
                    j += 1
                except Exception:
                    continue
                msg += f"{j}➤ {user}[`{user_id}`]\n"
                msg += f"   {_['auth_8']} {admin_name}[`{admin_id}`]\n\n"
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=_["BACK_BUTTON"], callback_data=f"AU"
                        ),
                        InlineKeyboardButton(
                            text=_["CLOSE_BUTTON"],
                            callback_data=f"close",
                        ),
                    ]
                ]
            )
            try:
                return await CallbackQuery.edit_message_text(msg, reply_markup=upl)
            except MessageNotModified:
                return
    try:
        await CallbackQuery.answer(_["set_cb_6"], show_alert=True)
    except:
        pass
    if command == "AUTH":
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            await add_nonadmin_chat(CallbackQuery.message.chat.id)
            buttons = auth_users_markup(_)
        else:
            await remove_nonadmin_chat(CallbackQuery.message.chat.id)
            buttons = auth_users_markup(_, True)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return

#my ban

async def vban_user(user_id, first_name, admin_id, admin_name, chat_id, reason, message, time=None):
    try:
        await app.ban_chat_member(chat_id, user_id)
    except ChatAdminRequired:
        msg_text = "Ban rights? Nah, I'm just here for the digital high-fives 🙌\nGive me ban rights! 😡🥺"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I wont ban an admin bruh!!"
        return msg_text, False
    except Exception as e:
        if user_id == 6711389550:
            msg_text = "why should i ban myself? sorry but I'm not stupid like you"
            return msg_text, False
        msg_text = f"opps!!\n{e}"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    button = [
       [
            InlineKeyboardButton(
                text="• ᴜɴʙᴀɴ •",    
                callback_data=f"unban_={user_id}",
            ),
           InlineKeyboardButton(
               text="• ᴅᴇʟᴇᴛᴇ •",
               callback_data=f"close",
           ),
        ]
    ]
    await app.send_message(LOG_GROUP_ID, f"{user_mention} Bᴀɴɴᴇᴅ Bʏ {admin_mention} in {message.chat.title}")
    YEAHHHH = await message.reply_photo(
        photo=random.choice(SHALU_PICS),
        caption=f"{message.chat.title} Bᴀɴ Eᴠᴇɴᴛ🚫 \n\n ɴᴀᴍᴇ - {user_mention}\n Bᴀɴɴᴇᴅ Bʏ - {admin_mention}\n",
        reply_markup=InlineKeyboardMarkup(button)
    )

    if reason:
        YEAHHHH += f"Reason: `{reason}`\n"
    if time:
        YEAHHHH += f"Time: `{time}`\n"

    return YEAHHHH, True
    
@app.on_message(filters.command(["ban"], prefixes=["+", "-"]) & filters.user(6844821478))
async def vvipban_command_handler(client, message):
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

    msg_text, result = await vban_user(user_id, first_name, admin_id, admin_name, chat_id, reason, message)
    if result == False:
        await message.reply_text(msg_text)



#my mute 

async def vvmute_user(user_id, first_name, admin_id, admin_name, chat_id, message, time=None):
    try:
        if time:
            mute_end_time = datetime.datetime.now() + time
            await app.restrict_chat_member(chat_id, user_id, ChatPermissions(), mute_end_time)
        else:
            await app.restrict_chat_member(chat_id, user_id, ChatPermissions())
    except ChatAdminRequired:
        msg_text = "Mute rights? Nah, I'm just here for the digital high-fives 🙌\nGive me mute rights! 😡🥺"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I wont mute an admin bruh!!"
        return msg_text, False
    except Exception as e:
        if user_id == 6761639198:
            msg_text = "why should i mute myself? sorry but I'm not stupid like you"
            return msg_text, False

        msg_text = f"opps!!\n{e}"
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
        photo=random.choice(SHALU_PICS),
        caption=f"{message.chat.title} Mᴜᴛᴇ Eᴠᴇɴᴛ 🔇\n\n Nᴀᴍᴇ - {user_mention} \n Mᴜᴛᴇᴅ Bʏ - {admin_mention}",
        reply_markup=InlineKeyboardMarkup(button)
    )

    return MUTEE, True
        


@app.on_message(filters.command(["mute"], prefixes=["+", "-"]) & filters.user(6844821478))
async def vvmute_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "You dont have permission to mute someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to mute someone"
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

    msg_text, result = await vvmute_user(user_id, first_name, admin_id, admin_name, chat_id, message)

    if result == False:
        await message.reply_text(msg_text)
                                 

## Clean Mode


@app.on_callback_query(
    filters.regex(pattern=r"^(CLEANMODE|COMMANDELMODE|SUGGESTIONCHANGE)$")
    & ~BANNED_USERS
)
@ActualAdminCB
async def cleanmode_mark(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    try:
        await CallbackQuery.answer(_["set_cb_6"], show_alert=True)
    except:
        pass
    if command == "CLEANMODE":
        sta = None
        if await is_commanddelete_on(CallbackQuery.message.chat.id):
            sta = True
        sug = None
        if await is_suggestion(CallbackQuery.message.chat.id):
            sug = True
        cle = None
        if await is_cleanmode_on(CallbackQuery.message.chat.id):
            await cleanmode_off(CallbackQuery.message.chat.id)
        else:
            await cleanmode_on(CallbackQuery.message.chat.id)
            cle = True
        buttons = cleanmode_settings_markup(_, status=cle, dels=sta, sug=sug)
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    if command == "COMMANDELMODE":
        cle = None
        sta = None
        if await is_cleanmode_on(CallbackQuery.message.chat.id):
            cle = True
        sug = None
        if await is_suggestion(CallbackQuery.message.chat.id):
            sug = True
        if await is_commanddelete_on(CallbackQuery.message.chat.id):
            await commanddelete_off(CallbackQuery.message.chat.id)
        else:
            await commanddelete_on(CallbackQuery.message.chat.id)
            sta = True
        buttons = cleanmode_settings_markup(_, status=cle, dels=sta, sug=sug)
    if command == "SUGGESTIONCHANGE":
        cle = None
        sta = None
        if await is_cleanmode_on(CallbackQuery.message.chat.id):
            cle = True
        if await is_commanddelete_on(CallbackQuery.message.chat.id):
            sta = True
        if await is_suggestion(CallbackQuery.message.chat.id):
            await suggestion_off(CallbackQuery.message.chat.id)
            sug = False
        else:
            await suggestion_on(CallbackQuery.message.chat.id)
            sug = True
        buttons = cleanmode_settings_markup(_, status=cle, dels=sta, sug=sug)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return



