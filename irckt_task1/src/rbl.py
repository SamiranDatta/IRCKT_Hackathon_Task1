#!/usr/bin/env python

import rospy
from std_msgs.msg import String

post_number = 0

def watch(data):
	watched = "I have seen Indian Robotics Community's post: " + str(data.data)
	print(watched)

def instagram_post():
	pub = rospy.Publisher('RBL_ig', String, queue_size=1)
	rospy.init_node('RigBetelLabs')
	rospy.Subscriber('IRC_ig', String, watch)
	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		global post_number
		video_title = "Rigbetel Labs published post number: " + str(post_number)
		pub.publish(str(post_number))
		print(video_title)
		post_number = post_number+1		
		rate.sleep()

if __name__ == '__main__' :
	try:
		instagram_post()
	except rospy.ROSInterruptException:
		pass