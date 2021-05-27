#importing Motor function in the MotorModule which is responsible for wheel movement.
from  MotorModule import Motor
#Importing getLaneCurve function , in the LineDetectionModule which is responsible for detecting the lane path.
from LineDetectionModule import getLaneCurve
#Importing the Camera function in the CamModule which is responsible for taking the environment images.
import CamModule
#OpenCV is an application which is capable to do many tasks in this project it will be the main base for Lane image detection.
import cv2

##################
#calling the GPIO pin layout from the raspberry pi to so that they can be useful in other modules
motor = Motor(33,32,36,35,38,40)
##################

def main():

    #calling the Image function in the CamModule
    img = CamModule.getImg()
    curveVal = getLaneCurve(img,2)

    sen = 1.3 #SENSITIVITY
    maxVA1= 0.3 # MAX SPEED
    if curveVal>maxVA1:curveVal = maxVA1
    if curveVal<-maxVA1:curveVal= -maxVA1
    #print(curveVa1)
    if curveVal>0:
        #sensation set to 1.7
        sen = 1.7
        #right curve calculation starts only above 0.05 else the path is defined straight.
        if curveVal<0.05: curveVal=0
    else:
        #left curve calculation starts only above -0.08 else the path is defined straight.
        if curveVal>-0.08: curveVal=0
    #the speed of the car is determined by the curve
    motor.move(0.20,-curveVal*sen,0.05)
    cv2.waitKey(1)


if __name__=='__main__':
    while True:
        main()

