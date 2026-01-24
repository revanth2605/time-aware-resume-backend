import os
from pymongo import MongoClient
from urllib.parse import quote_plus

USERNAME = os.getenv("revanth")
PASSWORD = os.getenv("revanth12@")
HOST = os.getenv("cluster0.y5ewexh.mongodb.net")

encoded_username = quote_plus(USERNAME)
encoded_password = quote_plus(PASSWORD)

MONGO_URI = (
    f"mongodb+srv://{encoded_username}:{encoded_password}"
    f"@{HOST}/?retryWrites=true&w=majority"
)

client = MongoClient(MONGO_URI)
