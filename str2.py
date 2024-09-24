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

print(f"+++ {d}")

e = "123456789"
print(e[:-2])

for ch in e:
    print(ch)

f = "leetscode"
print(f[8:9])
print(f[7:9])
print(f[5:9])