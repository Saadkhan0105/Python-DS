from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "<h1>Welcome to the Sample ToDo List App!</h1>"

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# POST create item (FIXED)
@app.route('/items', methods=['POST'])
def create_item():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": data['name'],
        "description": data.get('description', "")  # ✅ FIX HERE
    }

    items.append(new_item)
    return jsonify(new_item), 201

# PUT update item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()

    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])

    return jsonify(item)

# DELETE item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [i for i in items if i['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)