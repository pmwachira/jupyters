#!/usr/bin/env python
# coding: utf-8\

# read csv
import pandas as pd
import cv2


   

def draw_function(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = param[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        

def getColorName(R, G, B):
    minimum =10000
    for i in range(len(csv)):
        d =abs(R-int(csv.loc[i,'R']))+abs(G - int(csv.loc[i,'G']))+abs(B-int(csv.loc[i, 'B']))
        if (d<=minimum):
            minimum = d
            cname=csv.loc[i,'color_name']
            
    return cname

def getFrames():
    global clicked,r,g,b
    frame = 30
    cap.set(2, frame)
    frame_count = 0
    while (cap.isOpened):
        hasFrames, image = cap.read()
        window=cv2.imshow('image',image)
        cv2.setMouseCallback('image', draw_function, image)
        cv2.waitKey(20)
        if(clicked):
            cv2.rectangle(window,(20,20),(750,60),(b, g, r), -1)
            text = getColorName(r, g, b) + 'R='+str(r)+ 'G='+str(g)+ 'B='+str(b)
            cv2.putText(window, text,(50,50),2,.8,(255,255,255),2,cv2.LINE_AA)
            clicked=False

        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break

cap = cv2.VideoCapture(0)
sec=0
frameRate=50
count =1
clicked=False


r = g = b = xpos = ypos = 0

index = ['color','color_name','hex','R','G','B']
csv = pd.read_csv(r"C:\Users\mushirih\Desktop\projs\jupyter\data\colors.csv",names=index,header=None)



cv2.namedWindow('image')
getFrames()

if cv2.waitKey(25) & 0xFF == ord('q'): 
    cap.release()       
    cv2.destroyAllWindows()




cap.release()       
cv2.destroyAllWindows()

