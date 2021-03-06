import cv2
import numpy as np
import utlis
#import time

#curve value is stored in an area and its declared global since it will be required in couple of functions.
curveList = []
avgVal=10

#defining img and the display value
def getLaneCurve(img,display=1):
    

    imgCopy = img.copy()
    imgResult = img.copy()
    #### STEP 1
    imgThres = utlis.thresholding(img)

    ### STEP 2
    #to get the wheel points.
    hT, wT, c = img.shape
    points = utlis.valTrackbars()
    imgWarp = utlis.warpImg(imgThres,points,wT,hT)
    imgWarpPoints = utlis.drawPoints(imgCopy,points)

    ### STEP 3
    #For histogram and the middle point for the path.
    middlePoint,imgHist = utlis.getHistogram(imgWarp,display=True,minPer=0.5,region=4)
    curveAveragePoint,imgHist = utlis.getHistogram(imgWarp,display=True,minPer=0.9)
    curveRaw = curveAveragePoint - middlePoint

    ### STEP 4
    #to get the exact value of the curve.
    curveList.append(curveRaw)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))


    ### STEP 5
    #For warping points , and the range on which the algorthm need to calculate for the next curve.
    if display != 0:
        imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT, inv=True)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
        imgInvWarp[0:hT //3, 0:wT] = 0,0,0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1 ,0)
        midY = 450

        ##a erro fixed with (200,40,160), 1 
        cv2.putText(imgResult, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2,(200,40,160), 1)
        cv2.line(imgResult, (wT // 2, midY), (wT // 2 + (curve * 3), midY),(255,0,255), 5)
        ## error fixed with (255,100,255), 5
        cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY - 25), (wT // 2 + (curve * 3), midY),(255,100,255), 5)
        for x in range(-30, 30):
            w = wT // 20
            cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),(w * x + int(curve // 50), midY + 10), (0, 0,255), 2)
        #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        ## error fixed with (255,255,255)
        #cv2.putText(imgResult, 'FPS ' + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
    if display ==2:
        imgStacked = utlis.stackImages(0.7, ([img, imgWarpPoints, imgWarp], [imgHist, imgLaneColor, imgResult]))
        cv2.imshow('ImageStack', imgStacked)
    elif display == 1:
        cv2.imshow('Result',imgResult)
    
    ### normalization
    #giving conditions for when its rigght curve or left curve.
    curve = curve/100
    if curve> 1: curve == 1
    if curve<-1: curve == -1
    #######dispay for all the outputs
    #cv2.imshow('Thres',imgThres)
    #cv2.imshow('Warp',imgWarp)
    #cv2.imshow('Warp Points',imgWarpPoints)
    #cv2.imshow('Histogram',imgHist)
    return curve

if __name__ == '__main__':
    #traning model , picking the exact values for thresholding on the trackbar.
    cap = cv2.VideoCapture('vid1.mp4')
    intialTrackBarVals = [101,99, 34,230 ]
    utlis.initializeTrackbars(intialTrackBarVals)
    frameCounter = 0
    curveList = []
    
    while True:
        frameCounter +=1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter=0

        success, image = cap.read()
        pic= cv2.resize(image,(480,240))
        curve = getLaneCurve(pic, display=2)
        print(curve)
        ## for the display 0 is for when we are running in real time 
        ## 1 if for when we only want to the the last output
        ## 2 is for when we want to see everything

        #cv2.imshow('Vid',pic)
        cv2.waitKey(1)
