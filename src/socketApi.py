import json
import logging

from modules.color_tally   import ColorTally
from modules.cache_manager import ConnectionCache
from modules.api_client    import ApiClient

cache   = ConnectionCache()
success = {"statusCode": 200}
logger  = logging.getLogger("socket_logger")
logger.setLevel(logging.DEBUG)

def connect(event, context):
    cache.cacheConnection(event['requestContext']['connectionId'])
    return success

def disconnect(event, context):
    cache.evictConnection(event['requestContext']['connectionId'])
    return success

def defaultMessage(event, context):
    logger.warning(f'invalid action type event: {event}')
    ApiClient().send(event, {
      'event': 'error',
      'message': 'invalid action type'
    })

    return success