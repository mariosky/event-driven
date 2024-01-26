import redis
import os
import time

r = redis.StrictRedis( host=os.environ['REDIS_HOST'], port=6379, decode_responses=True, db=0)
#r = redis.StrictRedis( host='localhost', decode_responses=True, port=6379, db=0)

redis_ready = False

#intenta hasta que este listo el contenedor
while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print("waiting for redis")
        time.sleep(3)

print("setup: redis alive")


while True:
    _,palabra = r.brpop('input-queue')
    print(palabra.upper())
    r.lpush('upper-queue', palabra.upper())
    time.sleep(1)