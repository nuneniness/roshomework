#!/usr/bin/python2

import rospy
from service_client_hw03.srv import service
from std_msgs.msg import String
from hw00_pkg.msg import hw01

def client_request():
    rospy.wait_for_service('name_service')
    client = rospy.ServiceProxy('name_service', service)
    req = hw01()
    req.sign = raw_input('Press plus or minus or exit: ').lower()
    if req.sign == 'exit' :
        print('Exit')
        exit()
    req.n1 = int(input('Number1: '))
    req.n2 = int(input('Number2: '))
    res = client(req)
    print(res.res.data)
    client_request()
    
if __name__=='__main__':
    rospy.init_node('node_client',anonymous=True)
    client_request()
