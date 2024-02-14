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
    from sources import DATA_PORTFOLIO_CSV_2

# 2.19
    portfolio = read_portfolio(DATA_PORTFOLIO_CSV)
    print(portfolio)
    print(portfolio_total_cost(portfolio))
    print(holdings_with_with_more_than_100_shares(portfolio))
    # ibm_shares = sum([x[1] for x in portfolio if x[0] == 'IBM'])
    # print(ibm_shares)
    print([s for s in portfolio if s[0] in ('IBM', 'MSFT')])
    print(holdings_costs_more_than_10000(portfolio))


# 2.20
    total_value = sum([x[1]*x[2] for x in portfolio])
    print(total_value)

    portfolio2 = read_portfolio(DATA_PORTFOLIO_CSV_2)
    print(portfolio2)


# 2.21
    holdings = [s for s in portfolio if s[1] > 100]
    print(holdings)

    holdings = [s for s in portfolio if s[0] in ('MSFT', 'IBM')]
    print(holdings)

    holdings = [s for s in portfolio if s[1] * s[2] > 10000]
    print(holdings)


#2.22
    portfolio = read_portfolio_dict(DATA_PORTFOLIO_CSV)
    print(portfolio)
    holdings = [(d['name'], d['shares']) for d in portfolio]
    print(holdings)

    holdings = {(d['name'], d['shares']) for d in portfolio}
    print(holdings)
    names = {d['name'] for d in portfolio}
    print(names)

    holdings = {name: 0 for name in names}
    print(holdings)
    for s in portfolio:
        # print(holdings[s['name']])
        holdings[s['name']] += s['shares']
    print(holdings)

    # holdings = [{holdings[s.keys()]: s['price']} for s in portfolio]
    # print(holdings)

#2.23
    from sources import PORTFOLIODATE_CSV
    import csv

    def get_header(csv_file):
        with open(csv_file, 'rt') as file:
            data = csv.reader(file)
            header = next(data)
        return header


    # header = get_header(PORTFOLIODATE_CSV)
    # select = get_header(DATA_PORTFOLIO_CSV)
    # indices = [header.index(colname) for colname in select]
    # print(indices)

    selected = get_header(DATA_PORTFOLIO_CSV)
    print(selected)
    headers = get_header(PORTFOLIODATE_CSV)
    indices = [headers.index(colname) for colname in selected]  # [0, 3, 4]
    print(indices)
    data_list = list()
    with open(PORTFOLIODATE_CSV, 'rt') as file:
        data = csv.reader(file)
        header = next(data)
        for row in data:
            record = {name: row[index] for name, index in zip(selected, indices)}
            data_list.append(record)

    print(data_list)