# Martian Pathfinders
## Demonstration Video
## Downloading the Project
## Running the Project
### Starting
Ensure that in the same folder as the executable, you also have a folder named "Mars" with the csv files containing all the relevant data. The window may take 20-30 seconds to appear, since many gigabytes of data need to be loaded into RAM. Once started, you should see this:

![](https://github.com/Aydenalv6282/Martian-Pathfinders/blob/main/other_images/MP_Start.png)

### Setting the Points
Once this screen is loaded in, you can begin typing in your coordinates. The first box next to "From" is the longitude of your starting point, and the second box is the latitude. The same applies to the "To" point. Once your points have been written, click "Set Points" and you should see them marked on the map like this:

![](https://github.com/Aydenalv6282/Martian-Pathfinders/blob/main/other_images/Mars_Set_Points.png)

The center of the map is at 0° longitude. The bottom is -90° latitude, and the top is 90° latitude. The left and right sides are 180°. Note that near the edges and 0° longitude, there are not many data points. So, pathfinding in these areas _will not yield accurate paths._ Loading the entire dataset to get around this is not feasible, as it would likely use more than 64 gigabytes of RAM.
