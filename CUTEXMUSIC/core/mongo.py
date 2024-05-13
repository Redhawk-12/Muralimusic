from async_pymongo import AsyncClient as AsyncMongoClient
from pyrogram import Client
from typing import Dict, Union
import config
from ..logging import LOGGER
from config import *


TEMP_MONGODB = "mongodb+srv://CutexMusicdatabase:Cute937@cutedatabase.ubypaox.mongodb.net/?retryWrites=true&w=majority&appName=CuteDatabase"

_mongo_async_ = AsyncMongoClient(config.MONGO_DB_URI if config.MONGO_DB_URI else TEMP_MONGODB)


pymongodb = _mongo_async_.get_database('CUTEXMUSIC' if config.MONGO_DB_URI else info.username)


mongo = AsyncMongoClient(config.MURALI_DB)
db = mongo.get_database('MURALIBOTDATABASE')
coupledb = db.get_collection('couple')
afkdb = db.get_collection('afk')
nightmodedb = db.get_collection('nightmode')
notesdb = db.get_collection('notes')
filtersdb = db.get_collection('filters')


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
