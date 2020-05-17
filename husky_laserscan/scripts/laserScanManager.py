#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from math import pi, cos, sin
from husky_laserscan.msg import Entity

topic = rospy.get_param('/topic_name', '/scan')
queue_size = rospy.get_param('queue_size', 1)

inf = float('inf')


class LaserScanManager():
    """
    This class is responsible for  managing the laserScan input
    """

    def __init__(self):

        rospy.init_node('LaserScanManager', anonymous=True)
        rospy.loginfo("LaserScanManager is initialized")

        self.sub = rospy.Subscriber(
            topic, LaserScan, self.callback, None, queue_size)
        self.pub = rospy.Publisher('/laser', Entity, queue_size=10)

    def getObjectPosition(self, ranges):
        angle_min = -2.3561899662
        angle_inc = 0.0065540750511
        min_value = inf
        min_index = 0
        for idx, elt in enumerate(ranges):
            if elt < min_value:
                min_value = elt
                min_index = idx
        angle = angle_min + angle_inc*min_index
        angle_deg = angle*180/pi

        pillar = Entity(**{
            'name': "Pillar",
            'distance': min_value,
            'angle': angle
        })
        return pillar

    def callback(self, laser):
        ob_postion = self.getObjectPosition(laser.ranges)
        self.pub.publish(ob_postion)

    def spin(self):
        rospy.spin()


if __name__ == '__main__':
    rospy.loginfo("starting LaserScanManager")
    node = LaserScanManager()
    node.spin()
