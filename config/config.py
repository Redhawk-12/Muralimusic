import logging
import re
import sys
import os
import nekos
from os import getenv
import time
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_USERNAME = getenv("BOT_USERNAME" , "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "50000000")
)  # Remember to give value in Minutes

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "500000")
)  # Remember to give value in Minutes

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

# A name for your Music bot.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "༄𝐂𝐔𝐓𝐄 ✘ 𝐌𝐔𝐒𝐈𝐂 ࿐𝄟͢")

# Your User ID.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "6844821478").split())
) 

# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/CUTE-BACHHA/MURALIMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Murali")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", "")

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", None
)  
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", None
)  

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "50000000")
)  # Remember to give value in Seconds

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "50000000")
)  # Remember to give value in Seconds

# Set it True if you want to delete downloads after the music playout ends from your downloads folder
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", None)

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50000080"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50000006"))

# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "2147483648")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "2147483648")
)  

SET_CMDS = getenv("SET_CMDS", True)

# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @YukkiStringBot
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


MURALI_DB = getenv("MURALI_DB", "")

# Images
START_IMG_URL = nekos.img("neko")

PING_IMG_URL = nekos.img("neko")

PLAYLIST_IMG_URL = nekos.img("neko")

GLOBAL_IMG_URL = nekos.img("neko")

STATS_IMG_URL = nekos.img("neko")

TELEGRAM_AUDIO_URL = nekos.img("neko")

TELEGRAM_VIDEO_URL = nekos.img("neko")

STREAM_IMG_URL = nekos.img("neko")

SOUNCLOUD_IMG_URL = nekos.img("neko")

YOUTUBE_IMG_URL = nekos.img("neko")

SPOTIFY_ARTIST_IMG_URL = nekos.img("neko")

SPOTIFY_ALBUM_IMG_URL = nekos.img("neko")

SPOTIFY_PLAYLIST_IMG_URL = nekos.img("neko")

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


