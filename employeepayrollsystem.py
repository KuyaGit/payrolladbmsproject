from tkinter import*
from turtle import bgcolor, title, width
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll System-ADMIN Access by Mark Lowel Montealto")
        self.root.geometry("1350x800+0+0")
        self.root.configure(bg="#585858")
        title=Label(self.root,text="Employee Payroll Management System",font=("times new roman",30,"bold"),bg="#2F2F2F",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        #=====Frame 1/Employee Details===#
        Frame1=Frame(self.root,bd=2,relief=RIDGE, bg="#2f2f2f")
        Frame1.place(x=10,y=70,width=750,height=350)
        title2=Label(Frame1,text="Employee Details",font=("times new roman",18,"bold"),bg="#000000",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        #====Forms na===#
        lbl_id=Label(Frame1,text="Employee ID",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=40)
        txt_id=Entry(Frame1,font=("times new roman",15,"bold"),bg="#738086",fg="white").place(x=150,y=40)
        lbl_name=Label(Frame1,text="Name",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=70)
        txt_name=Entry(Frame1,font=("times new roman",15,"bold"),bg="#738086",fg="white").place(x=150,y=70,width=300)
        lbl_age=Label(Frame1,text="Age",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=100)
        lbl_gen=Label(Frame1,text="Gender",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=130)
        lbl_email=Label(Frame1,text="Email",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=160)
        lbl_position=Label(Frame1,text="Position",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=190)
        lbl_Saddress=Label(Frame1,text="Address",font=("times new roman",15,"bold"),bg="#2f2f2f",fg="white").place(x=20,y=220)
      
      
      
      
      
      
      
      
      
        #=====Frame 2/Employee Salary===#
        Frame2=Frame(self.root,bd=2,relief=RIDGE, bg="#2f2f2f")
        Frame2.place(x=770,y=70,width=550,height=350)
        title3=Label(Frame2,text="Salary Details",font=("times new roman",18,"bold"),bg="#000000",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        #=====Frame 3/Salary Receipt===#
        Frame3=Frame(self.root,bd=2,relief=RIDGE, bg="#2f2f2f")
        Frame3.place(x=10,y=425,width=1310,height=350)
        title3=Label(Frame3,text="Salary Receipt",font=("times new roman",18,"bold"),bg="#000000",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()