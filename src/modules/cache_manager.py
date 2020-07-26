import os
import redis
import uuid

class CacheManager:
    
    def __init__(self):
        redisHost  = os.environ.get('REDIS_HOST')
        redisPort  = os.environ.get('REDIS_PORT')
        redisUrl   = f'redis://{redisHost}:{redisPort}'
        self.cache = redis.Redis.from_url(redisUrl)
    
class VoteCache(CacheManager):

    def __init__(self, weight = 1, timeout = 30):
        CacheManager.__init__(self)
        self.voteWeight     = weight
        self.timeoutSeconds = timeout

    def countVotes(self, key):
        votes = self.cache.keys(f'{key}:*')
        return len(votes)

    def tally(self, key):
        id    = uuid.uuid1().hex
        key   = f'{key}:{id}'
        self.cache.set(key, self.voteWeight)
        self.cache.expire(key, self.timeoutSeconds)

class ConnectionCache(CacheManager):
    
    def cacheConnection(self, connectionId):
        key = f'connection:{connectionId}'
        self.cache.set(key, connectionId)

    def evictConnection(self, connectionId):
        key = f'connection:{connectionId}'
        self.cache.delete(key)
    
    def getConnections(self):
        return self.cache.mget('connection:*')