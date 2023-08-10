from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 ꜱᴜᴘᴘᴏʀᴛ 🥀",
                url="https://t.me/FallenSupport",
            ),
            InlineKeyboardButton(
                text="✨ ᴄʟᴏsᴇ ✨", callback_data="close"
            ),
        ],
    ]
    return buttons

def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✯ ᴄʟᴏsᴇ ✯",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
