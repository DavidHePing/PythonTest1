a = "123"
b = [(index, i) for index, i in enumerate(a)]
print(b)


record = set()
prefix = list()

for i, item in enumerate(a):
    if item in record:
        prefix.append(i)
    
    record.add(item)
    

print(prefix)
print(record)