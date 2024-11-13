import bisect

l = [10, 20, 30, 40, 50, 60]
print(bisect.bisect_left(l, 29))#2
print(bisect.bisect_left(l, 30))#2
print(bisect.bisect_left(l, 35))#3
