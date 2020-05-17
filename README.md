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

According the official documentation:
```
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
```

**Scripts**:
- hello_world.py:
> Prints hello world in the console 
### usage
```
 rosrun simple_husky_control hello_world.py 
```