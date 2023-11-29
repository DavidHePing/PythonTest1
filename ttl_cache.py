from cachetools import cached, TTLCache
import time

@cached(cache=TTLCache(maxsize=10, ttl=5))
def calc(a, b):
    print(a, b, a + b)
    return a + b

calc(1,2)
calc(1,2)
calc(1,2)

time.sleep(5)
calc(1,2)
calc(1,2)
calc(1,2)
