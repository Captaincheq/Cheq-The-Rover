from  MotorModule import Motor
from LineDetectionModule import getLaneCurve
import CamModule
import cv2

##################
motor = Motor(33,32,36,35,38,40)
##################

def main():

    img = CamModule.getImg()
    curveVal = getLaneCurve(img,2)

    sen = 1.3 #SENSITIVITY
    maxVA1= 0.3 # MAX SPEED
    if curveVal>maxVA1:curveVal = maxVA1
    if curveVal<-maxVA1:curveVal= -maxVA1
    #print(curveVa1)
    if curveVal>0:
        sen = 1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    motor.move(0.20,-curveVal*sen,0.05)
    cv2.waitKey(1)


if __name__=='__main__':
    while True:
        main()
