"""
DICTIONARIES
"""
import csv

def file_reading(filename):
    records = []  # empty list

    with open(filename, 'rt') as file:
        portfolio = csv.reader(file)
        header = next(portfolio)
        records.append(next(portfolio))
        records.append(next(portfolio))

    print(records)


def file_reading_2(filename):
    records = []
    line_rec = []
    with open(filename, 'rt') as file:
        next(file)
        for line in file:
            row = line.split(',')
            records.append((row[0], int(row[1]), float(row[2])))
            line_rec.append(line)

    print((records))
    print(line_rec)


def file_reading_3(filename):
    prices = {}
    portfolio = {}

    with open(filename, 'rt') as file:
        header = next(file).split(',')
        print(header)
        for line in file:
            row = line.split(',')
            portfolio = {
                header[0]: row[0]
                ,header[1]: row[1]
                ,header[2]: row[2]
            }
            prices[row[0]] = float(row[2])

            print(prices)
            print(portfolio)



"""
SETS 
"""

if __name__ == "__main__":
    # file_reading_3('Data/portfolio.csv')
    a = ['Baldur\'s Gate', 'Fallout', 'Civilization']
    b = ['Heroes Of Might and Magic', 'Diablo', 'Baldurs\'s Gate']
    games1 = set(a)
    games2 = set(b)
    games3 = games1 & games2
    print((games3))
