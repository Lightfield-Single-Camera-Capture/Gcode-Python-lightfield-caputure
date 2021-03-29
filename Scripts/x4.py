#!/usr/bin/python

import serial
import io
import time


import cv2
	

savefile = 'c:/Users/User/Desktop/gcam/image'

# setup video capture
cap0 = cv2.VideoCapture(0)
 
cap0.set(cv2.CAP_PROP_FRAME_WIDTH,640/4);
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT,480/4);



ser = serial.Serial('COM9',115200)


time.sleep(1)
#print(ser.in_waiting)

while  ser.in_waiting != 0:
	print(ser.readline() )
	time.sleep(0.1)

print('starting here\n')
print(ser.in_waiting)


#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

ser.write(b'G28\n')

#ser.flush()

time.sleep(20)

while  ser.in_waiting != 0:
	print(ser.readline() )
	time.sleep(0.1)


#ser.write(b'G0 X80\n')

#ser.flush()

#print(ser.readline() )

ser.write(b'M400\n')
print(ser.readline())




for h in range(1, 40):
	
	for i in range(1,40):
		
		posX =  i * 4 
		posY =  h * 4

		ser.write( bytes('G0 X' + str(posX) + ' Z' +str(posY) + '\n' , 'utf-8' ) )
		print(ser.readline() )
		
		if i == 1:
			time.sleep(2)
		

		while  ser.in_waiting != 0:
			print(ser.readline() )
			time.sleep(0.1)


		ser.write(b'M400\n')
		print(ser.readline())
		
		time.sleep(0.5)

		ret,im0 = cap0.read()
   
 
#	cv2.imwrite( savefile + str(i) + '.jpg',im0)
	
		cv2.imshow('video test0',im0)
#	cv2.waitKey(1)		   


		
		if i == 1:
			imtotal = im0
		else:
			imtotal = cv2.vconcat([imtotal, im0])
	
	
	cv2.imwrite( savefile+str(h)+'Y.jpg',imtotal)


	if h == 1:
		imtotalY = imtotal
	else:
		imtotalY = cv2.hconcat([imtotalY,imtotal])


cv2.imwrite( savefile + '-final.jpg',imtotalY)

ser.close()
