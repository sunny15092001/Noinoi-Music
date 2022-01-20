import os
from os import getenv
from dotenv import load_dotenv
from Noinoi.DREAMS.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

    
load_dotenv()
get_queue = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ɴᴏɪ ɴᴏɪ ᴍᴜsɪᴄ 🌸")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/88b954d019f1879737575.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/88b954d019f1879737575.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/88b954d019f1879737575.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/88b954d019f1879737575.jpg")
OWNER_NAME = getenv("OWNER_NAME", "BAZIGARYT")
ALIVE_NAME = getenv("ALIVE_NAME", "ᴄғᴄ ᴍᴜsɪᴄ 🔥")
BOT_USERNAME = getenv("BOT_USERNAME", "NOINOI_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "NOINOIASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CFC_BOT_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BAZIGARXD")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
MONGO_DB_URI = getenv("MONGO_DB_URI")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/88b954d019f1879737575.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Baziibro/NoinoiMusicBot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
