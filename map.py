l = [1, 2, 3, 4, 5]
it = map(lambda x: 1 + x, l)
print(list(it))
it = map(lambda x: x * x, l)
for num in it:
    print(num, end=",")
print("")