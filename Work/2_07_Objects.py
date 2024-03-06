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
from portfolio_functions import get_header
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

    portfolio_converted = [row[0](row[1]) for row in portfolio3]
    print(portfolio_converted)

# 2.25
    header = get_header(s.DATA_PORTFOLIO_CSV)
    # print(header)
    i = 0
    new_portfolio = list()

    while i < len(portfolio_converted) - 3:
        p = list()
        p.append(portfolio_converted[i])
        p.append(portfolio_converted[i+1])
        p.append(portfolio_converted[i+2])
        new_portfolio.append(p)
        i += 3

    print(new_portfolio)

    new_portfolio = [{row[0]: round(row[1] * row[2], 2)} for row in new_portfolio]
    print(new_portfolio)

# 2.26
    from sources import DATA_DOWSTOCKS_CSV
    from portfolio_functions import read_portfolio_str

    header = get_header(DATA_DOWSTOCKS_CSV)
    print(header)
    portfolio = read_portfolio_str(DATA_DOWSTOCKS_CSV)
    print(portfolio)
    types = [str, float, str, str, float, float, float, float, int]
    portfolio_converted = [[type(val) for val, type in zip(line, types)] for line in portfolio]
    print(portfolio_converted)
    portfolio_dict = [{head: value for head, value in zip(header, line)} for line in portfolio_converted]
    print(portfolio_dict)
