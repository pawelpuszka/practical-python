import csv


def print_portfolio_cost(file):
    with open(file, 'rt') as file:
        file_data = csv.reader(file)
        header = next(file_data)
        for line_nbr, line in enumerate(file_data, start=1):
            try:
                # print(int(line[1]))
                print(f"{line[0]:>10s} {int(line[1]):>10} {float(line[2]):>10.2f} {(int(line[1])*float(line[2])):15.2f}")
            except ValueError:
                print(f"Line number: {line_nbr} Couldn't convert {line}")


if __name__ == '__main__':
    print_portfolio_cost('Data/missing.csv')
