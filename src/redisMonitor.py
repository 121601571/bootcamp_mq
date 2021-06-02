import time
import redis
import json
import httputil
import asyncio

def getCon():
    pass
    r = redis.Redis(host='host.docker.internal', port=6379, db=0)
    return r

con1 = getCon()


def generatePS(con1):
    ps = con1.pubsub()
    ps.psubscribe('review-channel')
    return ps

def handler(msg):
    if msg['channel'] == b'review-channel':
        pass
        #res = asyncio.run(httputil.getresMain(msg['data']))
        res =httputil.getres(msg['data'])
        print(res)


if __name__ == '__main__':
    pass
    ps = generatePS(con1)
    while True:
        ms = ps.get_message()
        if ms:
            pass
            handler(ms)
        time.sleep(0.1)