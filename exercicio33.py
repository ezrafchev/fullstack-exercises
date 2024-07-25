
# Exercício 33 - Implementação de Autenticação JWT na API de Comentários de Produtos

from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

comments = []

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

@app.route('/comments', methods=['GET'])
@token_required
def get_comments():
    return jsonify(comments)

@app.route('/comments', methods=['POST'])
@token_required
def create_comment():
    comment = request.get_json()
    comments.append(comment)
    return jsonify(comment), 201

@app.route('/comments/<int:comment_id>', methods=['GET'])
@token_required
def get_comment(comment_id):
    comment = next((c for c in comments if c['id'] == comment_id), None)
    if comment is None:
        return jsonify({'error': 'Comentário não encontrado'}), 404
    return jsonify(comment)

@app.route('/comments/<int:comment_id>', methods=['PUT'])
@token_required
def update_comment(comment_id):
    comment = next((c for c in comments if c['id'] == comment_id), None)
    if comment is None:
        return jsonify({'error': 'Comentário não encontrado'}), 404
    data = request.get_json()
    comment.update(data)
    return jsonify(comment)

@app.route('/comments/<int:comment_id>', methods=['DELETE'])
@token_required
def delete_comment(comment_id):
    global comments
    comments = [c for c in comments if c['id'] != comment_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

