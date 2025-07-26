# All Nearest Neighbors
# Will generate an adjacency list from a list of cartesian coordinates

from sklearn.neighbors import NearestNeighbors
import numpy as np
import csv
import gc

source_path = "Mars/MarsCartesian.csv"
result_path = "Mars/MarsAdjaList.csv"
neighbor_count = 5

cart_coords = np.loadtxt(source_path, delimiter=",", dtype=np.int32)
print("Loaded cart_coords")
nn = NearestNeighbors(n_neighbors=neighbor_count, algorithm='kd_tree', metric="euclidean").fit(cart_coords)
distances, indices = nn.kneighbors(cart_coords)
del cart_coords
gc.collect()

print("Done calculating ANN!")

with open(result_path, "w", newline="") as mdata:
    writer = csv.writer(mdata)
    for i in range(len(distances)):
        line = []
        for n in range(1, neighbor_count):
            line.append(indices[i][n])
            line.append(int(distances[i][n]))
        writer.writerow(line)
