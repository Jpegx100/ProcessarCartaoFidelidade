from flask import Flask, request
from db import pagamentos

app = Flask("processarcartaofidelidade")

@app.route("/", methods=['POST'])
def adicionar_pagamento():
    try:
        json = request.json
        if cartao_valido(json):
            pagamentos.insert(json)
            return "OK", 200
        else: 
            return "Nem todos os campos foram repassados", 400
    except Exception as e:
        return "Erro interno ao servidor", 500

def cartao_valido(cartao):
    # return False
    chaves = ["numero_cartao", "validade", "cvv", "bandeira", "valor", "unidade", "latitude", "longitude"]
    chaves_cartao = cartao.keys()
    for c in chaves:
        if c not in chaves_cartao:
            return False
    return True

app.run(debug=True, use_reloader=True)

