
# Exercício 23 - Implementação de Autenticação JWT na API de Pedidos

from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

orders = []

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

@app.route('/orders', methods=['GET'])
@token_required
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
@token_required
def create_order():
    order = request.get_json()
    orders.append(order)
    return jsonify(order), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
@token_required
def get_order(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if order is None:
        return jsonify({'error': 'Pedido não encontrado'}), 404
    return jsonify(order)

@app.route('/orders/<int:order_id>', methods=['PUT'])
@token_required
def update_order(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if order is None:
        return jsonify({'error': 'Pedido não encontrado'}), 404
    data = request.get_json()
    order.update(data)
    return jsonify(order)

@app.route('/orders/<int:order_id>', methods=['DELETE'])
@token_required
def delete_order(order_id):
    global orders
    orders = [o for o in orders if o['id'] != order_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

