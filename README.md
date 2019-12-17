# Smart Crutch
An instrumented walking aid for monitoring crutch usage, with additional exercise monitoring system.

This project can be split into two stand alone systems, with the following Folder Names in the repo:

## 1. SmartCrutch
The code is written for use on an Adafruit Feather HUZZAH. This can be interfaced with using the Arduino IDE, found [here](https://www.arduino.cc/en/main/software). To set this IDE up for use with the Huzzah board, [these instructions](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-arduino-ide) should be followed. Additionally, a library must be installed and added to the Libary manager of the IDE to allow for interfacing with the HX711 (A load cell amplifier) - to reduce the risk of compatability errors experienced during implementation of the projcet, this can be found in this repo (more information below). 


| Folders     | Subfolders    | Files       |  Contents               |
| ----------- |---------------| ------------|-------------------------|
| BioFeedback | LED           | RGB Led Datasheet   | Datasheet for RGB LED |
|             |               | led_test    | Folder containing led_test.ino code for testing operation of LEDs in feedback system. Cycles through RGB colours, changing colour every second. |
|             | CoinMotor     | Vibration Motor datasheet    | Datasheet for coin motor|
|             |               | motor_test   | Folder containing motor_test.ino code for testing operation of Motors in feedback system. Pulses motor on/off every 5s.|
| DataAnalysis|spreadsheet.py|              |             |
|             |TimedTask.py|              |             |
| LoadCell    | HX711         | *various*    |Folder containing Library and other useful materials to be included in the Arduino IDE Library manager.  |
|             |force_demo     |force_demo.ino|Code for testing and demonstration of operation of Weight Sensor, LED and Motors in feedback system. Allows for calibration of weight sensor, Prints readings to the Serial Monitor and activiates Motor and LED above a threshold defined in the code. |
|             |HX711 Datasheet|              |Datasheet for Load Cell Amplifier.|
|FullSystem   |full_system     |full_system.ino|Code for full operation of on-crutch system.|
|             |Wiring Diagram     | |Wiring diagram of full on-crutch system.|
|             |System Schematic|full_system.ino|System schematic of full on-crutch system.|
|IMU          |imu_demo     |imu_demo.ino|Code for testing and demonstration of operation of IMU. |
|             |MPU9250 Datasheet|              |Datasheet for MPU9250.|



#### 2. ExerciseTracker


A github directory with all schematics, software, datasheets, experimental results files, supplementary figures etc, 
along with a detailed README file explaining the contents. 
In theory, this should allow a future group to pick up the research from where you left it and move it forward.
