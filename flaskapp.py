from flask import Flask, jsonify

app=Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the home page!"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
