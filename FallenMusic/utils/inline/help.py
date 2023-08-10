from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text="◁",
            callback_data=f"Pages Back|0",
        ),
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text="▷",
            callback_data=f"Pages Forw|1",
        ),
    ]
    mark = second
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Aᴅᴍɪɴ",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="Aᴜᴛʜ",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="Bʀᴏᴀᴅᴄᴀsᴛ",
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Bʟᴀᴄᴋʟɪsᴛ",
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text="Bʟ-Cʜᴀᴛ",
                    callback_data="help_callback hb14",
                ),
                InlineKeyboardButton(
                    text="C-Pʟᴀʏ",
                    callback_data="help_callback hb15",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Gʙᴀɴ",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="Pɪɴɢ",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="Pʟᴀʏ",
                    callback_data="help_callback hb8",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Pʟᴀʏʟɪsᴛ",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="Sᴛᴀʀᴛ",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="Sᴜᴅᴏ",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_panel_1(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Sᴘᴇᴇᴅ",
                callback_data="help_callback hb13",
            ),
            InlineKeyboardButton(
                text="Lᴏᴏᴘ",
                callback_data="help_callback hb5",
            ),
            InlineKeyboardButton(
                text="Sᴇᴇᴋ",
                callback_data="help_callback hb17",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Sʜᴜғғʟᴇ",
                callback_data="help_callback hb16",
            ),
            InlineKeyboardButton(
                text="Vɪᴅᴇᴏᴄʜᴀᴛs",
                callback_data="help_callback hb10",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data="settings_back_umm",
            ),
        ],
    ]
    return buttons


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                )
            ],
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄ ʜᴇʟᴩ ❄",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
