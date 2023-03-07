from collections import deque
d = deque('123456',maxlen=6)
print(d)
d.extend('789')
print(d)
d.extendleft('xyz')
print(d)