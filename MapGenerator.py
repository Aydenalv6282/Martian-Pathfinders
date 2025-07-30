from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math

# This function just converts polar coords (in tuple form) to cartesian
def cartesian(polar,width,height):
    x = width/2*math.cos(np.deg2rad(polar[1]))*math.cos(np.deg2rad(polar[0]))+width/2
    y = height/2*math.cos(np.deg2rad(polar[1]))*math.sin(np.deg2rad(polar[0]))+height/2
    return (x,y)
# This function will take in a vector of coordinate tuples and create an image
# with the given path
# Mars map is 1440 720
def MapGen(LLC):
    path = []
    mars = Image.open("elements/nasa_mars_map_001.png")
    width,height = mars.size
    for i in LLC:
        path.append(cartesian(i,width,height))

    x_coords, y_coords = zip(*path)
    plt.figure(figsize=(8, 8))
    plt.imshow(mars)
    plt.plot(x_coords, y_coords, color='red', linewidth=1)  # Draw path
    plt.scatter(x_coords, y_coords, color='yellow', s=20)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


polar_coords = [(0,180)]
MapGen(polar_coords)