import json
import logging

from modules.color_tally   import ColorTally
from modules.cache_manager import ConnectionCache
from modules.api_client    import ApiClient

cache     = ConnectionCache()
apiClient = ApiClient()
success   = {"statusCode": 200}
logger    = logging.getLogger("socket_logger")
logger.setLevel(logging.DEBUG)

def connect(event, context):
    cache.cacheConnection(event['requestContext']['connectionId'])
    return success

def disconnect(event, context):
    cache.evictConnection(event['requestContext']['connectionId'])
    return success

def defaultMessage(event, context):
    logger.warning(f'invalid action type event: {event}')
    apiClient.send(event['requestContext']['connectionId'], {
      'event': 'error',
      'message': 'invalid action type'
    })

    return success

def vote(event, context):
    response = {'event': 'success'}
    try:
        payload = json.loads(event['body'])
        ColorTally().tally(payload['color'])
    except ValueError:
        logger.error(f"invalid color specified {payload['color']}")
        response = {
            'event': 'error',
            'message': 'invalid vote option'
        }
    
    apiClient.send(event['requestContext']['connectionId'], response)
    _spamUpdates()
    return success

def inquire(event, context):
    apiClient.send(event['requestContext']['connectionId'], {
        'event': 'success',
        'body': json.dumps(ColorTally().getTally())
    })
    return success

def _spamUpdates():
    for connectionId in cache.getConnections():
        apiClient.send(connectionId.decode("utf-8"), {
            'event': 'success',
            'body': json.dumps(ColorTally().getTally())
        })