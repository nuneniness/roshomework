#!/usr/bin/python2
import rospy
from hw00_pkg.msg import hw01

def callback(recieveData):
    n1 = recieveData.n1
    n2 = recieveData.n2
    if  recieveData.sign == 'plus' : 
        a = '+'
        ans = n1 + n2
    elif recieveData.sign == 'minus' :
        a = '-'
        ans = n1 - n2
    msg = '%d %s %d = %d'%(n1, a, n2, ans)
    rospy.loginfo(msg)



if __name__=='__main__':
    rospy.init_node('node_subscriber', anonymous=True)
    rospy.Subscriber('/topic_publisher', hw01, callback)
    rospy.spin()
