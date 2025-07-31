import numpy as np
import gc
import math
import heapq
import MapGenerator


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

# Heuristics
#
# def euclidean(v):
#     return np.linalg.norm(car_coords[v] - car_coords[ending_index])
#
# def euclidean2(v):
#     return np.linalg.norm(car_coords[v] - car_coords[ending_index])*1.4
#
# def lazy_haversine(v):
#     R = 3389000.0
#     eu_dist = euclidean(v)
#     return eu_dist + eu_dist**3/(24*(R**2))
#
# def manhattan(v):
#     xdif = abs(car_coords[v][0] - car_coords[ending_index][0])
#     ydif = abs(car_coords[v][1] - car_coords[ending_index][1])
#     zdif = abs(car_coords[v][2] - car_coords[ending_index][2])
#     return xdif+ydif+zdif
#
# def haversine(v):
#     R = 3389000.0
#     lat1 = np.deg2rad(pol_coords[v][1])
#     lon1 = np.deg2rad(pol_coords[v][0])
#     lat2 = np.deg2rad(pol_coords[ending_index][1])
#     lon2 = np.deg2rad(pol_coords[ending_index][0])
#
#     dlon = abs(lon1-lon2)
#     dlat = abs(lat1-lat2)
#     dsigma = np.arccos(np.sin(lat1)*np.sin(lat2)+np.cos(lat1)*np.cos(lat2)*np.cos(dlon))
#     return R*dsigma
#
# def lazy_harversine(v):
#     R = 3389000.0
#     lat1 = np.deg2rad(pol_coords[v][1])
#     lon1 = np.deg2rad(pol_coords[v][0])
#     lat2 = np.deg2rad(pol_coords[ending_index][1])
#     lon2 = np.deg2rad(pol_coords[ending_index][0])
#
#     dlon = abs(lon1-lon2)
#     dlat = abs(lat1-lat2)
#
#
# # Reference: https://stackoverflow.com/questions/53116475/calculating-diagonal-distance-in-3-dimensions-for-a-path-finding-heuristic
# def diagnal(v):
#     D1 = 1
#     D2 = 1.41
#     D3 = 1.73
#     xdif = abs(pol_coords[v][0] - pol_coords[ending_index][0])
#     ydif = abs(pol_coords[v][1] - pol_coords[ending_index][1])
#     zdif = abs(pol_coords[v][2] - pol_coords[ending_index][2])
#     min_dist = min(xdif, ydif, zdif)
#     max_dist = max(xdif, ydif, zdif)
#     mid_dist = xdif + ydif + zdif - min_dist - max_dist
#     return (D3-D2)*min_dist + (D2 - D1) * mid_dist + D1 * max_dist
#
# def AStar(heuristic): # Evan
#     gs = [0] * num_points
#     fs = [math.inf] * num_points
#     prev = [-1] * num_points
#     visited = [False] * num_points
#
#     pq = [(0, starting_index)]
#
#     while pq:
#         _, u = heapq.heappop(pq)
#         if visited[u]:
#             continue
#         visited[u] = True
#
#         if u == ending_index:
#             break
#
#         neighbors = adjalist[u]
#         for i in range(0, len(adjalist[u]), 2):
#             v = neighbors[i]
#             w = neighbors[i + 1]
#             g = w + gs[u]
#             f = g + heuristic(v)
#             if f < fs[v]:
#                 gs[v] = g
#                 fs[v] = f
#                 prev[v] = u
#                 heapq.heappush(pq, (f, v))
#     print("Done pathfinding!")
#     path = []
#     node = ending_index
#     while node != starting_index:
#         path.append((pol_coords[node][0], pol_coords[node][1]))
#         node = prev[node]
#     path.append((pol_coords[starting_index][0], pol_coords[starting_index][1]))
#     return path

# Needs to take in starting and ending points, the adjacency list, and the polor coordinates
def Dijkstras(starting_index,ending_index,adjalist,pol_coords): # Sam
    num_points = len(pol_coords)
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


