


def portfolio_cost(filename):
    value = float()
    with open(filename, 'rt') as f:
        header = next(f)
        for line in f:
            try:
                row = line.split(',')  # splits the string to list
                value += float(row[1]) * float(row[2])
            except ValueError:
                print("There are string instead of float")
    return value

def portfolio_cost_csv(filename):
    import csv
    with open(filename, 'rt') as file:
        csv_lines = csv.reader(file)
        header = next(csv_lines)
        for line in csv_lines:
            print(line)

def portfolio_cost_2():
    import sys
    import csv
    filename = str()
    value = float()
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    with open(filename, 'rt') as file:
        csv_lines = csv.reader(file)
        header = next(csv_lines)
        for line in csv_lines:
            value += float(line[1]) * float(line[2])
            # print(line)

        return value



if __name__ == "__main__":
    cost = portfolio_cost_2()
    print(cost)
    portfolio_cost_csv('Data/portfolio.csv')



"""
value = portfolio_cost('Data/missing.csv')
print(value)
"""

# portfolio_cost_csv('Data/portfolio.csv')

