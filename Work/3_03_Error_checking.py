import csv
from sources import DATA_PORTFOLIO_CSV, PRICES_CSV, MISSING_DATA_CSV

def parse_csv(filename: str, delimiter: chr = ' ', selected_cols: list = None, types: list = None, has_header: bool = False) -> list:
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
                # if len(types) != len(records[0]):
                    # raise RuntimeError('Wrong number of items in list')
                for record in records:
                    try:
                        records = [tuple(func(item) for item, func in zip(record, types)) for record in records]
                    except ValueError as e:
                        print('Corrupted or missed value in the list')
        else:
            header = next(data)
            records = [{head: item for head, item in zip(header, row)} for row in data if row is not None]
            if selected_cols:
                records = [{item: record[item] for item in record if item in selected_cols} for record in records]
                if types:
                    # if len(types) != len(selected_cols):
                        # raise RuntimeError('Wrong number of items in list')
                    records = [{item: func(record[item]) for item, func in zip(record, types) if item in selected_cols} for record in records]
            else:
                for row in data:
                    if row is None:
                        continue
                    records.append(dict(zip(header, row)))
                if types:
                    # if len(types) != len(records[0]):
                        # raise RuntimeError('Wrong number of items in list')
                    records = [{item: func(record[item]) for item, func in zip(record, types) if item in header} for record in records]

    return records



if __name__ == "__main__":
    # print(parse_csv(filename=MISSING_DATA_CSV, types=[str, int, float]))

    types = [str, int, float]
    with open(MISSING_DATA_CSV, 'rt') as file:
        data = csv.reader(file)
        header = next(data)
        records = [tuple(record) for record in data if record is not None]
        records_tmp = []
        for i, record in enumerate(records):
            # records = [tuple(func(item) for item, func in zip(record, types)) for record in records]
            try:
                # records_tmp = [tuple(func(item) for item, func in zip(record, types))]
                records_tmp = tuple(zip(record, types))
            except ValueError as e:
                print('Corrupted or missed value in the list on position ', i)
        print(records_tmp)