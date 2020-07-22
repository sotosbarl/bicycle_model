#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from control.msg import float64
from geometry_msgs.msg import Twist

def data_provider():
    rospy.init_node('bicycle_movement', anonymous=True)
    rospy.Subscriber("/transform", control , callback)
    rospy.spin()

def callback(control):
    actuator = rospy.Publisher('/cmd_vel', Twist, queue_size=100)
    actuator_msg = Twist()
    rate = rospy.Rate(10) # 10hz
    lr = 1.25
    lf= 1.75
    beta = math.atan((lr/(lf+lr))*math.tan(control.steer)
    actuator_msg.angular.z= (control.gas/lr)*math.sin(beta)
    actuator_msg.linear.x= control.gas*math.cos(beta+actuator_msg.angular.z)
    actuator_msg.linear.y= control.gas*math.sin(beta+actuator_msg.angular.z)
    actuator.publish(actuator_msg)
    rate.sleep()

if __name__ == '__main__':
    try:
        data_provider()
    except rospy.ROSInterruptException:
        pass
