import queue

print("queue---")
q = queue.Queue()
q.put(1)
q.put('a')
q.put(3)
q.put("aaa")

result = []
while not q.empty():
    result.append(q.get())
    
print(result)

print("lifo queue--- (stack????)")    
q = queue.LifoQueue()

q.put(1)
q.put(2)
q.get()
q.put(3)
q.put(4)
q.get()

result = []
while not q.empty():
    result.append(q.get())
    
print(result)
 
 
print("priority queue---")    
q = queue.PriorityQueue()

q.put((3, "Priority 3"))
q.put((1, "Priority 1"))
q.put((2, "Priority 2"))

result = []
while not q.empty():
    result.append(q.get())
    
print(result)
 
q.put(("bc", "Priority 3"))
q.put(("ab", "Priority 1"))
q.put(("ac", "Priority 2"))

result = []
while not q.empty():
    result.append(q.get())
    
print(result) 
