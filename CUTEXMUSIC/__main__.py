import asyncio
import importlib
import sys
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
import config
from config import BANNED_USERS
from CUTEXMUSIC import LOGGER, app, userbot
from CUTEXMUSIC.core.call import CUTE
from CUTEXMUSIC.plugins import ALL_MODULES
from CUTEXMUSIC.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop_policy().get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("CUTEXMUSIC").error("Aᴅᴅ A Pʏʀᴏɢʀᴀᴍ Sᴛʀɪɴɢ Sᴇssɪᴏɴ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ..")
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("CUTEXMUSIC.plugins" + all_module)
    LOGGER("CUTEXMUSIC.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs ❄️.")
    await userbot.start()
    await CUTE.start()
    try:
        await CUTE.stream_call("https://telegra.ph/file/e7ba333606c078c840eb9.mp4")
    except NoActiveGroupCall:
        LOGGER("CUTEXMUSIC").error(
            "[ERROR] - \n\n ᴛᴜʀɴ ᴏɴ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇsᴛᴀʀᴛ."
        )
        sys.exit()
    except:
        pass
    await CUTE.decorators()
    LOGGER("CUTEXMUSIC").info("ʏᴏᴜʀ ᴍᴜsɪᴄ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴘʟᴏʏᴇᴅ ɴᴏᴡ ɢᴏ ᴀɴᴅ ᴇɴJᴏʏ ʟᴀɢ ғʀᴇᴇ Mᴜsɪᴄ")
    LOGGER("CUTEXMUSIC").info("Mᴀᴅᴇ Bʏ ZᴇʀᴏXCᴏᴅᴇʀZ (𝑴𝑼𝑹𝜦𝑳𝛪⎯꯭ ꯭ ✶꯭꯭⎯꯭͕🦅࿐) ")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("CUTEXMUSIC").info("Stopping Music Bot")
