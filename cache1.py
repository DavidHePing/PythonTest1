from cachetools import LRUCache

# Create an LRU cache with a max size of 100
cache = LRUCache(maxsize=100)

# Set values with integer keys
cache[1] = "one"
cache[2] = "two"

# Get values using integer keys
print(cache.get(1))  # Output: one
print(cache.get(2))  # Output: two
print(cache.get(3, "Not Found"))  # Output: Not Found (key 3 doesn't exist)
print(cache.get(4)) # Output: None

# Check if a key exists
if 1 in cache:
    print("Key 1 exists!")  # Output: Key 1 exists!

# Delete a key
del cache[1]

# Check if key 1 still exists
print(1 in cache)  # Output: False
