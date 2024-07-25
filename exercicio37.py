
# Exercício 37 - API RESTful para Gerenciamento de Avaliações de Produtos (CRUD)

from flask import Flask, request, jsonify

app = Flask(__name__)

reviews = []

@app.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify(reviews)

@app.route('/reviews', methods=['POST'])
def create_review():
    review = request.get_json()
    reviews.append(review)
    return jsonify(review), 201

@app.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = next((r for r in reviews if r['id'] == review_id), None)
    if review is None:
        return jsonify({'error': 'Avaliação não encontrada'}), 404
    return jsonify(review)

@app.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = next((r for r in reviews if r['id'] == review_id), None)
    if review is None:
        return jsonify({'error': 'Avaliação não encontrada'}), 404
    data = request.get_json()
    review.update(data)
    return jsonify(review)

@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    global reviews
    reviews = [r for r in reviews if r['id'] != review_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

