ary = [1,3,5,4,6,2,9,0]
ary.sort()
print(ary)
ary.sort(reverse=True)
print(ary)

# Example list of tuples
my_list = [(1, 3), (2, 2), (3, 1), (1, 2), (2, 1), (3, 3)]

# Sorting based on two conditions
sorted_list = sorted(my_list, key=lambda x: (x[0], x[1]), reverse=True)

# Display the sorted list
print(sorted_list)
