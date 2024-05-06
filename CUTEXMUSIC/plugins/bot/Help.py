from typing import Union
from pyrogram.types import InputMediaPhoto
import random 
from config import SUPPORT_GROUP
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message
from config import START_IMG_URL
from config import BANNED_USERS
from strings import get_command, get_string, helpers
from CUTEXMUSIC import app
from CUTEXMUSIC.misc import SUDOERS
from CUTEXMUSIC.utils import help_pannel
from CUTEXMUSIC.utils.database import get_lang, is_commanddelete_on
from CUTEXMUSIC.utils.decorators.language import LanguageStart, languageCB
from CUTEXMUSIC.utils.inline.help import help_back_markup, private_help_panel, threehelp_back_markup, secondhelp_back_markup, fourhelp_back_markup

### Command
HELP_COMMAND = get_command("HELP_COMMAND")

SHALU_PICS = [
"https://telegra.ph/file/63fa66baedf81f7300616.jpg",
"https://telegra.ph/file/a8f8f5fba1789a3e3f402.jpg",
"https://telegra.ph/file/a5ece51e1b7607e476846.jpg",
"https://telegra.ph/file/c998b6d3ab26f7a248784.jpg",
"https://telegra.ph/file/362ee7b2bc25057bf6bbc.jpg",
"https://telegra.ph/file/0039f9635b7e441cde44c.jpg",
"https://telegra.ph/file/14f461524ceae2cca0888.jpg",
"https://telegra.ph/file/04c0beee35ec540d7b3a6.jpg",
"https://telegra.ph/file/046a6281c6e290a993484.jpg",
]

@app.on_message(filters.command(HELP_COMMAND) & filters.private & ~BANNED_USERS)
@app.on_callback_query(
    filters.regex("settings_back_helper") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_GROUP), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_GROUP),
            reply_markup=keyboard,
      )


