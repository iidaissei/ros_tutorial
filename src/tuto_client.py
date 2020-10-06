#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from ros_tutorial.srv import Tutorial, TutorialResponse

def tutorialClient():
    rospy.wait_for_service('/tuto_service')
    tuto_service = rospy.ServiceProxy('/tuto_service', Tutorial)
    rospy.loginfo("Send request")
    res = tuto_service(data = 'helloworld')
    rospy.loginfo("Received response")
    print res.answer

if __name__ == '__main__':
    rospy.init_node('tuto_client', anonymous = True)
    tutorialClient()    
