from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("DB_NAME", "test")
DB_USER = os.environ.get("DB_USER", "user")
DB_PASS = os.environ.get("DB_PASS", "password")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json.get('data')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO info (data) VALUES (%s)", (data,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "success"})

@app.route('/list', methods=['GET'])
def list_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM info")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
