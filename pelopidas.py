import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pprint
import config
import time



client = MongoClient(config.mongoURL)
db = client.ameciclo
pesquisa = db.pesquisa_od


for doc in pesquisa.find({"protocolo": ''}):
    print ("Iniciando um novo envio!")
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
        print('\x1b[6;30;42m' + "Nenhum erro encontrado." + '\x1b[0m')
    if errors is not None:
        print (errors)
    try:
        protocolo = soup.em.string
    except(RuntimeError, TypeError, NameError, AttributeError):
        print('\x1b[1;37;41m' +"Não foi possivel encontrar protocolo, possivel erro de preenchimento." '\x1b[0m')
    if protocolo is not None:
        print(protocolo)
        pesquisa.update_one({'_id':id},{'$set':{'protocolo': protocolo}})
        print('\x1b[6;30;42m' + 'Envio com Sucesso!' + '\x1b[0m')
    time.sleep(36)
