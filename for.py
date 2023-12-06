lt = [1, -5, 3, 2, 4, 10, 100]
for num in lt:
    print(num)

shrimp = {1:10, 2:20, 3:30}
for key, value in shrimp.items():
    print(key, value)

for i in range(0, 8):
    print(i)

print([i for i in range(10) if i % 2 == 0])
print([10*i for i in range(10) if i % 2 == 0])
print([[i for i in range(3)] for j in range(4)] )
print([[i*j for i in range(1,10)] for j in range(1,10)] )
print([(row, col) for row in range(4) for col in range(3)])
print([[(row, col) for row in range(4)] for col in range(3)])
print([i*j for i in range(2,11) if i%2 == 0 for j in range(2,11) if j%2 == 0] )

for i in range(8, 0, -1):
    print(i)