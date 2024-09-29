from collections import OrderedDict

scores = OrderedDict([(8, 80), (7, 70), (10, 100)])
print(scores)
scores[1] = 10
print(scores)
print(scores.items())

print(next(iter(scores))) # show key
print(next(iter(scores.items()))) # show key,value
print(next(reversed(scores))) # show key
print(next(reversed(scores.items()))) # show key,value