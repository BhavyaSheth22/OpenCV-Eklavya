import cv2
import numpy as np
m = 0
Mx =0
#Capturing Video through webcam.

cap = cv2.VideoCapture(0)

while(1):
        _, img = cap.read()

        #converting frame(img) from BGR (Blue-Green-Red) to HSV (hue-saturation-value)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        #defining the range of red color
        red_lower = np.array([153,110,90],np.uint8)
        red_upper = np.array([237,255,255],np.uint8)

        #finding the range red colour in the image

        red = cv2.inRange(hsv, red_lower, red_upper)

        #Morphological transformation, Dilation         
        kernel = np.ones((5 ,5), "uint8")

        blue=cv2.dilate(red, kernel)

        res=cv2.bitwise_and(img, img, mask = red)

        m = m+1
        #Tracking Colour (Red) 
        (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>700):
                        
                   
			 x1, y1, w, h = cv2.boundingRect(contour)
       			 x2 = x1 + w                           # (x1, y1) = top-left vertex
       			 y2 = y1 + h                           # (x2, y2) = bottom-right vertex
   			 cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)
       
			 cv2.circle(img,((x1+x2)/2,(y1+y2)/2), 2, (0,0,255), -1)
			 
			 rect = cv2.minAreaRect(contour)
			 
			 box = cv2.boxPoints(rect)
			 box = np.int0(box)
			 img = cv2.drawContours(img,[box],0,(0,0,255),2)


			 d = 3708.2352/(x2-x1)
			 a = (x2+x1)/2
			 x = (a-320)*4.8/(x2-x1)
			 D = 3708.2352/(y2-y1)
			 A = (y1+y2)/2
			 y = (A-240)*4.8/(y2-y1)
			 print("X COORDINATE:", x)
			 print("Y COORDINATE:", y)
			 print("D DISTANCE:", (D+d)/2)
			 Mx = (Mx+x)
			 mean = Mx/m
			 print("mean x",mean)
			

	cv2.line(img,(0,240),(640,240),(255,0,0),1)
	cv2.line(img,(320,0),(320,5480),(255,0,0),1)	                
        cv2.imshow("Color Tracking",img)
        img = cv2.flip(img,1)
        cv2.imshow("mask",res)
      
        if cv2.waitKey(10) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break
