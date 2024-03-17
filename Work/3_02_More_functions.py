import csv
from sources import DATA_PORTFOLIO_CSV, PRICES_CSV


# Exercise 3.4: Building a Column Selector

def parse_csv(filename: str, selected_cols: list = None) -> list:
    """
    parse a csv file to list of dictionaries
    """
    records = []
    with open(filename, 'rt') as file:
        data = csv.reader(file)
        header = next(data)
        if selected_cols:
            records = [{head: item for head, item in zip(header, row)} for row in data if row is not None]
            records = [{item: record[item] for item in record if item in selected_cols} for record in records]
        else:
            for row in data:
                if row is None:
                    continue
                records.append(dict(zip(header, row)))
    return records


# Exercise 3.5: Performing Type Conversion
def parse_csv_2(filename: str, delimiter: chr = ' ', selected_cols: list = None, types: list = None, has_header: bool = False) -> list:
    """
    parse a csv file to list of dictionaries
    """
    if selected_cols and not has_header:
        raise RuntimeError("Selected columns should have headers")
    records = []
    with open(filename, 'rt') as file:
        data = csv.reader(file, delimiter=delimiter)
        if not has_header:
            records = [tuple(record) for record in data if record is not None]
            if types:
                records = [tuple(func(item) for item, func in zip(record, types)) for record in records]
        else:
            header = next(data)
            records = [{head: item for head, item in zip(header, row)} for row in data if row is not None]
            if selected_cols:
                records = [{item: record[item] for item in record if item in selected_cols} for record in records]
                if types:
                    records = [{item: func(record[item]) for item, func in zip(record, types) if item in selected_cols} for record in records]
            else:
                for row in data:
                    if row is None:
                        continue
                    records.append(dict(zip(header, row)))
                if types:
                    records = [{item: func(record[item]) for item, func in zip(record, types) if item in header} for record in records]

    return records


if __name__ == "__main__":
    # print(parse_csv(DATA_PORTFOLIO_CSV, ['name', 'shares']))
    # print(parse_csv_2(DATA_PORTFOLIO_CSV))
    # print(parse_csv_2(DATA_PORTFOLIO_CSV, ['name', 'shares'], [str, float]))
    # print(parse_csv_2(DATA_PORTFOLIO_CSV, has_header=False, types=[str, int, float], selected_cols=['name', 'shares']))

    types = [str, int]
    with open(PRICES_CSV, 'rt') as file:
        data = csv.reader(file)
        records = [tuple(record) for record in data if record is not None]
        if len(types) != len(records[0]):
            raise RuntimeError('Wrong number of item in list')
        try:
            records = [tuple(func(item) for item, func in zip(record, types)) for record in records if len(record) == len(types)]
            print(records)
        except ValueError as e:
            print(e)


