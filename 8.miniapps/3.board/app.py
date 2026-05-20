from flask import Flask, send_from_directory, request, jsonify
from database import MyDatabase

app = Flask(__name__)
db = MyDatabase()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/create', methods=['POST'])
def create():
    # 프론트에서 보낸 JSON 데이터 받기
    data = request.get_json()

    title = data.get('title')
    message = data.get('message')

    # 빈 값 체크
    if not title or not message:
        return jsonify({'result': 'fail', 'message': '제목과 내용을 입력하세요'}), 400

    sql = "INSERT INTO board (title, message) VALUES (?, ?)"

    db.execute(sql, (title, message))
    db.commit()

    return jsonify({'result': 'success'})

@app.route('/list')
def list():
    return jsonify({'result': 'success'})

@app.route('/delete', methods=['POST'])
def delete():
    return jsonify({'result': 'success'})

@app.route('/modify', methods=['POST'])
def modify():
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(debug=True)