from collections import Counter
scores = [35,70,10,20,35,70,70]
names = ['James', 'Michael', 'Ted', 'James', 'Leo']
count_score = Counter(scores)
print(count_score)
print(count_score[70])
print(Counter(names))
print(count_score.most_common(2))
item, count = count_score.most_common(2)[0]
print(item, count_score.most_common(2)[0][0])
print(count, count_score.most_common(2)[0][1])
[print(key,count) for key,count in count_score.items()]
a = ["MMMPPGG"]
count_a = Counter(a)
print(count_a)