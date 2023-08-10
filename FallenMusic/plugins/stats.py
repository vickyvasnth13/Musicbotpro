import asyncio
import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message
from pytgcalls.__version__ import __version__ as pytgver

import config
from config import BANNED_USERS, MUSIC_BOT_NAME
from strings import get_command
from FallenMusic import YouTube, app
from FallenMusic.core.userbot import assistants
from FallenMusic.misc import SUDOERS, pymongodb
from FallenMusic.plugins import ALL_MODULES
from FallenMusic.utils.database import (get_global_tops,
                                       get_particulars, get_queries,
                                       get_served_chats,
                                       get_served_users, get_sudoers,
                                       get_top_chats, get_topp_users)
from FallenMusic.utils.decorators.language import language, languageCB
from FallenMusic.utils.inline.stats import (back_stats_buttons,
                                           back_stats_markup,
                                           get_stats_markup,
                                           overallback_stats_markup,
                                           stats_buttons,
                                           top_ten_stats_markup)

loop = asyncio.get_running_loop()

# Commands
STATS_COMMAND = get_command("STATS_COMMAND")


@app.on_message(
    filters.command(STATS_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def stats_global(client, message: Message, _):
    upl = stats_buttons(
        _, True if message.from_user.id in SUDOERS else False
    )
    await message.reply_photo(
        photo=config.STATS_IMG_URL,
        caption=_["gstats_11"].format(config.MUSIC_BOT_NAME),
        reply_markup=upl,
    )
                    
@app.on_callback_query(filters.regex("TopOverall") & ~BANNED_USERS)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    if what != "s":
        upl = overallback_stats_markup(_)
    else:
        upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_8"].format(config.MUSIC_BOT_NAME))
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    total_queries = await get_queries()
    blocked = len(BANNED_USERS)
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    assistant = len(assistants)
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yes"
    else:
        ass = "No"
    cm = config.CLEANMODE_DELETE_MINS
    text = f"""<b><u>{MUSIC_BOT_NAME} sᴛᴀᴛs ᴀɴᴅ ɪɴғᴏ :</u></b>

**ᴀssɪsᴛᴀɴᴛs :** {assistant}
**ᴀssɪsᴛᴀɴᴛ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ :** {ass}
**ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs :** {blocked} 
**ᴄʜᴀᴛs :** {served_chats}
**ᴜꜱᴇʀꜱ :** {served_users}
**suᴅᴏᴇʀs :** {sudoers} 

**ᴘʟᴀʏ ᴅᴜʀᴀᴛɪᴏɴ ʟɪᴍɪᴛ :** {play_duration} ᴍɪɴs
**sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪᴍɪᴛ :** {song} ᴍɪɴs"""
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )


@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def overall_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id not in SUDOERS:
        return await CallbackQuery.answer(
            "Only for Sudo Users", show_alert=True
        )
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    if what != "s":
        upl = overallback_stats_markup(_)
    else:
        upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_8"].format(config.MUSIC_BOT_NAME))
    sc = platform.system()
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = (
        str(round(psutil.virtual_memory().total / (1024.0**3)))
        + "ɢʙ"
    )
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)} ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)} ᴍʜᴢ"
    except:
        cpu_freq = "Unable to Fetch"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    mod = len(ALL_MODULES)
    db = pymongodb
    call = db.command("dbstats")
    datasize = call["dataSize"] / 1024
    datasize = str(datasize)
    storage = call["storageSize"] / 1024
    objects = call["objects"]
    collections = call["collections"]
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    total_queries = await get_queries()
    blocked = len(BANNED_USERS)
    sudoers = len(await get_sudoers())
    text = f""" **ʙᴏᴛ sᴛᴀᴛs ᴀɴᴅ ɪɴғᴏ:**

**ɪᴍᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇs:** {mod}
**ᴘʟᴀᴛғᴏʀᴍ:** {sc}
**ʀᴀᴍ:** {ram}
**ᴘʜʏsɪᴄᴀʟ ᴄᴏʀᴇs:** {p_core}
**ᴛᴏᴛᴀʟ ᴄᴏʀᴇs:** {t_core}
**ᴄᴘᴜ ғʀᴇǫᴜᴇɴᴄʏ:** {cpu_freq}

**ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** {pyver.split()[0]}
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** {pyrover}
**ᴘʏ-TɢCᴀʟʟs ᴠᴇʀsɪᴏɴ :** {pytgver}

**sᴛᴏʀᴀɢᴇ ᴀᴠᴀɪʟ:** {total[:4]} ɢʙ
**sᴛᴏʀᴀɢᴇ ᴜsᴇᴅ:** {used[:4]} ɢʙ
**sᴛᴏʀᴀɢᴇ ʟᴇғᴛ:** {free[:4]} ɢʙ

**sᴇʀᴠᴇᴅ ᴄʜᴀᴛs:** {served_chats} 
**sᴇʀᴠᴇᴅ ᴜsᴇʀs:** {served_users} 
**ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs:** {blocked} 
**sᴜᴅᴏ ᴜsᴇʀs:** {sudoers} 

**ᴛᴏᴛᴀʟ ᴅʙ sɪᴢᴇ:** {datasize[:6]} ᴍᴘ
**ᴛᴏᴛᴀʟ ᴅʙ ᴛᴛᴏʀᴀɢᴇ:** {storage} ᴍᴘ
**ᴛᴏᴛᴀʟ ᴅʙ ᴄᴏʟʟᴇᴄᴛɪᴏɴs:** {collections}
**ᴛᴏᴛᴀʟ ᴅʙ ᴋᴇʏs:** {objects}
**ᴛᴏᴛᴀʟ ʙᴏᴛ ǫᴜᴇʀɪᴇs:** `{total_queries} `
    """
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )
