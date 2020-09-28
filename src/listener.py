#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Subscribed %s", data.data)

def listener():
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('listener', anonymous = True)
    listener()
