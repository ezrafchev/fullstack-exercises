
# Exercise 42: Create a RESTful API to Manage Discount Coupons (CRUD)

## Objective
Create a RESTful API to manage discount coupons. The API should support Create, Read, Update, and Delete (CRUD) operations.

## Instructions
1. Create a Python file named `exercise42.py`.
2. Use Flask to create the API.
3. Implement the following endpoints:
    - `GET /coupons`: Get a list of all coupons.
    - `POST /coupons`: Create a new coupon.
    - `GET /coupons/<id>`: Get details of a specific coupon.
    - `PUT /coupons/<id>`: Update a specific coupon.
    - `DELETE /coupons/<id>`: Delete a specific coupon.

## Example Code
Below is an example of how you can structure your Flask API.

### Python (exercise42.py)
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

coupons = [
    {'id': 1, 'code': 'SAVE10', 'description': 'Save 10% on your next purchase', 'expiration': '2023-12-31'},
    {'id': 2, 'code': 'FREESHIP', 'description': 'Free shipping on orders over $50', 'expiration': '2023-11-30'},
    {'id': 3, 'code': 'BOGO50', 'description': 'Buy one, get one 50% off', 'expiration': '2023-10-31'}
]

@app.route('/coupons', methods=['GET'])
def get_coupons():
    return jsonify(coupons)

@app.route('/coupons', methods=['POST'])
def create_coupon():
    new_coupon = request.get_json()
    new_coupon['id'] = len(coupons) + 1
    coupons.append(new_coupon)
    return jsonify(new_coupon), 201

@app.route('/coupons/<int:id>', methods=['GET'])
def get_coupon(id):
    coupon = next((coupon for coupon in coupons if coupon['id'] == id), None)
    if coupon is None:
        return jsonify({'error': 'Coupon not found'}), 404
    return jsonify(coupon)

@app.route('/coupons/<int:id>', methods=['PUT'])
def update_coupon(id):
    coupon = next((coupon for coupon in coupons if coupon['id'] == id), None)
    if coupon is None:
        return jsonify({'error': 'Coupon not found'}), 404
    updated_data = request.get_json()
    coupon.update(updated_data)
    return jsonify(coupon)

@app.route('/coupons/<int:id>', methods=['DELETE'])
def delete_coupon(id):
    global coupons
    coupons = [coupon for coupon in coupons if coupon['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(port=5000)
```

## Explanation
- The Flask API provides endpoints to manage discount coupons.
- The `GET /coupons` endpoint returns a list of all coupons.
- The `POST /coupons` endpoint creates a new coupon.
- The `GET /coupons/<id>` endpoint returns details of a specific coupon.
- The `PUT /coupons/<id>` endpoint updates a specific coupon.
- The `DELETE /coupons/<id>` endpoint deletes a specific coupon.

Feel free to modify the code to suit your needs.

