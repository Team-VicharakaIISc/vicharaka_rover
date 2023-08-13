#!/usr/bin/python3
import rospy
from vicharaka_rover.msg import controller

class commands:
    command_key=""

def callback(data):
    info.command_key=data.message
    rospy.loginfo("Received: %s",data.message)

def control_sub():
    rospy.init_node('receiver_module',anonymous=True)
    rospy.Subscriber('/comms_driver',controller,callback)
    rospy.spin()




if __name__=="__main__":
    info=commands()
    try:
        control_sub()
    except rospy.ROSInterruptException:
        pass
