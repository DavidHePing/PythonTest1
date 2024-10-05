from collections import defaultdict

d = defaultdict(int, {'a': 0, 'b': 0, 'c': 0})

# Check if there are any 0 values
print(all(value == 0 for value in d.values()))

l = [2,4,6,8,10,11]
print(all(num % 2 == 0 for num in l))
l = [2,4,6,8,10]
print(all(num % 2 == 0 for num in l))