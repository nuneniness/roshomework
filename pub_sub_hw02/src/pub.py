#!/usr/bin/python2
import rospy

from hw00_pkg.msg import hw01


def publisher() :
    inpu = hw01()
    inpu.sign = 'plus'
    inpu.n1 = 1
    inpu.n2 = 3
    pub = rospy.Publisher('/topic_publisher', hw01, queue_size=10)
    while not rospy.is_shutdown():
        rospy.loginfo(inpu)
        pub.publish(inpu)
    
if __name__=='__main__':
    rospy.init_node('node_publisher', anonymous=True)
    publisher()
