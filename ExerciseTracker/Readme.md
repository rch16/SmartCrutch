# Exercise tracker

## API

### Installation of dependencies

To install libraries used you will want to use:

    pip install [Library Name]

Some of the libraries used are flask, numpy and pandas.

### Config files

To change the exercises that the tracker can track you will want to edit the CSV files which contain the coordinates that translate to the vectors of a correct execution.

### Run API

To run the API you will need to make sure that all the ROS nodes are running. Once this is done we can run the API which will than be accesible to the app. Run the API by using:

    python api.py

## ROS nodes
### Installation

#### Installation from Packages

To install all packages from the this repository as Debian packages use

    sudo apt-get install ros-kinetic-[Name of dependencies]

#### Building from Source

##### Dependencies

- [Robot Operating System (ROS)](http://wiki.ros.org) (middleware for robotics),
- [OpenNi launcher](http://wiki.ros.org/openni_launch) (Driver for Kinect) ,
- [OpenNi tracker](http://wiki.ros.org/openni_tracker) (Skeletal tracking) ,
- [rosbridge-server](http://wiki.ros.org/rosbridge_suite) (Communication between listener and api.py)


##### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using

	cd catkin_workspace/src
	git clone https://github.com/rch16/SmartCrutch/tree/master/ExerciseTracker/ROS
	cd ../
	catkin_make


### Usage
Run the OpenNi launcher to start Kinect with 
	roslaunch ROS start.launch
Run the tf listener and OpenNi skeletal tracker with 
	roslaunch ROS start2.launch



### Nodes

#### OpenNi launch
Launch files to open an OpenNI device and load all nodelets to convert raw depth/RGB/IR streams to depth images, disparity images, and (registered) point clouds.

#### OpenNi tracker
Detects users in the Kinect frame and perform calibration. After this is successful, broadcast the tf over the /tf topic.

#### tf_Listener
Listens to the /tf broadcasted by the OpenNi tracker and inserts the data into a queue for api.py to process

##### Subscribed Topics
/tf (Transform of the planes with respect to the head)
There are subtopics such as 
* /head
* /neck
* /torso
* /left_shoulder
* /left_elbow
* /left_hand
* /right_shoulder
* /right_elbow
* /right_hand
* /left_hip
* /left_knee
* /left_foot
* /right_hip
* /right_knee
* /right_foot
For example to access the head subtopic, subscribe to /tf/head

