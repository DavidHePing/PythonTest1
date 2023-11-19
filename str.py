from functools import reduce


print('a'+'b'+'c')
print('a', 'b', 'c')
print('apple'*2)
a='apple'
print(a[2])
print(a[2:8])
print(len(a))
b = 'An apple a day, keeps the doctor away.'
print(b.split())
print(b.split(','))
print(b.split('7'))
print(b.split('.'))
print(','.join(b.split()))
print(a[::-1])
c = 'aabbccdde'
print(chr(reduce(lambda x,y: x^ord(y), c, 0)))

words = ["1", "0", "1", "0"]
d = "".join(words)
print(d)