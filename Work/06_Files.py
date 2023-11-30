value = float()
with open('Data/portfolio.csv', 'rt') as f:
    header = next(f)
    for line in f:
        row = line.split(',')  # splits the string to list
        value += float(row[1]) * float(row[2])

print('Total cost', value)


import gzip
with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')



