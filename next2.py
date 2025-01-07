dic = {}
dic[10] = 0
dic[1] = 0
dic[5] = 0
dic[2] = 0

it = iter(dic)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

try:
    print(next(it))
except StopIteration as e:
    print("StopIteration")

try:
    print(next(it))
except StopIteration as e:
    print("StopIteration")
