"""
import and use function Gcontrol(gaze,webcam). If you want to use for continuous
gaze tracking place Gcontrol in a loop

Requires import of...

 GazeTracking from gaze_tracking
 open cv or cv2

 Run these commands to get gaze and webcam imputs using the GazeTracking library and opencv
    #gaze = GazeTracking()
    #webcam = cv2.VideoCapture(0)
"""
import cv2
import numpy as np
from gaze_tracking import GazeTracking


def initGcontrol():
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)

def Gcontrol(gaze,webcam):

    #gaze = GazeTracking()
    #webcam = cv2.VideoCapture(0)


    XXold = 0 #to prevent argument issues when comparing old gaze points with new ones
    YYold = 0

    while True:
        # We get a new frame from the webcam
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""

        imgDim = frame.shape #need image dimensions, .shape is from cv2
        Xpixels = imgDim[1] #width in pixels
        Ypixels = imgDim[0] #height in pixels

        #XX = Xpixels/2 #Enter in the mid value for your webcame picture dimensions so gcontrol starts you with no velocity command
        #YY = Ypixels/2

        if gaze.is_blinking(): #part of the original framework, should merge
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

        frame = cv2.flip(frame, 1) #flip the image so it shows where picture is looking accurately
        R = 20 #radius units pixels for circle to show gaze point and set size per frame
        sX = 1.1 #scale factor x for gazepoint calculation
        sY = 0.6 #scale factor y for gazepoint calculation

#no reason to use all the if gaze is right/left/center besides me being lazy. Can all be incorporated into 1 if statement

        if gaze.is_right():
            XX = Xpixels - (gaze.horizontal_ratio() * Xpixels) #horizontal_ratio is 0 for far right and 1 for far left. Opposite of img axes
            XX = int(sX*XX)  #apply scale factor and round for future functions
            YY = gaze.vertical_ratio() * Ypixels #vertical_ratio is 0 for far up, 1 for far down. In line with image axes
            YY = int(sY*YY) #apply scale factor and round for future functions


        if gaze.is_left():
            XX = Xpixels - (gaze.horizontal_ratio() * Xpixels) #horizontal_ratio is 0 for far right and 1 for far left. Opposite of img axes
            XX = int(sX*XX)  #apply scale factor and round for future functions
            YY = gaze.vertical_ratio() * Ypixels #vertical_ratio is 0 for far up, 1 for far down. In line with image axes
            YY = int(sY*YY) #apply scale factor and round for future functions


        if gaze.is_center():
            XX = Xpixels - (gaze.horizontal_ratio() * Xpixels) #horizontal_ratio is 0 for far right and 1 for far left. Opposite of img axes
            XX = int(sX*XX)  #apply scale factor and round for future functions
            YY = gaze.vertical_ratio() * Ypixels #vertical_ratio is 0 for far up, 1 for far down. In line with image axes
            YY = int(sY*YY) #apply scale factor and round for future functions


        #smooth the gaze tracking by limiting step size to radius of circle R
        if not gaze.is_blinking():
            if (XX-XXold) >  R: #check to see if gaze point fasls outside of circle
                XX = XX + R
            elif (XXold-XX) >  R:
                 XX = XX - R

            if (YY-YYold) >  R: #check to see if gaze point fasls outside of circle
                YY = YY + R
            elif (YYold-YY) >  R:
                YY = YY - R
            #insert the circle in the frame
            cv2.circle(frame, center=(XX,YY), radius=R, color=(255,255,0), thickness= -1)


        #Control aspect

        pitch = 0 #no turning unless if statements below are satisfied
        yaw = 0

        if YY > (0.7 * Ypixels):
            pitch = 1 #pitch looks down, vert ratio = 1 when looking down
        elif YY < (0.3 * Ypixels):
            pitch = -1 #pitch looks up

        if XX > (0.6 * Ypixels):
            yaw = 1 #yaw looks right, horiz ratio = 1 when looking down
        elif XX < (0.3 * Ypixels):
            yaw = -1 #yaw looks left

        #cv2.circle(frame, center=(XX,YY), radius=R, color=(255,255,0), thickness= -1)

    #    if gaze.is_blinking():
    #        pitch = 0
    #        yaw = 0

        """
        Everything between here and next quote comment out is antoine lames code

        Uncomment line 138  cv.imshow("Demo",frame) if you want to demo outside
        ROS and see the image

        """


        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    #    cv2.imshow("Demo", frame)

        """
        Karim's code after this point. Returns Grot and breaks the while loop

        """

        #yaw = 1
        Grot = [yaw,pitch] #gaze rotation [X Y]

        #return print(Grot) $for testing
        return Grot

        if cv2.waitKey(1) == 27:
            break
