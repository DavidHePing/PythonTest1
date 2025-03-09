from cachetools import LRUCache

# Create an LRU cache with a max size of 100
cache = LRUCache(maxsize=100)

# Set values with integer keys
cache[1] = "one"
cache["2"] = "two"

print(cache.get("1"))  # Output: None
print(cache.get(2))  # Output: None
