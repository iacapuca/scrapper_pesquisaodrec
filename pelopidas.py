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
    r = requests.post(config.URL, data=doc)
    print (r.history)
    soup = BeautifulSoup(r.text, 'html.parser')
    protocolo = soup.em.string
    print(protocolo)
    time.sleep(5)
