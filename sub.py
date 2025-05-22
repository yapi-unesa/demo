#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from tutorials.msg import *

def callback(data):
    rospy.loginfo("%s x: %f y: %f ", data.massage, data.x ,data.y)


    
def listener():
    rospy.init_node("sub", anonymous = True)
    rospy.Subscriber('talking_topic', posisi,callback)
    rospy.spin()





if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass