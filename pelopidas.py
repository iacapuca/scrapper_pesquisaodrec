import mechanicalsoup

URL = "http://icps0517.recife.pe.gov.br/node/add/pesquisa-origem-destino-2016"

#Cria o objeto browser
browser = mechanicalsoup.StatefulBrowser()
browser.open(URL)
print(browser.get_url())
browser.set_verbose(2)
browser.select_form('form[action="/node/add/pesquisa-origem-destino-2016"]')
form = browser.select_form('form[action="/node/add/pesquisa-origem-destino-2016"]')
form.choose_submit('op')
browser["field_od16_sua_faixa_etaria[und]"] = "2"
browser["field_od16_possui_deficiencia_[und]"] = "2"
browser["field_od16_sexo[und]"] = "2"
browser["field_od16_endereco[und][0][postal_code]"] = "52071640"
browser["field_od16_endereco[und][0][thoroughfare]"] = "Rua de Apipucos"
browser["field_od16_endereco[und][0][dependent_locality]"] = "Monteiro"
browser["field_od16_endereco[und][0][locality]"] = "Recife"
browser["field_od16_endereco[und][0][administrative_area]"] = "PE"
browser["field_od16_possui_f_esco_fund_me[und]"] = "2"
browser["field_od16_renda_da_familia[und]"] = "7"
browser["field_od16_voce_trabalha_[und]"] = "2"
browser["field_od16_motivo_nao_trabalha[und]"] = "1"
browser["field_od16_ganha_bolsa_estudo[und]"] = "2"
browser["field_od16_voce_estuda_[und]"] = "1"
browser["field_od16_estuda_escol_ou_facul[und]"] = "2"
browser["field_descreva_faculdade_estuda[und][0][value]"] = "Escola Politecnica de Pernambuco"
browser["field_od16_sua_escolaridade[und]"] = "4"
browser["field_od16_hora_inicio_estudo[und]"] = "8"
browser["field_od16_minutos_inicio_estudo[und]"] = "0"
browser["field_od16_hora_fim_estudo[und]"] = "13"
browser["field_od16_minutos_fim_estudo[und]"] = "0"
browser["field_od16_onde_sai_para_aula[und]"] = "1"
browser["field_od16freq_aula_dessa_origem[und]"] = "4"
browser["field_od16_qt_tempo_leva_ir_aula[und]"] = "2"
browser["field_od16_modo_transp_aula[und]"] = "2"
browser["field_estaciona_bike_6[und]"] = "Em paraciclo do local onde trabalho"
browser["field_od16sempre_mesm_trans_aula[und]"] = "1"
browser["field_od16vc_foi_consulta_medica[und]"] = "2"
browser["field_od16_fez_compra_domestica_[und]"] = "2"
browser["field_od16_vc_procurou_servicos[und]"] = "2"
resp = browser.submit_selected()
print(browser.get_url())
print(resp.text)

