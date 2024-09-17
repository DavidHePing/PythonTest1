from collections import Counter

a_str = 'abcaaabfchcabaddgeage'
counter = Counter(a_str) 
print(counter)
result = [occur_once for occur_once in counter if counter[occur_once] == 1]
print(result)