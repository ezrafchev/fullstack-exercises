
# Exercise 47: Create a RESTful API to Manage Delivery Addresses (CRUD)

## Objective
Create a RESTful API to manage delivery addresses. The API should support Create, Read, Update, and Delete (CRUD) operations.

## Instructions
1. Create a Python file named `exercise47.py`.
2. Use Flask to create the API.
3. Implement the following endpoints:
    - `GET /addresses`: Get a list of all addresses.
    - `POST /addresses`: Create a new address.
    - `GET /addresses/<id>`: Get details of a specific address.
    - `PUT /addresses/<id>`: Update a specific address.
    - `DELETE /addresses/<id>`: Delete a specific address.

## Example Code
Below is an example of how you can structure your Flask API.

### Python (exercise47.py)
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

addresses = [
    {'id': 1, 'street': '123 Main St', 'city': 'Anytown', 'state': 'CA', 'zip': '12345'},
    {'id': 2, 'street': '456 Oak St', 'city': 'Othertown', 'state': 'TX', 'zip': '67890'},
    {'id': 3, 'street': '789 Pine St', 'city': 'Sometown', 'state': 'NY', 'zip': '11223'}
]

@app.route('/addresses', methods=['GET'])
def get_addresses():
    return jsonify(addresses)

@app.route('/addresses', methods=['POST'])
def create_address():
    new_address = request.get_json()
    new_address['id'] = len(addresses) + 1
    addresses.append(new_address)
    return jsonify(new_address), 201

@app.route('/addresses/<int:id>', methods=['GET'])
def get_address(id):
    address = next((address for address in addresses if address['id'] == id), None)
    if address is None:
        return jsonify({'error': 'Address not found'}), 404
    return jsonify(address)

@app.route('/addresses/<int:id>', methods=['PUT'])
def update_address(id):
    address = next((address for address in addresses if address['id'] == id), None)
    if address is None:
        return jsonify({'error': 'Address not found'}), 404
    updated_data = request.get_json()
    address.update(updated_data)
    return jsonify(address)

@app.route('/addresses/<int:id>', methods=['DELETE'])
def delete_address(id):
    global addresses
    addresses = [address for address in addresses if address['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(port=5000)
```

## Explanation
- The Flask API provides endpoints to manage delivery addresses.
- The `GET /addresses` endpoint returns a list of all addresses.
- The `POST /addresses` endpoint creates a new address.
- The `GET /addresses/<id>` endpoint returns details of a specific address.
- The `PUT /addresses/<id>` endpoint updates a specific address.
- The `DELETE /addresses/<id>` endpoint deletes a specific address.

Feel free to modify the code to suit your needs.

