from flask import Flask, jsonify
from dotenv import load_dotenv
from app.dynamo_db import get_secret

load_dotenv()

app = Flask(__name__)

@app.route('/secret', methods=['GET'])
def secret():
    return jsonify({"secret_code": get_secret()})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "container": "https://hub.docker.com/r/cybencyben/thedoctor-app",
        "project": "https://github.com/Cyben/devops-challenge"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)