dic = {1:10, 2:20, 3:30}
print(list(dic.keys()))
print(list(dic.values()))
print(dic.items())
dic2 = dic.copy()
print(dic2)
print(dic.get(200, -100))