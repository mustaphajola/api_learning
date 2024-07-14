from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "name": "Mustapha Jolaade",
        "user_id": user_id,
        "email": "john.doe@gmail.com"
    }

    extra = request.args.get("extra")

    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

@app.route("/create-user/<user_id>", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)
