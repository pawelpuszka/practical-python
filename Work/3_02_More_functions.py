import csv
from sources import DATA_PORTFOLIO_CSV


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
def parse_csv_2(filename: str, selected_cols: list = None, types: list = None) -> list:
    """
    parse a csv file to list of dictionaries
    """
    records = []
    with open(filename, 'rt') as file:
        data = csv.reader(file)
        header = next(data)
        if selected_cols:
            records = [{head: item for head, item in zip(header, row)} for row in data if row is not None]
            # records = [{item: type_(record[item]) for item, type_ in zip(record, types) if item in selected_cols} for record in records]
            records = [{item: record[item] for item in record if item in selected_cols} for record in records]
        if types:
            records = [{item: func(record[item]) for item, func in zip(record, types) if item in selected_cols} for record in records]
        else:
            for row in data:
                if row is None:
                    continue
                records.append(dict(zip(header, row)))
    return records


if __name__ == "__main__":
    print(parse_csv(DATA_PORTFOLIO_CSV, ['name', 'shares']))
    # print(parse_csv(DATA_PORTFOLIO_CSV))
    print(parse_csv_2(DATA_PORTFOLIO_CSV, ['name', 'shares'], [str, float]))

