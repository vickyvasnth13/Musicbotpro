from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup

from config import BANNED_USERS, PING_IMG_URL
from strings import get_command
from FallenMusic import app
from FallenMusic.core.call import Fallen
from FallenMusic.utils import bot_sys_stats
from FallenMusic.utils.decorators.language import language
from FallenMusic.utils.inline.play import start_pannel

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
)
@language
async def ping_com(client, message: Message, _):
    response = await app.send_photo(
        message.chat.id,
        photo=PING_IMG_URL,
        caption=_["ping_1"],
        protect_content=True,
    )
    start = datetime.now()
    name = (await app.get_me()).mention
    out = start_pannel(_, app.username)
    pytgping = await Fallen.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp, name, UP, RAM, CPU, DISK, pytgping
        ),
        reply_markup=InlineKeyboardMarkup(out)
    )
