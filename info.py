# Don't Remove Credit @prime3602
# Subscribe YouTube Channel For Amazing Bot @123telugfacts
# Ask Doubt on telegram @prime3602

import os
environ = os.environ
import re
id_pattern = re.compile(r'^-?\d+$')
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '20597576'))
API_HASH = environ.get('API_HASH', '9d3a1fbae5b3368cf8c62008d8a41e7d')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = environ.get('PICS', '').split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1876549409').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001977482249').split()]
AUTH_USERS = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://movieadda:nn56381373@movieadda.y7ntklw.mongodb.net/?retryWrites=true&w=majority&appName=movieadda")
DATABASE_NAME = environ.get('DATABASE_NAME', "movieadda")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))

# Your new channel and group links
GRP_LNK = environ.get('GRP_LNK', '(https://t.me/movie01request)')
CHNL_LNK = environ.get('CHNL_LNK', '(https://t.me/+mBGvu968HHdiNjE1)')
