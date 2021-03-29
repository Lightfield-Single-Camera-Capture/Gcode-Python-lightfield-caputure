#!/usr/bin/python

import cv2

# setup video capture
cap0 = cv2.VideoCapture(0)
 

while True:
    ret,im0 = cap0.read()
   
    cv2.imshow('video test0',im0)
 
    key = cv2.waitKey(10)
    if key == 27:
        break
    if key == ord(' '):
        cv2.imwrite('vid_result0.jpg',im0)
     


