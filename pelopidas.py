import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pprint
import config
import time



client = MongoClient(config.mongoURL)
db = client.ameciclo
pesquisa = db.pesquisa_od

contador_protocolo = 0

print("Incializando o programa...")
for doc in pesquisa.find({"protocolo": ''}):
    print ("Iniciando um novo envio!")
    protocolo = None
    errors = None
    error = None
    r = requests.post(config.URL, data=doc)
    print (r.history)
    id = doc["_id"]
    print (id)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        errors = soup.find('ul', attrs={'class':'messages__list'}).text.strip()
        error = soup.find('div', attrs={'class':'messages--error'}).text.strip()
        print(error.replace('Menssagem de erro', ''))
    except(RuntimeError, TypeError, NameError, AttributeError):
        print('\x1b[6;30;42m' + "Nenhum erro encontrado." + '\x1b[0m')
    if error is not None:
        error = error.replace('Menssagem de erro', '')
        print(error)
        if doc['errors'] is None:
            pesquisa.update_one({'_id':id},{'$set':{'errors': error}})
            print('\x1b[1;37;41m' +"Erro inserido na base de dados." '\x1b[0m')
        else:
            print('\x1b[1;37;41m' +"Este erro já foi inserido na base de dados." '\x1b[0m')
    if errors is not None:
        print (errors)
        if doc['errors'] is None:
            pesquisa.update_one({'_id':id},{'$set':{'errors': errors}})
            print('\x1b[1;37;41m' +"Erro inserido na base de dados." '\x1b[0m')
        else:
            print('\x1b[1;37;41m' +"Este erro já foi inserido na base de dados." '\x1b[0m')
    try:
        protocolo = soup.em.string
    except(RuntimeError, TypeError, NameError, AttributeError):
        print('\x1b[1;37;41m' +"Não foi possivel encontrar protocolo, possivel erro de preenchimento." '\x1b[0m')
    if protocolo is not None:
        print(protocolo)
        contador_protocolo +=1
        pesquisa.update_one({'_id':id},{'$set':{'protocolo': protocolo}})
        print('\x1b[6;30;42m' + 'Envio com Sucesso!' + '\x1b[0m')
    #time.sleep(1)
print("Envios encerrados")
print(contador_protocolo)