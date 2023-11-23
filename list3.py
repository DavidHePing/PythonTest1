import numpy


print(list(range(8)))
print(list(range(1,5)))
print(list(range(2,10)))
print(list(range(1,20,2)))
list = [0] * 5
print(list)
list2 = []
#list2[0] = 1 # Exception! 

li = [[j+i*3 for j in range(1,4)] for i in range(0,3)]
print(li)

li2 = [li[i][j] for i in range(3) for j in range(3) ]
print(li2)
