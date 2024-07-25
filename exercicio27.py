
# Exercício 27 - API RESTful para Gerenciamento de Categorias de Produtos (CRUD)

from flask import Flask, request, jsonify

app = Flask(__name__)

categories = []

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories)

@app.route('/categories', methods=['POST'])
def create_category():
    category = request.get_json()
    categories.append(category)
    return jsonify(category), 201

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = next((c for c in categories if c['id'] == category_id), None)
    if category is None:
        return jsonify({'error': 'Categoria não encontrada'}), 404
    return jsonify(category)

@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = next((c for c in categories if c['id'] == category_id), None)
    if category is None:
        return jsonify({'error': 'Categoria não encontrada'}), 404
    data = request.get_json()
    category.update(data)
    return jsonify(category)

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    global categories
    categories = [c for c in categories if c['id'] != category_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

