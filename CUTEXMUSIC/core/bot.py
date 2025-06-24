import sys
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, LOG_GROUP_ID, MUSIC_BOT_NAME
from CUTEXMUSIC.logging import LOGGER
from pyrogram.enums import ChatMemberStatus


class CUTEXBOT(Client):
    def __init__(self):
        super().__init__(
            "MusicBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            in_memory=True,
        )
        LOGGER(__name__).info("Starting your bot...")

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = me.username
        self.id = me.id
        self.name = me.first_name + " " + (me.last_name or "")
        self.mention = me.mention

        try:
            await self.send_message(
                LOG_GROUP_ID,
                f"✅ {MUSIC_BOT_NAME} started!\nID: {self.id}\nUsername: @{self.username}\nMade by Hawk 🥀",
            )
        except:
            LOGGER(__name__).error("Bot couldn't send message to log group. Is it admin?")
            sys.exit()

        member = await self.get_chat_member(LOG_GROUP_ID, self.id)
        if member.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("Please promote the bot as admin in the log group!")
            sys.exit()

        LOGGER(__name__).info(f"Bot started as {self.name}")
        
