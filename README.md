# Martian Pathfinders
## Running the Project
### Starting
Ensure that in the same folder as the executable, you also have a folder named "Mars" with the csv files containing all the relevant data. The window may take 20-30 seconds to appear, since many gigabytes of data need to be loaded into RAM. Once started, you should see this:

![](https://github.com/Aydenalv6282/Martian-Pathfinders/blob/main/other_images/MP_Start.png)

### Setting the Points
Once this screen is loaded in, you can begin typing in your coordinates. The first box next to "From" is the longitude of your starting point, and the second box is the latitude. The same applies to the "To" point. Once your points have been written, click "Set Points" and you should see them marked on the map like this:

![](https://github.com/Aydenalv6282/Martian-Pathfinders/blob/main/other_images/MP_Set.png)

### Calculating the Path
To choose the pathfinding algorithm you wish to execute behind the scenes, simply select the "Dijkstra" or "Astar" buttons on the bottom right. The selected algorithm will be used once the "Start" button is pressed.

![](https://github.com/Aydenalv6282/Martian-Pathfinders/blob/main/other_images/MP_Path.png)

Notice that the path drawn isn't simply a straight line. This is because a straight line would run into a mountanous region, and our pathfinding algorithms avoid traveling on areas that are too steep. Here is a heightmap for reference:

![](https://github.com/Aydenalv6282/Martian-Pathfinders/blob/main/other_images/topography.png)

### Start
After pressing the "Start" button located on the bottom right of your screen, a new window will be displayed containing a 3 dimensional rendering of the planet Mars with the path displayed on the surface. Closing this window will bring you back to the first window. Have fun exploring!

![](https://github.com/Aydenalv6282/Martian-Pathfinders/blob/main/other_images/Planet_showcase.gif)

### Notes
The center of the map is at 0° longitude. The bottom is -90° latitude, and the top is 90° latitude. The left and right sides are 180°. Note that near the edges and 0° longitude, there are not many data points. So, pathfinding in these areas _will not yield accurate paths._ Loading the entire dataset to get around this is not feasible, as it would likely use more than 64 gigabytes of RAM. Please note, crashes frequently occur for some Mac OS users.
## Demonstration Video

## Downloading the Project
The essential files are MapGenerator.py, main.py, PlanetViewer.py, and Algos.py. Pygame, numpy, PyOpenGL, pillow, and matplotlib are all also required. If you want to run this program in your IDE, simply download the listed files and use pip to install the listed libraries. The dataset used along with the listed files can be found here: https://drive.google.com/file/d/1ZzVTxSKxX_KW3XTG7uKGCKuo5No5QyqI/view?usp=sharing
