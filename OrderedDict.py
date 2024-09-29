from collections import OrderedDict

scores = OrderedDict([('James', 80), ('Andy', 70), ('Curry', 100)])
print(scores)
print('aaa' in scores)
print('James' in scores)
print(scores['James'])
scores['Harden'] = 95
print(scores)
scores.pop('James')
print(scores)
scores['James'] = 80
print(scores)
d = {'1':4,'2':3,'3':5,'4':2}
print(d)
order_d = OrderedDict(sorted(d.items(),key=lambda x:x[0]))
print(order_d)
order_d = OrderedDict(sorted(d.items(),key=lambda x:x[1]))
print(order_d)