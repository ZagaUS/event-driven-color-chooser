import json

from lib.color_tally.color_tally import ColorTally

def getRgb(event, context):
    
    print('event')
    print(json.dumps(event))
    
    tally = ColorTally()
    tally.tally('r')
    body = tally.getTally()
    
    print(f'BODY: {body}')

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
