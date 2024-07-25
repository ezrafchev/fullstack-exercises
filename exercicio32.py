
# Exercício 32 - API RESTful para Gerenciamento de Comentários de Produtos (CRUD)

from flask import Flask, request, jsonify

app = Flask(__name__)

comments = []

@app.route('/comments', methods=['GET'])
def get_comments():
    return jsonify(comments)

@app.route('/comments', methods=['POST'])
def create_comment():
    comment = request.get_json()
    comments.append(comment)
    return jsonify(comment), 201

@app.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = next((c for c in comments if c['id'] == comment_id), None)
    if comment is None:
        return jsonify({'error': 'Comentário não encontrado'}), 404
    return jsonify(comment)

@app.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    comment = next((c for c in comments if c['id'] == comment_id), None)
    if comment is None:
        return jsonify({'error': 'Comentário não encontrado'}), 404
    data = request.get_json()
    comment.update(data)
    return jsonify(comment)

@app.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    global comments
    comments = [c for c in comments if c['id'] != comment_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

