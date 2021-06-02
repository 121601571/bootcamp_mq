import urllib
from urllib import request
import json
import io
import os
import asyncio
import aiohttp
import redis
import redistuil
import io


def getres(name):
    host_env = os.environ.get('REVIEW_HOST', 'host.docker.internal')

    host = 'http://'+ host_env  + ':9998'
    try:
        name = name.decode('ascii')
    except:
        return
    url = host + "/api/v1/averageRatings/%s/?format=json" % (name)

    with request.urlopen(url) as f:
        data = f.read()
        str1 = data.decode('utf-8')
        redistuil.setLocalCache(name, json.loads(str1))

    return str1


async def getaysncres(session, url):
    async with session.get(url) as resp:
        res1 = await resp.json()
        return res1


async def getresMain(name):
    res = redistuil.getRankingStatus(name)
    if res !=  {}:
        return res


    async with aiohttp.ClientSession() as session:
        host_env = os.environ.get('REVIEW_HOST', 'host.docker.internal')
        host = 'http://' + host_env + ':9998'

        #host = os.environ.get('REVIEW_HOST', 'http://host.docker.internal:9998/')
        url = host + "/api/v1/averageRatings/%s/?/" % (name)
        tasks = []
        tasks.append(asyncio.ensure_future(getaysncres(session, url)))
        reslist = await  asyncio.gather(*tasks)
        # for i in reslist:
        #     print(i)
        # return 'abc'
        # [i for i in reslist]
        redistuil.setLocalCache(name, reslist )
        return reslist

if __name__ == '__main__':
    pass
    # res = getres('aa')
    # print(res)
    # a =  getresMain('aa')
    res  = asyncio.run(getresMain('liyi2'))
    print(res)