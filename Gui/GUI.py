import threading
import time
import cv2
import numpy as np
from playsound import playsound
from numba import njit
from tkinter import *
import numpy

njit()

  
def a(): 

 cap = cv2.VideoCapture('D:\J.A.R.V.I.S\Gui\startup.mp4')

 if (cap.isOpened()== False):
     print("Error opening video file")

 while(cap.isOpened()):
      
     ret, frame = cap.read()
     frame = cv2.resize(frame,(1620,900))
     if ret == True:
    
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
  
     else:
        break
     

 

 cap.release()



def b():
 playsound("D:\J.A.R.V.I.S\Gui\mp3.mp3")




 
def c():
 threading.Thread(target=a).start()
 threading.Thread(target=b).start()

c()