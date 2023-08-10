import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "10577960"))
API_HASH = getenv("API_HASH", "80fd047285f4e94ca80311928b6bb5da")

BOT_TOKEN = getenv("BOT_TOKEN", "6214239978:AAFti6lc9x4SAiiNFKAGFIPul8noQcQMXGw")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://AlishaBots:AlishaBots@cluster0.rklnj4z.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "900")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001840292554"))

LOGGER_ID = int(getenv("LOGGER_ID", "-1001952397338"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝗔𝗹𝗶𝘀𝗵𝗮 𝗠𝘂𝘀𝗶𝗰 [𝟭]")

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "6157453615").split())
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/btwfallen/Alisha1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", "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")

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "AlishaBots")

SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "FallenSupport")



AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400")
)

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

SET_CMDS = getenv("SET_CMDS", "True")

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/NAINA-XD/NAINA-MUSICX")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "7")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQAmtTk0pH6WXpTc0vjmkuhPIz8WMzor-rKcX0Tvpo0EHLGMbQqTooy6soW9KEtHWNqTBVJITdfH4Fp9BSj8cWA02jGV9SDiJ-pAFZqJwPUefvUnb87pGgJzhRKjjBSv96Hq2bf0GYo8GtQRnwL0DTI-Jq6mOEBuoZhSUjrcHVW1ysTK8SNcCYinvyOl2kFXNiZ-owgzmcE6kfypg25hpBThyR7_xyalx-0fDpECVA-G-6QtzzCPC-wpMeBoB_3r64ody1eKqIyGCtsYmRTmET-rzDIdeU_23RBhnh3FuxVKJSv3wl-0SWE_g7emU9uJkBPNmfz0oVHCyURoEgftxkEFdVkSHgA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
DEV = 1356469075
chatstats = {}
userstats = {}
clean = {}
votemode = {}
autoclean = []
confirmer = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/4e3b8b2c148e2dee5d9d8.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/d6bf7fec70a71321164b8.jpg",
)

RANDOM = [
    "https://telegra.ph/file/eb8399e4da061b8da0797.jpg",
    "https://telegra.ph/file/8f5b77b680801bbccadae.jpg",
    "https://telegra.ph/file/f90a864cb9dd6418cade2.jpg",
    "https://telegra.ph/file/63e7ec2cb5eb5446ab575.jpg",
]


PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://telegra.ph/file/e1472ef2fb42abb378dd6.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://telegra.ph/file/cde0ed78452880a872bc6.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://telegra.ph/file/cde0ed78452880a872bc6.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://te.legra.ph/file/46f93d469ddc6e4a38e80.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://te.legra.ph/file/46f93d469ddc6e4a38e80.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://te.legra.ph/file/46f93d469ddc6e4a38e80.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://te.legra.ph/file/46f93d469ddc6e4a38e80.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://te.legra.ph/file/46f93d469ddc6e4a38e80.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://te.legra.ph/file/a44ac871100a1aabb360f.jpg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://te.legra.ph/file/a44ac871100a1aabb360f.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://te.legra.ph/file/a44ac871100a1aabb360f.jpg",
)


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

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "AnonX/assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "AnonX/assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "AnonX/assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "AnonX/assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "AnonX/assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "AnonX/assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "AnonX/assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "AnonX/assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "AnonX/assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print(
        "[KYA RE LAVDE] - BOHOT FONT LAGANE KA SHAUKH HAI. JAA PHIR LUCKY KO APNI CHUMT DEKE AA"
    )
