from stat import FILE_ATTRIBUTE_ARCHIVE
from time import time
import pymysql
import time
import os
import tempfile

from tkinter import messagebox,ttk
from tkinter import*
from tokenize import String
from turtle import bgcolor, title, width
from webbrowser import get
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll System-ADMIN Access by Mark Lowel Montealto")
        self.root.geometry("1350x800+0+0")
        self.root.configure(bg="#585858")
        title=Label(self.root,text="Employee Payroll Management System",font=("times new roman",30,"bold"),bg="#2F2F2F",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_allemp=Button(self.root,text="All Employees",command=self.empFrame,font=("times new roman",15),bg="#738086",fg="white").place(x=1190,y=15,height=27,width=150)
        #====Variable====#
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gen=StringVar()
        self.var_email=StringVar()
        self.var_position=StringVar()
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_totalDays=StringVar()
        self.var_absents=StringVar()
        self.var_basicSalary=StringVar()
        self.var_totalSalary=StringVar()
    
        



        #=====Frame 1/Employee Details===#
        Frame1=Frame(self.root,bd=2,relief=RIDGE, bg="#2f2f2f")
        Frame1.place(x=10,y=70,width=750,height=350)
        title2=Label(Frame1,text="Employee Details",font=("times new roman",18,"bold"),bg="#000000",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        #====Forms na===#
        lbl_id=Label(Frame1,text="Employee ID",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=40)
        self.txt_id=Entry(Frame1,font=("times new roman",15,"bold"),textvariable=self.var_id,bg="#738086",fg="white")
        self.txt_id.place(x=150,y=40)
        btn_search=Button(Frame1,text="Search",command=self.search,font=("times new roman",15),bg="#738086",fg="white").place(x=360,y=40,height=27,width=91)


        lbl_name=Label(Frame1,text="Name",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=70)
        txt_name=Entry(Frame1,font=("times new roman",15,"bold"),textvariable=self.var_name,bg="#738086",fg="white").place(x=150,y=70,width=300)
        lbl_age=Label(Frame1,text="Age",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=100)
        txt_age=Entry(Frame1,font=("times new roman",15,"bold"),textvariable=self.var_age,bg="#738086",fg="white").place(x=150,y=100,width=300)
        lbl_gen=Label(Frame1,text="Gender",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=130)
        txt_gen=Entry(Frame1,font=("times new roman",15,"bold"),textvariable=self.var_gen,bg="#738086",fg="white").place(x=150,y=130,width=300)
        lbl_email=Label(Frame1,text="Email",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=160)
        txt_email=Entry(Frame1,font=("times new roman",15,"bold"),textvariable=self.var_email,bg="#738086",fg="white").place(x=150,y=160,width=300)
        lbl_position=Label(Frame1,text="Position",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=190)
        txt_position=Entry(Frame1,font=("times new roman",15,"bold"),textvariable=self.var_position,bg="#738086",fg="white").place(x=150,y=190,width=300)
        
        
        lbl_address=Label(Frame1,text="Address",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=220)
        self.address=Text(Frame1,font=("times new roman",15,"bold"),bg="#738086",fg="white")
        self.address.place(x=150,y=220,width=570,height=100)

        
      
      
      
      
      
      
      
      
        #=====Frame 2/Employee Salary===#
        Frame2=Frame(self.root,bd=2,relief=RIDGE, bg="#2f2f2f")
        Frame2.place(x=770,y=70,width=550,height=350)
        title3=Label(Frame2,text="Employee Salary Details",font=("times new roman",18,"bold"),bg="#000000",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        #====Forms Para Computation ng Salary====#
        lbl_month=Label(Frame2,text="Month",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=40)
        txt_month=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_month,bg="#738086",fg="white").place(x=95,y=40)
        lbl_year=Label(Frame2,text="Year",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=70)
        txt_year=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_year,bg="#738086",fg="white").place(x=95,y=70)
        lbl_totalDays=Label(Frame2,text="Total Days",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=125)
        txt_totalDays=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_totalDays,bg="#738086",fg="white").place(x=150,y=125,width=300)
        lbl_absents=Label(Frame2,text="Absents",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=155)
        txt_Absents=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_absents,bg="#738086",fg="white").place(x=150,y=155,width=300)
        lbl_basicSalary=Label(Frame2,text="Basic Salary",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=185)
        txt_basicSalary=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_basicSalary,bg="#738086",fg="white").place(x=150,y=185,width=300)
        lbl_totalSalary=Label(Frame2,text="Total Salary",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=215)
        txt_totalSalary=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_totalSalary,bg="#738086",fg="white").place(x=150,y=215,width=300)
        
        
        #===Buttons For Save,Delete,Calculate,Update===#
        btn_calculate=Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman",15),bg="#738086",fg="white").place(x=75,y=270,width=100,height=25)
        self.btn_save=Button(Frame2,text="Save",state=DISABLED,command=self.add,font=("times new roman",15),bg="#738086",fg="white")
        self.btn_save.place(x=250,y=270,width=100,height=25)
        btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",15),bg="#738086",fg="white").place(x=425,y=270,width=100,height=25)
        self.btn_update=Button(Frame2,text="Update",state=DISABLED,command=self.update,font=("times new roman",15),bg="#738086",fg="white")
        self.btn_update.place(x=166,y=305,width=100,height=25)
        self.btn_delete=Button(Frame2,text="Delete",state=DISABLED,command=self.delete,font=("times new roman",15),bg="#738086",fg="white")
        self.btn_delete.place(x=340,y=305,width=100,height=25)
        
        #=====Frame 3/Salary Receipt===#
        Frame3=Frame(self.root,bd=2,relief=RIDGE, bg="#2f2f2f")
        Frame3.place(x=10,y=425,width=1310,height=350)
        title3=Label(Frame3,text="Salary Receipt",font=("times new roman",18,"bold"),bg="#000000",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        sal_Frame2=Frame(Frame3,bg="#738086",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=5,height=315)

        self.sample=f'''\tCompany Name, XYZ\n\tAddress:XYZ,Floor4
-----------------------------------------------
Employee ID\t\t:    ----
Salary of\t\t:  MM-YYYY
Generated on\t\t:   MM-DD-YYYY
-----------------------------------------------
Total Days\t\t:    ----
Total Present\t\t:    ----
Total Absents\t\t:  ----
Basic Salary\t\t:   ----
Total Salary\t\t:    ----
-----------------------------------------------
This is computer generated slip,not
required any signature
********Employee Payroll System BY Mark Lowel Montealto********
'''

        #===SCROLLBAR SA SALARY RECEIPT====#
        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)


        self.txt_salary_receipt=Text(sal_Frame2,font=("times new roman",20),bg='#738086',fg="white",yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END,self.sample)
        
        self.check_connection()

        #=====Print Button Printing Document salary receipt====#
        btn_print=Button(Frame3,text="Print",command=self.print,font=("times new roman",15),bg="#738086",fg="white").place(x=1165,y=315,height=30,width=120)

    def add(self):
        if self.var_id.get()=='' or self.var_name.get()=='' or self.var_gen.get()=='' or self.var_age.get()=='' or self.var_email.get()=='' or self.var_position.get=='':
            messagebox.showerror("Error",'Employee Details are required')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employeepayroll')
                cur=con.cursor()
                cur.execute("select * from empsalary where id=%s",(self.var_id.get()))
                row=cur.fetchone()
                #print(rows)
                if row!=None:
                    messagebox.showerror("Error",'This Employee ID is already on our Database',parent=self.root)
                else:
                    cur.execute("insert into empsalary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gen.get(),
                        self.var_email.get(),
                        self.var_position.get(),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_totalDays.get(),
                        self.var_absents.get(),
                        self.var_basicSalary.get(),
                        self.address.get('1.0',END),
                        self.var_totalSalary.get(),
                        self.var_id.get()+".txt"
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('salaryreciept/'+str(self.var_id.get())+".txt",'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()

                    messagebox.showinfo("Success","Record,Successfully Added")

            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def update(self):
        if self.var_id.get()=='' or self.var_name.get()=='' or self.var_gen.get()=='' or self.var_age.get()=='' or self.var_email.get()=='' or self.var_position.get=='':
            messagebox.showerror("Error",'Employee Details are required')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employeepayroll')
                cur=con.cursor()
                cur.execute("select * from empsalary where id=%s",(self.var_id.get()))
                row=cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("Error",'This Employee ID is in invalid, Try again with valid ID',parent=self.root)
                else:
                    cur.execute("UPDATE `empsalary` SET `id`=%s,`name`=%s,`age`=%s,`gen`=%s,`email`=%s,`position`=%s,`month`=%s,`year`=%s,`totaldays`=%s,`absents`=%s,`basicsalary`=%s,`address`=%s,`totalsalary`=%s,`salaryreciept`=%s WHERE 'id'=%s",
                    (
                        
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gen.get(),
                        self.var_email.get(),
                        self.var_position.get(),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_totalDays.get(),
                        self.var_absents.get(),
                        self.var_basicSalary.get(),
                        self.address.get('1.0',END),
                        self.var_totalSalary.get(),
                        self.var_id.get()+".txt",
                        self.var_id.get()
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('salaryreciept/'+str(self.var_id.get())+".txt",'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()

                    messagebox.showinfo("Success","Record,Successfully Updated")

            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')


    def calculate(self):
        if self.var_basicSalary.get()=='' or self.var_totalDays.get=='' or self.var_absents.get=='':
            messagebox.showerror("Error",'All Details are Required')
        else:
            per_day=int(self.var_basicSalary.get())/int(self.var_totalDays.get())
            work_day=int(self.var_totalDays.get())-int(self.var_absents.get())
            totalsalary=per_day*work_day
            self.var_totalSalary.set(str(round(totalsalary,2)))
            new_sample=f'''\tCompany Name, XYZ\n\tAddress:XYZ,Floor4
-----------------------------------------------
Employee ID\t\t:    {self.var_id.get()}
Salary of\t\t:  {self.var_month.get()}-{self.var_year.get()}
Generated on\t\t:   {str(time.strftime("%d-%M-%Y"))}
-----------------------------------------------
Total Days\t\t:    {str(int(self.var_totalDays.get())-int(self.var_absents.get()))}
Total Present\t\t:    {self.var_totalDays.get()}
Total Absents\t\t:  {self.var_absents.get()}
Basic Salary\t\t:   {self.var_basicSalary.get()}
Total Salary\t\t:    {self.var_totalSalary.get()}
-----------------------------------------------
This is computer generated slip,not
required any signature
********Employee Payroll System BY Group 2********
'''
            self.txt_salary_receipt.delete('1.0',END)
            self.txt_salary_receipt.insert(END,new_sample)

    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.txt_id.config(state=NORMAL)
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_age.set(""),
        self.var_gen.set(""),
        self.var_email.set(""),
        self.var_position.set(""),
        self.var_month.set(""),
        self.var_year.set(""),
        self.var_totalDays.set(""),
        self.var_absents.set(""),
        self.var_basicSalary.set(""),
        self.address.delete('1.0',END),
        self.var_totalSalary.set(""),
        self.txt_salary_receipt.delete('1,0',END)
        self.txt_salary_receipt.insert(END,self.sample)


    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='employeepayroll')
            cur=con.cursor()
            cur.execute("select * from empsalary where id=%s",(self.var_id.get()))
            row=cur.fetchone()
            #print(rows)
            if row==None:
                messagebox.showerror("Error","Invalid Employee ID, Please try with another Employee ID")
            else:
                print(row)
                self.var_id.set(row[0]),
                self.var_name.set(row[1]),
                self.var_age.set(row[2]),
                self.var_gen.set(row[3]),
                self.var_email.set(row[4]),
                self.var_position.set(row[5]),
                self.var_month.set(row[6]),
                self.var_year.set(row[7]),
                self.var_totalDays.set(row[8]),
                self.var_absents.set(9),
                self.var_basicSalary.set(10),
                self.address.delete('1.0',END),
                self.address.insert(END,row[11])
                self.var_totalSalary.set(row[12]),
                file_=open('salaryreciept/'+str(row[13]),'r')
                self.txt_salary_receipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_receipt.insert(END,i)
                file_.close()
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_id.config(state='readonly')





        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')
    
    def delete(self):
        if self.var_id.get()=='':
            messagebox.showerror("Error","Employee ID must Required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employeepayroll')
                cur=con.cursor()
                cur.execute("select * from empsalary where id=%s",(self.var_id.get()))
                row=cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID, Please try with another Employee ID")
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from empsalary where id=%s",(self.var_id.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Successfully Deleted",parent=self.root)
                        self.clear()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')


    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='employeepayroll')
            cur=con.cursor()
            cur.execute("select * from empsalary")
            rows=cur.fetchall()
            print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')
    
    def showall(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='employeepayroll')
            cur=con.cursor()
            cur.execute("select * from empsalary")
            rows=cur.fetchall()
            # print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def empFrame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll System-ADMIN Access by Mark Lowel Montealto")
        self.root2.geometry("1000x500+120+100")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee Details",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        self.root2.focus_force()

        scrollY=Scrollbar(self.root2,orient=VERTICAL)
        scrollX=Scrollbar(self.root2,orient=HORIZONTAL)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollX.pack(side=BOTTOM,fill=X)

        self.employee_tree=ttk.Treeview(self.root2,columns=('id', 'name', 'age', 'gen', 'email', 'position', 'month', 'year', 'totaldays', 'absents', 'basicsalary', 'address', 'totalsalary', 'salaryreciept'))#,yscrollcommand=scrollY.set,xscrollcommand=scrollX.set)
        self.employee_tree.heading('id',text='Employeee ID')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gen',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('position',text='Position')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('totaldays',text='Total Days')
        self.employee_tree.heading('absents',text='Absents')
        self.employee_tree.heading('basicsalary',text='Basic Salary')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('totalsalary',text='Total Salary')
        self.employee_tree.heading('salaryreciept',text='Salary Reciept')
        self.employee_tree['show']='headings'
        self.employee_tree.column('id',width=70)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=50)
        self.employee_tree.column('gen',width=50)
        self.employee_tree.column('email',width=50)
        self.employee_tree.column('position',width=50)
        self.employee_tree.column('month',width=50)
        self.employee_tree.column('year',width=10)
        self.employee_tree.column('totaldays',width=10)
        self.employee_tree.column('absents',width=50)
        self.employee_tree.column('basicsalary',width=50)
        self.employee_tree.column('address',width=100)
        self.employee_tree.column('totalsalary',width=50)
        self.employee_tree.column('salaryreciept',width=50)
        scrollX.config(command=self.employee_tree.xview)
        scrollY.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.showall()
        
        
        self.root2.mainloop()
    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_,'print')


root=Tk()
obj=EmployeeSystem(root)
root.mainloop()