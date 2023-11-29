from collections import Counter
team1 = Counter({'BlackTea': 3, 'GreenTea': 2, 'MilkTea': 1})
team2 = Counter(['BlackTea', 'BlackTea', 'BlackTea', 'MilkTea', 'MilkTea', 'MilkTea'])
team3 = Counter(GreenTea=3, MilkTea=2)
print(team1, team2, team3)
print(team1+team2)
print((team1+team2)[0])
print(team2-team3)
print(team2 & team3)
print(team2 | team3)
print(team3.keys())
print(team3.values())
print(sum((team2 | team3).values()))
print(list(team1))
print(team1)
print([key for key in Counter(team1)])

a = "00000000000000000000000000001011"
print(Counter(a))