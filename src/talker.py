#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def talker():
    # ('トピック名', メッセージの型, キューサイズ)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # １秒間の送信回数を決める（任意）
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        str = "hello world %s" % rospy.get_time()
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()

if __name__ == '__main__':
    rospy.init_node('talker', anonymous = True)
    talker()
