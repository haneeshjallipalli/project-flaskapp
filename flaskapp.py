from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, this is the root endpoint!")

@app.route('/health')
def health():
    return jsonify(status="OK", message="App is healthy!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
