import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pprint
import config
import time

r = requests.get('http://localhost:3000/')
soup = BeautifulSoup(r.text, 'html.parser')
error = soup.find('div', attrs={'class':'messages--error'}).text.strip()
print(error.replace('Menssagem de erro', ''))

