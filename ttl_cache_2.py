from cachetools import cached, TTLCache
import time

@cached(cache=TTLCache(maxsize=5, ttl=1000))
def calc(a, b):
    if a == 1 and b ==1:
        print(a, b, a + b)
    return a + b

calc(1,1)
calc(1,2)
calc(1,3)
calc(1,4)
calc(1,5)
calc(1,6)
calc(1,1)

print("---case 2---")
@cached(cache=TTLCache(maxsize=10, ttl=1000))
def calc2(a, b):
    if a == 1 and b ==1:
        print(a, b, a + b)
    return a + b

calc2(1,1)
calc2(1,2)
calc2(1,3)
calc2(1,4)
calc2(1,5)
calc2(1,6)
calc2(1,1)
