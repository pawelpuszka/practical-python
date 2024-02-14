"""
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(id(a), id(b), id(c))
print(a == c)
print(a is c)

a = [1, 2, (1, 2, 3), 3]
b = list(a)  # shallow copy
print(a is b)
print(a == b)
print(a[2] is b[2])

d = [1, 2, [1, 2, 3], 3]
import copy
e = copy.deepcopy(a)  # deep copy
print(id(d), id(e))
print(d, e)
print(id(d) == id(e))

a = []
if isinstance(a, tuple):
    print("a is tuple")
"""


# 2.24
from portfolio_functions import read_portfolio_str
import sources as s


if __name__ == "__main__":
    conversion = (str, int, float)
    # print(conversion[1]('54'))

    portfolio = read_portfolio_str(s.DATA_PORTFOLIO_CSV)
    # print(portfolio)
    portfolio2 = list()
    # print(portfolio2)
    # portfolio2.append([[conv(element[i]) for element in portfolio] for i, conv in enumerate(conversion)])
    # print(portfolio2)

    portfolio2 = [[conv(item) for conv, item in zip(conversion, row)] for row in portfolio]
    print(portfolio2)

    portfolio3 = list()
    for row in portfolio:
        for item, conv in zip(row, conversion):
            l = (conv, item)
            portfolio3.append(l)

    print(portfolio3)

# The zipped list is useful if you want to perform conversions on all of the values, one after the other. Try this:
