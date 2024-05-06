from CUTEXMUSIC.core.bot import CUTEXBOT
from CUTEXMUSIC.core.dir import dirr
from CUTEXMUSIC.core.git import git
from CUTEXMUSIC.core.userbot import Userbot
from CUTEXMUSIC.misc import dbb, heroku, sudo
from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = CUTEXBOT()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

