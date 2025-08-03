from PIL import Image
import matplotlib.pyplot as plt

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
    dpi = 100
    fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi) # Ensures figure is same size as input
    ax = plt.Axes(fig,[0,0,1,1])
    fig.add_axes(ax)
    ax.imshow(mars)
    ax.plot(x_coords, y_coords, color='red', linewidth=1)
    ax.set_axis_off()
    plt.savefig("output/mars_path.png", dpi=dpi, bbox_inches='tight', pad_inches=0) # Generates Image and saves
    plt.close(fig)

# Takes in vector of coordinate tuples (only 2 in this case) and creates a new image with these
# two coordinates highlighted
def PointmapGen(LLC):
    path = []
    mars = Image.open("elements/nasa_mars_map_001.png")
    width,height = mars.size
    for i in LLC:
        path.append(cartesian(i,width,height))

    x_coords, y_coords = zip(*path)
    dpi = 100
    fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi) # Ensures figure is same size as input
    ax = plt.Axes(fig,[0,0,1,1])
    fig.add_axes(ax)
    ax.imshow(mars)
    ax.scatter(x_coords, y_coords, color='red', linewidth=1,edgecolors='black')
    ax.set_axis_off()
    plt.savefig("output/mars_index.png", dpi=dpi, bbox_inches='tight', pad_inches=0) # Generates Image and saves
    plt.close(fig)

