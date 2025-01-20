l1 = [1, 2, 3]
l2 = ["a", "b", "c"]
l3 = [-1, -2, -3]
for l1_item, l2_item in zip(l1, l2):
    print(l1_item, l2_item, end=", ")
print("")
for l1_item, l2_item, l3_item in zip(l1, l2, l3):
    print(l1_item, l2_item, l3_item, end=", ")
print("")