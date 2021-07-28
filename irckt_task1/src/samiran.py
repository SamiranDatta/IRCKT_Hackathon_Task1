#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def watch1(data):
	watched1 = "I have seen Indian Robotics Community's post: " + str(data.data)
	print(watched1)

def watch2(data):
	watched2 = "I have seen Rigbetel Labs' post: " + str(data.data)
	print(watched2)

def subscriber():
	rospy.init_node('Samiran')
	sub1 = rospy.Subscriber('IRC_ig', String, watch1)
	sub2 = rospy.Subscriber('RBL_ig', String, watch2)
	rospy.spin()

if __name__ == '__main__' :
	try:
		subscriber()
	except rospy.ROSInterruptException:
		pass