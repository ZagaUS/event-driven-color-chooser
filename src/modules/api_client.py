import logging

logger  = logging.getLogger("api_client_logger")
logger.setLevel(logging.DEBUG)

class ApiClient():
    
    def send(self, event, message):
        logger.warning(f'sending message: {message}')