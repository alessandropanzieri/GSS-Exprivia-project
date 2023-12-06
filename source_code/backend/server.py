from flask import Flask, jsonify
from flask_cors import CORS

server = Flask(__name__)
CORS(server)

@server.get("/")
def index():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == "__main__": server.run(debug = True)