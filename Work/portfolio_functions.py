import csv


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


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as file:
        file_rows = csv.reader(file)
        header = next(file_rows)
        for row in file_rows:
            line = (row[0], int(row[1]), float(row[2]))
            portfolio.append(line)

    return portfolio


def read_portfolio_str(filename):
    portfolio = []
    with open(filename, 'rt') as file:
        file_rows = csv.reader(file)
        header = next(file_rows)
        for row in file_rows:
            line = [item for item in row]
            portfolio.append(line)

    return portfolio