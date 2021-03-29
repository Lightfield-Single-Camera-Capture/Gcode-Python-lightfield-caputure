#!/usr/bin/python

import serial
import io
import time


import cv2
    

savefile = 'c:/Users/User/Desktop/gcam/image'

# setup video capture
cap0 = cv2.VideoCapture(0)
 




ser = serial.Serial('COM8',115200)

print(ser.readline() )
print(ser.readline() )
print(ser.in_waiting)
print(ser.readline() )
print(ser.readline() )
print(ser.readline() )
print(ser.readline() )
time.sleep(1)
print(ser.in_waiting)


#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

ser.write(b'G28\n')

#ser.flush()

#time.sleep(5)

print(ser.readline() )


ser.write(b'G0 X80\n')

#ser.flush()

print(ser.readline() )

ser.write(b'M400\n')
print(ser.readline())




for i in range(1, 10):

    time.sleep(0.5)

    pos = 180 - i *  11
    ret,im0 = cap0.read()
   
 
    cv2.imwrite( savefile + str(i) + '.jpg',im0)
    
    cv2.imshow('video test0',im0)
       

    ser.write( bytes('G0 X' + str(pos) +'\n' , 'utf-8' ) )
    print(ser.readline() )

    ser.write(b'M400\n')
    print(ser.readline())


    if i == 1:
        imtotal = im0
    else:
        imtotal = cv2.vconcat([imtotal, im0])

cv2.imwrite( savefile + '-final.jpg',imtotal)

ser.close()
