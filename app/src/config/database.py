from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
    URL = os.getenv("URL_DB")

    client = MongoClient(URL)
    db = client["marcos-estudos"]
    return db