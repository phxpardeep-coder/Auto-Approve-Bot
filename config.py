import os
from typing import List

API_ID = os.environ.get("API_ID", "23231578")
API_HASH = os.environ.get("API_HASH", "6016ef2dc043865f26667d89719b2c7e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8388780172:AAEHmbonE1oTzo8ArUj0dhwdMP6LtYm9SHk")
ADMIN = int(os.environ.get("ADMIN", "6960971297"))
PICS = (os.environ.get("PICS", "")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003153138847"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "False").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://Phxpardeep233:phx11234@cluster0.oykmvgo.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Phxpardeep233")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-100******** -100*********").split())) # Add Multiple channel ids
