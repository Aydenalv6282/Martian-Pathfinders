# Makes sure all points are unique

import csv

source_path = "Mars/MarsPolar.csv"
result_path = "Mars/MarsPolarND.csv"
count = 0

points = set()

with open(source_path, "r") as file:
    reader = csv.reader(file)
    for line in reader:
        points.add((float(line[0]), float(line[1]), float(line[2])))
        if count % 1000000 == 0:
            print(count / 595000000)
        count += 1

print(len(points))
print(count)

l_points = len(points)

if l_points != count:
    count = 0
    with open(result_path, "w", newline="") as file:
        writer = csv.writer(file)
        for p in points:
            writer.writerow(p)
            if count % 1000000 == 0:
                print(count/595000000)
            count += 1
