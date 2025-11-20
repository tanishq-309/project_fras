from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('Student Details')

        #declaring variables
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

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
        Left_frame=LabelFrame(main_frame,bg="white", bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=40, width=500, height=500)
        #current course information
        current_course_frame=LabelFrame(Left_frame,bg="white", bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=42, width=460, height=100)
        #department label
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",9,"bold"),bg="white")
        dep_label.grid(row=0,column=0,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",9,"bold"),width=14,state="read only")
        dep_combo["values"]=("Deptartment","Computer","Business")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1)
        #Course label
        course_label=Label(current_course_frame,text="Course",font=("times new roman",9,"bold"),bg="white")
        course_label.grid(row=0,column=2,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",9,"bold"),width=14,state="read only")
        course_combo["values"]=("Select Course","BCA","BBA","B.ED","B.COM","B.Tech","MCA","M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3)
        #Year label
        year_label=Label(current_course_frame,text="Year",font=("times new roman",9,"bold"),bg="white")
        year_label.grid(row=1,column=0,sticky=W,padx=10)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",9,"bold"),width=14,state="read only")
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10)

        #Semester label
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",9,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,sticky=W,padx=10)
        
        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",9,"bold"),width=16,state="read only")
        Semester_combo["values"]=("Select Semester"," 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10)

        #class student information frame
        class_Student_frame=LabelFrame(Left_frame,bg="white", bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=10,y=150, width=460, height=300)

        #studentId
        studentId_label=Label(class_Student_frame,text="Student ID:",font=("times new roman",9,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,sticky=W,padx=5)
        
        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",9,"bold"))
        studentID_entry.grid(row=0, column=1,padx=5,sticky=W)

        #student name
        studenname_label=Label(class_Student_frame,text="Student Name",font=("times new roman",9,"bold"),bg="white")
        studenname_label.grid(row=0,column=2,sticky=W,padx=5)
        
        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",9,"bold"))
        studentName_entry.grid(row=0, column=3,padx=5,sticky=W)

        #class division
        class_div_label=Label(class_Student_frame,text="Class Division",font=("times new roman",9,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,sticky=W,padx=5,pady=5)
        
        class_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",9,"bold"))
        class_div_entry.grid(row=1, column=1,padx=5,sticky=W,pady=5)

        #Roll No
        roll_no_label=Label(class_Student_frame,text="Roll No.",font=("times new roman",9,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,sticky=W,padx=5,pady=5)
        
        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("times new roman",9,"bold"))
        roll_no_entry.grid(row=1, column=3,padx=5,sticky=W,pady=5)

        #Gender
        gender_label=Label(class_Student_frame,text="Gender",font=("times new roman",9,"bold"),bg="white")
        gender_label.grid(row=2,column=0,sticky=W,padx=5,pady=5)
        
        gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",9,"bold"))
        gender_entry.grid(row=2, column=1,padx=5,sticky=W,pady=5)

        #Date Of Birth
        dob_label=Label(class_Student_frame,text="DOB",font=("times new roman",9,"bold"),bg="white")
        dob_label.grid(row=2,column=2,sticky=W,padx=5,pady=5)
        
        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("times new roman",9,"bold"))
        dob_entry.grid(row=2, column=3,padx=5,sticky=W,pady=5)

        #Email
        email_label=Label(class_Student_frame,text="Email",font=("times new roman",9,"bold"),bg="white")
        email_label.grid(row=3,column=0,sticky=W,padx=5,pady=5)
        
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",9,"bold"))
        email_entry.grid(row=3, column=1,padx=5,sticky=W,pady=5)

        #Phone Number
        phone_label=Label(class_Student_frame,text="Phone No.",font=("times new roman",9,"bold"),bg="white")
        phone_label.grid(row=3,column=2,sticky=W,padx=5,pady=5)
        
        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=15,font=("times new roman",9,"bold"))
        phone_entry.grid(row=3, column=3,padx=5,sticky=W,pady=5)

        #Address
        address_label=Label(class_Student_frame,text="Address",font=("times new roman",9,"bold"),bg="white")
        address_label.grid(row=4,column=0,sticky=W,padx=5,pady=5)
        
        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",9,"bold"))
        address_entry.grid(row=4, column=1,padx=5,sticky=W,pady=5)

        #Teacher Name
        teacher_label=Label(class_Student_frame,text="Teacher Name",font=("times new roman",9,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,sticky=W,padx=5,pady=5)
        
        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",9,"bold"))
        teacher_entry.grid(row=4, column=3,padx=5,sticky=W,pady=5)

        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)
        #radio buttons
        
        radionbtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)
        
        #button Frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=170, width=415, height=100)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=12,font=("times new roman",9,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=12,command=self.update_data,font=("times new roman",9,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=12,font=("times new roman",9,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("times new roman",9,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,command=self.generate__dataset,text="Take Photo",width=12,font=("times new roman",9,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame,command=self.update__dataset,text="Update Photo",width=12,font=("times new roman",9,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)


        #right frame
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=550,y=40, width=800, height=500)

        # ========Table Frame=========
        table_frame=Frame(Right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5,y=15, width=780, height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Divison")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="EMAIL")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    

    # ==========function declaration=========
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Bed#gva$N",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.va_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student's details has been added Successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    #fetching data from database to student detials table
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Bed#gva$N",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get details in student details for updation
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data = content.get("values", [])
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.va_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    #updating student details via update button
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Bed#gva$N",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Divison=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.va_std_id.get()))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student Details have been updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #delete function
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Data Deletion","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Bed#gva$N",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deletion","Data deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #reset data fields
    def reset_data(self):
        self.var_dep.set("Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #generating data samples Take photos button
    def generate__dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Bed#gva$N",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=str(self.va_std_id.get())
                my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Divison=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.va_std_id.get()))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #loading haarcascade frontalface file via opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+id+"."+str(img_id)+".jpg"      
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset Generation Completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  

    def update__dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Bed#gva$N",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=str(self.va_std_id.get())
                # for x in myresult:
                #     id+=1
                my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Divison=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.va_std_id.get()))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #loading haarcascade frontalface file via opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=self.va_std_id.get()
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id=self.va_std_id.get()
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+id+"."+str(img_id)+".jpg"      
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset Updation Completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)       

if __name__=='__main__':
    root=Tk()
    obj=student(root)
    root.mainloop()