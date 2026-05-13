from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return"""
<html>
    <head>
        <title>타이틀</title>
    </head>
    <body>
        <h1>안녕</h1>
    </body>
</html>
"""

if __name__=='__main__':
    app.run(debug=True)