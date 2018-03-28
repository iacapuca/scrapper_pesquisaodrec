import requests
import csv
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pprint
import json
import config
import time



client = MongoClient(config.mongoURL)
db = client.ameciclo
pesquisa = db.pesquisa_od


for doc in pesquisa.find({"protocolo": ''}):
    protocolo = None
    errors = None
    r = requests.post(config.URL, data=doc)
    print (r.history)
    id = doc["_id"]
    print (id)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        errors = soup.find('ul', attrs={'class':'messages__list'}).text.strip()
    except(RuntimeError, TypeError, NameError, AttributeError):
        print("Nenhum erro encontrado.")
    if errors is not None:
        print (errors)
    try:
        protocolo = soup.em.string
    except(RuntimeError, TypeError, NameError, AttributeError):
        print("Não foi possivel encontrar protocolo, possivel erro de preenchimento.")
    if protocolo is not None:
        print(protocolo)
        pesquisa.update_one({'_id':id},{'$set':{'protocolo': protocolo}})
    time.sleep(180)
