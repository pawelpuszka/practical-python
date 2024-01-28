a = [x for x in range(10)]
print(a)
print(len(a))
print(sum(a))
print(a[:5])
a[2:10] = [x for x in range(20)]
print(a)

import csv

def read_file(filename):
    with open(filename, 'rt') as file:
        file_text = csv.reader(file)
        header = next(file_text)
        for i, line in enumerate(file_text, start=1):
            print(f"{i:<5} {line}")


def file_to_tuples(filename):
    shares_list = list()
    with open(filename, 'rt') as file:
        file_text = csv.reader(file)
        header = next(file_text)
        for line in file_text:
            share_info = tuple(line)
            shares_list.append(share_info)

        for name, number, price in shares_list:
            print(name, number, price)

        for line in shares_list:
            print(line)


def zip_to_dict(filename):
    list_of_pairs = list()
    with open(filename, 'rt') as file:
        file_text = csv.reader(file)
        header = next(file_text)
        for line in file_text:
            print(line)
            # pair = zip(header, line)
            list_of_pairs.append(dict(zip(header, line)))

    for pair in list_of_pairs:
        print(pair)


def zip_to_list(filename):
    x = list()
    with open(filename, 'rt') as file:
        file_text = csv.reader(file)
        header = next(file_text)
        for line in file_text:
            x = list(zip(header, line))
            print(x)



# 2.15
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


# 2.16
def portfolio_cost(file):
    total_cost = float()
    with open(file, 'rt') as file:
        file_data = csv.reader(file)
        header = next(file_data)
        for line_nbr, line in enumerate(file_data, start=1):
            record = dict(zip(header, line))
            try:
                name = record['name']
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares * price
                # print(f"{name:>10s} {shares:>10} {price:>10.2f} {total_cost:15.2f}")
            except ValueError:
                print(f"Line number: {line_nbr} Couldn't convert {line}")
    print(total_cost)


# 2.17


if __name__ == '__main__':
    # read_file('Data/portfolio.csv')
    # file_to_tuples('Data/portfolio.csv')
    # zip_to_dict('Data/portfolio.csv')
    # zip_to_list('Data/portfolio.csv')
    portfolio_cost('Data/portfolio.csv')
    print()
    portfolio_cost('Data/portfoliodate.csv')

