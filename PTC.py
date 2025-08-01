# Polar to Cartesian

import csv
import numpy as np

source_path = "Mars/MarsPolarLR3.csv"
result_path = "Mars/MarsCartesianLR3.csv"
count = 0

with open(source_path, "r") as mdatap:
    with open(result_path, "w", newline="") as mdatac:
        reader = csv.reader(mdatap)
        writer = csv.writer(mdatac)
        for line in reader:
            rho = float(line[2])
            lon = np.deg2rad(float(line[0]))
            lat = np.deg2rad(float(line[1]))
            x = int(rho*np.cos(lat)*np.sin(lon))
            y = int(rho*np.sin(lat)*np.sin(lon))
            z = int(rho*np.cos(lon))
            writer.writerow([x, y, z])
            count += 1