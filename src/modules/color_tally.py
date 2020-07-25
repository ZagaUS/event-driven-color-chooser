import os
import redis
import uuid

from enum import Enum

class Color(Enum):
    r = 'r'
    g = 'g'
    b = 'b'

class ColorTally:
    
    def __init__(self, weight = 1, timeout = 30, maximum = 255, baselineColor = 85):
        self.voteWeight     = weight
        self.timeoutSeconds = timeout
        self.maximum        = maximum
        self.baselineColor  = baselineColor
        
        redisHost  = os.environ.get('REDIS_HOST')
        redisPort  = os.environ.get('REDIS_PORT')
        redisUrl   = f'redis://{redisHost}:{redisPort}'
        self.cache = redis.Redis.from_url(redisUrl)

    def getTally(self):
        totals = {
            Color.r.name: self._countVotes(Color.r),
            Color.g.name: self._countVotes(Color.g),
            Color.b.name: self._countVotes(Color.b)
        }
        totals['hex'] = self.calculateHex(totals)
        return totals 
    
    def calculateHex(self, totals):
        hash     = {}
        maxVotes = max(list(totals.values()) + [1])

        for item in totals.items():
            bounds        = self.maximum - self.baselineColor
            translated    = round(((item[1] / maxVotes) * bounds) + self.baselineColor)
            hash[item[0]] = format(translated, '02x')

        return f'#{hash[Color.r.name]}{hash[Color.g.name]}{hash[Color.b.name]}'
    
    def _countVotes(self, color):
        votes = self.cache.keys(f'{color.name}:*')
        return len(votes)

    def tally(self, color):
        id    = uuid.uuid1().hex
        key   = f'{Color(color).name}:{id}'
        self.cache.set(key, self.voteWeight)
        self.cache.expire(key, self.timeoutSeconds)