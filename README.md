# IRCKT_Hackathon_Task1

We are required to make a ROS Computational Graph representing Real-Life scenarios.

For carrying out this task, I turned to Instagram and have made a simple Follower-Following model as depicted below.

I follow both the Indian Robotics Community and RigBetel Labs on Instagram and I noticed that they follow each other too. This ROS publisher/subscriber model represents the same.

Here, Instagram is analogous to the ROS Master on which the publishers (RigbetelLabs, Indian_Robotics_Commnunity) and the subcriber (me) are registered. The publishers then publish messages (or posts) in their respective topics which are considered to be the names of their Instagram handles (IRC_ig and RBL_ig). I (Samiran) have subscribed to both of them (or follow both of them) and hence can see their posts as can be visualized from the terminal. IRC and RBL have also subscribed to each other and hence can also view each other's posts as again, is clearly depicted in the terminal.

This is my submission for Task 1.
