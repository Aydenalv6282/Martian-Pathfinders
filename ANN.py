# All Nearest Neighbors
# Will generate an adjacency list from a list of cartesian coordinates

from sklearn.neighbors import NearestNeighbors
import numpy as np
import csv
import gc

source_path = "Mars/MarsCartesianLR10.csv"
result_path = "Mars/MarsAdjaListLR10N20.csv"
neighbor_count = 20

# Loading the file using numpy instead of csv.reader is much more efficient.
# Each is of type int32 to save RAM space.
cart_coords = np.loadtxt(source_path, delimiter=",", dtype=np.int32)
print("Loaded cart_coords")
# A KD Tree turns O(n) complexity into O(logn) complexity for finding the nearest neighbor to a particular point.
# Finding all nearest neighbors becomes O(d*nlogn) complexity where d is the number of dimensions.
nn = NearestNeighbors(n_neighbors=neighbor_count, algorithm='kd_tree', metric="euclidean").fit(cart_coords)
distances, indices = nn.kneighbors(cart_coords)
del cart_coords
gc.collect()

print("Done calculating ANN!")

# Write all the neighbors and weights into a file, this is the adjacency list.
with open(result_path, "w", newline="") as mdata:
    writer = csv.writer(mdata)
    for i in range(len(distances)):
        line = []
        for n in range(1, neighbor_count):
            line.append(indices[i][n])
            line.append(int(distances[i][n]))
        writer.writerow(line)
        if i % 100000 == 0:
            print(i/len(distances))
