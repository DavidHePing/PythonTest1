import heapq


li = [[1,2,3],  [4,5,6],  [7,8,9]]
print(li)
heapq._heapify_max(li)
print(li)
heapq.heapify(li)
print(li)

res = []

for i in range(len(li)):
    for j in range(len(li[i])):
        heapq.heappush(res, (-(i+j), -i, li[i][j]))

print(res)

print(heapq.heappop(res)[2])
print(heapq.heappop(res)[2])