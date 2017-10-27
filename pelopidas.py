import mechanicalsoup
from bs4 import BeautifulSoup
import csv
import datetime

data = open("data.csv", encoding="utf8")
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
    browser["field_od16_sua_faixa_etaria[und]"] = str(registro["faixa_etaria"])
    browser["field_od16_possui_deficiencia_[und]"] = str(registro["possui_deficiencia"])
    browser["field_od16_sexo[und]"] = str(registro["sexo"])
    browser["field_od16_endereco[und][0][postal_code]"] = str(registro["cep"])
    browser["field_od16_endereco[und][0][thoroughfare]"] = str(registro["rua"])
    browser["field_od16_endereco[und][0][dependent_locality]"] = str(registro["bairro"])
    browser["field_od16_endereco[und][0][locality]"] = str(registro["cidade"])
    browser["field_od16_endereco[und][0][administrative_area]"] = str(registro["uf"])
    browser["field_od16_possui_f_esco_fund_me[und]"] = str(registro["filho_escola"])
    browser["field_od16_renda_da_familia[und]"] = str(registro["renda_familia"])
    browser["field_od16_voce_trabalha_[und]"] = str(registro["trabalha"])
    browser["field_od16_motivo_nao_trabalha[und]"] = str(registro["motivo_não_trabalha"])
    browser["field_od16_ganha_bolsa_estudo[und]"] = str(registro["ganha_bolsa"])
    browser["field_od16_voce_estuda_[und]"] = str(registro["estuda"])
    browser["field_od16_estuda_escol_ou_facul[und]"] = str(registro["faculdade_ou_escola"])
    browser["field_descreva_faculdade_estuda[und][0][value]"] = str(registro["nome_faculdade"])
    browser["field_od16_sua_escolaridade[und]"] = str(registro["escolaridade"])
    browser["field_od16_hora_inicio_estudo[und]"] = str(registro["hora_inicio"])
    browser["field_od16_minutos_inicio_estudo[und]"] = str(registro["minuto_inicio"])
    browser["field_od16_hora_fim_estudo[und]"] = str(registro["hora_fim"])
    browser["field_od16_minutos_fim_estudo[und]"] = str(registro["minuto_fim"])
    browser["field_od16_onde_sai_para_aula[und]"] = str(registro["onde_sai_aula"])
    browser["field_od16freq_aula_dessa_origem[und]"] = str(registro["freq_aula"])
    browser["field_od16_qt_tempo_leva_ir_aula[und]"] = str(registro["qt_tempo_leva"])
    browser["field_od16_modo_transp_aula[und]"] = str(registro["modo_transporte"])
    browser["field_estaciona_bike_6[und]"] = str(registro["estaciona_bike"])
    browser["field_od16sempre_mesm_trans_aula[und]"] = str(registro["sempre_mesmo_modal"])
    browser["field_od16vc_foi_consulta_medica[und]"] = str(registro["consulta_medica"])
    browser["field_od16_fez_compra_domestica_[und]"] = str(registro["compra_domestica"])
    browser["field_od16_vc_procurou_servicos[und]"] = str(registro["servicos"])
    browser.launch_browser()
    resp = browser.submit_selected()
    print(browser.get_url())
    soup = BeautifulSoup(resp.text, 'html.parser')
    protocolo = soup.em.string
    print(protocolo)
    saida = csv.writer(
            open('pelopidas.csv',
                mode='a',
                encoding='utf8'),
            lineterminator = '\n'
            )
    saida.writerow([str(datetime.datetime.now()), protocolo])
