a = [x for x in range(1, 6)]
print(a)

b = [2*x for x in a]
print(b)

c = [3 * element for element in a if element % 2 == 0]
print(c)

value = sum([s for s in b if s > 4])
print(value)

import csv
shares_list = list()
with open('Data/portfolio.csv', 'rt') as file:
    data = csv.reader(file)
    header = next(data)
    # print(header)

    for line in data:
        shares_list.append(dict(zip(header, line)))

    print(shares_list)

share_value = [round(int(val['shares']) * float(val['price']), 2) for val in shares_list]
total_value = sum(price for price in share_value)
print(total_value)


# next General Syntax
