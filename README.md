#### PLEASE USE visgraph.py, NOT path.py

#### Installation
Install libgeos-dev if you don't have it (native geo library)  
`sudo apt-get install libgeos-dev`  
Also install shapely (Python wrapper providing geometric functions)  
`python -m pip install shapely`  
or whatever python package manager you use

Depending on your python installation, you might need to install yaml as well.  

#### Usage
To use the ROS pacakge, start roscore, and then run publisher.py in python 2.7, passing the file of the obstacle map in as a parameter
Ex: `python publisher.py my_map.json`


#### Using this for Trap Placement

THINGS THAT STILL NEED TO BE DONE FOR TRAP PLACEMENT:
1. Set default radius (200m) for a trap
2. Publish the list of trap coordinates in maintrap.py using publisher.py

To run the trap placement code, run the file called "maintrap.py". It has the main function. 
The other files required for the trap placement are "trapzone.py" and "t2.py". Refer to the 
other README in this repo for installing the shapely library. 

After running maintrap.py, a series of prompts appears on the console. The inputs include
specifying if a hard-coded map or a new map will be used. There are 3 hard-coded maps that 
can be selected. If a new map is used, the user will enter the number of points that define
the fly-zone. Then, they will input them as tuples of the form (x,y). Then, the obstacles will 
need to be specified in the same manner. Then, the user will input the radius of a trap (no
default is included in the code, but the competition says the default should be 200m). After
that, the user will be asked if they want to use a buffer. The buffer is used to shrink the 
fly-zone and expand the obstacles. The purpose of the buffer is to not allow traps to be placed
too close to the edges of the fly-zone. Then, the buffer amount is specified. After inputting 
all of this, a window will pop up that displays the fly-zone, obstacles, traps that are included, 
and traps that were excluded because they fell inside obstacles. 

The output of the program is a list of tuples. Each tuple represents the x,y coordinate for a trap. 
This list needs to be published to ros. Currently, a publisher has been written, but it does not 
publish the correct information. The publisher needs to publish the resulting list in maintrap.py. 
I have commented "THIS NEEDS TO BE PUBLISHED" on the variable that needs to be published. So just 
search for that. This should be easy with the publisher.py that has been written. 
