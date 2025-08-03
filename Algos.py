import numpy as np
import heapq

def point_finder(starting_point,ending_point,pol_coords):
    # This function loops through the file of polar coordinates and picks a starting/ending coordinate based on
    # the minimum Euclidean distance to the user-entered coordinates.
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
        new_start_distance = np.linalg.norm(check_coords - starting_point) # A more efficient way to calculate Euclidean distance.
        new_end_distance = np.linalg.norm(check_coords - ending_point)
        if new_start_distance < min_starting_distance:
            starting_index = i
            min_starting_distance = new_start_distance
        if new_end_distance < min_ending_distance:
            ending_index = i
            min_ending_distance = new_end_distance

    return starting_index, ending_index

# Calculate the Euclidean distance between 2 points.
def euclidean(v,car_coords,ending_index):
    return np.linalg.norm(car_coords[v] - car_coords[ending_index])

# Calculate the great-circle distance between 2 points.
def great_circle(v,car_coords,ending_index):
    R = 3389000.0

    chord = euclidean(v,car_coords,ending_index)
    dsigma = 2*np.arcsin(chord/(2*R))
    return R * dsigma

def AStar(starting_index,ending_index,adjalist,pol_coords,car_coords): # Evan
    # Using numpy arrays minimizes RAM usage and speeds up the code.
    num_points = len(adjalist)
    # Minimum total weights to travel to specified points.
    gs = np.zeros(num_points, dtype=np.int64)
    # Heuristic scores for each point.
    fs = np.full(shape=num_points, fill_value=np.iinfo(np.int64).max, dtype=np.int64)
    # Index (in pol_coords) of node previously accessed to get to this point.
    prev = np.full(shape=num_points, fill_value=-1, dtype=np.int64)
    visited = np.full(shape=num_points, fill_value=0, dtype=np.bool)

    # A priority queue data structure to improve time complexity.
    pq = [(0, starting_index)]

    # While the priority queue isn't empty...
    while pq:
        # Pop the point with the minimum heuristic score.
        _, u = heapq.heappop(pq)
        # Skip points already visited.
        if visited[u]:
            continue
        visited[u] = True

        # Stop when the goal point is reached.
        if u == ending_index:
            break

        # Loop through neighbors, determine heuristic score, update f, g values, and push relaxed neighbors into queue.
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
    # Find the most efficient path traversed and add it to the list "path". This will be used to draw the path.
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


