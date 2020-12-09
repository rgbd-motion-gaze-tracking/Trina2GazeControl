# Trina2GazeControl
Scripts necessary for Trina2GazeControl

Control your camera orientation for the trina2 robot simulation using your eyes!

Instructions for installation and use:

1. download and install ros melodic 

2. git clone and follow installation instructions the trina 2 simulation from the Hiro labs, found here. https://github.com/hiro-wpi/TRINA-WPI-2.0

3. git clone Antoine Lame's gaze tracker, found here https://github.com/antoinelame/GazeTracking

4. copy the gaze_tracking folder from Antoine Lame and move it into /catkin_ws/src/TRINA-WPI-2.0/trina2_control/src

5. git clone this repository into /catkin_ws/src/TRINA-WPI-2.0/trina2_control/src

6. return your cmd directory to catkin_ws to launch and run this. You will need 4 command windows.

7. `roslaunch trina2_gazebo trina2.launch`

8. press play on gazebo when it starts to Rviz will open, wait for arms to home. In the event the arms do not home, go to the Rviz gui, click on the box next to navigation, got to
the navigation panel now located in the center of the gui and select an arm from the drop down menu and set its goal state to home. Plan then execute. Otherwise, trina will T pose 
on you like no one's business.

9. `rosrun trina2_navigation_gui trina2_navigation_gui`  That navigation gui is your camera screen, its optional but much better for controlling the robot with gaze.

10. `rosrun trina2_control gaze_tracking_interface.py`  You should see ascii art confirming the code is running. 

11. `rosrun trina2_control key_tracking_interface.py`   Optional, but reccomended if you want to use the robot to move around and not just look. Instructions for keys will appear on the cmd window. You need to be clicked on the command window to use the keyboard steering. It outputs velocity, so it won't stop moving just because you stop pressing keys.
