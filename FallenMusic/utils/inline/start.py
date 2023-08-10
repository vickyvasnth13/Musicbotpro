from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHANNEL, SUPPORT_GROUP

def start_pannel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(
                text="Sᴜᴘᴘᴏʀᴛ",
                url=f"https://t.me/{SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text="Cʜᴀɴɴᴇʟ",
                url=f"https://t.me/AlishaUpdates",
            )
        ],
        ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            ),
        ],
        [
            InlineKeyboardButton(text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="settings_back_helper")
        ],
        [
            InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", callback_data="support"),
            InlineKeyboardButton(text="Sᴏᴜʀᴄᴇ", callback_data="gib_source")
        ]
    ]
    return buttons

close_key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]
            ]
        )
