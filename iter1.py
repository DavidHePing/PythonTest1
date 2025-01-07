ary = [1, 2, 3, 4, 5]
it = iter(ary)

print(next(it))
print(it)

while True:
    try:
        print(next(it))
    except StopIteration:
        break
