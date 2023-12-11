li1 = [-11, 1,2,3,4,5,6]
print(max(li1))
print(max(li1, key=abs))

def minus(num: int) -> int:
    return -num

print(minus(100))

print(max(li1, key=minus))

#Set
li2 = [1,2,2,3,3,3,3,3,4,4,5,5,5]
print(li2.count(2))
print(li2.count(0))
print(max(li2, key=li2.count))
