import numpy as np
import math
import heapq

# You can ignore all code here up until line 39.

# source_path_1 = "Mars/MarsAdjaListLR100N20.csv" # Source Path for the Adjacency List
# source_path_2 = "Mars/MarsPolarLR100.csv" # Source Path for Polar Coordinates
# source_path_3 = "Mars/MarsCartesianLR100.csv"

# The starting and ending points are stored in arrays of size 2.
# We look through the polar coordinates and save the closest pair of coordinates.

# starting_point = np.array([np.float64(input("Enter starting longitude: ")), np.float64(input("Enter starting latitude: "))])
# ending_point = np.array([np.float64(input("Enter ending longitude: ")), np.float64(input("Enter ending latitude: "))])

def point_finder(starting_point,ending_point,pol_coords):
    starting_index = 0
    min_starting_distance = np.inf
    ending_index = 0
    min_ending_distance = np.inf
    num_points = len(pol_coords)
    for i in range(num_points):
        if i % 1000000 == 0:
            print(i/num_points)
        if (int(starting_point[0]) != int(pol_coords[i][0]) or int(starting_point[1]) != int(pol_coords[i][1])) and (int(ending_point[0]) != int(pol_coords[i][0]) or int(ending_point[1]) != int(pol_coords[i][1])):
           continue
        check_coords = np.array([pol_coords[i][0], pol_coords[i][1]])
        new_start_distance = np.linalg.norm(check_coords - starting_point)
        new_end_distance = np.linalg.norm(check_coords - ending_point)
        if new_start_distance < min_starting_distance:
            starting_index = i
            min_starting_distance = new_start_distance
        if new_end_distance < min_ending_distance:
            ending_index = i
            min_ending_distance = new_end_distance

    return starting_index, ending_index


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

def euclidean(v,car_coords,ending_index):
    return np.linalg.norm(car_coords[v] - car_coords[ending_index])

def great_circle(v,car_coords,ending_index):
    R = 3389000.0

    chord = euclidean(v,car_coords,ending_index)
    dsigma = 2*np.arcsin(chord/(2*R))
    return R * dsigma

def AStar(starting_index,ending_index,adjalist,pol_coords,car_coords): # Evan
    num_points = len(adjalist)
    gs = np.zeros(num_points, dtype=np.int64)
    fs = np.full(shape=num_points, fill_value=np.iinfo(np.int64).max, dtype=np.int64)
    prev = np.full(shape=num_points, fill_value=-1, dtype=np.int64)
    visited = np.full(shape=num_points, fill_value=0, dtype=np.bool)

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
            f = g + great_circle(v, car_coords, ending_index)
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

# Needs to take in starting and ending points, the adjacency list, and the polor coordinates
def Dijkstras(starting_index,ending_index,adjalist,pol_coords): # Sam
    num_points = len(adjalist)
    next = np.full(shape=num_points, fill_value=np.iinfo(np.int64).max, dtype=np.int64)
    prev = np.full(shape=num_points, fill_value=-1, dtype=np.int64)
    visited = np.full(shape=num_points, fill_value=0, dtype=np.bool)

    # priority queue that stores (current_dist, node) and has the source node already in it
    pq = [(0, starting_index)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        # if node already has been processed, then skipped
        if visited[u]:
            continue
        visited[u] = True

        # end if reach target node
        if u == ending_index:
            break

        neighbors = adjalist[u]
        # iterate over the neighbor list
        for i in range(0, len(adjalist[u]), 2):
            v = neighbors[i]
            w = neighbors[i + 1]
            # if better path to v is found, then update it
            if current_dist + w < next[v]:
                # update the distance
                next[v] = current_dist + w
                # record the predecessor of the current node
                prev[v] = u
                # push updated values
                heapq.heappush(pq, (current_dist + w, v))
    print("Done pathfinding!")
    # reconstruct the path
    path = []
    node = ending_index
    while node != starting_index:
       path.append((pol_coords[node][0], pol_coords[node][1]))
       node = prev[node]
    path.append((pol_coords[starting_index][0], pol_coords[starting_index][1]))
    return path


