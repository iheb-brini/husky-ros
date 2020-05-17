#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist, Pose
from husky_laserscan.msg import Entity
from time import time


class CommandRobot():
    ob_position = Entity()

    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber(
            '/laser', Entity, callback=self.callback, queue_size=10)
        rospy.init_node('CommandRobot', anonymous=True)

        self.speed = Twist()
        self.speed.linear.x = 0
        self.speed.linear.y = 0

    def callback(self, data):
        self.ob_position = data

    def stopTheRobot(self):
        self.speed = Twist()
        self.pub.publish(self.speed)

    def spin(self):
        try:
            rospy.loginfo('Waiting for sensor node')
            res = rospy.wait_for_message(
                '/laser', Entity, rospy.Duration.from_sec(3.0))
            if not res:
                raise Exception("sensor unavailable")
        except:
            rospy.logwarn("sensor unavailable")
            exit()

        rate = rospy.Rate(4)
        speed = Twist()

        if self.ob_position.distance > 30:
            if not self.startFullScan():
                rospy.logwarn('No objects in the area...')

        self.speed.linear.x = 3
        self.speed.linear.y = 0

        while not rospy.is_shutdown():
            if self.ob_position.distance < 2:
                finished = True
                for i in range(4):
                    if self.ob_position.distance > 2:
                        finished = False
                        break
                    rospy.loginfo('current distance %0.3f' %self.ob_position.distance)
                    rospy.loginfo('check #%d...' % (i+1))
                    rospy.sleep(1)

                if finished:
                    rospy.loginfo('The Robot has reached the %s' %self.ob_position.name)
                    self.stopTheRobot()
                    break

            self.speed.angular.z = -self.ob_position.angle
            self.speed.linear.x = 5

            self.pub.publish(self.speed)
            rate.sleep()

    def startFullScan(self):
        rospy.loginfo('Scanning the surrounding area...')
        found_objects = False

        speed = Twist()
        speed.angular.z = 0.5

        now = time()
        while (time()-now < 8) and (self.ob_position.distance > 50):
            self.pub.publish(speed)

            if self.ob_position.distance < 30:
                found_objects = True
                rospy.loginfo('found object')
                break

        return found_objects


if __name__ == "__main__":
    rospy.loginfo("starting CommandRobot")
    node = CommandRobot()
    node.spin()
