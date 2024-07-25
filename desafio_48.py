
from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Dados de exemplo
enderecos = [
    {"id": 1, "nome": "João Silva", "endereco": "Rua das Flores, 123", "cidade": "São Paulo", "estado": "SP", "cep": "01000-000"},
    {"id": 2, "nome": "Maria Oliveira", "endereco": "Avenida Brasil, 456", "cidade": "Rio de Janeiro", "estado": "RJ", "cep": "20000-000"}
]

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-tokens')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

# Rota para listar todos os endereços
@app.route('/enderecos', methods=['GET'])
@token_required
def listar_enderecos():
    return jsonify(enderecos)

# Rota para obter um endereço pelo ID
@app.route('/enderecos/<int:id>', methods=['GET'])
@token_required
def obter_endereco(id):
    endereco = next((endereco for endereco in enderecos if endereco["id"] == id), None)
    return jsonify(endereco) if endereco else ('', 404)

# Rota para criar um novo endereço
@app.route('/enderecos', methods=['POST'])
@token_required
def criar_endereco():
    novo_endereco = request.get_json()
    novo_endereco["id"] = len(enderecos) + 1
    enderecos.append(novo_endereco)
    return jsonify(novo_endereco), 201

# Rota para atualizar um endereço existente
@app.route('/enderecos/<int:id>', methods=['PUT'])
@token_required
def atualizar_endereco(id):
    endereco = next((endereco for endereco in enderecos if endereco["id"] == id), None)
    if endereco:
        dados_atualizados = request.get_json()
        endereco.update(dados_atualizados)
        return jsonify(endereco)
    return ('', 404)

# Rota para excluir um endereço
@app.route('/enderecos/<int:id>', methods=['DELETE'])
@token_required
def excluir_endereco(id):
    global enderecos
    enderecos = [endereco for endereco in enderecos if endereco["id"] != id]
    return ('', 204)

if __name__ == '__main__':
    app.run(port=5000)

