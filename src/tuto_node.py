#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------
# Title: ROS Nodeを理解するためのサンプルコード
# Author: Issei Iida
# Date: 2020/09/21
# Memo: １秒おきに世界に挨拶するプログラム 
#       Ctrl + C押されたら別れを告げる
#------------------------------------------------

import rospy

def main():
    count = 1
    # "rospy.is_shutdown"はプログラムが中断されたことを返す
    while not rospy.is_shutdown():
        # "rospy.loginfo"はROS仕様のプリント文と思えば良い
        rospy.loginfo('Hello World')
        print('Hello World' + str(count))
        count += 1
        rospy.sleep(1.0)
    rospy.loginfo('Good bye...')

if __name__ == '__main__':
    # この記述がないとマスターにノードとして登録されない
    rospy.init_node('tuto_node', anonymous = True)
    main()
