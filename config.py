import  os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1745816793:AAGxQggoHrGB2EWTzXmCUoLMD85s4KgyHDY")
APP_ID = int(os.environ.get("API_ID", 2158704))
API_HASH = os.environ.get("API_HASH", "227f3bd8c1d7fc3ecfa243e1a85dd2fa")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001231683570)
BOT_USERNAME = os.environ.get("BOT_USERNAME", "testleonvibot")
SESSION_NAME = os.environ.get("SESSION_NAME", "LeoYTDownloaderBot")
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1069002447))
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Naviyaa:navi18572@cluster0.swycj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001560862542))

youtube_next_fetch = 0  # time in minute


EDIT_TIME = 5
