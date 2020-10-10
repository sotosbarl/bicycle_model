# bicycle_model
You need the following packages: 
 robot_control
 bicycle_model_description
 bicycle_robot_gazebo 
 You also need to run in a terminal: sudo apt-get install ros-melodic-teleop-twist-keyboard
 in order to download the teleop_twist_keyboard
1) catkinize your workspace
2) open a terminal and run roslaunch bicycle_robot_gazebo bicycle_model_gazebo.launch (opens a world with the model)
3) in another terminal run roslaunch robot_control bicycle_control.launch    (spawns the controller manager and ackermann_controller)
4) in another terminal run rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/bicycle_model/mobile_base_controller/cmd_vel (teleop)
