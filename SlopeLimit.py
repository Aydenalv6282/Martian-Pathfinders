import math
import csv
import numpy as np

source_path_1 = "Mars/MarsAdjaListLR100.csv" # Source Path for the Adjacency List
source_path_2 = "Mars/MarsPolarLR100.csv" # Source Path for Polar Coordinates
source_path_3 = "Mars/MarsCartesianLR100.csv"

# The starting and ending points are stored in arrays of size 2.
# We look through the polar coordinates and save the closest pair of coordinates.

adjalist = np.loadtxt(source_path_1, delimiter=",", dtype=np.int32)
pol_coords = np.loadtxt(source_path_2, delimiter=",", dtype=np.float64)
car_coords = np.loadtxt(source_path_3, delimiter=",", dtype=np.int32)
num_points = len(pol_coords)

def slope_limit(max_angle=10.0):
    removed = 0
    num_nodes = len(adjalist)
    for i in range(num_nodes):
        neighbors = adjalist[i]
        neighbor_len = len(neighbors)
        u = 0
        source_rad = pol_coords[i][2]
        while u < neighbor_len:
            v = neighbors[u]
            if v < 0 or v >= num_points:
                u += 2
                continue
            if u + 1 >= neighbor_len:
                break
            run = neighbors[u + 1]
            dest_rad = pol_coords[v][2]
            rise = dest_rad - source_rad

            angle_rad = math.atan2(abs(rise), run)
            angle_deg = math.degrees(angle_rad)

            if angle_deg > max_angle:
                if neighbors[u] != -1:
                    removed += 1
                adjalist[i][u] = -1
                adjalist[i][u + 1] = -1
            u += 2

    f = "Mars/MarsAdjaListLR100N20S1.csv"
    with open(f, "w") as file:
        writer = csv.writer(file)
        for i in range(len(adjalist)):
            writer.writerow(adjalist[i])

    return removed

before = sum(1 for row in adjalist for i in range(0, len(row), 2) if row[i] >= 0)
removed = slope_limit(10.0)
after = sum(1 for row in adjalist for i in range(0, len(row), 2) if row[i] >= 0)

print(f"Valid edges before: {before}")
print(f"Edges removed by slope filter: {removed}")
print(f"Valid edges after: {after}")
print(removed/before)