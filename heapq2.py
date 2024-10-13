import heapq

l = [21, 11, 67, 19, 45, 31, 16, 12, 86, 82]
heapq.heapify(l)
heapq.heappush(l, 32)

heapq.heappush(l, 1)
# l.append(1) # wrong answer: 11, 1, 12, 16,... 

for i in range(len(l)):
    print(heapq.heappop(l), end=", ")
print("")
