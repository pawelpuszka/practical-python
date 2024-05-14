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
            line = [item for item in row]
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

def parse_csv(filename: str, delimiter: chr = ' ', selected_cols: list = None, types: list = None, has_header: bool = False) -> list:
    """
    parse a csv file to list of dictionaries
    """
    if selected_cols and not has_header:
        raise RuntimeError("Selected columns should have defined headers")

    records = []
    with open(filename, 'rt') as file:
        records_tmp = []

        data = csv.reader(file)

        if has_header:
            header = next(data)

            if selected_cols:
                # records = [{item: record[item] for item in record if item in selected_cols} for record in data]
                records = [{head: item for item, head in zip(record, header) if head in selected_cols} for record in data]
            else:
                records = [{head: item for item, head in zip(record, header)} for record in data]
        else:
            records = [tuple(record) for record in data]

        if types:
            if len(types) != len(records[0]):
                raise RuntimeError('Wrong number of items in list with types')

            if isinstance(records[0], tuple):  # checking only the first item of the list
                for i, record in enumerate(records):
                    try:
                        records_tmp.append(tuple(func(item) for item, func in zip(record, types)))
                    except ValueError as e:
                        print("Problem with data conversion in line", i)
            elif isinstance(records[0], dict):
                for i, record in enumerate(records):
                    try:
                        records_tmp.append({item: func(record[item]) for item, func in zip(record, types)})
                    except ValueError as e:
                        print("Problem with data conversion in line", i+1)
            else:
                raise RuntimeError('Unknown object type')

            records = records_tmp

    return records


# przeczytać sekcję Commentary w 04_Modules