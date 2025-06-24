from pyrogram import filters
from pyrogram.types import CallbackQuery
from CUTEXMUSIC import app
from CUTEXMUSIC.utils.localization import get_string  # Assuming you use a localization system

from CUTEXMUSIC.utils.database import get_cmode


async def get_channeplayCB(_, command, CallbackQuery):
    if command == "c":
        chat_id = await get_cmode(CallbackQuery.message.chat.id)
        if chat_id is None:
            try:
                return await CallbackQuery.answer(_["setting_12"], show_alert=True)
            except:
                return
        try:
            chat = await app.get_chat(chat_id)
            channel = chat.title
        except:
            try:
                return await CallbackQuery.answer(_["cplay_4"], show_alert=True)
            except:
                return
    else:
        chat_id = CallbackQuery.message.chat.id
        channel = None
    return chat_id, channel


def register_channel_players():
    @app.on_callback_query(filters.regex("^ChannelPlay"))
    async def handle_channel_play_callback(client, callback_query: CallbackQuery):
        _ = await get_string(callback_query.message.chat.id)  # localization
        data = callback_query.data.split("|")  # e.g. "ChannelPlay|c"
        if len(data) < 2:
            return await callback_query.answer("Invalid command.", show_alert=True)

        command = data[1]
        result = await get_channeplayCB(_, command, callback_query)
        if not result:
            return
        chat_id, channel = result
        await callback_query.message.reply_text(
            f"Channel Play triggered for chat: `{chat_id}`\nChannel: `{channel}`"
        )
