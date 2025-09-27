from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "26407665"
# -------------------------------------------------------------
API_HASH = "f10822a551f38b26ee1179e1a6515e01"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "8158429107"))
SUPPORT_GRP = "promXSH"
UPDATE_CHNL = "promXSH"
OWNER_USERNAME = "hye_babu"
