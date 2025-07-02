from flask import Flask, jsonify
from dotenv import load_dotenv
import boto3
import os

load_dotenv()

app = Flask(__name__)

def get_secret():
    code_name = os.getenv("CODE_NAME", "theDoctor")
    table_name = "devops-challenge"

    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION", "eu-west-1")
    )
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={"codeName": code_name})
    return response['Item'].get('secretCode', 'NOT_FOUND')

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