
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados de exemplo
enderecos = [
    {"id": 1, "nome": "João Silva", "endereco": "Rua das Flores, 123", "cidade": "São Paulo", "estado": "SP", "cep": "01000-000"},
    {"id": 2, "nome": "Maria Oliveira", "endereco": "Avenida Brasil, 456", "cidade": "Rio de Janeiro", "estado": "RJ", "cep": "20000-000"}
]

# Rota para listar todos os endereços
@app.route('/enderecos', methods=['GET'])
def listar_enderecos():
    return jsonify(enderecos)

# Rota para obter um endereço pelo ID
@app.route('/enderecos/<int:id>', methods=['GET'])
def obter_endereco(id):
    endereco = next((endereco for endereco in enderecos if endereco["id"] == id), None)
    return jsonify(endereco) if endereco else ('', 404)

# Rota para criar um novo endereço
@app.route('/enderecos', methods=['POST'])
def criar_endereco():
    novo_endereco = request.get_json()
    novo_endereco["id"] = len(enderecos) + 1
    enderecos.append(novo_endereco)
    return jsonify(novo_endereco), 201

# Rota para atualizar um endereço existente
@app.route('/enderecos/<int:id>', methods=['PUT'])
def atualizar_endereco(id):
    endereco = next((endereco for endereco in enderecos if endereco["id"] == id), None)
    if endereco:
        dados_atualizados = request.get_json()
        endereco.update(dados_atualizados)
        return jsonify(endereco)
    return ('', 404)

# Rota para excluir um endereço
@app.route('/enderecos/<int:id>', methods=['DELETE'])
def excluir_endereco(id):
    global enderecos
    enderecos = [endereco for endereco in enderecos if endereco["id"] != id]
    return ('', 204)

if __name__ == '__main__':
    app.run(port=5000)

