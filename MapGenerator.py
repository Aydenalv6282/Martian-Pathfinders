from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math
import csv

# This function just converts polar coords (in tuple form) to cartesian
def cartesian(polar, width, height):
    lon, lat = polar
    x = (lon + 180) * (width / 360) % width
    y = (90 - lat) * (height / 180) % height
    return x, y
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
    plt.figure(figsize=(8, 4))
    plt.imshow(mars)
    plt.plot(x_coords, y_coords, color='red', linewidth=1)  # Draw path
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("output/mars_path.png", dpi=180)
