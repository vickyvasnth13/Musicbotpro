from FallenMusic.core.bot import FallenMusic
from FallenMusic.core.dir import dirr
from FallenMusic.core.git import git
from FallenMusic.core.userbot import Userbot
from FallenMusic.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = FallenMusic()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
