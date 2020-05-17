cmake_minimum_required(VERSION 3.0.2)
project(simple_husky_control)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

################################################
## Declare ROS messages, services and actions ##
################################################



###################################
## catkin specific configuration ##
###################################

catkin_package(
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)
