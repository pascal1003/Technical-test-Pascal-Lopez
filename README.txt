FOLDER ORDER:

deteccion_yolo.py: First test, saves the YOLO detection images in "resultados_ojas"

clasificacion.py: Classifies the plants and finds the centroid, saves the results in "resultados_plantas"

Paltech: Folder with ROS2-related files

ALGORITHM ACHIEVEMENTS

I was able to estimate the center of the plants by first finding the center of each detected plant (bounding box) and then using DBSCAN to group nearby centers into clusters by distance. For each group, I took the outermost points to create a new rectangle encompassing all the leaves in the group, and from that rectangle I calculated the final centroid.


GOOD THINGS I ACHIEVED

Classification algorithm working: detects plants, calculates centers and groups by proximity

Basic ROS nodes created: can send and receive messages (currently only text)

Clear visualization: draws bounding boxes, individual centers


FUTURE IMPROVEMENTS WITH MORE TIME

With more than 2 hours, I would achieve:

Fully integrate the detection code into the ROS nodes

Create a complete image publisher/subscriber system


PROBLEMS I ENCOUNTERED

Time wasted installing libraries: the computer had outdated versions of certain libraries and some packages were missing

Adjusting DBSCAN parameters

ROS-Python integration: initial setup takes time

Problems with submission: I noticed when uploading the repository that the folder was empty, and it took me a long time to find and copy the correct files to the repository.
