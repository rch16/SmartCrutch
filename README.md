# SmartCrutch
Imperial College London EEE Human-Centered Robotics Research Project

## Introduction
The purpose of this project was to investigate how a sensor-enabled crutch could be used to improve injury recovery, through:
- Regular feedback for the patient and physicians on use and gate with the crutches
- A 3D video tracking system to provide the patient with feedback on their exercise technique

The full research paper containing the group's findings and further information about the system implementation can be found [here](https://github.com/rch16/SmartCrutch/blob/master/Research%20Paper.pdf).

This repository contains all the schematics, code and instructions required to reconstruct the system, and continue the research.

# Crutch Monitoring and Feedback System
## System Diagram

<img src="https://github.com/rch16/SmartCrutch/blob/master/SmartCrutches/FullSystem/Hardware_System_Diagram.png">

## Component Diagram

<img src="https://github.com/rch16/SmartCrutch/blob/master/SmartCrutches/FullSystem/Crutch_System_Diagram.png" width="400">

## Hardware

* **Microcontroller**: Adafruit Feather Huzzah
* **Battery**: 3.7V Li-ion cell
* **Weight Sensor**: Load Cell and HX711 Load Cell Amplifier
* **Inertial Measurement Unit (IMU)**: MPU9250
* **Bio-Feedback**: RGB LED and Coin Vibration Motor

## Crutch Software

Located within the SmartCrutches Folder:

**IMU**:
* **imu_demo/imu_demo.ino**: Code for testing and demonstration of operation of IMU

**LoadCell**:
* **force_demo/force_demo.ino**: Code for testing and demonstration of operation of Weight Sensor, LED and Motors in feedback system. Allows for calibration of weight sensor, Prints readings to the Serial Monitor and activiates Motor and LED above a threshold defined in the code.

**BioFeedback**:
* **LED/led_test/led_test.ino**: Code for testing operation of LEDs in feedback system. Cycles through RGB colours, changing colour once a second.
* **Motor/motor_test/motor_test.ino**: Code for testing operation of Motors in feedback system. Pulses motor on/off every 5s.

**FullSystem**:
* **full_system/full_system.ino**: Code for full operation of on-crutch system, including transfer to the Google Sheet for treatment by the Data Analysis section. Editing the links found in this code will change the end location of the data transfer.

## Data Analysis
The data analysis is done using two scripts:
* **TimedTask.py**
* **spreadsheet.py**

**TimedTask.py** checks wether or not the new data has been added to the sheet. You can control how long it performs this check for and how often it checks by changing the parameters in **sleep** and **Repeatedimer** respectfully. To set up **TimedTask.py** you will need to use the sheetfu library to access the google sheets you want to use. This library was hosen over the official google api as it gives slightly more flexibility.

When **TimedTask.py** finds that the dimensions of the google sheet have changed (meaning that data was added) it runs **spreadsheet.py**. One limitation is that you cannot check for an update to the google sheet quicker than **speadsheet.py** takes to run as this will cause errors and crashes.

**Spreadsheet.py** is the script that actually analyses the data. When called, it takes the most recent X lies of data added at the botom of the google sheet. It is therefore important that you agree ahead of time with the person handling the data transfer from the crutch to the sheet how big your batch sizes will be as you will want to change the range of rows looked at based off of that number. You also need to agree how the batch is formatted. Currently, each batch is preceded with a "New upload" row, a row dedicated to the date and timeand a row indicating the start of the sample. These must all be taken into account so that the script knows where to look to find the actual data.

The only other thing that needs to be changed in the **spreadsheet.py** script the the value you decide to assign for the weight threshold. This is imporant as it is used to determine what consitutes a step using the crutch which impacts many of the end values computed. Similarly to the **TimedTask.py** you will use the sheetfu library to connect to both the google sheet containing the raw data but also the google sheet which you will be sending the data to. More information can be found on how to do this here: https://github.com/socialpoint-labs/sheetfu/blob/master/documentation/usage.rst


## System Setup
The system can be assembled by following this wiring diagram: 

<img src="https://github.com/rch16/SmartCrutch/blob/master/SmartCrutches/FullSystem/Wiring_Diagram.png">


The code is written for use on an Adafruit Feather HUZZAH. This can be interfaced with using the Arduino IDE, found [here](https://www.arduino.cc/en/main/software). To set this IDE up for use with the Huzzah board, [these instructions](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-arduino-ide) should be followed. Additionally, a library must be installed and added to the Libary manager of the IDE to allow for interfacing with the HX711 (A load cell amplifier) - to reduce the risk of compatability errors experienced during implementation of the project, this can be found in this repo [here](www.github.com/rch16/SmartCrutch/SmartCrutches/LoadCell/HX711).

To get the on-crutch system running, download, compile and load the code found [here](https://github.com/rch16/SmartCrutch/tree/master/SmartCrutches/FullSystem/full_system) onto your board. Open the Serial Monitor at the Baud rate specified in the code for debugging.

# Mobile App

To be able to interact with the mobile application the API and the ROS nodes need to be running. This is because the mobile application will need to redirect itself to the internet address of the API server.

## Building the Mobile App

To build the mobiles app requires the latest version of Android Studio. When importing the project, use the gradle build in SmartCrutch/App/HCR_App/ directory.

This application requires, Android SDK Platform 28 and at least Android 9 to run on the target device.
To install the app on a mobile devices, run the command.

    gradlew assembleDebug

This will build an APK in build/outputs/apk. This apk file then can be transferred to the mobile device and installed.

# Exercise Monitoring and Feedback System

## System Diagram
<img src="https://github.com/rch16/SmartCrutch/blob/master/ExerciseTracker/Figures/Complete_Exercise_Tracker_System.png" width="400">

## Hardware

The only hardware requirement to use the Exercise Tracker is to have a Kinect camera, connected to a computer. This computer must be able to run all the scripts listed in the ExerciseTracker folder.

## Data Analysis

visual_plot.py can be used to plot the skeletal profiles from the coordinates of all elements of the human body of the user.


## API

### Installation of dependencies

To install libraries used, in Mac OS/Linux Terminal or Windows Command Prompt:

    pip install [Library Name]

Some of the libraries used are flask, numpy and pandas.

### Config files

To change the exercises that the tracker can track, you will want to edit the CSV files. These contain the coordinates that translate to the vectors of a correct execution.

### Run API

To run the API, you will to ensure that all the ROS nodes are running. Once this is done the API can be run, which will than be accesible to the app. Run the API by using:

    python api.py

## ROS nodes

### Installation

#### Installation from Packages

To install all packages from this repository as Debian packages, use:

    sudo apt-get install ros-kinetic-[Name of dependencies]

#### Building from Source

##### Dependencies

- [Robot Operating System (ROS)](http://wiki.ros.org) (middleware for robotics),
- [OpenNi launcher](http://wiki.ros.org/openni_launch) (Driver for Kinect) ,
- [OpenNi tracker](http://wiki.ros.org/openni_tracker) (Skeletal tracking) ,
- [rosbridge-server](http://wiki.ros.org/rosbridge_suite) (Communication between listener and api.py)


##### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using the following commands:

	cd catkin_workspace/src
	git clone https://github.com/rch16/SmartCrutch/tree/master/ExerciseTracker/ROS
	cd ../
	catkin_make


### Usage
Run the OpenNi launcher to start Kinect with start.launch and
run the tf listener and OpenNi skeletal tracker with start2.launch

	roslaunch ROS start.launch
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
