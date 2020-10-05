#Task 2 Image Basics Moya Clarke 30.09.2020
#Instructions as follows:
#1. Open a user selected image
#2. Show this image on screen
#3. Capture users click on image
#4. Draw a 201x201, 5 pixel red square around user location (why 201x201? the pixel being clicked takes up a 1x1 space, and the 201x201 allows for an even square)
#5. COnvert pixels inside to YUV
#Advanced Task, don't fall off the edge

#importing all necessary libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

#draw function
def draw (event,x,y,flags,param):
    

    if event==cv2.EVENT_LBUTTONDOWN: #if mouse is clicked
        I=cv2.imread(f)
        height,width=I.shape[:2] #setting up the parameters for image size
        
        #making sure square does not fall off image by capping x and y values
        if x<100:
            x=100
        if y<100:
            y=100 
        if x>width-100:
            x=width-100
        if y>height-100:
            y=height-100 
         
        #drawing rectangle around mouse event on screen         
        cv2.rectangle(img=I,pt1=(x-100,y-100),pt2=(x+100, y+100), color=(0, 0, 255),thickness=5)
        
        #converion of image to YUV from BGR
        YUV=cv2.cvtColor(I,cv2.COLOR_BGR2YUV)
        
        #Selection of pixels to change to YUV
        I[y-100:y+100,x-100:x+100]=YUV[y-100:y+100,x-100:x+100]
        
        #Displaying image
        cv2.imshow("image",I)

# Opening an image using a File Open dialog:
f = easygui.fileopenbox()
I = cv2.imread(f)
Original=I.copy()#keep a copy
 
#displaying image 
cv2.namedWindow("image")
cv2.imshow("image",I)
cv2.setMouseCallback("drawWindow",draw)
key = cv2.waitKey(0)