from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message
from config import BANNED_USERS
from strings import get_command, get_string
from CUTEXMUSIC import app
from CUTEXMUSIC.utils.database import get_lang, set_lang
from CUTEXMUSIC.utils.decorators import ActualAdminCB, language, languageCB

# Languages Available

def stlanuages_keyboard(_):
    keyboard = InlineKeyboard(row_width=2)
    keyboard.row(
        InlineKeyboardButton(
            text="❄️ ᴋᴀɴɴᴀᴅᴀ ❄️",
            callback_data=f"languages:kn",
        ),
        InlineKeyboardButton(
            text="🇮🇳 हिन्दी 🇮🇳",
            callback_data=f"languages:hi",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="🇦🇺 ᴇɴɢʟɪsʜ 🇦🇺",
            callback_data=f"languages:en",
        ),
        InlineKeyboardButton(
            text="✨ PᴜɴJᴀʙɪ ✨",
            callback_data=f"languages:pnj",
        ),
    )
    keyboard.row(
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="help_back",
            ),
        InlineKeyboardButton(text=_["NEXT_BUTTON"], callback_data="NXTLANG"),
    )
    return keyboard
    
def secstlanuages_keyboard(_):
    keyboard = InlineKeyboard(row_width=2)
    keyboard.row(
        InlineKeyboardButton(
            text="🐕 ᴄʜᴇᴇᴍs 🐕",
            callback_data=f"languages:cheems",
        ),
        InlineKeyboardButton(
            text="🇮🇳 ગુજરાતી 🇮🇳",
            callback_data=f"languages:gu",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="💗 मराठी 💗",
            callback_data=f"languages:mar",
        ),
        InlineKeyboardButton(
            text="🕊️ Tᴇʟᴜɢᴜ 🕊️",
            callback_data=f"languages:tel",
        ),
    )
    keyboard.row(
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="LANGCHANGE",
            ),
        InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
    )
    return keyboard
    
@app.on_callback_query(filters.regex("NXTLANG") & ~BANNED_USERS)
@languageCB
async def laggnuasgecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    keyboard = secstlanuages_keyboard(_)
    await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
    


def lanuages_keyboard(_):
    keyboard = InlineKeyboard(row_width=2)
    keyboard.row(
        InlineKeyboardButton(
            text="❄️ ᴋᴀɴɴᴀᴅᴀ ❄️",
            callback_data=f"languages:kn",
        ),
        InlineKeyboardButton(
            text="🇮🇳 हिन्दी 🇮🇳",
            callback_data=f"languages:hi",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="🇦🇺 ᴇɴɢʟɪsʜ 🇦🇺",
            callback_data=f"languages:en",
        ),
        InlineKeyboardButton(
            text="✨ PᴜɴJᴀʙɪ ✨",
            callback_data=f"languages:pnj",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="🐕 ᴄʜᴇᴇᴍs 🐕",
            callback_data=f"languages:cheems",
        ),
        InlineKeyboardButton(
            text="🇮🇳 ગુજરાતી 🇮🇳",
            callback_data=f"languages:gu",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="💗 मराठी 💗",
            callback_data=f"languages:mar",
        ),
        InlineKeyboardButton(
            text="🕊️ Tᴇʟᴜɢᴜ 🕊️",
            callback_data=f"languages:tel",
        ),
    )
    keyboard.row(
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
        InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close"),
    )
    return keyboard


LANGUAGE_COMMAND = get_command("LANGUAGE_COMMAND")


@app.on_message(filters.command(LANGUAGE_COMMAND) & filters.group & ~BANNED_USERS)
@language
async def langs_command(client, message: Message, _):
    keyboard = lanuages_keyboard(_)
    await message.reply_text(
        _["Lang_1"].format(message.chat.title, message.chat.id, app.mention),
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("LANGCHANGE") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    keyboard = stlanuages_keyboard(_)
    caption = """
    <b><u>✪ ʜᴇʀᴇ ɪs ᴀʟʟ ᴍʏ ʟᴀɴɢᴜᴀɢᴇs </b></u>

✯ Aʟʟ Lᴀɴɢᴜᴀɢᴇs Aʀᴇ Sᴜᴘᴘᴏʀᴛᴇᴅ
✯ Esᴘᴇᴄɪᴀʟʟʏ Tʜᴀɴᴋs Tᴏ Vɪᴠᴀɴ Fᴏʀ Kᴀɴɴᴀᴅᴀ Lᴀɴɢ
✯ Aɴᴅ Yᴜᴋᴋɪ Fᴏʀ Sᴏᴍᴇ ʟᴀɴɢᴜᴀɢᴇs 
✯ ᴀɴᴅ ᴍᴇ ғᴏʀ Mᴀʀᴀᴛʜɪ Lᴀɴɢᴜᴀɢᴇ 
"""
    await CallbackQuery.edit_message_caption(caption)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)



@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
    

@app.on_callback_query(filters.regex(r"languages:(.*?)") & ~BANNED_USERS)
@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
    langauge = (CallbackQuery.data).split(":")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer(
            "ʏᴏᴜ'ʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜsɪɴɢ sᴀᴍᴇ ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.", show_alert=True
        )
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(
            "sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ʏᴏᴜʀ ʟᴀɴɢᴜᴀɢᴇ.", show_alert=True
        )
    except:
        return await CallbackQuery.answer(
            "ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ʟᴀɴɢᴜᴀɢᴇ ᴏʀ ᴛʜᴇ ʟᴀɴɢᴜᴀɢᴇ ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ.",
            show_alert=True,
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
  #  keyboard = stlanuages_keyboard(_)
    #return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
