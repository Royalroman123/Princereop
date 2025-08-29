import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 28976608

API_HASH = "1e200bdfdcc3cc816f9f6a62e6e6f4a0"
BOT_TOKEN = "7656161134:AAHjCxbnREPaZSVYr8SWY70703vPnMyXyUg"

BOT_ID = 7825870013

BOT_USERNAME = "@Music_Silent_bot"

OWNER_USERNAME = "@finalbossrock"

BOT_NAME = "━──『 🎶ＳɪʟᴇɴᴛＭᴜꜱɪᴄＢᴏᴛ🎶 』──━"

ASSUSERNAME = "@SilentAssistant"

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Sarkar123:GAUTAMMISHRA@sarkar.1uiwqkd.mongodb.net/?retryWrites=true&w=majority"
DURATION_LIMIT_MIN = 500000

LOGGER_ID = int(getenv("LOGGER_ID", -1003063952141)

DISASTER_LOG =  -1003063952141

OWNER_ID = 5016636419

SPECIAL_USER = 5016636419

HEROKU_APP_NAME = None

HEROKU_API_KEY = None

UPSTREAM_REPO = "https://github.com/Sixeyesuser07/Sam-empire"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = "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"

SUPPORT_CHANNEL = "https://t.me/hxh_bot_support"

SUPPORT_CHAT = "https://t.me/zenitsu_bot_support"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000

SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = getenv("STRING1", "BQEx4WEAQq83h1iMorDLLa39qxuEjzwNWe_4lTZEhsVtayWAoG4jK8wpl2AbGpPYtCFDmtcANZI4GrrtuGXM7cScmwkUKs9PMtNAl779rAprVWUx2Q9PwhTlvbUeE5MBVv2MHyC4D35yTI2oU1Ry2nMraLvK1LR4iZgRFzBrFYW4e5mCwqLdrgpZ4mTPhjSnPl6RtFeeAj1Y74Gcz2HQxAIK3FZdgrd4bxOZ6_ZKMfG2c-8smB7-Nk7kwxbUt0PGMHxibQWHVSCixnGnKTWIXG4Wz5TCX78KOkCxfFGbH8mKAZtbFARGD1a9VBnA5hLrnE_t7r_XoIL3_iGtpAgxSPSGy6vaHgAAAAFugCNSAA")
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://i.ibb.co/Q8K36xH/photo-2025-01-20-17-07-20-7462045458169331720.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/XFyfNRC/photo-2024-12-14-04-11-48-7448115436119392264.jpg"
STATS_IMG_URL = "https://i.ibb.co/k1KyRqd/photo-2025-01-20-17-10-11-7462046184018804752.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/TrJhtN4/photo-2024-12-14-04-12-15-7448115547788542008.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/XFyfNRC/photo-2024-12-14-04-11-48-7448115436119392264.jpg"
STREAM_IMG_URL = "https://i.ibb.co/THd3s2g/photo-2024-12-14-04-12-49-7448115698112397328.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/TrJhtN4/photo-2024-12-14-04-12-15-7448115547788542008.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/THd3s2g/photo-2024-12-14-04-12-49-7448115698112397328.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/XFyfNRC/photo-2024-12-14-04-11-48-7448115436119392264.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/THd3s2g/photo-2024-12-14-04-12-49-7448115698112397328.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/THd3s2g/photo-2024-12-14-04-12-49-7448115698112397328.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
