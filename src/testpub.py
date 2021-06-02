import time

import redis
import json


def getCon():
    pass
    r = redis.Redis(host='localhost', port=6379, db=0)
    return r

con1 = getCon()


if __name__ == '__main__':
    pass
    ps = con1.pubsub()
    #payload with format {k,v}
    samplePl = json.dumps({'contact':'liyi', 'handler': '123'})
    con1.publish('review-channel', samplePl)
