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