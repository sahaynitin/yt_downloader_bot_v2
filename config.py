import  os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME")
SESSION_NAME = os.environ.get("SESSION_NAME", "LeoYTDownloaderBot")
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1069002447))
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
MONGODB_URI = os.environ.get("MONGODB_URI", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
© 2021 GitHub, Inc.

youtube_next_fetch = 0  # time in minute


EDIT_TIME = 5
