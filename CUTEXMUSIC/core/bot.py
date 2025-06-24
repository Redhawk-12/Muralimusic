import sys
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, MUSIC_BOT_NAME
from CUTEXMUSIC.logging import LOGGER
from pyrogram.enums import ChatMemberStatus

# âœ… New log group ID
LOG_GROUP_ID = -1002693180392

class CUTEXBOT(Client):
    def __init__(self):
        super().__init__(
            "MusicBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            in_memory=True,
        )
        LOGGER(__name__).info("ðŸš€ Starting your bot...")

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = me.username
        self.id = me.id
        self.name = me.first_name + " " + (me.last_name or "")
        self.mention = me.mention

        LOGGER(__name__).info(f"ðŸ¤– Logged in as: {self.name} (@{self.username})")

        # Debug print
        print("âœ… LOG_GROUP_ID is:", LOG_GROUP_ID)

        try:
            await self.send_message(
                LOG_GROUP_ID,
                f"âœ… {MUSIC_BOT_NAME} started!\n\nðŸ†” ID: `{self.id}`\nðŸ“› Username: @{self.username}\nðŸ›  Made by Hawk ðŸ¥€",
            )
            LOGGER(__name__).info("ðŸ“¨ Sent startup message to log group.")
        except Exception as e:
            LOGGER(__name__).error(f"âŒ Failed to send message to log group: {e}")
            sys.exit()

        try:
            member = await self.get_chat_member(LOG_GROUP_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error("ðŸš« Bot is not admin in the log group.")
                sys.exit()
            LOGGER(__name__).info("âœ… Bot is an admin in the log group.")
        except Exception as e:
            LOGGER(__name__).error(f"âŒ Failed to fetch bot member status in log group: {e}")
            sys.exit()

        LOGGER(__name__).info("ðŸŽ‰ Bot started successfully!")
        
