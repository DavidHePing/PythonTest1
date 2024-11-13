import bisect

l = [10, 20, 30, 40, 50, 60]
print(bisect.bisect_right(l, 29))#2
print(bisect.bisect_right(l, 30))#3
print(bisect.bisect_right(l, 35))#3
