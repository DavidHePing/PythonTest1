import queue

l = [9,8,7,6,5,4,3,2,1]
pq = queue.PriorityQueue()

for i, num in enumerate(l):
    pq.put((i, num))
    # pq.put((num, i))

result = []

while not pq.empty():
    result.append(pq.get())

print(result)