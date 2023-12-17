from functools import reduce

li = [1,2,3,4,5]
print(reduce(lambda x, y: x+y, li))
print(reduce(lambda x,y: x*y, li))
print(reduce(lambda x, y: x+y, li,10000))

li3 = [1,1,2,2,3,3,4,4,5,5]
print(reduce(lambda x, y: x^y, li3))

st1 = "leetcode"
print(reduce(lambda x, y: x ^ ord(y), st1, 0))

