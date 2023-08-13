#!/usr/bin/python3
import rospy
from vicharaka_rover.msg import controller

def control_pub():
    pub=rospy.Publisher('comms_driver',controller,queue_size=1)
    rospy.init_node('command_module',anonymous=True)
    r=rospy.Rate(10)
    msg=controller()
    msg.message="Hello from command_module"

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()
    
if __name__=='__main__' :
    try:
        control_pub()
    except rospy.ROSInterruptException :
        pass
    