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
    data = [[1.5824941841576496, 0.02467203825922914, 0.5682399147168499], [1.6718440039887672, 0.023983586628506078, 0.3589849478433582], [1.5958826838779216, 0.29248178363725114, 0.7227166111410417], [1.70195318059245, 0.38841952066869756, 0.536478428551051], [1.6890551209164255, 0.17335939943748901, 0.3578125518577004], [1.6601252496660541, 0.02349492473240662, 0.1246910074276997], [1.6546328870610947, -0.1253922223657796, 0.36015734382901593], [1.6268903779813146, -0.34480289250849044, 0.4852236688812772], [1.521927923247053, -0.26929616746090235, 0.67939846238917]] 

    while not rospy.is_shutdown():
        # i = i+1
        # turtle_vel.publish(str(i)*100)
        # rate.sleep()
        try:
            turtle_vel.publish(str(data))

        
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue


        
        rate.sleep()