@app.on_message(filters.command(HELP_COMMAND) & filters.group & ~BANNED_USERS)
@languageCB
async def help_com_group(client, message: Message, _):
    keyboard = help_pannel(_, True)
    await message.reply_photo(photo=random.choice(SHALU_PICS),
                              caption=_["help_2"],
                              reply_markup=keyboard
                             )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    keyboardtwo = secondhelp_back_markup(_)
    keyboardthree = threehelp_back_markup(_)
    keyboardfour = fourhelp_back_markup(_)
    if cb == "hb38":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "ᴏɴʟʏ ғᴏʀ ᴏᴡɴᴇʀ ᴀɴᴅ sᴜᴅᴏᴇʀs", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(helpers.HELP_38, reply_markup=keyboard)
            return await CallbackQuery.answer()
    if cb == "hb37":
        if CallbackQuery.from_user.id != 6844821478:
            return await CallbackQuery.answer(
                "ᴏɴʟʏ ғᴏʀ ᴏᴡɴᴇʀ ", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(helpers.HELP_38, reply_markup=keyboard)
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)
    elif cb == "hb16":
        await CallbackQuery.edit_message_text(helpers.HELP_16, reply_markup=keyboard)
    elif cb == "hb17":
        await CallbackQuery.edit_message_text(helpers.HELP_17, reply_markup=keyboard)
    elif cb == "hb18":
        await CallbackQuery.edit_message_text(helpers.HELP_18, reply_markup=keyboard)
    elif cb == "hb19":
        await CallbackQuery.edit_message_text(helpers.HELP_19, reply_markup=keyboardtwo)
    elif cb == "hb20":
        await CallbackQuery.edit_message_text(helpers.HELP_20, reply_markup=keyboardtwo)
    elif cb == "hb21":
        await CallbackQuery.edit_message_text(helpers.HELP_21, reply_markup=keyboardtwo)
    elif cb == "hb22":
        await CallbackQuery.edit_message_text(helpers.HELP_22, reply_markup=keyboardtwo)
    elif cb == "hb23":
        await CallbackQuery.edit_message_text(helpers.HELP_23, reply_markup=keyboardtwo)
    elif cb == "hb24":
        await CallbackQuery.edit_message_text(helpers.HELP_24, reply_markup=keyboardtwo)
    elif cb == "hb25":
        await CallbackQuery.edit_message_text(helpers.HELP_25, reply_markup=keyboardtwo)
    elif cb == "hb26":
        await CallbackQuery.edit_message_text(helpers.HELP_26, reply_markup=keyboardtwo)
    elif cb == "hb27":
        await CallbackQuery.edit_message_text(helpers.HELP_27, reply_markup=keyboardtwo)
    elif cb == "hb28":
        await CallbackQuery.edit_message_text(helpers.HELP_28, reply_markup=keyboardtwo)
    elif cb == "hb29":
        await CallbackQuery.edit_message_text(helpers.HELP_29, reply_markup=keyboardtwo)
    elif cb == "hb30":
        await CallbackQuery.edit_message_text(helpers.HELP_30, reply_markup=keyboardtwo)
    elif cb == "hb31":
        await CallbackQuery.edit_message_text(helpers.HELP_31, reply_markup=keyboardtwo)
    elif cb == "hb32":
        await CallbackQuery.edit_message_text(helpers.HELP_32, reply_markup=keyboardtwo)
    elif cb == "hb33":
        await CallbackQuery.edit_message_text(helpers.HELP_33, reply_markup=keyboardtwo)
    elif cb == "hb34":
        await CallbackQuery.edit_message_text(helpers.HELP_34, reply_markup=keyboardtwo)
    elif cb == "hb35":
        await CallbackQuery.edit_message_text(helpers.HELP_35, reply_markup=keyboardtwo)
    elif cb == "hb36":
        await CallbackQuery.edit_message_text(helpers.HELP_36, reply_markup=keyboardtwo)
    elif cb == "hb37":
        await CallbackQuery.edit_message_text(helpers.HELP_37, reply_markup=keyboardthree)
    elif cb == "hb38":
        await CallbackQuery.edit_message_text(helpers.HELP_38, reply_markup=keyboardthree)
    elif cb == "hb40":
        await CallbackQuery.edit_message_text(helpers.HELP_40, reply_markup=keyboardfour)
    elif cb == "hb41":
        await CallbackQuery.edit_message_text(helpers.HELP_41, reply_markup=keyboardfour)
    elif cb == "hb42":
        await CallbackQuery.edit_message_text(helpers.HELP_42, reply_markup=keyboardfour)
    elif cb == "hb43":
        await CallbackQuery.edit_message_text(helpers.HELP_43, reply_markup=keyboardfour)
    elif cb == "hb44":
        await CallbackQuery.edit_message_text(helpers.HELP_44, reply_markup=keyboardfour)
    elif cb == "hb45":
        await CallbackQuery.edit_message_text(helpers.HELP_45, reply_markup=keyboardfour)
    elif cb == "hb46":
        await CallbackQuery.edit_message_text(helpers.HELP_46, reply_markup=keyboardfour)
    elif cb == "hb47":
        await CallbackQuery.edit_message_text(helpers.HELP_47, reply_markup=keyboardfour)
    elif cb == "hb48":
        await CallbackQuery.edit_message_text(helpers.HELP_48, reply_markup=keyboardfour)
    elif cb == "hb49":
        await CallbackQuery.edit_message_text(helpers.HELP_49, reply_markup=keyboardfour)
    elif cb == "hb50":
        await CallbackQuery.edit_message_text(helpers.HELP_50, reply_markup=keyboardfour)
    elif cb == "hb51":
        await CallbackQuery.edit_message_text(helpers.HELP_51, reply_markup=keyboardfour)
    elif cb == "hb52":
        await CallbackQuery.edit_message_text(helpers.HELP_52, reply_markup=keyboardfour)
    elif cb == "hb53":
        await CallbackQuery.edit_message_text(helpers.HELP_53, reply_markup=keyboardfour)
    elif cb == "hb54":
        await CallbackQuery.edit_message_text(helpers.HELP_54, reply_markup=keyboardfour)
    elif cb == "hb55":
        await CallbackQuery.edit_message_text(helpers.HELP_52, reply_markup=keyboardfour)
    elif cb == "hb56":
        await CallbackQuery.edit_message_text(helpers.HELP_56, reply_markup=keyboardfour)
    elif cb == "hb57":
        await CallbackQuery.edit_message_text(helpers.HELP_57, reply_markup=keyboardfour)
    
