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

def get_portfolio_cost(portfl):
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
            try:
                prices[line[0]] = float(line[1])
            except IndexError:
                # print('Brak danych')
                pass
    return prices


# Exercise 2.7

def get_number_of_shares(filename):
    shares = {}
    with open(filename, 'rt') as file:
        text = csv.reader(file)
        header = next(file)
        for line in text:
            shares = {
                line[0]: int(line[1])
            }
    return shares


def prepare_portfolio_with_new_prices(pfolio, new_prices):
    new_pfolio = []
    for row in pfolio:
        for key in new_prices:
            if str(row[0]) == str(key):
                new_pfolio.append((key, row[1], row[2], new_prices[key]))  # list of tuples

    return new_pfolio


def print_gain_loss(pfolio):
    for row in pfolio:
        old_cost = row[1] * row[2]
        new_cost = row[1] * row[3]
        if old_cost > new_cost:
            print(f"Zysk na {row[0]} wynosi {round(old_cost - new_cost, 2)}")
        elif old_cost < new_cost:
            print(f"Strata na {row[0]} wynosi {round(new_cost - old_cost, 2)}")
        else:
            print(f"Na {row[0]} wyszedłem na 0")


def print_total_gain(pfolio):
    total = float()
    total_old = float()
    total_new = float()
    for row in pfolio:
        old_cost = round(row[1] * row[2], 2)
        new_cost = round(row[1] * row[3], 2)
        total += new_cost - old_cost
        total_old += old_cost
        total_new += new_cost

    print("Koszt starego portfolio: ", total_old)
    print("Koszt nowego portfolio: ", total_new)

    if total < 0.0:
        print("Strata wyniosła: ", total)
    elif total > 0.0:
        print("Zysk wyniósł: ", total)
    else:
        print("Wyszedłem na 0")


def print_prices_diff(pfolio): # name, shares, old_price, new_price
    print("{name:>10s} {shares:>15s} {new_price:>15s} {change:>15s}".format(name="Name", shares="Shares", new_price="New price", change="Change"))
    for row in pfolio:
        print(f"{row[0]:>10s} {row[1]:>15d} {row[3]:>15.2f} {(row[3] - row[2]):>15.2f}")




def compare_portfolio(filename_old, filename_new):
    old_portfolio = read_portfolio(filename_old)  # list of tuples
    # print(old_portfolio)
    new_prices = read_prices(filename_new)  # dictionary of new prices
    new_prices_pfolio = prepare_portfolio_with_new_prices(old_portfolio, new_prices)
    print_gain_loss(new_prices_pfolio)
    print_total_gain(new_prices_pfolio)
    print()
    print_prices_diff(new_prices_pfolio)

if __name__ == '__main__':
    #portfolio = read_portfolio_dict('Data/portfolio.csv')
    #total_cost = get_portfolio_cost(portfolio)
    #prices = read_prices('Data/prices.csv')
    #print(prices)
    #print(total_cost)
    #print(prices)
    compare_portfolio('Data/portfolio.csv', 'Data/prices.csv')

    # print_portfolio(portfolio)
