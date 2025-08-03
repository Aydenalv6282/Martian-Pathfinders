# Lower Resolution of File
# Only 1/lrf points would be saved to a new file. This is to reduce runtime and the workload on RAM.

import csv
import random

source_path = "Mars/MarsPolar.csv"

lrf = 3 # Lower Resolution Factor

result_path = "Mars/MarsPolarLR" + str(lrf) + ".csv"

count = 0

with open(source_path, "r") as rfile:
    reader = csv.reader(rfile)
    with open(result_path, "w", newline="") as wfile:
        writer = csv.writer(wfile)
        for line in reader:
            if random.randint(1,lrf) == lrf:
                writer.writerow(line)
            count += 1
            if count % 1000000 == 0:
                print(count/595000000)