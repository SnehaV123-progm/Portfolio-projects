# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:32:16 2024

@author: Sneha Vasudevan.
@Reach_Batch:  Python_11
@Project Name: Database GUI Project.
"""

import tkinter
from tkinter import messagebox
from tkinter import*
import pymysql

def task():
    if(e_id.get()=="" or e_name.get()=="" or e_age.get()=="" or e_phone.get()=="" or e_email.get()=="" or e_city.get()=="" or e_desig.get()=="" or e_sal.get()=="" or var.get()==""):
        messagebox.showinfo("Invalid Input", "Please fill all mandatory fields") 
    else:
        id=e_id.get()
        name=e_name.get()
        age=e_age.get()
        phone=e_phone.get()
        email=e_email.get()
        city=e_city.get()
        designation=e_desig.get()
        salary=e_sal.get()
        job_type=var.get()
        db=pymysql.connect(host="localhost", user="root", password="sql123", database="pytest")
        cursor=db.cursor()
        cursor.execute("insert into employer_data(emp_id,emp_name,emp_age,emp_phone, emp_email, emp_city,emp_designation,emp_salary,emp_job_type) values('"+id+"','"+name+"','"+age+"','"+phone+"','"+email+"','"+city+"','"+designation+"','"+salary+"','"+job_type+"')")
        cursor.execute("commit")
        messagebox.showinfo("Employee Details","Data inserted successfully")
        
        '''sql="Insert into 'emp_data'('emp_name','emp_age','emp_address') values('%s','%s','%s')"%(id,name,age,city)
        
        try:
            cursor.execute(sql,val)
            db.commit()
            messagebox.showinfo("Employee Details","Data inserted successfully")
        except:
            db.rollback()
            print("Not sorted")'''
        db.close()
        
eproj=tkinter.Tk()        
eproj.title(" Employer Data Survey Entry System")


#window background color and size.

eproj.config(bg="Beige")
eproj.geometry("520x450") #row x column


#Label names of the employer details.

l=Label(eproj,text="Enter employer's ID number: ",font=("Constantia Bold",10),bg="beige").place(x=10,y=10)      
l1=Label(eproj,text="Enter employer's Name: ",font=("Constantia Bold",10),bg="beige").place(x=10,y=40)
l2=Label(eproj,text="Enter employer's Age:", font=("Constantia Bold",10),bg="beige").place(x=10,y=80)
l3=Label(eproj,text="Enter employer's Phone number:", font=("Constantia Bold",10),bg="beige").place(x=10,y=120)
l4=Label(eproj,text="Enter employer's Email-id:", font=("Constantia Bold",10),bg="beige").place(x=10,y=160)
l5=Label(eproj,text="Enter employer's City:", font=("Constantia Bold",10),bg="beige").place(x=10,y=200)
l6=Label(eproj,text="Enter employer's Designation:", font=("Constantia Bold",10),bg="beige").place(x=10,y=240)
l7=Label(eproj,text="Enter employer's Salary:", font=("Constantia Bold",10),bg="beige").place(x=10,y=280)
l8=Label(eproj,text="Enter employer's Job type:", font=("Constantia Bold",10),bg="beige").place(x=10,y=325)


#Textbox design to enter the employer details.

e_id=tkinter.Entry(eproj)
e_id.place(x=270,y=10) 
    
e_name=tkinter.Entry(eproj)
e_name.place(x=270,y=40)

e_age=tkinter.Entry(eproj)
e_age.place(x=270,y=80)

e_phone=tkinter.Entry(eproj)
e_phone.place(x=270,y=120)

e_email=tkinter.Entry(eproj)
e_email.place(x=270,y=160)
           
e_city=tkinter.Entry(eproj)
e_city.place(x=270,y=200)

e_desig=tkinter.Entry(eproj)
e_desig.place(x=270,y=240)

e_sal=tkinter.Entry(eproj) 
e_sal.place(x=270,y=280)


# Drop-down list to select the job-type of the employment.

var=tkinter.StringVar()
var.set("Select job-type")
e_job=tkinter.OptionMenu(eproj,var,"Full-time","Part-time","Freelance")
e_job.configure(font=("Arial",10),bg="white")
e_job.place(x=265,y=320)


#Submit Button functionality.

a1=tkinter.Button(eproj,text="Submit", font=("Arial Bold",12) ,bg="green",fg="white", command= task).place(x=190,y=380)         
eproj.mainloop()
