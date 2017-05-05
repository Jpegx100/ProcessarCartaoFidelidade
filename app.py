from flask import Flask, request

app = Flask("processarcartaofidelidade")

@app.route("/", methods=['POST'])
def processar():
    json = request.json
    if cartao_valido(json):
        return "OK", 200
    else: 
        return "Nem todos os campos foram repassados", 400

def cartao_valido(cartao):
    chaves = ["numero_cartao", "validade", "cvv", "bandeira", "valor", "unidade", "latitude", "longitude"]
    chaves_cartao = cartao.keys()
    for c in chaves:
        if c not in chaves_cartao:
            return False
    return True

app.run(debug=True, use_reloader=True)

