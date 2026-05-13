from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>안녕하세요!</h1>'

users = [
    {'name':'lee','age': 17}
]
@app.route('/user/<int:age>')
def get_user_by_age(age):
    user = []
    for u in users

if __name__ == '__main__':
    app.run()