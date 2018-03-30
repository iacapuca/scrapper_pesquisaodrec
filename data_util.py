import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pprint
import config
import time



client = MongoClient(config.mongoURL)
db = client.ameciclo
pesquisa = db.pesquisa_od


result = pesquisa.delete_many({"protocolo":''})
print(result.deleted_count)