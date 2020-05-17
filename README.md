# husky-ros
Python Ros packages to control the **Husky** robot

## Dependencies: 

Add these packages to your ROS workspace

**Official husky packages**: https://github.com/husky/husky

**telep_twist_keyboard package (for manual control)**: https://github.com/ros-teleop/teleop_twist_keyboard


**Setup with catkin**.
```
cd <your catkin_ws>/src
git clone https://github.com/husky/husky
git clone https://github.com/ros-teleop/teleop_twist_keyboard
cd ..
catkin_make 
source devel/setup.bash
```

## Packages:
### **simple_husky_control**: 

**Launch files**:
- gazebo.launch : 
>launch a *gazebo* simulation of an empty world and a husky robot + *rviz*.
You can control the robot with your keyboard.

## Usage:
```
 roslaunch simple_husky_control gazebo.launch
```
