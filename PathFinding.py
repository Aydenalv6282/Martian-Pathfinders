import numpy as np
import gc
import math
import heapq
import MapGenerator

# You can ignore all code here up until line 39.

source_path_1 = "Mars/MarsAdjaListLR100N100.csv" # Source Path for the Adjacency List
source_path_2 = "Mars/MarsPolarLR100.csv" # Source Path for Polar Coordinates
source_path_3 = "Mars/MarsCartesianLR100.csv"

# The starting and ending points are stored in arrays of size 2.
# We look through the polar coordinates and save the closest pair of coordinates.

starting_point = np.array([np.float64(input("Enter starting longitude: ")), np.float64(input("Enter starting latitude: "))])
ending_point = np.array([np.float64(input("Enter ending longitude: ")), np.float64(input("Enter ending latitude: "))])
starting_index = 0
min_starting_distance = np.inf
ending_index = 0
min_ending_distance = np.inf

pol_coords = np.loadtxt(source_path_2, delimiter=",", dtype=np.float64)
car_coords = np.loadtxt(source_path_3, delimiter=",", dtype=np.int32)
num_points = len(pol_coords)
for i in range(num_points):
    if i % 100000 == 0:
        print(i/num_points)
    check_coords = np.array([pol_coords[i][0], pol_coords[i][1]])
    new_start_distance = np.linalg.norm(check_coords - starting_point)
    new_end_distance = np.linalg.norm(check_coords - ending_point)
    if new_start_distance < min_starting_distance:
        starting_index = i
        min_starting_distance = new_start_distance
    if new_end_distance < min_ending_distance:
        ending_index = i
        min_ending_distance = new_end_distance

print(starting_index, ending_index)

adjalist = np.loadtxt(source_path_1, delimiter=",", dtype=np.int32)

'''
- When the pathfinding is done, write a list of all the indexes of the coordinates visited in order to a file.
- Use the variables "starting_index" and "ending_index".
- These are the index of the closest points to the entered value. They may not be exact.
- adjalist[starting_index] is the starting position, same for ending.
- Each index in adjalist has 8 elements. The first one is the closest neighbor, the second is the distance to the
  closest neighbor, the third is the second closest neighbor, the fourth is the distance...
- The pathfinding algorithms should minimize total distance traveled. No need to account for slope, we can modify
  the file later in the project to add that in with no modifications to the pathfinding.
'''

def AStar(): # Evan
    gs = [0] * num_points
    fs = [math.inf] * num_points
    prev = [-1] * num_points
    visited = [False] * num_points

    pq = [(0, starting_index)]

    while pq:
        _, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        if u == ending_index:
            break

        neighbors = adjalist[u]
        for i in range(0, len(adjalist[u]), 2):
            v = neighbors[i]
            w = neighbors[i + 1]
            g = w + gs[u]
            f = g + np.linalg.norm(car_coords[v] - car_coords[ending_index])
            if f < fs[v]:
                gs[v] = g
                fs[v] = f
                prev[v] = u
                heapq.heappush(pq, (f, v))
    print("Done pathfinding!")
    path = []
    node = ending_index
    while node != starting_index:
        path.append((pol_coords[node][0], pol_coords[node][1]))
        node = prev[node]
    path.append((pol_coords[starting_index][0], pol_coords[starting_index][1]))

    return path


def to_cartesian(line):
    rho = line[2]
    lon = np.deg2rad(line[0])
    lat = np.deg2rad(line[1])
    x = rho * np.cos(lat) * np.sin(lon)
    y = rho * np.sin(lat) * np.sin(lon)
    z = rho * np.cos(lon)
    return x,y,z

def heuristic(n1,n2):
    # sqrt( (x2-x1)^2+(y2-1)^2 +())
    return math.sqrt((n2[0]-n1[0])**2 + (n2[1]-n1[1])**2 + (n2[2]-n1[2])**2)

def jumpPoint(): # Ayden
    pass

def Dijkstras(): # Sam
    next = [math.inf] * num_points
    prev = [-1] * num_points
    visited = [False] * num_points

    pq = [(0, starting_index)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        if u == ending_index:
            break

        neighbors = adjalist[u]
        for i in range(0, len(adjalist[u]), 2):
            v = neighbors[i]
            w = neighbors[i + 1]
            if current_dist + w < next[v]:
                next[v] = current_dist + w
                prev[v] = u
                heapq.heappush(pq, (current_dist + w, v))
    print("Done pathfinding!")
    path = []
    node = ending_index
    while node != starting_index:
       path.append((pol_coords[node][0], pol_coords[node][1]))
       node = prev[node]
    path.append((pol_coords[starting_index][0], pol_coords[starting_index][1]))

    return path

print("Starting Astar!")
MapGenerator.MapGen(AStar())
print("Starting Dijkstras!")
MapGenerator.MapGen(Dijkstras())

print("Done!")
