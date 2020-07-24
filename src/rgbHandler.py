import json

from lib.color_tally.color_tally import ColorTally

def rgb(event, context):
    payload = json.load(event.body)
    print(f'COLOR: {payload.color}')
    
    tally = ColorTally()
    tally.tally(payload.color)

    return {
        "statusCode": 200
    }

def votes(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(ColorTally().getTally())
    }