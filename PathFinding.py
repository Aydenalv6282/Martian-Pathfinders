import numpy as np
import gc
import math

# You can ignore all code here up until line 39.

source_path_1 = "Mars/MarsAdjaListLR100.csv" # Source Path for the Adjacency List
source_path_2 = "Mars/MarsPolarLR100.csv" # Source Path for Polar Coordinates

# The starting and ending points are stored in arrays of size 2.
# We look through the polar coordinates and save the closest pair of coordinates.

starting_point = np.array([np.float64(input("Enter starting longitude: ")), np.float64(input("Enter starting latitude: "))])
ending_point = np.array([np.float64(input("Enter ending longitude: ")), np.float64(input("Enter ending latitude: "))])
starting_index = 0
min_starting_distance = np.inf
ending_index = 0
min_ending_distance = np.inf

pol_coords = np.loadtxt(source_path_2, delimiter=",", dtype=np.float64)
num_points = len(pol_coords)
for i in range(num_points):
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
del pol_coords
gc.collect()

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
    pass

def jumpPoint(): # Ayden
    pass

def Dijkstras(): # Sam
    pass

