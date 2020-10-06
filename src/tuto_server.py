#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from ros_tutorial.srv import Tutorial, TutorialResponse


def handleTutorial(req):
    rospy.loginfo("Request received")
    print req.data
    return TutorialResponse(answer = 'success')

def tutorialServer():
    s = rospy.Service('/tuto_service', Tutorial, handleTutorial)
    rospy.spin()


if __name__ == '__main__':
    rospy.init_node('tuto_server', anonymous = True)
    rospy.loginfo("Ready to server")
    tutorialServer()
