import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16232265"))
    API_HASH = os.environ.get("API_HASH", "6d91b2dc7ae916ac955d3e66d11f4c3f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
