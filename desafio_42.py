
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados de exemplo
cupons = [
    {"id": 1, "codigo": "DESCONTO10", "descricao": "10% de desconto em todos os produtos", "valor": "10%", "validade": "31/12/2023"},
    {"id": 2, "codigo": "FRETEGRATIS", "descricao": "Frete grátis para compras acima de R$100", "valor": "R$0", "validade": "30/06/2023"}
]

# Rota para listar todos os cupons
@app.route('/cupons', methods=['GET'])
def listar_cupons():
    return jsonify(cupons)

# Rota para obter um cupom pelo ID
@app.route('/cupons/<int:id>', methods=['GET'])
def obter_cupom(id):
    cupom = next((cupom for cupom in cupons if cupom["id"] == id), None)
    return jsonify(cupom) if cupom else ('', 404)

# Rota para criar um novo cupom
@app.route('/cupons', methods=['POST'])
def criar_cupom():
    novo_cupom = request.get_json()
    novo_cupom["id"] = len(cupons) + 1
    cupons.append(novo_cupom)
    return jsonify(novo_cupom), 201

# Rota para atualizar um cupom existente
@app.route('/cupons/<int:id>', methods=['PUT'])
def atualizar_cupom(id):
    cupom = next((cupom for cupom in cupons if cupom["id"] == id), None)
    if cupom:
        dados_atualizados = request.get_json()
        cupom.update(dados_atualizados)
        return jsonify(cupom)
    return ('', 404)

# Rota para excluir um cupom
@app.route('/cupons/<int:id>', methods=['DELETE'])
def excluir_cupom(id):
    global cupons
    cupons = [cupom for cupom in cupons if cupom["id"] != id]
    return ('', 204)

if __name__ == '__main__':
    app.run(port=5000)

