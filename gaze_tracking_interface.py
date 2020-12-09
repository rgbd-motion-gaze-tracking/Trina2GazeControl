#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Joy
import time
import math
import numpy as np
import socket
import struct
import threading
import roslib; roslib.load_manifest('teleop_twist_keyboard')
#from tf.transformations import euler_from_quaternion
#import tf
import gaze2screen #gaze control function
import cv2 #opencv for webcam control
from gaze_tracking import GazeTracking

import sys, select, termios, tty


"""
gaze_tracking_interface.py

"""

msg = """

___
                  `. \
                    \_)
    ____ _,..OOO......\...OOO-...._ ___
  .`    '_.-(  9``````````P  )--...)   `.
 ` ((     `  || __         ||   `     )) `
(          ) |<`  ````---__||  (          )
 `        `  ||) ,xx  xx.  //)__`        `
  `-____-`   ,/  O`  O`   //,'_ )`-____-`
           ,/     ,,     //  |//
          /      ((          //
         (   (._    _,)     (_) -OH YEAH! The Code Works!!!
          \    \````/        /
           \    ^--^        /
            \_   _____   __/
              | |     | |
             (   )   (   )
           ,--'~'\   /'~'--,
          (_______) (_______)dwb
    _ __ ___  ___  _        ___  _  ___
   | / /| . || . || |  ___ | . || || . \
   |  \ | | || | || |_|___||   || || | |
   |_\_\`___'`___'|___|    |_|_||_||___/
            __ __  ___  _ _  _

"""
print(msg)


class GazeTrackingControl():

    def __init__(self):
        # variables
        self.UDP_IP = "192.168.1.134"
        self.UDP_PORT = 4242

        self.joystick_mode = False

        self.kp_pitch = 0.05
        self.kp_yaw = 0.05

        # instantiate the node
        rospy.init_node('gaze_tracking_control')

            # publish to the camera controller

        self.pitch_yaw_pub = rospy.Publisher('/trina2_1/main_cam_controller/pitch_yaw',
            Twist, queue_size=5)



    def publish_gaze_tracking(self): #use gaze control for velocity control like below

        pitch_yaw_cmd = Twist()

        if Grot[0] >= 1:
            pitch_yaw_cmd.angular.z = -1.5
        elif Grot[0] <= -1:
            pitch_yaw_cmd.angular.z = 1.5
        else:
            pitch_yaw_cmd.angular.z = 0

        # publish
        self.pitch_yaw_pub.publish(pitch_yaw_cmd)


if __name__ == "__main__":


    try:
        #Gaze camera control
        camera_control = GazeTrackingControl()
        gaze = GazeTracking()
        webcam = cv2.VideoCapture(0)


        while not rospy.is_shutdown():


            Grot = gaze2screen.Gcontrol(gaze,webcam)
            camera_control.publish_gaze_tracking()


    except rospy.ROSInterruptException:
        pass
