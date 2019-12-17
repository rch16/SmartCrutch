from __future__ import print_function
import roslibpy
import numpy as np
# import matplotlib as plt
import playground as pg
import pandas as pd
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from multiprocessing import Manager
import roslibpy
import settings



def callback(message):
	msg = message['data']
	msg = getNumArr(msg)

	flatTuple = tuple([ item for elem in msg for item in elem])
	settings.qu.put(flatTuple)

			

def getNumArr(msg):
	data = []
	msg = msg[1:-1]
	m = msg.split("[")
	m.pop(0)
	for tmp in m:
		tmp = tmp[:-3]
		f = list(map(float, tmp.split(",")))
		data.append(f)
	return data


client = roslibpy.Ros(host='localhost', port=9090)
client.run()

listener = roslibpy.Topic(client, '/listener', 'std_msgs/String')
listener.subscribe(callback)


# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     client.terminate()
