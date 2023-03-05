set1 = set([5,4,3,2,1])
set1.add(2)
set1.add(2)
set1.add(2)
print(set1)
print(1 in set1)
print(999 in set1)
st1 = {'A', 'C', 'E'}
st2 = {'B', 'C', 'A', 'D'}
print(st1.intersection(st2))
print(st1 | st2)
print(st1 - st2)
print(st1.difference(st2))
print(st2 - st1)
print(st1 ^ st2)
st3 = {'A', 'C', 'E'}
st4 = {'A', 'B','C', 'D','E'}
print(st1 <= st2)
print(st3 <= st4)