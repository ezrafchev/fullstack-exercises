
# Exercício 28 - Implementação de Autenticação JWT na API de Categorias de Produtos

from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

categories = []

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return jsonify({'message': 'Could not verify!'}), 401

@app.route('/categories', methods=['GET'])
@token_required
def get_categories():
    return jsonify(categories)

@app.route('/categories', methods=['POST'])
@token_required
def create_category():
    category = request.get_json()
    categories.append(category)
    return jsonify(category), 201

@app.route('/categories/<int:category_id>', methods=['GET'])
@token_required
def get_category(category_id):
    category = next((c for c in categories if c['id'] == category_id), None)
    if category is None:
        return jsonify({'error': 'Categoria não encontrada'}), 404
    return jsonify(category)

@app.route('/categories/<int:category_id>', methods=['PUT'])
@token_required
def update_category(category_id):
    category = next((c for c in categories if c['id'] == category_id), None)
    if category is None:
        return jsonify({'error': 'Categoria não encontrada'}), 404
    data = request.get_json()
    category.update(data)
    return jsonify(category)

@app.route('/categories/<int:category_id>', methods=['DELETE'])
@token_required
def delete_category(category_id):
    global categories
    categories = [c for c in categories if c['id'] != category_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

