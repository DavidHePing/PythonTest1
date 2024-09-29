from collections import OrderedDict

scores = OrderedDict([(8, 80), (7, 70), (10, 100)])
print(scores)
scores[1] = 10
print(scores)
print(scores.items())

print(next(iter(scores.items())))
print(next(reversed(scores.items())))