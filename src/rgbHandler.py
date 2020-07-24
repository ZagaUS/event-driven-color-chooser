import json

from lib.color_tally.color_tally import ColorTally

def rgb(event, context):
    payload = json.loads(event['body'])
    ColorTally().tally(payload['color'])

    return {
        "statusCode": 200
    }

def votes(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(ColorTally().getTally())
    }