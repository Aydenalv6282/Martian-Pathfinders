# Shrink XYZ Coords
# This file was used to visualize the cartesian coordinates as a point cloud.
# This was to ensure that we ended up with a sphere and properly converted from polar to cartesian.

import csv
import numpy as np

source_path = "Mars/MarsCartesian.csv"

shrink = 1000

result_path = "Mars/MarsCartesianS.csv"

count = 0

car_coords = np.loadtxt(source_path, delimiter=",", dtype=np.int32)

with open(result_path, "w", newline="") as wfile:
    writer = csv.writer(wfile)
    for line in car_coords:
        writer.writerow([str(float(line[0])/shrink) + " " + str(float(line[1])/shrink) + " " + str(float(line[2])/shrink)])