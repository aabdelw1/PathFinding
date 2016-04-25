#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg  import Point

import trapzone

# Publish location of traps to ROS
def talker(traps):
    pub = rospy.Publisher('traps', String, queue_size=10)
    rospy.init_node('trap_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    messages = []
    for trap in traps:
        for x,y,z in trap:
            message = Point(x, y, z)
        messages.append(message)

    while not rospy.is_shutdown():
        for msg in messages:
            rospy.loginfo(msg)
            pub.publish(msg)
            rate.sleep()

if __name__ == '__main__':
    traps = trapzone.genPoints()
    try:
        talker(traps)
    except rospy.ROSInterruptException:
        pass
