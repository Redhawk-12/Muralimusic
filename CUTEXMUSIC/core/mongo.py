from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client
from typing import Dict, Union
import config
from ..logging import LOGGER
from config import *

TEMP_MONGODB = "mongodb+srv://CutexMusicdatabase:Cute937@cutedatabase.ubypaox.mongodb.net/?retryWrites=true&w=majority&appName=CuteDatabase"


if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning("No MONGO DB URL found.")
    temp_client = Client(
        "CUTEXMUSIC",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = AsyncIOMotorClient(TEMP_MONGODB)
    _mongo_sync_ = AsyncIOMotorClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = AsyncIOMotorClient(config.MONGO_DB_URI)
    _mongo_sync_ = AsyncIOMotorClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.CUTEXMUSIC
    pymongodb = _mongo_sync_.CUTEXMUSIC

#### next



mongo = AsyncIOMotorClient(MURALI_DB)
db = mongo.MURALIBOTDATABSE
coupledb = db.couple
afkdb = db.afk
nightmodedb = db.nightmode
notesdb = db.notes
filtersdb = db.filters


async def _get_lovers(cid: int):
    lovers = await coupledb.find_one({"chat_id": cid})
    if lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers

async def _get_image(cid: int):
    lovers = await coupledb.find_one({"chat_id": cid})
    if lovers:
        lovers = lovers["img"]
    else:
        lovers = {}
    return lovers

async def get_couple(cid: int, date: str):
    lovers = await _get_lovers(cid)
    if date in lovers:
        return lovers[date]
    else:
        return False


async def save_couple(cid: int, date: str, couple: dict, img: str):
    lovers = await _get_lovers(cid)
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": cid},
        {"$set": {"couple": lovers, "img": img}},
        upsert=True,
    )
