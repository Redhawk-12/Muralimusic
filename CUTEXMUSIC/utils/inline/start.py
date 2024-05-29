from typing import Union
import config
from pyrogram.types import InlineKeyboardButton
from config import *
from config import SUPPORT_CHANNEL, SUPPORT_GROUP
from CUTEXMUSIC import app

START_BUT = [
       [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ",
                url=f"https://t.me/CuteXMusicBot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users",
            ),
        ], 
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
        ),
        ],
      [
            InlineKeyboardButton(
               text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", 
               url=f"tg://openmessage?user_id=6844821478",
                    ),
           InlineKeyboardButton(
               text="sᴜᴘᴘᴏʀᴛ",
               url=f"https://t.me/MUSIC_WORL_SH"
           ),
        ],
      [
            InlineKeyboardButton(
               text="Lᴀɴɢᴜᴀɢᴇ", 
               callback_data="LANGCHANGE"
                    ),
           InlineKeyboardButton(
                text="sᴏᴜʀᴄᴇ",
                callback_data="source_codeprank"
                   ),
        ],
]







def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}")]
            )
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
       [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users",
            ),
        ], 
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
        ),
        ],
      [
            InlineKeyboardButton(
               text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", 
               user_id=OWNER,
                    ),
           InlineKeyboardButton(
               text="sᴜᴘᴘᴏʀᴛ",
               url=SUPPORT_GROUP,
           ),
        ],
      [
            InlineKeyboardButton(
               text="Lᴀɴɢᴜᴀɢᴇ", 
               callback_data="LANGCHANGE"
                    ),
           InlineKeyboardButton(
                text="sᴏᴜʀᴄᴇ",
                callback_data="source_codeprank"
                   ),
        ],
]
    return buttons






