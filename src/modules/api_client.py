import boto3
import json
import os

class ApiClient():
    def __init__(self):
        apiId  = os.environ['WEBSOCKET_API_ID']
        region = os.environ['AWS_REGION']
        stage  = os.environ['STAGE']
        url    = f'https://{apiId}.execute-api.{region}.amazonaws.com/{stage}'
        
        self.client = boto3.client('apigatewaymanagementapi', endpoint_url=url)

    def send(self, connectionId, message):
        dumped     = json.dumps(message)
        binMessage = bytes(dumped, 'utf-8')
        self.client.post_to_connection(
            Data         = binMessage,
            ConnectionId = connectionId)
    
    def deregister(self, connectionId):
        self.client.delete_connection(ConnectionId = connectionId)
