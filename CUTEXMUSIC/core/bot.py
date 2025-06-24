import sys
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, MUSIC_BOT_NAME
from CUTEXMUSIC.logging import LOGGER
from pyrogram.enums import ChatMemberStatus

# ✅ New log group ID
LOG_GROUP_ID = -1002113460681

class CUTEXBOT(Client):
    def __init__(self):
        super().__init__(
            "MusicBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            in_memory=True,
        )
        LOGGER(__name__).info("🚀 Starting your bot...")

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = me.username
        self.id = me.id
        self.name = me.first_name + " " + (me.last_name or "")
        self.mention = me.mention

        LOGGER(__name__).info(f"🤖 Logged in as: {self.name} (@{self.username})")

        # Debug print
        print("✅ LOG_GROUP_ID is:", LOG_GROUP_ID)

        try:
            await self.send_message(
                LOG_GROUP_ID,
                f"✅ {MUSIC_BOT_NAME} started!\n\n🆔 ID: `{self.id}`\n📛 Username: @{self.username}\n🛠 Made by Hawk 🥀",
            )
            LOGGER(__name__).info("📨 Sent startup message to log group.")
        except Exception as e:
            LOGGER(__name__).error(f"❌ Failed to send message to log group: {e}")
            sys.exit()

        try:
            member = await self.get_chat_member(LOG_GROUP_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error("🚫 Bot is not admin in the log group.")
                sys.exit()
            LOGGER(__name__).info("✅ Bot is an admin in the log group.")
        except Exception as e:
            LOGGER(__name__).error(f"❌ Failed to fetch bot member status in log group: {e}")
            sys.exit()

        LOGGER(__name__).info("🎉 Bot started successfully!")
        
