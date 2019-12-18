# SmartCrutch
Imperial College London EEE Human-Centered Robotics Research Project

## Introduction
The purpose of this project was to investigate how a sensor-enabled crutch could be used to improve injury recovery, through:
- Regular feedback for the patient and physicians on use and gate with the crutches
- A 3D video tracking system to provide the patient with feedback on their exercise technique

The full research paper containing the group's findings can be found here.

This repository contains all the schematics, code and instructions required to reconstruct the system, and continue the research.

# Crutch Monitoring and Feedback System
## System Diagram

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
* **/imu_demo/imu_demo.ino**: Code for testing and demonstration of operation of IMU

**LoadCell**:
* **/force_demo/force_demo.ino**: Code for testing and demonstration of operation of Weight Sensor, LED and Motors in feedback system. Allows for calibration of weight sensor, Prints readings to the Serial Monitor and activiates Motor and LED above a threshold defined in the code.

**BioFeedback**:
* **/LED/led_test/led_test.ino**: Code for testing operation of LEDs in feedback system. Cycles through RGB colours, changing colour every second.
* **/Motor/motor_test/motor_test.ino**: Code for testing operation of Motors in feedback system. Pulses motor on/off every 5s.

**FullSystem**:
* **/full_system/full_system.ino**: Code for full operation of on-crutch system.

## Data Transfer
## Data Analysis

The following two scripts perform the data analysis
* **TimedTask.py**:
* **spreadsheet.py**:

## Mobile App

## System Setup
The code is written for use on an Adafruit Feather HUZZAH. This can be interfaced with using the Arduino IDE, found [here](https://www.arduino.cc/en/main/software). To set this IDE up for use with the Huzzah board, [these instructions](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-arduino-ide) should be followed. Additionally, a library must be installed and added to the Libary manager of the IDE to allow for interfacing with the HX711 (A load cell amplifier) - to reduce the risk of compatability errors experienced during implementation of the project, this can be found in this repo [here](www.github.com/rch16/SmartCrutch/SmartCrutches/LoadCell/HX711). 

# Exercise Monitoring and Feedback System
## System Diagram
## Hardware
## Data Analysis
## Mobile App
## System Setup
