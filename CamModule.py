import cv2

cap = cv2.VideoCapture(0)

def getImg(display = False, size= [480,240]):
	_,img = cap.read()
	img = cv2.resize(img, (size[0],size[1]))
	return img

while cap.isOpened():
	img = getImg(True)
	if cv2.waitKey(10) == ord('q'):
		break
	cv2.imshow("Window",img)
