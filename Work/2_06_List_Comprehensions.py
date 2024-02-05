a = [x for x in range(1, 6)]
# print(a)

b = [2*x for x in a]
# print(b)

c = [3 * element for element in a if element % 2 == 0]
# print(c)

value = sum([s for s in b if s > 4])
# print(value)

import csv
shares_list = list()
with open('Data/portfolio.csv', 'rt') as file:
    data = csv.reader(file)
    header = next(data)
    # print(header)

    for line in data:
        shares_list.append(dict(zip(header, line)))

    # print(shares_list)

share_value = [round(int(val['shares']) * float(val['price']), 2) for val in shares_list]
total_value = sum(price for price in share_value)
# print(total_value)

# 2.20

def portfolio_total_cost(portfolio):
    return sum(round(s[1]*s[2], 2) for s in portfolio)


def holdings_with_with_more_than_100_shares(portfolio):
    holdings = ([x for x in portfolio if x[1] > 100])
    return holdings


def holdings_costs_more_than_10000(portfolio):
    return [s for s in portfolio if s[1] * s[2] > 10000]


def create_tuple(portfolio: dict()):
    return [(s['name'], s['shares']) for s in portfolio]


# Exercises
if __name__ == '__main__':
    from report import read_portfolio
    from report import read_portfolio_dict
    from sources import DATA_PORTFOLIO_CSV

# 2.19
    portfolio = read_portfolio(DATA_PORTFOLIO_CSV)
    print(portfolio)
    print(portfolio_total_cost(portfolio))
    print(holdings_with_with_more_than_100_shares(portfolio))
    # ibm_shares = sum([x[1] for x in portfolio if x[0] == 'IBM'])
    # print(ibm_shares)
    print([s for s in portfolio if s[0] in ('IBM', 'MSFT')])
    print(holdings_costs_more_than_10000(portfolio))


