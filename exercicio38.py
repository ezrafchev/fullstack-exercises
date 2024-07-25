
# Exercício 38 - Implementação de Autenticação JWT na API de Avaliações de Produtos

from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

reviews = []

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

@app.route('/reviews', methods=['GET'])
@token_required
def get_reviews():
    return jsonify(reviews)

@app.route('/reviews', methods=['POST'])
@token_required
def create_review():
    review = request.get_json()
    reviews.append(review)
    return jsonify(review), 201

@app.route('/reviews/<int:review_id>', methods=['GET'])
@token_required
def get_review(review_id):
    review = next((r for r in reviews if r['id'] == review_id), None)
    if review is None:
        return jsonify({'error': 'Avaliação não encontrada'}), 404
    return jsonify(review)

@app.route('/reviews/<int:review_id>', methods=['PUT'])
@token_required
def update_review(review_id):
    review = next((r for r in reviews if r['id'] == review_id), None)
    if review is None:
        return jsonify({'error': 'Avaliação não encontrada'}), 404
    data = request.get_json()
    review.update(data)
    return jsonify(review)

@app.route('/reviews/<int:review_id>', methods=['DELETE'])
@token_required
def delete_review(review_id):
    global reviews
    reviews = [r for r in reviews if r['id'] != review_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

