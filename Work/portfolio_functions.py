import csv
import report as r


def get_header(csv_file):
    with open(csv_file, 'rt') as file:
        data = csv.reader(file)
        header = next(data)
    return header


def read_portfolio_dict(filename) -> list:
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


def read_portfolio(filename) -> list:
    portfolio = []
    with open(filename, 'rt') as file:
        file_rows = csv.reader(file)
        header = next(file_rows)
        for row in file_rows:
            line = (row[0], int(row[1]), float(row[2]))
            portfolio.append(line)
    return portfolio


def read_portfolio_str(filename) -> list:
    portfolio = []
    with open(filename, 'rt') as file:
        file_rows = csv.reader(file)
        header = next(file_rows)
        for row in file_rows:
            line = (row[0], row[1], row[2])
            portfolio.append(line)
    return portfolio


def compare_portfolio(filename_old, filename_new):
    old_portfolio = read_portfolio(filename_old)  # list of tuples
    # print(old_portfolio)
    new_prices = r.read_prices(filename_new)  # dictionary of new prices
    new_prices_pfolio = r.prepare_portfolio_with_new_prices(old_portfolio, new_prices)
    r.print_gain_loss(new_prices_pfolio)
    r.print_total_gain(new_prices_pfolio)
    print()
    r.print_prices_diff(new_prices_pfolio)