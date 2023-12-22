# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as file:
        file_rows = csv.reader(file)
        header = next(file_rows)
        for row in file_rows:
            line = (row[0], int(row[1]), float(row[2]))
            portfolio.append(line)

    return portfolio


# Exercise 2.5

def read_portfolio_dict(filename):
    portfolio = []
    with open(filename, 'rt') as file:
        file_rows = csv.reader(file)
        header = next(file_rows)
        for row in file_rows:
            record = {
                      header[0]: row[0]
                    , header[1]: int(row[1])
                    , header[2]: float(row[2])
            }
            portfolio.append(record)

    return portfolio

def get_prices_2(portfl):
    # share_cost = float()
    total_cost = float()
    for row in portfl:
        share_cost = row['shares'] * row['price']
        total_cost += share_cost

    return total_cost

def print_portfolio(portflo):
    from pprint import pprint
    pprint(portflo)


# Exercise 2.6

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as file:
        file_txt = csv.reader(file)
        for line in file_txt:
            # prices[line[0]] = float(line[1])
            try:
                print(line[0])


    return prices


if __name__ == '__main__':
    # portfolio = read_portfolio_dict('Data/portfolio.csv')
    # total_cost = get_prices_2(portfolio)
    prices = read_prices('Data/prices.csv')
    print(prices)

    # print_portfolio(portfolio)
