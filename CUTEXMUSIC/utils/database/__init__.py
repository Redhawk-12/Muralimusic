from .assistantdatabase import *
from .memorydatabase import *
from .mongodatabase import *
from .randomthumb import *
from motor.motor_asyncio import AsyncIOMotorClient as AsyncClient
from config import *


DBNAME = "CUTIEXMUSICBOT"

mongo = AsyncClient(MURALI_DB)
dbname = mongo[DBNAME]

