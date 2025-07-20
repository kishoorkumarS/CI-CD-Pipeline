from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello from CI/CD Pipeline Web App'})

@app.route('/data')
def data():
    return jsonify({'value': random.randint(1, 100)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
