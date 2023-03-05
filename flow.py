a=8
if(a > 9):
    print('over')
else:
    print('less')

for w in ['cat', 'window', 'defenestrate']:
    print(w)

users = {'Hans': 'active', 'David': 'inactive', 'Marry': 'active'}
print(users)
for user, status in users.items():
    if status == 'inactive':
        del users[user]
print(users)
