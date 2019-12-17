# Smart Crutch
An instrumented walking aid for monitoring crutch usage, with additional exercise monitoring system.

This project can be split into two stand alone systems, with the following Folder Names in the repo:

## 1. SmartCrutch
The code is written for use on an Adafruit Feather HUZZAH. This can be interfaced with using the Arduino IDE, found [here](https://www.arduino.cc/en/main/software). To set this IDE up for use with the Huzzah board, [these instructions](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-arduino-ide) should be followed. Additionally, a library must be installed and added to the Libary manager of the IDE to allow for interfacing with the HX711 (A load cell amplifier) - to reduce the risk of compatability errors experienced during implementation of the projcet, this can be found in this repo (more information below). 

1. **BioFeedback**
    1. **LED**
        1. **RGB Led Datasheeet**
        2. **led_test/led_test.ino**: *Code for testing operation of LEDs in feedback system. Cycles through RGB colours, changing colour every second.*
    2. **CoinMotor**
        1. **Vibration Motor datasheet**
        2. **motor_test/motor_test.ino**: *Code for testing operation of Motors in feedback system. Pulses motor on/off every 5s.*
2. **DataAnalysis**
    1. **spreadsheet.py**: ??
    2. **TimedTask.py**: ??
3. **LoadCell**
    1. **HX711**: *Folder containing Library and other useful materials to be included in the Arduino IDE Library manager.*
    2. **force_demo/force_demo.ino**: *Code for testing and demonstration of operation of Weight Sensor, LED and Motors in feedback system. Allows for calibration of weight sensor, Prints readings to the Serial Monitor and activiates Motor and LED above a threshold defined in the code.*
    3. **HX711 Datasheet**
4. **FullSystem**
    1. **full_system/full_system.ino**: *Code for full operation of on-crutch system.*
    2. **Wiring Diagram**
    3. **System Schematic**
5. **IMU**
    1. **imu_demo/imu_demo.ino**: *Code for testing and demonstration of operation of IMU.*
    2. **MPU9250 Datasheet**



#### 2. ExerciseTracker


A github directory with all schematics, software, datasheets, experimental results files, supplementary figures etc, 
along with a detailed README file explaining the contents. 
In theory, this should allow a future group to pick up the research from where you left it and move it forward.
