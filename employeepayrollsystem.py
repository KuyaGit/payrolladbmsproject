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
        



        #=====Frame 1/Employee Details===#
        Frame1=Frame(self.root,bd=2,relief=RIDGE, bg="#2f2f2f")
        Frame1.place(x=10,y=70,width=750,height=350)
        title2=Label(Frame1,text="Employee Details",font=("times new roman",18,"bold"),bg="#000000",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        #====Forms na===#
        lbl_id=Label(Frame1,text="Employee ID",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=40)
        txt_id=Entry(Frame1,font=("times new roman",15,"bold"),textvariable=self.var_id,bg="#738086",fg="white").place(x=150,y=40)
        btn_search=Button(Frame1,text="Search",font=("times new roman",15),bg="#738086",fg="white").place(x=360,y=40,height=27,width=91)


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
        lbl_absents=Label(Frame2,text="Absents",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=170)
        txt_Absents=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_absents,bg="#738086",fg="white").place(x=150,y=170,width=300)
        lbl_basicSalary=Label(Frame2,text="Basic Salary",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=215)
        txt_basicSalary=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_basicSalary,bg="#738086",fg="white").place(x=150,y=215,width=300)
        
        
        #===Buttons For Save,Delete,Calculate,Update===#
        btn_calculate=Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman",15),bg="#738086",fg="white").place(x=75,y=270,width=100,height=25)
        btn_save=Button(Frame2,text="Save",font=("times new roman",15),bg="#738086",fg="white").place(x=250,y=270,width=100,height=25)
        btn_clear=Button(Frame2,text="Clear",font=("times new roman",15),bg="#738086",fg="white").place(x=425,y=270,width=100,height=25)
        btn_update=Button(Frame2,text="Update",font=("times new roman",15),bg="#738086",fg="white").place(x=166,y=305,width=100,height=25)
        btn_delete=Button(Frame2,text="Delete",font=("times new roman",15),bg="#738086",fg="white").place(x=340,y=305,width=100,height=25)
        
        #=====Frame 3/Salary Receipt===#
        Frame3=Frame(self.root,bd=2,relief=RIDGE, bg="#2f2f2f")
        Frame3.place(x=10,y=425,width=1310,height=350)
        title3=Label(Frame3,text="Salary Receipt",font=("times new roman",18,"bold"),bg="#000000",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        sal_Frame2=Frame(Frame3,bg="#738086",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=5,height=315)


        #===SCROLLBAR SA SALARY RECEIPT====#
        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)


        self.txt_salary_receipt=Text(sal_Frame2,font=("times new roman",20),bg='#738086',fg="white",yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        


        #=====Print Button Printing Document salary receipt====#
        btn_print=Button(Frame3,text="Print",font=("times new roman",15),bg="#738086",fg="white").place(x=1165,y=315,height=30,width=120)

    def calculate(self):
        print(self.var_id.get(),
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
        self.address.get('1.0',END)
        )



root=Tk()
obj=EmployeeSystem(root)
root.mainloop()