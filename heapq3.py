import heapq

l = [21, 11, 67, 19, 45, 31, 16, 12, 86, 82]
l2 = []

for num in l:
    heapq.heappush(l2, num)

print(l2)
