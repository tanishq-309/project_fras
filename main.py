from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from student import student
import cv2
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        #creating the main window
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('Face Recognition Attendance System')
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        #bacground image bacground_FRAS.jpg
        img1=Image.open(os.path.join(BASE_DIR, "img", "bacground_FRAS.jpg"))
        img1=img1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1366,height=768)

        #showing time on main window
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(f_lbl,font=("times new roman",22,"bold"),background='white',foreground='red')
        lbl.place(x=1000,y=450,height=25)
        time()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        #bacground image bacground_FRAS.jpg
        img2=Image.open(os.path.join(BASE_DIR, "img", "student.jpg"))
        img2=img2.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(image=self.photoimg2,command=self.student_detials,cursor="hand2")
        b1.place(x=100,y=200)
        #student button text and adding functionality
        b1_1=Button(text="Student Details",command=self.student_detials,cursor="hand2",font=("times new roman",20,"bold"),bg="blue")
        b1_1.place(x=100,y=350)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        #bacground image bacground_FRAS.jpg
        img3=Image.open(os.path.join(BASE_DIR, "img", "detector.jpg"))
        img3=img3.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(image=self.photoimg3,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=200)
        #Face Detect Text and adding functionality
        b1_1=Button(text=" Face Detector ",cursor="hand2",command=self.face_data,font=("times new roman",20,"bold"),bg="blue")
        b1_1.place(x=400,y=350)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        #bacground image bacground_FRAS.jpg
        img4=Image.open(os.path.join(BASE_DIR, "img", "attendance.jpg"))
        img4=img4.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(image=self.photoimg4,cursor="hand2",command=self.attendance_data)
        b1.place(x=690,y=200)
        #Attendance Text and adding functionality
        b1_1=Button(text="    Attendance   ",cursor="hand2",command=self.attendance_data,font=("times new roman",20,"bold"),bg="blue")
        b1_1.place(x=690,y=350)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        #bacground image bacground_FRAS.jpg
        img5=Image.open(os.path.join(BASE_DIR, "img", "train.jpg"))
        img5=img5.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2=Button(image=self.photoimg5,cursor="hand2",command=self.train_data)
        b2.place(x=100,y=500)
        #Train button text and adding functionality
        b1_2=Button(text="       Train         ",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="blue")
        b1_2.place(x=100,y=650)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        #bacground image bacground_FRAS.jpg
        img6=Image.open(os.path.join(BASE_DIR, "img", "photos.jpg"))
        img6=img6.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(image=self.photoimg6,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=500)
        #Photos button text and adding functionality
        b1_1=Button(text="       Photos        ",command=self.open_img,cursor="hand2",font=("times new roman",20,"bold"),bg="blue")
        b1_1.place(x=400,y=650)

        #Exit button image and adding functionality
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        img7=Image.open(os.path.join(BASE_DIR, "img", "exit.jpg"))
        img7=img7.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(image=self.photoimg7,cursor="hand2",command=self.iExit)
        b1.place(x=690,y=500)
        #Exit button text adding functionality
        b1_1=Button(text="         Exit           ",cursor="hand2",command=self.iExit,font=("times new roman",20,"bold"),bg="blue")
        b1_1.place(x=690,y=650)
    
    #Adding Functionality to buttons and their corresponding images

    def student_detials(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def open_img(self):
        os.startfile("data")

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Exit","Do you want to exit the project?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

if __name__=='__main__':
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

        