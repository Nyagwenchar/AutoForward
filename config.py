import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "11406332"))
    API_HASH = os.environ.get("API_HASH", "2e6494826d5b4b8be07df1ad8f022286")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6199708079:AAE0eymVOAiBog2xQosqV5xWBqQ-sXD_jNc")
    BOT_SESSION = os.environ.get("BOT_SESSION", "")
    OWNER_ID = os.environ.get("OWNER_ID", "879440576")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://ghostier:ghostier@file-store.zbf7vts.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "file-store")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001866916365"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
