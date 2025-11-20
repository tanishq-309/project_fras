from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from student import student
import cv2
import os
import face_recognition
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('Attendance')

        #variables' declaration
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #bacground image bacground_FRAS.jpg
        img1=Image.open(r"C:\Users\user\Documents\Projects\Project_FRAS\img\bacground_FRAS.jpg")
        img1=img1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1366,height=768)

        #main frame
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=0,y=170,width=1360,height=760)

        #left frame
        Left_frame=LabelFrame(main_frame,bg="white", bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=40, width=500, height=500)

        #left inside frame
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg='white')
        left_inside_frame.place(x=10,y=20,width=470,height=250)

        #labels and entries
        #attendance ID
        attendaceId_label=Label(left_inside_frame,text="Attendance ID",font=("times new roman",9,"bold"),bg="white")
        attendaceId_label.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        attendaceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",9,"bold"))
        attendaceID_entry.grid(row=0, column=1,padx=5,pady=5,sticky=W)

        #Roll
        rollLabel=Label(left_inside_frame,text="Roll No",font=("times new roman",9,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,sticky=W,padx=5,pady=5)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",9,"bold"))
        atten_roll.grid(row=0, column=3,padx=5,pady=5,sticky=W)

        #Name
        nameLabel=Label(left_inside_frame,text="Name",font=("times new roman",9,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",9,"bold"))
        atten_name.grid(row=1, column=1,padx=5,pady=5,sticky=W)

        #Department
        depLabel=Label(left_inside_frame,text="Department",font=("times new roman",9,"bold"),bg="white")
        depLabel.grid(row=1,column=2,sticky=W,padx=5,pady=5)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",9,"bold"))
        atten_dep.grid(row=1, column=3,padx=5,pady=5,sticky=W)

        #Time
        timeLabel=Label(left_inside_frame,text="Time",font=("times new roman",9,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,sticky=W,padx=5,pady=5)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",9,"bold"))
        atten_time.grid(row=2, column=1,padx=5,pady=5,sticky=W)

        #date
        dateLabel=Label(left_inside_frame,text="Date",font=("times new roman",9,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,sticky=W,padx=5,pady=5)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",9,"bold"))
        atten_date.grid(row=2, column=3,padx=5,pady=5,sticky=W)
        
        #attendance
        attendaceLabel=Label(left_inside_frame,text="Attendance Status",font=("times new roman",9,"bold"),bg="white")
        attendaceLabel.grid(row=3,column=0,sticky=W,padx=5,pady=5)

        self.atten_status=ttk.Combobox(left_inside_frame,width=10,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="read only")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=5, pady=5)
        self.atten_status.current(0)

        #button Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=170, width=385, height=30)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=12,font=("times new roman",9,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",width=12,command=self.exportCsv,font=("times new roman",9,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=12,font=("times new roman",9,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=12,command=self.reset_data,font=("times new roman",9,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #right frame
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Attendance",font=("times new roman",12,"bold"))
        Right_frame.place(x=550,y=40, width=800, height=500)

        #table frame 
        table_frame=Frame(Right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5, width=780, height=450)

        #creating X and Y axis based scroll bar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
    
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #fetching the data and creating function for the same
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv button functionality
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    #export csv button functionality
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.csv*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Sucess","Your data has been exported to "+os.path.basename(fln)+" sucessfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #fetching data into data fields
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    #giving functionality to reset button
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

if __name__=='__main__':
    root=Tk()
    obj=Attendance(root)
    root.mainloop()