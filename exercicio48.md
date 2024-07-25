
# Exercise 48: Implement JWT Authentication in the Delivery Addresses API

## Objective
Implement JWT (JSON Web Token) authentication in the delivery addresses API created in Exercise 47.

## Instructions
1. Create a Python file named `exercise48.py`.
2. Use Flask and Flask-JWT-Extended to implement JWT authentication.
3. Protect the endpoints so that only authenticated users can access them.

## Example Code
Below is an example of how you can structure your Flask API with JWT authentication.

### Python (exercise48.py)
```python
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

addresses = [
    {'id': 1, 'street': '123 Main St', 'city': 'Anytown', 'state': 'CA', 'zip': '12345'},
    {'id': 2, 'street': '456 Oak St', 'city': 'Othertown', 'state': 'TX', 'zip': '67890'},
    {'id': 3, 'street': '789 Pine St', 'city': 'Sometown', 'state': 'NY', 'zip': '11223'}
]

users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/addresses', methods=['GET'])
@jwt_required()
def get_addresses():
    return jsonify(addresses)

@app.route('/addresses', methods=['POST'])
@jwt_required()
def create_address():
    new_address = request.get_json()
    new_address['id'] = len(addresses) + 1
    addresses.append(new_address)
    return jsonify(new_address), 201

@app.route('/addresses/<int:id>', methods=['GET'])
@jwt_required()
def get_address(id):
    address = next((address for address in addresses if address['id'] == id), None)
    if address is None:
        return jsonify({'error': 'Address not found'}), 404
    return jsonify(address)

@app.route('/addresses/<int:id>', methods=['PUT'])
@jwt_required()
def update_address(id):
    address = next((address for address in addresses if address['id'] == id), None)
    if address is None:
        return jsonify({'error': 'Address not found'}), 404
    updated_data = request.get_json()
    address.update(updated_data)
    return jsonify(address)

@app.route('/addresses/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_address(id):
    global addresses
    addresses = [address for address in addresses if address['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(port=5000)
```

## Explanation
- The Flask API now includes JWT authentication.
- The `/login` endpoint allows users to obtain a JWT token by providing valid credentials.
- The `@jwt_required()` decorator is used to protect the endpoints, ensuring that only authenticated users can access them.

Feel free to modify the code to suit your needs.

