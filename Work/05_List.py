names = ['Ania', 'Paweł', 'Filip', 'Antek']
names2 = ['Grażyna', 'Anna', 'Marek', 'Mieczysław']

stocks = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
stocks_list = stocks.split(',')
print(stocks_list)
stocks_list.append('GOOG')
print(stocks_list)
stocks_list.insert(1, 'ORCL')
print(stocks_list)

family_names = names + names2
print(family_names)

# for i in range(0, len(family_names), 1):
#    print(family_names[i])

# print('\n')

for name2 in names2:
    family_names.remove(name2)

for name in family_names:
    print(name)

# ['FALLOUT', 'FALLOUT 2', 'FALLOUT TACTICS', 'FALLOUT 3', 'FALLOUT NEW VEGAS', 'FALLOUT NEW CALIFORNIA', 'FALLOUT 4']
blackisle_fallouts = ['FALLOUT', 'FALLOUT 2']
blackisle_fallouts.append('FALLOUT TACTICS')

bethesda_fallouts = []
bethesda_fallouts.append('FALLOUT NEW VEGAS')
bethesda_fallouts.append('FALLOUT 4')

print(blackisle_fallouts)
print(bethesda_fallouts)

# fallouts = blackisle_fallouts + bethesda_fallouts
# print(fallouts)

fallouts = []
i = 0
for f1, f2 in zip(blackisle_fallouts, bethesda_fallouts):
    fallouts.insert(i, f1)
    fallouts.insert(i, f2)
    i += 1

fallouts.insert(len(fallouts), 'FALLOUT 3')
print(fallouts)

fallouts.append("FALLOUT NEW CALIFORNIA")
print(fallouts)

fallouts.remove("FALLOUT NEW CALIFORNIA")
print(fallouts)
# next 1.20

fallouts.append("FALLOUT")
print(fallouts)

print(fallouts.index("FALLOUT"))
fallouts.remove(f"FALLOUT")
print(fallouts)

fallouts.sort()
print(fallouts)

fallouts_s = ', '.join(fallouts)
print(fallouts_s)

best_games = [fallouts, "CIVILIZATION 5"]
print(best_games)

print(best_games[0][3])

