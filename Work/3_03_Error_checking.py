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
        records = []
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
            records = records_tmp

    return records



if __name__ == "__main__":
    # print(parse_csv(filename=MISSING_DATA_CSV, selected_cols=['name', 'shares'], has_header=True, types=[str, int, float]))  # types=[str, int, float]))
    print(parse_csv(filename=MISSING_DATA_CSV, has_header=True, types=[str, int, float]))
    # print(parse_csv(filename=MISSING_DATA_CSV, has_header=False, types=[str, int, float]))

    # types = [str, int, float]
    # with open(MISSING_DATA_CSV, 'rt') as file:
    #     data = csv.reader(file)
    #     header = next(data)
    #     records = [tuple(record) for record in data if record is not None]
    #     records_tmp = []
    #     for i, record in enumerate(records):
    #         print(header)
    #         try:
    #             record_tmp = [func(item) for item, func in zip(record, types)]
    #             records_tmp.append(record_tmp)
    #         except ValueError as e:
    #             print("Wystąpił problem w linii", i)
    #             print(e)
    #         # records = [tuple(func(item) for item, func in zip(record, types)) for record in records]
    #         # try:
    #         #     # records_tmp = [tuple(func(item) for item, func in zip(record, types))]
    #         #     records_tmp = tuple(zip(record, types))
    #         # except ValueError as e:
    #         #     print('Corrupted or missed value in the list on position ', i)
    #     print(records_tmp)