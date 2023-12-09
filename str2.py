from functools import reduce

#string join
a = ["ab", "c", "de", "f"]
b = "".join(a)
print(b)
c = ",".join(a)
print(c)

#string order
a = "abcdefg"
print(sorted(a, reverse=True))
c= "".join(sorted(a, reverse=True))
print(c)

d = "123"
c = 4
print(d+str(c))
