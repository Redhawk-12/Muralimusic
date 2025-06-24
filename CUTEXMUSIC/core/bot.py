import asyncio
import sys
from pyrogram import Client
from pyrogram.errors import FloodWait
from config import API_ID, API_HASH, BOT_TOKEN, LOG_GROUP_ID, FLOOD_WAIT_DELAY, MAX_RETRIES
from CUTEXMUSIC.logging import LOGGER

class CUTEXBOT(Client):
    def __init__(self):
        super().__init__(
            name="MusicBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            in_memory=True,
            sleep_threshold=30,
            workers=4
        )
        
    async def safe_send_message(self, chat_id, text):
        for attempt in range(MAX_RETRIES):
            try:
                return await self.send_message(chat_id, text)
            except FloodWait as e:
                wait_time = e.value + FLOOD_WAIT_DELAY
                if attempt == MAX_RETRIES - 1:
                    raise
                LOGGER.warning(f"FloodWait: Sleeping for {wait_time} seconds")
                await asyncio.sleep(wait_time)

    async def start(self):
        LOGGER.info("Initializing bot...")
        for attempt in range(MAX_RETRIES):
            try:
                await super().start()
                me = await self.get_me()
                self.username = me.username
                self.id = me.id
                self.name = me.first_name
                
                # Verify log group
                if LOG_GROUP_ID:
                    try:
                        await self.safe_send_message(
                            LOG_GROUP_ID,
                            f"✅ Bot started!\n\nID: {self.id}\nUsername: @{self.username}"
                        )
                        member = await self.get_chat_member(LOG_GROUP_ID, self.id)
                        if member.status != "administrator":
                            LOGGER.error("Bot must be admin in log group")
                            sys.exit(1)
                    except Exception as e:
                        LOGGER.error(f"Log group verification failed: {e}")
                
                LOGGER.info(f"Bot started as @{self.username}")
                return
                
            except FloodWait as e:
                if attempt == MAX_RETRIES - 1:
                    raise
                wait_time = e.value + FLOOD_WAIT_DELAY
                LOGGER.warning(f"Startup FloodWait: Sleeping {wait_time}s")
                await asyncio.sleep(wait_time)
            except Exception as e:
                LOGGER.error(f"Startup failed: {e}")
                sys.exit(1)
