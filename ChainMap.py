from collections import ChainMap
a_dict = {'a1':1, 'a2':2, 'c1':3} 
b_dict = {'b1':4, 'b2':5, 'b3':6}
c_dict = {'c1':7, 'c2':8, 'c3':9}
map = ChainMap(a_dict, b_dict, c_dict)
print(map['a2']) 
print(map['c1'])# find first value, so be 3
print(map['c2']) 
print(map['b2']) 
print('b4' in map) 
# print(map['b4']) #failed