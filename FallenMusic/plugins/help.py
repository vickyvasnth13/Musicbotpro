from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

import config
from config import BANNED_USERS
from strings import get_command, get_string, helpers
from FallenMusic import app
from FallenMusic.misc import SUDOERS
from FallenMusic.utils import help_pannel
from FallenMusic.utils.database import get_lang, is_commanddelete_on
from FallenMusic.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from FallenMusic.utils.inline.help import (help_back_markup, help_panel_1,
                                          private_help_panel)

### Command
HELP_COMMAND = get_command("HELP_COMMAND")


@app.on_message(
    filters.command(HELP_COMMAND)
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_callback_query(
    filters.regex("settings_back_helper") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        if update.message.photo:
            await update.edit_message_text(
                _["help_1"], reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                _["help_1"], reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_sticker("CAACAgUAAxkBAAIjVmKPYTFByKZlCo9d8mUv8QVAJEw7AAL9BQACiy14VGoQxOCDfE1KJAQ")
        await update.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["help_1"], reply_markup=keyboard)


@app.on_callback_query(
    filters.regex("settings_back_umm") & ~BANNED_USERS
)
async def helper_umm(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        if update.message.photo:
            await update.edit_message_text(
                _["help_1"], reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                _["help_1"], reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_sticker("CAACAgUAAxkBAAIjVmKPYTFByKZlCo9d8mUv8QVAJEw7AAL9BQACiy14VGoQxOCDfE1KJAQ")
        await update.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["help_1"], reply_markup=keyboard)

@app.on_callback_query(filters.regex("Pages") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    state, pages = callback_request.split("|")
    pages = int(pages)
    if state == "Forw":
        if pages == 1:
            buttons = help_panel_1(_)
        if pages == 0:
            buttons = help_pannel(_)
    if state == "Back":
        if pages == 1:
            buttons = help_pannel(_)
        if pages == 0:
            buttons = help_panel_1(_)
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except:
        return
        
        
@app.on_message(
    filters.command(HELP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await app.send_photo(
        message.chat.id,
        photo=config.START_IMG_URL,
        caption=_["help_2"], protect_content=True, reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb9":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "sɪʀ ɪ ᴀᴍ ᴠᴇʀʏ sᴏʀʀʏ 🥺\nᴛʜɪs ʙᴜᴛᴛᴏɴ ɪs ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs ❣︎", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                helpers.HELP_9, reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            helpers.HELP_1, reply_markup=keyboard
        )
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            helpers.HELP_2, reply_markup=keyboard
        )
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            helpers.HELP_3, reply_markup=keyboard
        )
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            helpers.HELP_4, reply_markup=keyboard
        )
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(
            helpers.HELP_5, reply_markup=keyboard
        )
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(
            helpers.HELP_6, reply_markup=keyboard
        )
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(
            helpers.HELP_7, reply_markup=keyboard
        )
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(
            helpers.HELP_8, reply_markup=keyboard
        )
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(
            helpers.HELP_10, reply_markup=keyboard
        )
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(
            helpers.HELP_11, reply_markup=keyboard
        )
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(
            helpers.HELP_12, reply_markup=keyboard
        )
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(
            helpers.HELP_13, reply_markup=keyboard
        )
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(
            helpers.HELP_14, reply_markup=keyboard
        )
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(
            helpers.HELP_15, reply_markup=keyboard
        )
    elif cb == "hb16":
        await CallbackQuery.edit_message_text(
            helpers.HELP_16, reply_markup=keyboard
        )
    elif cb == "hb17":
        await CallbackQuery.edit_message_text(
            helpers.HELP_17, reply_markup=keyboard
        )
