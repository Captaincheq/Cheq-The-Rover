from picamera.array import PiRGBArray
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import cv2
import numpy as np
import math

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

GPIO.output(32, GPIO.LOW)
GPIO.output(36, GPIO.LOW)
GPIO.output(40, GPIO.LOW)
GPIO.output(38, GPIO.LOW)

theta=0
minLineLength = 5
maxLineGap = 10

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 15

rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
   GPIO.output(32, GPIO.LOW)
   GPIO.output(36, GPIO.LOW)
   GPIO.output(38, GPIO.LOW)
   GPIO.output(40, GPIO.LOW)
   time.sleep(0.0)
   image = frame.array
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   blurred = cv2.GaussianBlur(gray, (5, 5), 0)
   edged = cv2.Canny(blurred, 85, 85)
   lines = cv2.HoughLinesP(edged,1,np.pi/180,10,minLineLength,maxLineGap)
   
   if(lines !=[]):
       for x in range(0, len(lines)):
           for x1,y1,x2,y2 in lines[x]:
               cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
               theta=theta+math.atan2((y2-y1),(x2-x1))
          
   threshold=6
   
   if(theta>threshold):
       GPIO.output(32, GPIO.LOW)
       GPIO.output(36, GPIO.HIGH)
       GPIO.output(40, GPIO.LOW)
       GPIO.output(38, GPIO.HIGH)
       print("left")
       
   if(theta<-threshold):
       GPIO.output(36, GPIO.LOW)
       GPIO.output(32, GPIO.HIGH)
       GPIO.output(38, GPIO.LOW)
       GPIO.output(40, GPIO.HIGH)
       print("right")
       
   if(abs(theta)<threshold):
      GPIO.output(32, GPIO.LOW)
      GPIO.output(36, GPIO.HIGH)
      GPIO.output(38, GPIO.LOW)
      GPIO.output(40, GPIO.HIGH)
      print ("straight")
   
   theta=0
   cv2.imshow("Frame",image)
   key = cv2.waitKey(1) & 0xFF
   rawCapture.truncate(0)
   
   if key == ord("q"):
       break