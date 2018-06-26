#!/usr/bin/python3

import cv2
import random
face_data=cv2.CascadeClassifier('har.xml')

cap=cv2.VideoCapture(0)

while cap.isOpened() :
	status,frame=cap.read()
	grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=face_data.detectMultiScale(grayimg,1.15,5)
	for(x,y,w,h) in faces :
		cv2.rectangle(frame,(x,y),(x+w,y+h), (0,225,0),2)
		roi_gray=grayimg[y:y+h,x:x+w]
		roi_coloor=frame[y:y+h,x:x+w]
#showing current image

	cv2.imshow("current",frame)

	if cv2.waitKey(30) & 0xff==ord('w') :
		break

#destroying window
cv2.DestroyAllWindows()
cap.release()


