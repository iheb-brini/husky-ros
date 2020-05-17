cmake_minimum_required(VERSION 3.0.2)
project(husky_laserscan)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
  genmsg
  sensor_msgs
  geometry_msgs
)

################################################
## Declare ROS messages, services and actions ##
################################################
add_message_files(
    FILES
    Entity.msg
)

## Generate messages in the 'msg' folder
generate_messages(
  DEPENDENCIES
  std_msgs
)
###################################
## catkin specific configuration ##
###################################

catkin_package(
	INCLUDE_DIRS
	CATKIN_DEPENDS
	sensor_msgs
  geometry_msgs
  rospy
  std_msgs
  message_runtime
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)






