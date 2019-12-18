#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv
from std_msgs.msg import String 

class Person:
  def __init__(self):
    self.head = None
    self.neck = None
    self.torso = None 
    self.l_shoulder = None
    self.l_elbow = None
    self.l_hand = None
    self.r_shoulder = None
    self.r_elbow = None
    self.r_hand = None

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')

    listener = tf.TransformListener()
    turtle_vel = rospy.Publisher('/listener', String ,queue_size=1)
    person = Person()

    rate = rospy.Rate(1)
    i = 0
    while not rospy.is_shutdown():
        # i = i+1
        # turtle_vel.publish(str(i)*100)
        # rate.sleep()
        try:
            parts_list = []
            parts = ["head", "neck", "left_hand", "left_elbow", "left_shoulder", "torso", "right_shoulder", "right_elbow", "right_hand"]
            for p in parts:
                frame = "/%s_1" %p
                # print(frame)
                (trans,rot) = listener.lookupTransform('/openni_depth_frame', frame, rospy.Time(0))
                parts_list.append(trans) 


        
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        # print("\n", parts_list)
        # parts_list = list(map(lambda x: str(x), parts_list))
        # msg = ''.join(parts_list)
        turtle_vel.publish(str(parts_list))

        
        rate.sleep()






