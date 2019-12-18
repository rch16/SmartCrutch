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
	git clone https://github.com/ethz-asl/ros_package_template.git
	cd ../
	catkin_make


#### Unit Tests

Run the unit tests with

	catkin_make run_tests_ros_package_template


### Usage

Describe the quickest way to run this software, for example:

Run the main node with

	roslaunch ros_package_template ros_package_template.launch

### Config files

Config file folder/set 1

* **config_file_1.yaml** Shortly explain the content of this config file

Config file folder/set 2

* **...**

### Launch files

* **launch_file_1.launch:** shortly explain what is launched (e.g standard simulation, simulation with gdb,...)

     Argument set 1

     - **`argument_1`** Short description (e.g. as commented in launch file). Default: `default_value`.

    Argument set 2

    - **`...`**

* **...**

### Nodes

#### ros_package_template

Reads temperature measurements and computed the average.


##### Subscribed Topics

* **`/temperature`** ([sensor_msgs/Temperature])

	The temperature measurements from which the average is computed.


##### Published Topics

...
