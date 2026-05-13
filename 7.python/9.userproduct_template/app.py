from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

users = {
    1: {"id": 1, "name": "홍길동", "email": "hong@example.com"},
    2: {"id": 2, "name": "김철수", "email": "kim@example.com"},
    3: {"id": 3, "name": "이영희", "email": "lee@example.com"},
    4: {"id": 4, "name": "박민수", "email": "park@example.com"},
    5: {"id": 5, "name": "최지우", "email": "choi@example.com"},
}

products = {
    101: {"id": 101, "name": "Laptop", "price": 1200},
    102: {"id": 102, "name": "Keyboard", "price": 80},
    103: {"id": 103, "name": "Mouse", "price": 40},
    104: {"id": 104, "name": "Monitor", "price": 300},
    105: {"id": 105, "name": "Headset", "price": 150},
}

@app.route("/")
def home():
    return render_template(
        "index.html",
        users=users,
        products=products
    )


@app.route("/user")
def get_users():
    return jsonify(list(users.values()))


@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)

    if user is None:
        return jsonify({"message": "사용자를 찾을 수 없습니다."}), 404

    return jsonify(user)


@app.route("/product")
def get_products():
    product_id = request.args.get("id")
    name = request.args.get("name")

    if product_id:
        product_id = int(product_id)
        product = products.get(product_id)

        if product is None:
            return jsonify({"message": "상품을 찾을 수 없습니다."}), 404

        return jsonify(product)

    if name:
        result = [
            product for product in products.values()
            if product["name"].lower() == name.lower()
        ]

        if not result:
            return jsonify({"message": "상품을 찾을 수 없습니다."}), 404

        return jsonify(result)

    return jsonify(list(products.values()))


if __name__ == "__main__":
    app.run(debug=True)