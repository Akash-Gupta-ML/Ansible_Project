from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_conn():
    conn = mysql.connector.connect(
        host='10.81.4.243',
        database='ansibledb',
        user='akash',
        password='akash'
    )
    return conn

@app.route('/')
def index():
    try:
        connection = get_db_conn()
        cursor = connection.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        connection.close()
        return jsonify({'current_time': result[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

