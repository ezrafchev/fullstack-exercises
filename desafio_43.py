
from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Dados de exemplo
cupons = [
    {"id": 1, "codigo": "DESCONTO10", "descricao": "10% de desconto em todos os produtos", "valor": "10%", "validade": "31/12/2023"},
    {"id": 2, "codigo": "FRETEGRATIS", "descricao": "Frete grátis para compras acima de R$100", "valor": "R$0", "validade": "30/06/2023"}
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

# Rota para listar todos os cupons
@app.route('/cupons', methods=['GET'])
@token_required
def listar_cupons():
    return jsonify(cupons)

# Rota para obter um cupom pelo ID
@app.route('/cupons/<int:id>', methods=['GET'])
@token_required
def obter_cupom(id):
    cupom = next((cupom for cupom in cupons if cupom["id"] == id), None)
    return jsonify(cupom) if cupom else ('', 404)

# Rota para criar um novo cupom
@app.route('/cupons', methods=['POST'])
@token_required
def criar_cupom():
    novo_cupom = request.get_json()
    novo_cupom["id"] = len(cupons) + 1
    cupons.append(novo_cupom)
    return jsonify(novo_cupom), 201

# Rota para atualizar um cupom existente
@app.route('/cupons/<int:id>', methods=['PUT'])
@token_required
def atualizar_cupom(id):
    cupom = next((cupom for cupom in cupons if cupom["id"] == id), None)
    if cupom:
        dados_atualizados = request.get_json()
        cupom.update(dados_atualizados)
        return jsonify(cupom)
    return ('', 404)

# Rota para excluir um cupom
@app.route('/cupons/<int:id>', methods=['DELETE'])
@token_required
def excluir_cupom(id):
    global cupons
    cupons = [cupom for cupom in cupons if cupom["id"] != id]
    return ('', 204)

if __name__ == '__main__':
    app.run(port=5000)

