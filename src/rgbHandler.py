import json
import logging

from modules.color_tally import ColorTally

logger = logging.getLogger("rgb_logger")
logger.setLevel(logging.DEBUG)

def rgb(event, context):
    responseCode = 200
    try:
        payload = json.loads(event['body'])
        ColorTally().tally(payload['color'])
    except ValueError:
        logger.error(f"invalid color specified {payload['color']}")
        responseCode = 400
    
    return {
        "statusCode": responseCode
    }

def votes(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(ColorTally().getTally())
    }