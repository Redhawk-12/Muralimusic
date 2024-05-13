from .assistantdatabase import *
from .memorydatabase import *
from .mongodatabase import *
from .randomthumb import *
from pymongo import MongoClient
from config import *

DBNAME = "CUTIEXMUSICBOT"

# Connect to MongoDB
mongo = MongoClient(MURALI_DB)
dbname = mongo[DBNAME]


