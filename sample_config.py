import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7580377760:AAHIDVIkbMwlXPpCw1ht35w695LKsA01Xu4")

    APP_ID = int(os.environ.get("APP_ID", 22487047))

    API_HASH = os.environ.get("API_HASH", "7fea27db5c011ef2ed75074c4a195610")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "8059380015").split())
