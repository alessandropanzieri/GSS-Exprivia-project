from flask import Flask, jsonify

server = Flask(__name__)

@server.get("/")
def index():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == "__main__": server.run(debug = True)
