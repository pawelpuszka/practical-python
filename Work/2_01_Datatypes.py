"""
TUPLES, CSV files
"""
def calculate_portfolio_cost_csv(filename):
    import csv
    stock = ()  # tuple
    cost = float()
    total_cost = float()
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            stock = row
            cost = float(stock[1]) * float(stock[2])
            total_cost += cost

    return total_cost

def calculate_portfolio_cost_csv_2(filename):
    import csv
    stock = ()  # tuple
    total_cost = float()

    with open(filename, 'rt') as file:
        rows = csv.reader(file)  # reads the whole file to rows
        headert = next(rows)  # reads the header
        print(headert)
        for row in rows:
            stock = (str(row[0]), float(row[1]), float(row[2]), float(row[1]) * float(row[2]))
            print(stock)
            total_cost += stock[3]

    return total_cost


def calculate_portfolio_cost_csv_3(filename):
    import csv
    stock =()
    name = str()
    shares = int()
    cost = float()
    total_cost = float()

    with open(filename, 'rt') as file:
        whole_file = csv.reader(file)
        header = next(whole_file)
        for row in whole_file:
            name, shares, cost = row
            total_cost += int(shares) * float(cost)

    return total_cost


def print_portfolio_cost(cost):
    print(cost)

if __name__ == "__main__":
    total_value = calculate_portfolio_cost_csv_3('Data/portfolio.csv')
    print_portfolio_cost(total_value)

"""
DICTIONARIES 2.2
"""


