print(dict())
dic = {1:10, 2:20, 3:30}
print(dic[1])
# print(dic[10])# failed
print(10 in dic)
print(2 in dic)
tul = (['a','b'],['c','d'],['e','f'],['g','h'])
print(dict(tul))
list = ['ab','cd','13']
print(dict(list))
dic[4] = 40
print(dic)
del dic[4]
print(dic)
dic.clear()
print(dic)