import sys
from pyrogram import Client
import config
from ..logging import LOGGER
from pyrogram.enums import ChatMemberStatus


class CUTEXBOT(Client):
    def __init__(self):
        super().__init__(
            "MusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
        )
        LOGGER(__name__).info(f"sᴛᴀʀᴛɪɴɢ Yᴏᴜʀ Bᴏᴛ")

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = get_me.first_name + " " + (get_me.last_name or "")
        self.mention = get_me.mention
        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"๏ {config.MUSIC_BOT_NAME} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ ➛ \n\n๏ ɪᴅ ➛ {self.id}\n๏ ɴᴀᴍᴇ ➛ {self.name}\n๏ ᴜsᴇʀɴᴀᴍᴇ ➛ @{self.username} \n\n|| ᴍᴀᴅᴇ ʙʏ ᴍᴜʀᴀʟɪ 🥀 ||."
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"ᴍᴜsɪᴄ ʙᴏᴛ Sᴛᴀʀᴛᴇᴅ as  {self.name}")
    
