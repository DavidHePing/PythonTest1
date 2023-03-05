tpl = (1, 3, 'XD', '9', 123)
print(tpl)
print(tpl[1])
# tpl[1] = 100 #failed
a,b,c,d,e = tpl
print(a,b,c,d,e)
tuples = [('1', '2'),('1', '3'), ('2', '4'), ('3', '6')]
print(tuples)
for a,b in tuples:
    print(a,b)