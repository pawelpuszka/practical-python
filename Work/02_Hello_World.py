sears_tower_hgh = 442.3 * 100 * 10
bill_hgh = 0.11

bill_number = 1
num_of_days = 1
bills_tower = bill_hgh

while bill_hgh * bill_number < sears_tower_hgh:
    bill_number *= 2
    num_of_days += 1
    # bills_tower += bill_hgh * bill_number

print(num_of_days)
