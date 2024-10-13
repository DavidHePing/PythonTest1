x = 24
print(not x > 20)
print(0<x<100)
lt = [1, 3, 24, 10, 33]
print(x in lt and not x < 23)

if x % 2 == 0:
    if x % 3 == 0:
        print('6 times')
    else:
        print('2 times')
else:
    print('not 2 times')

lt = []
if not lt:
    print('lt is null or empty')

a = None

if a is None:
    print('a is None')

a = 10
b = 11

if a == 11 or b == 11:
    print("11")

b = b if b == 10 else 77
print(b)