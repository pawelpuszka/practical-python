import csv
from collections import Counter
from collections import defaultdict


def portfolio(filename):
    prtflio = list()
    with open(filename, 'rt') as file:
        lines = csv.reader(file)
        header = next(lines)

        total_shares = Counter()
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



if __name__ == '__main__':
    portfolio_2('Data/portfolio.csv')

# next Exercises