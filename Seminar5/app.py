from flask import Flask, render_template, request, jsonify
from modules.user import User

app = Flask(__name__)


def validate_user_data(data):
    required_fields = ["id", "name", "email", "password"]

    for field in required_fields:
        if field not in data:
            return False

    return True


@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if not validate_user_data(data):
        return jsonify({"message": "Invalid data"}), 400

    user = User(data["id"], data["name"], data["email"], data["password"])
    user.save()

    return jsonify({"message": "User added successfully"}), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = User.find_by_id(user_id)

    if user is None:
        return jsonify({"message": "User not found"}), 404

    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.password = data.get("password", user.password)

    if not user.validate():
        return jsonify({"message": "Invalid user data"}), 500

    user.save()

    return jsonify({"message": "User updated successfully"}), 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.find_by_id(user_id)

    if user is None:
        return jsonify({"message": "User not found"}), 404

    user.delete()

    return jsonify({"message": "User deleted successfully"}), 200


@app.route("/add_user", methods=["GET"])
def add_user_page():
    return render_template("add_user.html")


@app.route("/users", methods=["GET"])
def list_users():
    users = User.get_all()
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
