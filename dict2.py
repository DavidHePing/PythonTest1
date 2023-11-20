dic = {1:10, 2:20, 3:30}
print(list(dic.keys()))
print(list(dic.values()))
print(dic.items())
dic2 = dic.copy()
print(dic2)
print(dic.get(200, -100))
print(len(dic))

dic3 = {5: 50, 4: 40, 7: 70, 6: 60}
for key, val in dic3.items():
    print(key, val)

print(dic3)

orderDic1 = dict(sorted(dic3.items(), key=lambda item: item[0]))
print(orderDic1)

orderDic2 = dict(sorted(dic3.items(), key=lambda item: -item[0]))
print(orderDic2)
