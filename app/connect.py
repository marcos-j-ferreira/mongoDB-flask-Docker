from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("URL_DB")

client = MongoClient(uri)
db = client["marcos-estudos"]
colecao = db["usuarios"]


client = MongoClient(uri, server_api=ServerApi('1'))

def connect():
    try:
        client.admin.command('ping')
        return True
    except Exception as e:
        print(e)

def firtData():

    if not connect():
        print("banco de dados não conectado ")

    try:
        user = {
            'name':"Luiz",
            'age':20
        }

        result = colecao.insert_one(user)

        print({"id_inserido": str(result.inserted_id)})
    
    except Exception as e:
        print("Erro", e)

firtData()