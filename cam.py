from tkinter import *
import cv2
from PIL import Image,ImageTk
from time import sleep
import datetime
from threading import Thread
import os

root=Tk()
root.title("camera")
root.geometry("300x480")





def open_cam():

    global fra
    cap=cv2.VideoCapture(0)
    
    while(True):
        ret,fra=cap.read()
        if not ret:
            break
    
        fra=cv2.resize(fra,(400,400))
        cv2img=cv2.cvtColor(fra,cv2.COLOR_BGR2RGBA)
        img=Image.fromarray(cv2img)

        imgtk=ImageTk.PhotoImage(image=img)
        ca.create_image(0, 0, image=imgtk, anchor=NW)
        root.update()
        

def take_picture():
    timenow = datetime.datetime.now()
    date = timenow.strftime("%Y-%m-%d %I %M %Sn %p")
    sleep(0.4)
    current_file_path = os.path.abspath(__file__)
    x=current_file_path+ str(date) +".png"
    cv2.imwrite(x,fra)

        
ca=Canvas(root, width=300, height=400,bg="black")
ca.pack()

open=Button(root,text="open",command=open_cam,bg="#A4A4A4",width=10)
open.pack()

take=Button(root,text="take a picture",command=take_picture,bg="#A4A4A4",width=10)
take.pack()


root.mainloop()


