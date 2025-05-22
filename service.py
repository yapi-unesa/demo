#! /usr/bin/env python
import rospy
from Multiplier.srv import Multiplier , multiplierResponse


def callback(request):
    return multiplierResponse(request.a * request.b)


def multipy():
    rospy.init_node("Multiplier")
    service = rospy.Service("multipier", Multiplier,callback)
    rospy.spin()

if __name__ =='__main__':
    multipy()



