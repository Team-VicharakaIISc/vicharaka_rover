#!/usr/bin/python3
import rospy
import roslib
from std_msgs.msg import Int16
from std_msgs.msg import String


def ack_checker(data):
    print(data)


class arduino_commands:
    
    pub_arduino=rospy.Publisher('/arduino_receiver',Int16,queue_size=1)
    

    def send_command(self,command):     
        self.pub_arduino.publish(command)
        rospy.loginfo("Sent: %s",command)
        rospy.sleep(0.001)
        

if __name__=="__main__":
    rospy.init_node('serial_comms',anonymous=True)
    info=arduino_commands()
    rospy.Subscriber('/ack_arduino',String,ack_checker)
    try:
        while True:
            command=input("Enter command: ")
            info.send_command(Int16(int(command)))

    except rospy.ROSInterruptException:
        pass


