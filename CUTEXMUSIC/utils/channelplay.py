from CUTEXMUSIC import app
from pyrogram import filters
from pyrogram.types import CallbackQuery
from CUTEXMUSIC.utils.database import get_cmode


async def get_channeplayCB(command, CallbackQuery):
    if command == "c":
        chat_id = await get_cmode(CallbackQuery.message.chat.id)
        if chat_id is None:
            try:
                return await CallbackQuery.answer(
                    "You need to set a channel for this feature.", show_alert=True
                )
            except:
                return
        try:
            chat = await app.get_chat(chat_id)
            channel = chat.title
        except:
            try:
                return await CallbackQuery.answer(
                    "Couldn’t fetch the linked channel. Is the bot in it?", show_alert=True
                )
            except:
                return
    else:
        chat_id = CallbackQuery.message.chat.id
        channel = None
    return chat_id, channel


def register_channel_players():
    @app.on_callback_query(filters.regex("^ChannelPlay"))
    async def handle_channel_play_callback(client, callback_query: CallbackQuery):
        data = callback_query.data.split("|")  # Example: "ChannelPlay|c"
        if len(data) < 2:
            return await callback_query.answer("Invalid command.", show_alert=True)

        command = data[1]
        result = await get_channeplayCB(command, callback_query)
        if not result:
            return
        chat_id, channel = result
        await callback_query.message.reply_text(
            f"✅ Channel Play activated.\nChat ID: `{chat_id}`\nChannel: `{channel or 'None'}`"
        )
