# Shrink XYZ Coords

import csv

source_path = "Mars/MarsCartesianLR100T.csv"

shrink = 1000

result_path = "Mars/MarsCartesianLR100S.csv"

count = 0

with open(source_path, "r") as rfile:
    reader = csv.reader(rfile)
    with open(result_path, "w", newline="") as wfile:
        writer = csv.writer(wfile)
        for line in reader:
            writer.writerow([str(float(line[0])/shrink) + " " + str(float(line[1])/shrink) + " " + str(float(line[2])/shrink)])