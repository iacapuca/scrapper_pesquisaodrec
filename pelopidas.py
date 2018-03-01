import mechanicalsoup
from bs4
import BeautifulSoup
import csv
import datetime
import itertools


data = open("data.csv", encoding = "utf8")
URL = "http://icps0517.recife.pe.gov.br/node/add/pesquisa-origem-destino-2016"

#Cria o objeto browser
browser = mechanicalsoup.StatefulBrowser()
browser.open(URL)
print(browser.get_url())
browser.set_verbose(2)
browser.select_form('form[action="/node/add/pesquisa-origem-destino-2016"]')
form = browser.select_form('form[action="/node/add/pesquisa-origem-destino-2016"]')
form.choose_submit('op')
for registro in csv.DictReader(data):
    if not registro['protocolo']:
        for field, value in zip_longest(fields, values):
            browser[field] = str(registro[value])
            browser.launch_browser()
            resp = browser.submit_selected()
            print(browser.get_url())
            soup = BeautifulSoup(resp.text, 'html.parser')
            protocolo = soup.em.string
            print(protocolo)
            saida = csv.writer(
                open('pelopidas.csv',
                    mode = 'a',
                    encoding = 'utf8'),
                lineterminator = '\n'
            )
            saida.writerow([str(datetime.datetime.now()), protocolo])
    else:
        print ("Arquivo já protocolado")
