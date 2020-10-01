#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Subscribed %s", data.data)

def listener():
    # ('トピック名', メッセージ型, コールバック関数)
    rospy.Subscriber('chatter', String, callback)
    # 処理を継続するための記述
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('listener', anonymous = True)
    listener()
