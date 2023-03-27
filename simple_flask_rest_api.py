from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane.doe@example.com"},
    {"id": 3, "name": "Bob Smith", "email": "bob.smith@example.com"},
]

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET a user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": f"User with ID {user_id} not found"})

# POST a new user
@app.route("/users", methods=["POST"])
def create_user():
    new_user = request.get_json()
    new_user["id"] = max(user["id"] for user in users) + 1
    users.append(new_user)
    return jsonify(new_user)

# PUT/UPDATE an existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        user.update(request.get_json())
        return jsonify(user)
    else:
        return jsonify({"error": f"User with ID {user_id} not found"})

# DELETE an existing user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
