from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from student import student
import cv2
import os
import face_recognition
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('Train the Dataset')
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        #bacground image bacground_FRAS.jpg
        img1=Image.open(os.path.join(BASE_DIR, "img", "bacground_FRAS.jpg"))
        img1=img1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1366,height=768)

        #main frame
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=0,y=170,width=1360,height=760)

        b1_1=Button(main_frame,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="cyan")
        b1_1.place(x=550,y=350)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert("L")  #to convert into grayscale L is written
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        #train the classifier and save data

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Dataset Training Completed!")


if __name__=='__main__':
    root=Tk()
    obj=Train(root)
    root.mainloop()