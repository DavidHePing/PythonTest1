from collections import defaultdict
dict1 = defaultdict(int)
print(dict1[1])
dict2 = defaultdict(str)
print(dict2[1])
dict3 = defaultdict(list)
print(dict3[1])
dict4 = defaultdict(tuple)
print(dict4[1])

multi_dict = defaultdict(list) 
key_values = [('even',2),('odd',1),('even',8),('odd',3),('float',2.4),('odd',7)]

for key,value in key_values:
    multi_dict[key].append(value)

print(multi_dict)

for key, value in multi_dict.items():
      print(key, value)

counter_dict = defaultdict(int)
a_list = ['a','b','x','a','a','b','z']

for element in a_list:
        counter_dict[element] += 1

print(counter_dict) 