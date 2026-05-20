from flask import Flask, render_template, request
from flask import redirect, url_for
from flask import session, flash

from datetime import timedelta

import sqlite3

DATABASE = 'profile.sqlite3'

app = Flask(__name__)
app.secret_key = 'my-random-key'
app.permanent_session_lifetime = timedelta(minutes=30)


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login_id TEXT NOT NULL UNIQUE,
            pw TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT
        )
    ''')

    conn.commit()
    conn.close()

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # 로그인 안 되어 있으면 로그인 페이지로 보내기
    # if 'user_id' not in session:
    #     return redirect(url_for('login'))

    user_id = session['user_id']

    conn = get_db_connection()
    cur = conn.cursor()

    # 수정 버튼을 눌러서 POST 요청이 들어온 경우
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        cur.execute('''
            UPDATE users
            SET name = ?, email = ?
            WHERE id = ?
        ''', (name, email, user_id))

        conn.commit()
        conn.close()

        flash('프로필이 수정되었습니다.')
        return redirect(url_for('profile'))

    # GET 요청이면 내 정보 조회
    cur.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cur.fetchone()

    conn.close()

    return render_template('profile.html', user=user)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)