from flask import Flask, render_template

app = Flask(__name__)

#사용자 로컬 db

users = [
    {"name": "Alice", "id": "alice01", "pw": "a1234"},
    {"name": "Brian", "id": "brian02", "pw": "b5678"},
    {"name": "Chris", "id": "chris03", "pw": "c9012"}
]

@app.route('/')
def home()
    return render_template('index.html')

