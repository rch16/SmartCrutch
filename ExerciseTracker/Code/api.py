from flask import Flask, jsonify, request
from threading import Thread
from multiprocessing import Process, Manager, Value
from math import pi
import numpy as np
import time
import ctypes
import pandas as pd
import json
import rosbridge
import settings
threshold = 50
import csv

# settings.init()

def transform(tuple_el):
    new_tuple_el = ()
    for el in tuple_el:
        el = el.replace("'", "\"")
        new_el = json.loads(el)
        new_tuple_el += (new_el['x'],new_el['y'],new_el['z'])
    return (new_tuple_el)

def readFile(csvFileName):
    data = pd.read_csv(csvFileName)

    subset = data[["head", "neck", "left_hand", "left_elbow", "left_shoulder", "torso", "right_shoulder", "right_elbow", "right_hand", "left_hip", "left_knee", "left_foot", "right_hip", "right_knee", "right_foot"]]

    tuples = [tuple(x) for x in subset.values]
    new_tuples = []
    for i in range(len(tuples)):
        new_tuples.append(transform(tuples[i]))
    return new_tuples

# def addToQueue(element):
#   qu.put(element)

#0.0.0.0:8003/api/start?exercise_number=1
exercise = []
exercise.append(readFile("excercise1.csv"))
exercise.append(readFile("excercise2.csv"))
exercise.append(readFile("excercise3.csv"))
exercise.append(readFile("excercise4.csv"))

execution_correct = Value(ctypes.c_bool, False)
feedback = Value('d', 0.5)

# manager = Manager()
# global qu
# qu = manager.Queue()

app = Flask('')
@app.route('/')
def home():
    return  "I'm alive"

@app.route('/api/set_threshold', methods=['PUT'])
def setThreshold():
    global threshold
    threshold = request.args.get('threshold')
    print("setting threshold to", threshold)
    return threshold

@app.route('/api/get_threshold', methods=['GET'])
def get():
    # return jsonify(threshold=threshold)
    return str(threshold)


@app.route('/api/start', methods=['GET'])
def add():
    # return jsonify(exercise=1, execution="Correct", feedback=1.0)


    while(settings.qu.qsize() != 0):
        settings.qu.get()

    exercise_number = int(request.args.get("exercise_number"))

    p1 = Process(target=check, args=(exercise_number,))
    p1.start()
    p2 = Process(target=get_stream)
    p2.start()
    p1.join()

    if(execution_correct.value):
        execution = "Correct"
    else:
        execution = "Not Correct"

    return jsonify(exercise=exercise_number, execution=execution, feedback=feedback.value)

def run():
    app.run(host='0.0.0.0',port=8000)

def get_stream():
    print("Started operarion") #change values here
#https://medium.com/initial-state/how-to-stream-push-data-to-a-real-time-dashboard-api-in-python-7a910e41c001

"""Center person around point eg torso"""

def check(exercise_number):
    exercise_data = exercise[exercise_number - 1]

    start_time = time.time()
    i = 0
    exercise_start_time = time.time()
    with open('state.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        while(i<len(exercise_data)):
            if((time.time() - start_time > 10)): #Allow 5s to do the exercise
                execution_correct.value = False
                score = i/len(exercise_data)
                print(score)
                feedback.value = score
                return
            #if(settings.qu.qsize() == 0):
                #time.sleep(0.1)
            element = settings.qu.get()
            writer.writerow(list(element))
            if(angle_between(tuple(exercise_data[i]), element, exercise_number)):
                if i == 0:
                    exercise_start_time = time.time()
                i += 1
    execution_correct.value = True
    if(time.time() - exercise_start_time < 0.8): #If exercise takes less than 0.8sec than exercise has been executed too fast
        feedback.value = 1.0
    elif(time.time() - exercise_start_time > 2): #If exercise takes more than 2sec than exercise has been executed too slow
        feedback.value = 0.0
    return

""" Returns the unit vector of the vector. """
def unit_vector(vector):
    return vector / np.linalg.norm(vector)

""" Returns true if angle between the two vectos is under 5% difference or 0.16 radians """
def angle_between(v1, v2, exercise_number):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    angle = np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))*100/pi
    # Sprint(angle)
    if(exercise_number == 1 and angle < 8 ): #Allow 8% difference in angle
        print(str(angle) + " Match")
        return True
    elif(exercise_number == 2 and angle < 6 ): #Allow 6% difference in angle
        print(str(angle) + " Match")
        return True
    elif(exercise_number == 3 and angle < 5 ): #Allow 4% difference in angle
        print(str(angle) + " Match")
        return True
    elif(exercise_number == 4 and angle < 10 ): #Allow 10% difference in angle
        print(str(angle) + " Match")
        return True

    else:
        # print(angle)
        return False

t = Thread(target=run)
t.start()