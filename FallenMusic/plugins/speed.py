from pyrogram import filters
from pyrogram.types import Message
from config import MUSIC_BOT_NAME, BANNED_USERS, adminlist
from FallenMusic import app
from FallenMusic.core.call import Fallen
from FallenMusic.misc import SUDOERS, db
from FallenMusic.utils import AdminRightsCheck
from FallenMusic.utils.database.memorydatabase import is_active_chat, is_nonadmin_chat
from FallenMusic.utils.decorators.language import languageCB
from FallenMusic.utils.inline.play import close_keyboard
from FallenMusic.utils.inline.speed import speed_markup
from strings import get_command

checker = []

SEEK_COMMAND = get_command("SEEK_COMMAND")
@app.on_message(
    filters.command(["speed"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def playback(cli, message: Message, _, chat_id):
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text(_["admin_35"])
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await message.reply_text(_["admin_35"])
    upl = speed_markup(_, chat_id)
    return await message.reply_text(
        f"**{MUSIC_BOT_NAME} sᴘᴇᴇᴅ ʙᴜᴛᴛᴏɴꜱ**\n\nʏᴏᴜ ᴄᴀɴ ᴄʜᴀɴɢᴇ ᴛʜᴇ sᴘᴇᴇᴅ ᴏғ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠᴄ.",
        reply_markup=upl,
    )
@app.on_callback_query(filters.regex("SpeedUP") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat, speed = callback_request.split("|")
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_6"], show_alert=True)
    is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
    if not is_non_admin:
        if CallbackQuery.from_user.id not in SUDOERS:
            admins = adminlist.get(CallbackQuery.message.chat.id)
            if not admins:
                return await CallbackQuery.answer(_["admin_18"], show_alert=True)
            else:
                if CallbackQuery.from_user.id not in admins:
                    return await CallbackQuery.answer(_["admin_19"],show_alert=True)
    playing = db.get(chat_id)
    if not playing:
        return await CallbackQuery.answer(_["queue_2"], show_alert=True)
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await CallbackQuery.answer(_["admin_35"], show_alert=True)
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await CallbackQuery.answer(_["admin_35"], show_alert=True)
    checkspeed = (playing[0]).get("speed")
    if checkspeed:
        if str(checkspeed) == str(speed):
            if str(speed) == str("1.0"):
                speed = "ɴᴏʀᴍᴀʟ"
            return await CallbackQuery.answer(
                f"» ᴀʟʀᴇᴀᴅʏ ᴘʟᴀʏɪɴɢ ᴏɴ {speed} sᴘᴇᴇᴅ.",
                show_alert=True,
            )
    else:
        if str(speed) == str("1.0"):
            return await CallbackQuery.answer(
                f"» ᴀʟʀᴇᴀᴅʏ ᴘʟᴀʏɪɴɢ ᴏɴ {speed} sᴘᴇᴇᴅ.",
                show_alert=True,
            )
    if chat_id in checker:
        return await CallbackQuery.answer(
            "» sᴏᴍᴇᴏɴᴇ ɪs ᴀʟsᴏ ᴛʀʏɪɴɢ ᴛᴏ ᴄᴏɴᴛʀᴏʟ ᴛʜᴇ sᴘᴇᴇᴅ ᴘᴀɴᴇʟ, ʟᴇᴍᴍᴇ ᴄᴏᴍᴘʟᴇᴛᴇ ʜɪs ᴏʀᴅᴇʀ ғɪʀsᴛ.",
            show_alert=True,
        )
    else:
        checker.append(chat_id)
    mystic = await app.send_message(
        CallbackQuery.message.chat.id,
        text=f"» ᴄʜᴀɴɢɪɴɢ ᴛʜᴇ sᴘᴇᴇᴅ ᴏғ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.\n\n**ᴄʜᴀɴɢᴇᴅ ʙʏ :** {CallbackQuery.from_user.mention}",
        reply_markup=close_keyboard
    )
    try:
        await Fallen.speedup_stream(
            chat_id,
            file_path,
            speed,
            playing
        )
    except Exception as e:
        print(e)
        if chat_id in checker:
            checker.remove(chat_id)
        return await mystic.edit_text(
            "**ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇ sᴘᴇᴇᴅ ᴏғ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.",
            reply_markup=close_keyboard
        )
    if chat_id in checker:
        checker.remove(chat_id)
    await mystic.edit_text(
        f"» ᴄʜᴀɴɢᴇᴅ ᴛʜᴇ sᴘᴇᴇᴅ ᴏғ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴛᴏ `{speed}x`\n\nᴄʜᴀɴɢᴇᴅ ʙʏ : {CallbackQuery.from_user.mention}",
        reply_markup=close_keyboard
    )
