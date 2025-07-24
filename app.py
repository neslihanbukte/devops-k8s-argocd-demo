from flask import Flask, jsonify, Response
import psycopg2
import os
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)


REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn

@app.route('/')
def index():
    REQUEST_COUNT.inc()  
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT NOW()')
    result = cur.fetchone()
    conn.close()
    print("connected to postgresql, current time is:", result[0])
    return jsonify({'current_time': result[0].isoformat()})


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)