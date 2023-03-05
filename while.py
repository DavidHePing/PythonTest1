x=1
while x < 3:
    x+=1
print("exit x while!")
y=1
while y < 3:
    y+=1 
else:
   print("exit y while!")

while y < 20:
    y+=1
    if(y % 2 == 0):
        break
else:
   print("not print")