# Counts points in file

import csv

source_path = "Mars/MarsPolar.csv"
source_path_2 = "Mars/MarsPolarND.csv"
count_1 = 0
count_2 = 0

with open(source_path, "r") as mdata:
    reader = csv.reader(mdata)
    for line in reader:
        count_1 += 1
        if count_1 % 1000000 == 0:
            print(count_1/595000000)

with open(source_path_2, "r") as mdata:
    reader = csv.reader(mdata)
    for line in reader:
        count_2 += 1
        if count_2 % 1000000 == 0:
            print(count_2/595000000)

print()
print(count_1)
print(count_2)