from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client
from typing import Dict, Union
import config
from ..logging import LOGGER
from config import *

TEMP_MONGODB = "mongodb+srv://CutexMusicdatabase:Cute937@cutedatabase.ubypaox.mongodb.net/?retryWrites=true&w=majority&appName=CuteDatabase"


_mongo_async_ = AsyncIOMotorClient(config.MONGO_DB_URI if config.MONGO_DB_URI else TEMP_MONGODB)
pymongodb = _mongo_async_.CUTEXMUSIC if config.MONGO_DB_URI else _mongo_async_[info.username]

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
