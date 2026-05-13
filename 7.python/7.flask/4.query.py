from flask import Flask, jsonify, request

app = Flask(__name__)

people = [
    {"name": "James", "age": 24, "phone": "010-1234-5678"},
    {"name": "Emma", "age": 31, "phone": "010-9876-5432"},
    {"name": "Daniel", "age": 28, "phone": "010-4567-8910"},
    {"name": "Sophia", "age": 22, "phone": "010-2222-3333"}
]

@app.route('/search')
def search_user():
    result = None

    #

    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)

