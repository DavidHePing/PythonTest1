from cachetools import TTLCache
import time

# Create an LRU cache with a max size of 100
cache = TTLCache(maxsize=100, ttl=2)

# Set values with integer keys
cache[1] = "one"
print(cache.get(1))
time.sleep(2)
print(cache.get(1))