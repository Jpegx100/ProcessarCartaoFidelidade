import os
from db import pagamentos
from config import *
from datetime import datetime

def primeiro(iterable, condition = lambda x: True):
    """Retorna o primeiro item do Iterable que satisfizer a condição"""
    for i in iterable:
    	return dict(i)

def get_pagamento():
	"""Pega o primeiro pagamento do banco de dados e retorna-o como um dicionario, 
	ou None caso não existam pagamentos no banco de dados ou ocorra algum erro."""
	try:
		pagamento = pagamentos.find(_limit=1, order_by=['id'])
		return primeiro(pagamento)
	except Exception as e:
		print("Erro ao procurar registro: "+str(e))
		return None

def criar_arquivo_pagamento(pagamento, caminho):
	"""Cria arquivo temporario do pagamento e salva-o no caminho especificado."""
	nome_arq = caminho+'v'+str(pagamento['numero_cartao'])+'.vnd'
	try:
		arq = open(nome_arq, 'w')
		arq.write(
				str(pagamento['numero_cartao'])+'\n'+
				str(pagamento['valor'])+'\n'+
				str('1')+'\n'+
				str(pagamento['unidade'])+'\n'
			)
		arq.close()
		return True
	except Exception as e:
		print("Erro ao gravar arquivo: "+str(e))
		return False

def get_arquivo_resposta(timeout, caminho):
	"""Espera a criação do arquivo de resposta até que haja timeout."""
	tempo_inicial = datetime.now()
	while (datetime.now()-tempo_inicial).total_seconds() < timeout:
		try:
			arq = open(caminho+'resp.vnd', 'r')
			return arq.read()
		except Exception as e:
			continue
	return None

def apaga_arquivos(numero_cartao, caminho):
	arquivo = caminho+'v'+str(numero_cartao)+'.vnd'
	resposta = caminho+'resp.vnd'
	if os.path.isfile(arquivo):
		os.remove(arquivo)
	if os.path.isfile(resposta):
		os.remove(resposta)

def notifica_erro_resposta(url_erro, pagamento_id):
	"""Faz requisicao para informar erro ao servidor do ITAXI"""
	print("ERRRROO")
	pass

def notifica_sucesso_resposta(url_sucesso, pagamento_id):
	"""Faz requisicao para informar sucesso ao servidor do ITAXI"""
	print("SUCESOOO")
	pass

def remove_pagamento(pagamento_id):
	"""Apaga o registro do pagamento do banco de dados"""
	try:
		pagamentos.delete(id=pagamento_id)
	except Exception as e:
		print("Erro ao remover registro: "+str(e))

if __name__ == "__main__":
	while True:
		pagamento = get_pagamento()
		if pagamento:
			print("Processando pagamento: "+str(pagamento['id']))
			if not criar_arquivo_pagamento(pagamento, CAMINHO):
				notifica_erro_resposta(URL_NOTIFICA_ERRO, pagamento['id'])
				continue
			
			resposta = get_arquivo_resposta(TIMEOUT, CAMINHO)
			if not resposta:
				notifica_erro_resposta(URL_NOTIFICA_ERRO, pagamento['id'])
			else:
				notifica_sucesso_resposta(URL_NOTIFICA_SUCESSO, pagamento['id'])
			remove_pagamento(pagamento['id'])
			apaga_arquivos(pagamento['numero_cartao'], CAMINHO)