from collections import Counter

a_str = 'abcaaabccabaddeae'
counter = Counter(a_str) 
print(counter)
print(counter.most_common(3)) 
print(counter['a'])
print(counter['z']) 
counter.update('aaeebbc') 
print(counter)
print(Counter(['a','a','n']))
print(Counter({'a':2,'n':1}))
print(Counter(a=2,n=1))

for key, item in counter.items():
    print(key, item)

print("a" in counter)
print("h" in counter)

li2 = Counter([1,2,2,3,3,3,3,3,4,4,5,5,5])
print(li2.get(2))
print(li2.get(3))