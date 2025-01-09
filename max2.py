array_2d = [
    [1, 2, 3],
    [4, 100, 6],
    [7, 8, -1],
    [10,11,12]
]
max_value = max(max(ary) for ary in array_2d)
print(max_value)
print(min(min(ary) for ary in array_2d))