import numpy as np

source_path_1 = "Mars/MarsAdjaListLR100N20.csv" # Source Path for the Adjacency List
source_path_2 = "Mars/MarsPolarLR100.csv" # Source Path for Polar Coordinates
source_path_3 = "Mars/MarsCartesianLR100.csv"

# The starting and ending points are stored in arrays of size 2.
# We look through the polar coordinates and save the closest pair of coordinates.

adjalist = np.loadtxt(source_path_1, delimiter=",", dtype=np.int32)
pol_coords = np.loadtxt(source_path_2, delimiter=",", dtype=np.float64)
car_coords = np.loadtxt(source_path_3, delimiter=",", dtype=np.int32)
num_points = len(pol_coords)

