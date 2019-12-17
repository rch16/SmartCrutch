
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pandas as pd
import json
import numpy as np
from math import pi
from sklearn.preprocessing import normalize
import csv

excercise = pd.read_csv("./excercise1.csv")
# excercise2 = pd.read_csv("./excercise2.csv")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def csv_reader():
    data = []
    # with open('state.csv') as csv_file:
    with open('state2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if len(row) == 1:
                data.append(row)
            else:
                row = np.array(row).reshape(-1,3)
                d = np.array((0,1))
                row = row[:, d]
                data.append(row)
    return data

c = csv_reader() 
state = 0



def getJSON(data, part):
    d = data[part]
    d= d.replace("'", "\"")
    # print(d, type(d))
    d= json.loads(d)
    return d

def plot_body(data):
    parts = ["head", "neck", "left_hand", "left_elbow", "left_shoulder", "torso", "right_shoulder", "right_elbow", "right_hand", "left_hip", "left_knee", "left_foot", "right_hip", "right_knee", "right_foot"]
    body = []
    for p in parts:
        h = getJSON(data, p)
        tmp = (h["x"], h["y"])
        body.append(tmp)
    body = np.array(body)
    return body 

def angle_between(v1, v2):
    # print("v1", v1)
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    n = len(v1_u)
    a = []
    # print("v1_u",v1_u)
    for i in range(n):
        a.append(np.arccos(np.dot(v1_u[i,:], v2_u[i,:]))*180/pi)
    # print(np.array(a).reshape(-1,1))
    return a
    # return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))*100/pi


def get_vector(p1,p2):
    vec = p1 -p2
    return vec 

def get_points(data):
    parts = ["head", "neck", "left_hand", "left_elbow", "left_shoulder", "torso", "right_shoulder", "right_elbow", "right_hand", "left_hip", "left_knee", "left_foot", "right_hip", "right_knee", "right_foot"]
    parts2 = np.array(["head", "neck", "left_shoulder", "left_elbow", "neck", "right_shoulder", "right_elbow", "torso", "left_hip", "left_knee", "torso", "right_hip", "right_knee", "neck"])
    parts3 = np.array(["neck", "left_shoulder", "left_elbow", "left_hand", "right_shoulder", "right_elbow", "right_hand", "left_hip", "left_knee", "left_foot", "right_hip", "right_knee", "right_foot", "torso"])
    #Dictionary of values 
    part_list = dict(zip(parts, data))
    tmp = []
    for p in parts2:
        tmp.append(part_list[p])
    p1 = np.array(tmp)
    tmp = []
    for p in parts3:
        tmp.append(part_list[p])
    p2 = np.array(tmp)
    return p1,p2

""" Returns the unit vector of the vector. """
def unit_vector(vector):
    return normalize(vector, norm='l2')
    # vector / normalize(vector, axis =0)

# def get_angle():

# state =2
updated = False
frame = 0
old_state = 0


def animate(i):
    global updated
    global state
    global frame
    global old_state
    old_state = state

    frame = frame + 1
    # i = i+40

    if updated:
        time.sleep(3)
        updated = False

    print("i", i , ";")
    parts = ["head", "neck", "left_hand", "left_elbow", "left_shoulder", "torso", "right_shoulder", "right_elbow", "right_hand", "left_hip", "left_knee", "left_foot", "right_hip", "right_knee", "right_foot"]
    parts2 = np.array(["head", "neck", "left_shoulder", "left_elbow", "neck", "right_shoulder", "right_elbow", "torso", "left_hip", "left_knee", "torso", "right_hip", "right_knee", "neck"])

    axis = ax1
    ax1.cla()

    ex1 = excercise.iloc[state]
    body1 = plot_body(ex1)
    # print("body1", type(body1[0][0]))
    #Array of coordinates for body parts
    p1,p2 = get_points(body1)

##################################################
    # ex2 = excercise2.iloc[i]
    # body2 = plot_body(ex2)

    # Using data from CSV
    idx = i + state
    print("idx", idx)
    # print(idx, c[idx])
    next = idx+1
    if len(c[next]) == 1:
        print("yo")
    body2 = c[idx]
    body2 = body2.astype('float64')
    #Array of coordinates for body parts
    p3,p4 = get_points(body2)
    

    v1 = get_vector(p1,p2)
    v2 = get_vector(p3,p4)


    ab = angle_between(v1,v2)
    print(ab)
    cond = all(item < abs(30) for item in ab)
    if cond:
        print("updated")
        state = state+1
        updated = True


    for i in range(len(parts2)):
        print(ab[i])
        if ab[i] < abs(30):
            col = 'go-'
        else:
            col = 'ro-'

        axis.plot((p1[i][0], p2[i][0]) , (p1[i][1], p2[i][1]), 'bo-')
        axis.plot((p3[i][0], p4[i][0]) , (p3[i][1], p4[i][1]), col)
    axis.set_title('Frame:' + str(frame) +  ", Checking for position: " +  str(old_state))
    # if updated == True:
    #     name = "position" + str(state) + ".png"
    #     plt.savefig(name)

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()



