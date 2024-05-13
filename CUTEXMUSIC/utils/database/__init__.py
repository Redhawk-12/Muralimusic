from .assistantdatabase import *
from .memorydatabase import *
from .mongodatabase import *
from .randomthumb import *
from async_pymongo import AsyncClient
from config import *


DBNAME = "CUTIEXMUSICBOT"

mongo = AsyncClient(MURALI_DB)
dbname = mongo[DBNAME]

