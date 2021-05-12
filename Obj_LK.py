#!/usr/bin/env python
# coding: utf-8

# In[19]:


def onMouse(event,x,y,f,p):
    global initial_y,initial_x,k
    if event ==cv2.EVENT_LBUTTONDOWN:
        initial_x,initial_y=x,y
        
        k=-1


import cv2
import numpy as np
initial_y,initial_x,k=0,0,1
cv2.namedWindow("window")
cv2.setMouseCallback("window",onMouse)
cap=cv2.VideoCapture(0)
old_pts=np.array([[ix,iy]],dtype="float32").reshape(-1,1,2)
while True :
    _,frame=cap.read()
    cv2.imshow("window",frame)
    if cv2.waitKey(1)==27 or k==-1:
        old_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cap.release()
        cv2.destroyAllWindows()
        break
cap1=cv2.VideoCapture(0)  
old_pts=np.array([[ix,iy]],dtype="float32").reshape(-1,1,2)
mask=np.zeros_like(frame2)
while True:
    _,frame2=cap1.read()
    new_gray=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    new_pts,status,err=cv2.calcOpticalFlowPyrLK(old_gray,new_gray,old_pts,None,maxLevel=1,criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,15,0.008))
    cv2.circle(mask,(new_pts.ravel()[0],new_pts.ravel()[1]),2,(0,255,0),2)
    comvined=cv2.addWeighted(frame2,0.7,mask,0.3,0.1)
    cv2.imshow("new win",mask)
    cv2.imshow("win",comvined)
    old_gray=new_gray.copy()
    old_pts=new_pts.copy()
    if cv2.waitKey(1)==27:
        
        old_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cap1.release()
        cv2.destroyAllWindows()
        break

