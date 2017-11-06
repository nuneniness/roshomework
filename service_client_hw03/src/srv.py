#!/usr/bin/python2
import rospy
from service_client_hw03.srv import service
from std_msgs.msg import String
def callback(req):
    n1 = req.req.n1
    n2 = req.req.n2
    sign = req.req.sign
    if sign == "plus":
        res = String('%d + %d = %d'%(n1, n2, n1+n2))
    elif sign == 'minus':
        res = String('%d - %d = %d'%(n1, n2, n1-n2))
    return res



if __name__ == '__main__':
    rospy.init_node('node_service', anonymous=True)
    service = rospy.Service('name_service', service, callback)
    rospy.spin()
