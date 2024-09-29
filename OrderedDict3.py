from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict()

# Append key-value pairs
ordered_dict['a'] = 4
ordered_dict['b'] = 3
ordered_dict['c'] = 2

# Append a new item
ordered_dict['d'] = 1

# Print the OrderedDict
for key, value in ordered_dict.items():
    print(key, value)
