from collections import defaultdict

d = defaultdict(int, {'a': 1, 'b': 0, 'c': 2})

# Check if there are any 0 values
print(any(value == 0 for value in d.values()))
print(any(value == 'a' for value in d))

l = [2,4,6,8,10,11]
print(any(num % 2 == 1 for num in l))
l = [2,4,6,8,10]
print(any(num % 2 == 1 for num in l))