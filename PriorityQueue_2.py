import queue

print("priority queue---")    
q = queue.PriorityQueue()

q.put(1)
q.put(2)
q.put(3)

print("length:", q.qsize())
print(q.queue[0])
print(q.queue[1])
print(q.queue[2])

while not q.empty():
    print(q.get(), end=" ")
print(" ")

l = [1,2,3,4,5,6,7,8,9]

for num in l:
    q.put(-num)

while not q.empty():
    print(-q.get(), end=" ")
print(" ")