
# Exercise 43: Implement JWT Authentication in the Discount Coupons API

## Objective
Implement JWT (JSON Web Token) authentication in the discount coupons API created in Exercise 42.

## Instructions
1. Create a Python file named `exercise43.py`.
2. Use Flask and Flask-JWT-Extended to implement JWT authentication.
3. Protect the endpoints so that only authenticated users can access them.

## Example Code
Below is an example of how you can structure your Flask API with JWT authentication.

### Python (exercise43.py)
```python
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

coupons = [
    {'id': 1, 'code': 'SAVE10', 'description': 'Save 10% on your next purchase', 'expiration': '2023-12-31'},
    {'id': 2, 'code': 'FREESHIP', 'description': 'Free shipping on orders over $50', 'expiration': '2023-11-30'},
    {'id': 3, 'code': 'BOGO50', 'description': 'Buy one, get one 50% off', 'expiration': '2023-10-31'}
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

@app.route('/coupons', methods=['GET'])
@jwt_required()
def get_coupons():
    return jsonify(coupons)

@app.route('/coupons', methods=['POST'])
@jwt_required()
def create_coupon():
    new_coupon = request.get_json()
    new_coupon['id'] = len(coupons) + 1
    coupons.append(new_coupon)
    return jsonify(new_coupon), 201

@app.route('/coupons/<int:id>', methods=['GET'])
@jwt_required()
def get_coupon(id):
    coupon = next((coupon for coupon in coupons if coupon['id'] == id), None)
    if coupon is None:
        return jsonify({'error': 'Coupon not found'}), 404
    return jsonify(coupon)

@app.route('/coupons/<int:id>', methods=['PUT'])
@jwt_required()
def update_coupon(id):
    coupon = next((coupon for coupon in coupons if coupon['id'] == id), None)
    if coupon is None:
        return jsonify({'error': 'Coupon not found'}), 404
    updated_data = request.get_json()
    coupon.update(updated_data)
    return jsonify(coupon)

@app.route('/coupons/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_coupon(id):
    global coupons
    coupons = [coupon for coupon in coupons if coupon['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(port=5000)
```

## Explanation
- The Flask API now includes JWT authentication.
- The `/login` endpoint allows users to obtain a JWT token by providing valid credentials.
- The `@jwt_required()` decorator is used to protect the endpoints, ensuring that only authenticated users can access them.

Feel free to modify the code to suit your needs.

