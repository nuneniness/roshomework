#!/usr/bin/python2
import rospy

if __name__=='__main__':
    rospy.init_node('hw00')
    sign = raw_input()
    n1 = input()
    n2 = input()
    res = 0
    if sign == "1" :
        res = n1 + n2
    elif sign == "2" :
        res = n1 - n2
    print(res)
        
