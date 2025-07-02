import boto3
import os

def get_secret():
    code_name = os.getenv("CODE_NAME", "thedoctor")
    table_name = "devops-challenge"

    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION", "eu-west-1")
    )
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={"code_name": code_name})
    return response['Item'].get('secret_code', 'NOT_FOUND')