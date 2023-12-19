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


"""
DICTIONARIES 2.2
"""

def calc_portfolio_dict(filename):
    import csv
    total_cost = float()
    with open(filename, 'rt') as file:
        text = csv.reader(file)
        header = next(text)
        for line in text:
            d = {
                header[0]: line[0]
                ,header[1]: int(line[1])
                ,header[2]: float(line[2])
                ,'cost': int(line[1]) * float(line[2])
            }
            line_list = list(d)
            print(line_list)
            total_cost += d['cost']
            for key in d:  # iterating over dictionary
                print(key, d[key]) # prints the key of dict and a value associated with the key
        keys = d.keys()  # returns dict_keys object
        print(keys)
        print(d.items())  # items gives a tuple made aout of dictionary
        a = d.items()
        dict_new = dict(a) # creates a dictionary out of tuple created by items() method
        print(dict_new)
    return total_cost

if __name__ == "__main__":
    # total_value = calculate_portfolio_cost_csv_3('Data/portfolio.csv')
    total_value = calc_portfolio_dict('Data/portfolio.csv')
    print_portfolio_cost(total_value)




