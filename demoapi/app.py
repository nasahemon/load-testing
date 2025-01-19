from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/resource', methods=['GET'])
def get_resource():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/v1/resource', methods=['POST'])
def create_resource():
    data = request.json
    return jsonify({"message": "Resource created!", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True)

