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


def zip_function(filename):
    with open(filename, 'rt') as file:
        file_text = csv.reader(file)
        header = next(file_text)
        print(header)
        for line in file_text:
            print(line)
            # pair = zip(header, line)
            print(dict(zip(header, line)))


if __name__ == '__main__':
    # read_file('Data/portfolio.csv')
    # file_to_tuples('Data/portfolio.csv')
    zip_function('Data/portfolio.csv')


exercise 2.13