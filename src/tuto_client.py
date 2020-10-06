#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python
import sys
# ROS
import rospy
from ros_tutorial.srv import Tutorial, TutorialResponse

def tutorialClient():
    rospy.wait_for_service('/tuto_service')
    try:
        tuto_service = rospy.ServiceProxy('/tuto_service', Tutorial)
        rospy.loginfo("Send request")
        res = tuto_service(data = 'helloworld')
        rospy.loginfo("Received response")
        print res.answer
    except rospy.ServiceException, e:
        rospy.loginfo("Service call failed: %s" %e)

if __name__ == '__main__':
    rospy.init_node('tuto_client', anonymous = True)
    tutorialClient()    
