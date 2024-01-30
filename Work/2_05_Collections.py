import csv
from collections import Counter
from collections import defaultdict


def portfolio(filename):
    prtflio = list()
    with open(filename, 'rt') as file:
        lines = csv.reader(file)
        header = next(lines)

        total_shares = Counter()
        print(total_shares)
        for name, shares, price in lines:
            total_shares[name] += int(shares)

    print(total_shares)


def portfolio_2(filename):
    with open(filename, 'rt') as file:
        lines = csv.reader(file)
        header = next(lines)
        holdings = defaultdict(list)
        # print(holdings)
        for name, shares, price in lines:
            holdings[name].append((shares, price))
    print(holdings)


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as file:
        file_rows = csv.reader(file)
        header = next(file_rows)
        for row in file_rows:
            line = (row[0], int(row[1]), float(row[2]))
            portfolio.append(line)

    return portfolio


def tabulate_portfolio(portfolio):
    from collections import Counter
    holdings = Counter()
    for val in portfolio:
        holdings[val[0]] += val[1]
        # holdings[val[0]] += val[2]
    # print(holdings)
    return holdings


def get_most_common(holdings, how_much):
    from collections import Counter
    print(holdings.most_common(how_much))


def print_holdings(holdings):
    print(holdings)


if __name__ == '__main__':
    # portfolio('Data/portfolio.csv')
    portfolio = read_portfolio('Data/portfolio.csv')
    portfolio_2 = read_portfolio('Data/portfolio2.csv')
    holdings = tabulate_portfolio(portfolio)
    holdings2 = tabulate_portfolio(portfolio_2)
    combined_holdings = holdings2 + holdings
    print_holdings(combined_holdings)
    get_most_common(combined_holdings, 2)
