import json

from lib.color_tally.color_tally import ColorTally

def rgb(event, context):
    responseCode = 200
    try:
        payload = json.loads(event['body'])
        ColorTally().tally(payload['color'])
    except ValueError:
        responseCode = 400
    
    return {
        "statusCode": responseCode
    }

def votes(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(ColorTally().getTally())
    }