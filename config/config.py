import logging
import os
import requests
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# API Configuration with validation
try:
    API_ID = int(os.getenv("API_ID", "23791517"))
    API_HASH = os.getenv("API_HASH", "cbd37141690ac36f9cacb5b2daa61bad")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8123997116:AAGxmlSKpRABgoQrreKcQrL69qzUmIaHhQ0")
    
    if not all([API_ID, API_HASH, BOT_TOKEN]):
        raise ValueError("Missing required API configuration")
except Exception as e:
    logging.error(f"Configuration error: {e}")
    exit(1)

# Duration Limits with sane defaults
DURATION_LIMIT_MIN = min(int(os.getenv("DURATION_LIMIT", "50000000")), 1440)  # Max 24 hours
SONG_DOWNLOAD_DURATION = min(int(os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", "500000")), 180)  # Max 3 hours

# Log Group with validation
try:
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1002693180392"))
except:
    LOG_GROUP_ID = None

# Enhanced Security for MongoDB
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
if not MONGO_DB_URI.startswith("mongodb+srv://jckson8822:jckson8822@cluster0.knqdzyw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"):
    logging.warning("Invalid MongoDB URI format")

# Rate Limiting Configuration
FLOOD_WAIT_DELAY = int(os.getenv("FLOOD_WAIT_DELAY", "5"))  # Default 5 second buffer
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))

# Audio Quality Settings
class AudioQuality:
    LOW = "64K"
    MEDIUM = "128K"
    HIGH = "192K"

AUDIO_QUALITY = os.getenv("AUDIO_QUALITY", AudioQuality.MEDIUM)

# Image Handling with fallback
try:
    image_url = requests.get("https://nekos.best/api/v2/neko").json()["results"][0]["url"]
except:
    image_url = "https://telegra.ph/file/2b5f5d0d1b5e5e5e5e5e5.jpg"

START_IMG_URL = os.getenv("START_IMG_URL", image_url)
# ... (other image URLs with same fallback)

def time_to_seconds(time):
    try:
        return sum(int(x) * 60**i for i, x in enumerate(reversed(str(time).split(":")))
    except:
        return 0

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
SONG_DOWNLOAD_DURATION_LIMIT = time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
