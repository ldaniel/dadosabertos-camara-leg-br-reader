import json
from pymongo import MongoClient

client = MongoClient(port=27017)
#serverStatusResult = db.command("serverStatus")
#pprint(serverStatusResult)
db = client.dadosabertos
collection = db.deputados

with open('../data/json/response_deputados.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

    for deputado in data['dados']:
        collection.insert_one(deputado)
