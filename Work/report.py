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


def get_prices(portfl):
    # share_cost = float()
    total_cost = float()
    for name, shares, price in portfl:
        share_cost = shares * price
        total_cost += share_cost

    return total_cost


# Exercise 2.5



if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    total_cost = get_prices(portfolio)

    print(total_cost)
