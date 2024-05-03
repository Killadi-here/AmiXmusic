from AmiXmusic.core.bot import Anony
from AmiXmusic.core.dir import dirr
from AmiXmusic.core.git import git
from AmiXmusic.core.userbot import Userbot
from AmiXmusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
