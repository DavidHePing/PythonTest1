from functools import reduce

tpl = (1, 3, 'XD', '9', 123)
print(tpl)
print(tpl[1])
print(tpl[2])
# tpl[1] = 100 #failed
a,b,c,d,e = tpl
print(a,b,c,d,e)
tuples = [('1', '2'),('1', '3'), ('2', '4'), ('3', '6')]
print(tuples)
for a,b in tuples:
    print(a,b)
tuples.append(('4', '8'))
print(tuples)
print([a+b for a,b in tuples])
print(reduce(lambda x,y: x+"{{{0}, {1}}}".format(y[0], y[1]), tuples, ''))

x=1
y=2
x,y=y,x
print(x, y)