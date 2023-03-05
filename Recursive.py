def fib(n):
    return fib(n-1) + fib(n-2) if n > 1 else n

for i in range(20):                 
    print(fib(i), end = ',')

# 例：
# cs(1) = 1 (1)
# cs(2) = 2 (1+1, 2)
# cs(3) = 3 (1+2, 2+1, 1+1+1)
# cs(4) = 5 (1+1+2, 2+2, 1+2+1, 2+1+1, 1+1+1+1)

print()
def cs(n):
    if(n <= 2):
        return n
    dp = [1,2]
    for i in range(2, n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n-1]

print(cs(3))
print(cs(6))
print(cs(18))