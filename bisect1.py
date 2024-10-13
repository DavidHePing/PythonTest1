import bisect

l = [10, 20, 30, 40, 50, 60]
print(bisect.bisect_left(l, 35))
print(bisect.bisect_left(l, 61))
print(bisect.bisect_right(l, 61))
