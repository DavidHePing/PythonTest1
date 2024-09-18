import queue

print("queue---")
q = queue.Queue()
q.put(1)
q.put('a')
q.put(3)
q.put("aaa")
#print(len(q)) no len

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
 
 
