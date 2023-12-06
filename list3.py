import numpy


print(list(range(8)))
print(list(range(1,5)))
print(list(range(2,10)))
print(list(range(1,20,2)))
list1 = [0] * 5
print(list1)
list2 = []
#list2[0] = 1 # Exception! 

li = [[j+i*3 for j in range(1,4)] for i in range(0,3)]
print(li)

li2 = [li[i][j] for i in range(3) for j in range(3) ]
print(li2)

li3 = list(range(4))
print(li3)

prefix_sum = [sum(li3[:i+1]) for i in range(len(li3))]
print(prefix_sum)

a, b = [1,2]
print(a,b)
#c,d = [1,2,3] #exception
a,b = ["a", "b"]
print(a, b)

li = list(range(10))

for i in range(1, len(li)):
    print(li[-i-1])

