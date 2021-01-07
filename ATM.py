from tkinter import *
import time
import random
import sqlite3
from PIL import ImageTk, Image
import os
from tkinter import messagebox
img=""
acno=""
bal=""
p=""
Name=""
path=path="img1.gif"
conn=sqlite3.connect("atm.db")
def call_StartWindow():
    global img
    global path
    def open_win():
        atm_1.destroy()
        call_Login()
        
    def openwin():
        atm_1.destroy()
        call_NewAccount()
        
    def quitwin():
        messagebox.showinfo("Exit","Thanks for using our ATM Service")
        atm_1.destroy()
    atm_1=Tk()
    atm_1.title("Start Window")
    atm_1.geometry("1366x768")
    atm_1.configure(background="grey")
    #path="C:/Users/mayan/Desktop/Python/ATM PROJECT FRAMES/img1.gif"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(atm_1, image = img)
    panel.place(x=0,y=0)

    f1=Frame(atm_1,height=800,width=400,bd=5,relief="raise",bg="grey")
    f1.pack(side=TOP)
    text='''Welcome to Singh's Bank of India ATM!
Please Choose any one option from the  options Given Below'''
    L1=Label(f1,text=text,font=("arial",25,"bold"))
    L1.grid(columnspan=1)

    f2=Frame(atm_1,height=800,width=400,bd=5,relief="raise",bg="grey")
    f2.pack(side=LEFT)
    B1=Button(f2,text="New Account",font=("arial",20,"bold"),bg="grey",fg="white",bd=10,relief = GROOVE,activebackground="red",command=openwin)
    B1.grid(row=0,column=0)
    B2=Button(f2,text="Login",font=("arial",20,"bold"),bg="grey",fg="white",bd=10,padx=50,relief = GROOVE,activebackground="red",command=open_win)
    B2.grid(row=1,column=0)
    B3=Button(f2,text="QUIT",font=("arial",20,"bold"),bg="grey",fg="white",bd=10,padx=55,relief = GROOVE,activebackground="red",command=quitwin)
    B3.grid(row=2,column=0)
    atm_1.mainloop()
    
def call_NewAccount():
    def openwin():
        atm_2.destroy()
        call_StartWindow()
    def quitwin():
        messagebox.showinfo("Exit","Thanks for using our ATM Service")
        atm_2.destroy()
        
    def acnogen():
        ac_no=""
        E2.delete(0, 'end')
        conn=sqlite3.connect("atm.db")
        r=random.randint(100000000,1000000000000000000)
        E2.insert(0,r)
        ac_no=r
        m="""Your New Account Number has been succesfully Generated
Your Account Number is  '{}'""".format(r)
        messagebox.showinfo("Acount Number",m)
        
    def NewAcCode():
                    
        def act():
            if checkvar1.get()==1 and checkvar2.get()==1:
                return "None"
            elif checkvar1.get()==1:
                return "CURRENT"
            elif checkvar2.get()==1:
                return "SAVING"
            elif checkvar1.get()==0 and checkvar2.get()==0:
                return "None1"
        def sex():
            if checkvar3.get()==1 and checkvar4.get()==1:
                return "None"
            elif checkvar3.get()==1:
                return "Male"
            elif checkvar4.get()==1:
                return "Female"
            elif checkvar3.get()==0 and checkvar4.get()==0:
                return "None1"
            
        b=0
        name=E1.get()
        name=name.capitalize()
        #print(name)
        ac_no=E2.get()
        actype=act()
        #print(actype)
        p_no=(E3.get())
        email=E4.get()
        #print(email)
        gender=sex()
        #print(gender)
        age=E6.get()
        pin=E5.get()
        try:
            if name!='Enter name here':
                if ac_no!='press get button':
                    ac_no=int(E2.get())
                    if actype!='None' and gender!='None' and actype!='None1' and gender!='None1':
                        if p_no!='enter phone no. here':
                            p_no=int(E3.get())
                            if p_no>=1000000000 and p_no<=9999999999:
                                if email!='enter e-mail here':
                                    if age!='enter age here':
                                        age=int(E6.get())
                                        if pin!='enter pin here':
                                            pin=int(E5.get())
                                            if pin>=1000 and pin<=9999:
                                                try:
                                                    conn.execute("""INSERT INTO ATM (NAME,AC_NO,AC_TYPE,P_NO,EMAIL,GENDER,AGE,PIN,balance)\
                                                    VALUES(?,?,?,?,?,?,?,?,?);""",(name,ac_no,actype,p_no,email,gender,age,pin,b))
                                                    conn.commit()
                                                    m="""{}, Your Account Successfully Created!
Account Number: {}
PIN: {}
Please Login...""".format(name,ac_no,pin)
                                                    messagebox.showinfo("New Account",m)
                                                    atm_2.destroy()
                                                    call_Login()
                                                except:
                                                    conn.rollback()
                                                    messagebox.showwarning("New Account","Error ! Account Creation Unsuccessfull !")
                                            else:
                                                messagebox.showinfo("New Account","Invalid PIN, The PIN Should be of 4 digits only")
                                        else:
                                            messagebox.showinfo("New Account","Please Enter Your PIN")
                                    else:
                                        messagebox.showinfo("New Account","Please Enter Your Age")
                                else:
                                    messagebox.showinfo("New Account","Please Enter Your E-mail")
                            else:
                                messagebox.showinfo("New Account","Invalid Phone Number, The Phone Number Should be of 10 digits only")
                        else:
                            messagebox.showinfo("New Account","Please Enter Your Phone Number")
                            
                    else:
                        if actype=='None':
                                messagebox.showinfo("New Account","""Dear User !
Please Choose only One Account Type either 'Current' or 'Saving'""") 
                        if gender=='None':
                                messagebox.showinfo("New Account","""Dear User !
Please Choose only One Gender either 'Male' or 'Female'""")
                        if actype=='None1':
                            messagebox.showinfo("New Account",'''Dear User !
You do not have selected any Account Type Please Select''')
                        if gender=='None1':
                                messagebox.showinfo("New Account",'''Dear User !
You do not have selected Your Gender Please Select''')
                else:
                    messagebox.showinfo("New Account","Please Press Get Button to Generate Your Account Number")
            else:
                messagebox.showinfo("New Account","Please Enter Your Name")
        except:
            messagebox.showwarning("New Account","Error ! Please Fill Your Details Carefully")
            E1.delete(0, 'end')
            E2.delete(0,'end')
            E3.delete(0,'end')
            E4.delete(0,'end')
            E5.delete(0,'end')
            E6.delete(0,'end')
            E1.insert(0,'enter name here')
            E2.insert(0,'press get button')
            E3.insert(0,'enter phone no. here')
            E4.insert(0,'enter e-mail here')
            E5.insert(0,'enter pin here')
            E6.insert(0,'enter age here')
        
    
    global img 
    atm_2=Tk()
    atm_2.title("Create Account")
    atm_2.geometry("1366x1768")
    atm_2.configure(background="Light grey")
    
    #path="C:/Users/mayan/Desktop/Python/ATM PROJECT FRAMES/img1.gif"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(atm_2, image = img)
    panel.place(x=0,y=0)
    
    checkvar1 = IntVar()  
    checkvar2 = IntVar()
    checkvar3 = IntVar()  
    checkvar4 = IntVar()
    
    f1=Frame(atm_2,height=800,width=400,relief="raise",bd=5,bg="grey")
    f1.pack(side=TOP)
    L1=Label(f1,text="Please Fill Your Details",font=("arial",25,"bold"))
    L1.grid(columnspan=3)

    f2=Frame(atm_2,height=800,width=400,relief="raise",bd=5,bg="grey")
    f2.place(x=370,y=150)
    L2=Label(f2,text="NAME",font=("arial",15,"bold"),padx=57)
    L2.grid(row=0,column=0)
    L3=Label(f2,text="ACCOUNT NO.",font=("arial",15,"bold"),padx=15)
    L3.grid(row=1,column=0)
    L4=Label(f2,text="ACCOUNT TYPE",font=("arial",15,"bold"),padx=7)
    L4.grid(row=2,column=0)
    cb1 = Checkbutton(f2, text = "CURRENT", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10,font=("arial",10))
    cb1.place(x=363,y=75,height=25,width=100)
    cb2 = Checkbutton(f2, text = "SAVING", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10,font=("arial",10))
    cb2.place(x=492,y=75,height=25,width=100)
    L5=Label(f2,text="PHONE NO.",font=("arial",15,"bold"),padx=29)
    L5.grid(row=3,column=0)
    L6=Label(f2,text="E-MAIL",font=("arial",15,"bold"),padx=52)
    L6.grid(row=4,column=0)
    L6=Label(f2,text="GENDER",font=("arial",15,"bold"),padx=44)
    L6.grid(row=5,column=0)
    cb3 = Checkbutton(f2, text = "MALE", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10,font=("arial",10))
    cb3.place(x=365,y=178,height=25,width=100)
    cb4 = Checkbutton(f2, text = "FEMALE", variable = checkvar4, onvalue = 1, offvalue = 0, height = 2, width = 10,font=("arial",10))
    cb4.place(x=492,y=178,height=25,width=100)
    L7=Label(f2,text="CREATE PIN",font=("arial",15,"bold"),padx=27)
    L7.grid(row=6,column=0)
    L8=Label(f2,text="Age",font=("arial",15,"bold"),padx=69)
    L8.grid(row=7,column=0)
    E1=Entry(f2,font=("arial",15),bg="white",fg="black",bd=5)
    E1.grid(row=0,column=2)
    E1.insert(0,'enter name here')
    E2=Entry(f2,font=("arial",15),bg="white",fg="black",bd=5)
    E2.grid(row=1,column=2)
    E2.insert(0,'press get button')
    E3=Entry(f2,font=("arial",15),bg="white",fg="black",bd=5)
    E3.grid(row=3,column=2)
    E3.insert(0,'enter phone no. here')
    E4=Entry(f2,font=("arial",15),bg="white",fg="black",bd=5)
    E4.grid(row=4,column=2)
    E4.insert(0,'enter e-mail here')
    E5=Entry(f2,font=("arial",15),bg="white",fg="black",bd=5)
    E5.grid(row=6,column=2)
    E5.insert(0,'enter pin here')
    E6=Entry(f2,font=("arial",15),bg="white",fg="black",bd=5)
    E6.grid(row=7,column=2)
    E6.insert(0,'enter age here')
    
    B1=Button(f2,text="Submit",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=68,relief = GROOVE,activebackground="red",command=NewAcCode)
    B1.grid(row=8,column=2)
    B2=Button(f2,text="Back",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=50,relief = GROOVE,activebackground="red",command=openwin)
    B2.grid(row=8,column=0)
    B3=Button(f2,text="QUIT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=50,relief = GROOVE,activebackground="red",command=quitwin)
    B3.grid(row=9,column=1)
    B4=Button(f2,text="GET",font=("arial",13),bg="grey",fg="white",bd=10,padx=50,relief = GROOVE,activebackground="red",command=acnogen)
    B4.place(x=290,y=37,height=34,width=60)

    atm_2.mainloop()

def call_Login():
    def openwin():
        atm_3.destroy()
        call_StartWindow()
        
    def quitwin():
        messagebox.showinfo("Exit","Thanks for using our ATM Service")
        atm_3.destroy()
    def msgwin():
        try:
            global Name
            global p
            global acno
            global bal
            ac=False
            acno=E1.get()
            pin=E2.get()
            if acno!='enter account no. here':
                acno=int(E1.get())
                if acno>=100000000 and acno<1000000000000000000:
                    if pin!='enter pin here':
                        pin=int(E2.get())
                        if pin>=1000 and pin<=9999: 
                            temp = conn.execute("select name,pin,ac_no,ac_type,balance from atm where ac_no = ? ", (acno,))
                            for i in temp:
                                Name=i[0]
                                a = i[2]
                                p=i[1]
                                bal=i[4]
                                acno=a
                                if a==acno:
                                    ac=True
                                    if i[1]==pin:
                                        ac = True
                                        m = '''Login Sucessfull !
Welcome ! {},'''.format(i[0])
                                        messagebox.showinfo("Login Info", m)
                                        atm_3.destroy()
                                        call_MainWindow()
                                        
                                    else:
                                        ac = True
                                        m = " Login UnSucessFull ! Wrong PIN Number"
                                        messagebox.showinfo("Login Info!", m)

                            if not ac:
                                m = " Wrong Account Number !"
                                messagebox.showwarning("Login Info!", m)
                        else:
                            messagebox.showwarning("warning","Invalid PIN Try again")
                    else:
                        messagebox.showwarning("warning","Please Enter Your PIN")
                else:
                    messagebox.showwarning("warning","Invalid Account Number Try again")
            else:
                messagebox.showwarning("warning","Please Enter Your Account Number")
        except:
            E1.delete(0,'end')
            E2.delete(0,'end')
            E1.insert(0,'enter account no. here')
            E2.insert(0,'enter pin here')
            messagebox.showwarning("warning","Error ! Login Details Incorrect")
                
    global img    
    atm_3=Tk()
    atm_3.title("Login")
    atm_3.geometry("1366x768")
    atm_3.configure(background="Light grey")

    #path="C:/Users/mayan/Desktop/Python/ATM PROJECT FRAMES/img1.gif"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(atm_3, image = img)
    panel.place(x=0,y=0)

    f2=Frame(atm_3,height=800,width=400,relief="raise",bd=5,bg="grey")
    f2.pack(side=TOP)
    L1=Label(f2,text="Please Enter Your Login Details",font=("arial",25,"bold"))
    L1.grid(columnspan=2)

    f1=Frame(atm_3,height=800,width=400,relief="raise",bd=5,bg="grey")
    f1.place(x=410,y=150)
    L2=Label(f1,text="Account No.",font=("arial",15,"bold"))
    L2.grid(row=1,column=0)
    L6=Label(f1,text="                                          ",bg="grey")
    L6.grid(row=1,column=1)
    L7=Label(f1,text="",bg="grey")
    L7.grid(row=6,column=0)
    L4=Label(f1,text="",bg="grey")
    L4.grid(row=2,column=0)
    L3=Label(f1,text="ATM PIN:",font=("arial",15,"bold"),padx=15)
    L3.grid(row=3,column=0)
    L5=Label(f1,text="",bg="grey")
    L5.grid(row=4,column=0)
    E1=Entry(f1,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
    E1.grid(row=1,column=2)
    E1.insert(0,'enter account no. here')
    E2=Entry(f1,font=("arial",15,"bold"),bg="white",fg="black",bd=5,show="*")
    E2.grid(row=3,column=2)
    E2.insert(0,'enter pin here')
    B1=Button(f1,text="Login",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=30,relief = GROOVE,activebackground="red",command=msgwin)
    B1.grid(row=5,column=2)
    B1=Button(f1,text="Back",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=22,relief = GROOVE,activebackground="red",command=openwin)
    B1.grid(row=5,column=0)
    B2=Button(f1,text="QUIT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=30,relief = GROOVE,activebackground="red",command=quitwin)
    B2.grid(row=7,columnspan=3)

    atm_3.mainloop()


def call_withdraw():
        def call_centrywin():
            ac=False
            global acno
            ac_type='CURRENT'
            for i in conn.execute("select ac_type from atm where ac_no=?",(acno,)):
                if i[0]==ac_type:
                    ac=True
                    centrywin()
                else:
                    pass
            if not ac:
                    messagebox.showinfo("imformation",'''Dear User !
you do not have Current Account''')
        def call_sentrywin():
            ac=False
            global acno
            ac_type='SAVING'
            for i in conn.execute("select ac_type from atm where ac_no=?",(acno,)):
                if i[0]==ac_type:
                    ac=True
                    sentrywin()
                else:
                    pass
            if not ac:
                    messagebox.showinfo("imformation",'''Dear User !
you do not have Saving Account''')
        def openwin():
            atm_5.destroy()
            call_MainWindow()
            
        def quitwin():
            messagebox.showinfo("Exit","Thanks for using our ATM Service")
            atm_5.destroy()
        def centrywin():
            def execute_withdraw():
                global acno
                global bal
                try:
                            amt=E1.get()
                            if amt!='enter amount here':
                                amt=int(E1.get())
                                if amt>0:
                                    if amt%500==0:
                                        if amt<=bal:
                                            try:
                                                conn.execute("update atm set balance = balance - ? where ac_no = ?",(amt,acno))
                                                conn.commit()
                                                acc_list=[]
                                                for i in conn.execute("select name,balance,ac_no from atm where ac_no = ?",(acno,)):
                                                    bal=i[1]
                                                    if i[2]==acno:
                                                        acc_list.append("{}".format(i[0]))
                                                        text='''{}, RS.{} Withdrawal Successfully'''.format(i[0],amt)
                                                        L2=Label(f6,text=text,font="arial")
                                                        L2.grid(row =0,column=0)
                                                        E1.delete(0,'end')
                                                        E1.insert(0,'enter amount here')
                                                for i in conn.execute("select name,balance,ac_no from atm where ac_no = ?",(acno,)):
                                                    if i[2]==acno:
                                                            m = '''{}, RS.{} Withdrawal Successfully'''.format(i[0],amt)
                                                            messagebox.showinfo("Money Withdraw !", m)
                                            
                                            except:
                                                messagebox.showwarning("Failed","Error !")
                                                conn.rollback()
                                        else:
                                            E1.delete(0,'end')
                                            E1.insert(0,'enter amount here')
                                            messagebox.showinfo("imformation",'''Sorry !
Insufficient Balance in your Acount
please Enter Amount within Your Balance Limit''')
                                            
                                    else:
                                        
                                        messagebox.showinfo("imformation",'''Dear User !
Entered Amount Should be Multiple of 500
please Enter Your Amount Again''')
                                else:
                                    messagebox.showwarning("warning","Invalid Amount Try again")
                            else:
                                messagebox.showinfo("Withdraw Amount","Please Enter Your Amount You want to Withdraw")
                except:
                    E1.delete(0,'end')
                    E1.insert(0,'enter amount here')
                    messagebox.showinfo("Withdraw Amount","Error ! Please enter a valid amount")

                
            L1=Label(f4,text="Amount",font=("arial",15,"bold"))
            L1.grid(row=0,column=0)
            L1=Label(f4,text="       ",font=("arial",15,"bold"),bg="grey")
            L1.grid(row=0,column=1)
            E1=Entry(f4,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
            E1.grid(row=0,column=2)
            E1.insert(0,'enter amount here')
            B1=Button(f4,text="Submit",font=("arial",10,"bold"),bg="grey",fg="white",bd=10,padx=40,relief = GROOVE,activebackground="red",command=execute_withdraw)
            B1.grid(row=2,column=2)
        def sentrywin():
            def execute_withdraw():
                global acno
                global bal
                try:
                            amt=E1.get()
                            if amt!='enter amount here':
                                amt=int(E1.get())
                                if amt>0:
                                    if amt%500==0:
                                        if amt<=bal:
                                            try:
                                                conn.execute("update atm set balance = balance - ? where ac_no = ?",(amt,acno))
                                                conn.commit()
                                                acc_list=[]
                                                for i in conn.execute("select name,balance,ac_no from atm where ac_no = ?",(acno,)):
                                                    bal=i[1]
                                                    if i[2]==acno:
                                                        acc_list.append("{}".format(i[0]))
                                                        text='''{}, RS.{} Withdrawal Successfully'''.format(i[0],amt)
                                                        L2=Label(f6,text=text,font="arial")
                                                        L2.grid(row =0,column=0)
                                                        E1.delete(0,'end')
                                                        E1.insert(0,'enter amount here')
                                                for i in conn.execute("select name,balance,ac_no from atm where ac_no = ?",(acno,)):

                                                    if i[2]==acno:
                                                            m = '''{}, RS.{} Withdrawal Successfully'''.format(i[0],amt)
                                                            messagebox.showinfo("Money Withdraw !", m)
                                            
                                            except:
                                                messagebox.showwarning("Failed","Error !")
                                                conn.rollback()
                                        else:
                                            E1.delete(0,'end')
                                            E1.insert(0,'enter amount here')
                                            messagebox.showinfo("imformation",'''Sorry !
Insufficient Balance in your Acount
please Enter Amount within Your Balance Limit''')
                                            
                                    else:
                                        
                                        messagebox.showinfo("imformation",'''Dear User !
Entered Amount Should be Multiple of 500
please Enter Your Amount Again''')
                                else:
                                    messagebox.showwarning("warning","Invalid Amount Try again")
                            else:
                                messagebox.showinfo("Withdraw Amount","Please Enter Your Amount You want to Withdraw")
                except:
                    E1.delete(0,'end')
                    E1.insert(0,'enter amount here')
                    messagebox.showinfo("Withdraw Amount","Error ! Please enter a valid amount")

                
            L1=Label(f4,text="Amount",font=("arial",15,"bold"))
            L1.grid(row=0,column=0)
            L1=Label(f4,text="       ",font=("arial",15,"bold"),bg="grey")
            L1.grid(row=0,column=1)
            E1=Entry(f4,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
            E1.grid(row=0,column=2)
            E1.insert(0,'enter amount here')
            B1=Button(f4,text="Submit",font=("arial",10,"bold"),bg="grey",fg="white",bd=10,padx=40,relief = GROOVE,activebackground="red",command=execute_withdraw)
            B1.grid(row=2,column=2)
        global img
        atm_5=Tk()
        atm_5.title("Withdraw")
        atm_5.geometry("1366x768")
        atm_5.configure(background="Light grey")

        #path="C:/Users/mayan/Desktop/Python/ATM PROJECT FRAMES/img1.gif"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(atm_5, image = img)
        panel.place(x=0,y=0)

        f1=Frame(atm_5,height=800,width=400,relief="raise",bd=5,bg="grey")
        f1.pack(side=TOP)
        L1=Label(f1,text="Please Choose Your Account Type",font=("arial",25,"bold"))
        L1.grid(columnspan=2)

        f2=Frame(atm_5,height=800,width=400,relief="raise",bd=5,bg="grey")
        f2.pack(side=RIGHT)
        L2=Label(f2,text="",bg="grey")
        L2.grid(row=1,column=0)        
        B1=Button(f2,text="CURRENT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=59,relief = GROOVE,activebackground="red",command=call_centrywin)
        B2=Button(f2,text="SAVING",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=70,relief = GROOVE,activebackground="red",command=call_sentrywin)

        f3=Frame(atm_5,height=800,width=400,relief="raise",bd=5,bg="grey")
        f3.pack(side=LEFT)
        L3=Label(f3,text="",bg="grey")
        L3.grid(row=1,column=0)
        B3=Button(f3,text="BACK",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=70,relief = GROOVE,activebackground="red",command=openwin)
        B4=Button(f3,text="QUIT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=72,relief = GROOVE,activebackground="red",command=quitwin)
        B1.grid(row=0,column=0)
        B2.grid(row=2,column=0)
        B3.grid(row=0,column=0)
        B4.grid(row=2,column=0)

        f4=Frame(atm_5,height=0,width=0,relief="raise",bd=5,bg="grey")
        f4.pack(side=TOP)

        f5=Frame(atm_5,height=0,width=0,relief="flat",bd=5,bg="grey")
        f5.pack(side=TOP)
        
        f6=Frame(atm_5,height=0,width=0,relief="flat",bd=5,bg="grey")
        f6.pack(side=TOP)

        atm_5.mainloop()

def BalCheck():
        def openwin():
                atm_6.destroy()
                call_MainWindow()
            
        def quitwin():
            messagebox.showinfo("Exit","Thanks for using our ATM Service")
            atm_6.destroy()
        def centrywin():
            actype=False
            global acno
            ac_type='CURRENT'
            acc_list=[]
            for i in conn.execute("select name,balance,pin from atm where ac_type = ?",(ac_type,)):
                if i[2]==pin:
                    actype=True
                    acc_list.append("{}".format(i[0]))
                    acc_list.append("{}".format(i[1]))
                    text=acc_list[0]+",Your Current Account Balance is Rs."+acc_list[1]
                    L1=Label(f4,text=text,font="arial")
                    L1.grid(row =0,column=0)
            for i in conn.execute("select name,balance,ac_no from atm where ac_type = ?",(ac_type,)):
                if i[2]==acno:
                    actype=True
                    m='''{},
Your Current Account Balance is Rs.{}'''.format(i[0],i[1])
                    messagebox.showinfo("Current Account Balance",m)
            
            
            if not actype:
                messagebox.showinfo("Balance Enquiry","Sorry ! You do not have Current Account")
            
        def sentrywin():
            actype=False
            global acno
            ac_type='SAVING'
            acc_list=[]
            for i in conn.execute("select name,balance,ac_no from atm where ac_type = ?",(ac_type,)):
                if i[2]==acno:
                    actype=True
                    acc_list.append("{}".format(i[0]))
                    acc_list.append("{}".format(i[1]))
                    text=acc_list[0]+",Your Saving Account Balance is Rs."+acc_list[1]
                    L1=Label(f4,text=text,font="arial")
                    L1.grid(row =0,column=0)
            for i in conn.execute("select name,balance,ac_no from atm where ac_type = ?",(ac_type,)):
                if i[2]==acno:
                    actype=True
                    m='''{},
Your Saving Account Balance is Rs.{}'''.format(i[0],i[1])
                    messagebox.showinfo("Savings Account Balance",m)
            
                    
            if not actype:
                messagebox.showinfo("Balance Enquiry","Sorry ! You do not have Saving Account")
        global img
        atm_6=Tk()
        atm_6.title("Balance Check")
        atm_6.geometry("1366x768")
        atm_6.configure(background="Light grey")

        #path="C:/Users/mayan/Desktop/Python/ATM PROJECT FRAMES/img1.gif"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(atm_6, image = img)
        panel.place(x=0,y=0)

        f1=Frame(atm_6,height=800,width=400,relief="raise",bd=5,bg="grey")
        f1.pack(side=TOP)
        L1=Label(f1,text="Please Choose Your Account Type",font=("arial",25,"bold"))
        L1.grid(columnspan=2)

        f2=Frame(atm_6,height=800,width=400,relief="raise",bd=5,bg="grey")
        f2.pack(side=RIGHT)
        L2=Label(f2,text="",bg="grey")
        L2.grid(row=1,column=0)        
        B1=Button(f2,text="CURRENT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=59,relief = GROOVE,activebackground="red",command=centrywin)
        B2=Button(f2,text="SAVING",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=70,relief = GROOVE,activebackground="red",command=sentrywin)

        f3=Frame(atm_6,height=800,width=400,relief="raise",bd=5,bg="grey")
        f3.pack(side=LEFT)
        L3=Label(f3,text="",bg="grey")
        L3.grid(row=1,column=0)
        B3=Button(f3,text="BACK",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=70,relief = GROOVE,activebackground="red",command=openwin)
        B4=Button(f3,text="QUIT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=72,relief = GROOVE,activebackground="red",command=quitwin)
        B1.grid(row=0,column=0)
        B2.grid(row=2,column=0)
        B3.grid(row=0,column=0)
        B4.grid(row=2,column=0)

        f4=Frame(atm_6,height=0,width=0,relief="flat",bd=5,bg="grey")
        f4.pack(side=TOP)

        atm_6.mainloop()

def Deposit():
        def call_centrywin():
            ac=False
            global acno
            ac_type='CURRENT'
            for i in conn.execute("select ac_type from atm where ac_no=?",(acno,)):
                if i[0]==ac_type:
                    ac=True
                    centrywin()
                else:
                    pass
            if not ac:
                    messagebox.showinfo("imformation",'''Dear User !
you do not have Current Account''')
        def call_sentrywin():
            ac=False
            global acno
            ac_type='SAVING'
            for i in conn.execute("select ac_type from atm where ac_no=?",(acno,)):
                if i[0]==ac_type:
                    ac=True
                    sentrywin()
                else:
                    pass
            if not ac:
                    messagebox.showinfo("imformation",'''Dear User !
you do not have Saving Account''')
        def openwin():
            atm_7.destroy()
            call_MainWindow()
            
        def quitwin():
            messagebox.showinfo("Exit","Thanks for using our ATM Service")
            atm_7.destroy()
        def centrywin():
            def execute_deposit():
                global bal
                global acno
                try:
                            amt=E1.get()
                            if amt!='enter amount here':
                                amt=int(E1.get())
                                if amt>0:
                                    if amt%500==0:
                                        try:
                                                conn.execute("update atm set balance = balance + ? where ac_no = ?",(amt,acno))
                                                conn.commit()
                                                acc_list=[]
                                                for i in conn.execute("select name,balance,ac_no from atm where ac_no = ?",(acno,)):
                                                    bal=i[1]
                                                    if i[2]==acno:
                                                        acc_list.append("{}".format(i[0]))
                                                        text='''{}, RS.{} Deposited Successfully'''.format(i[0],amt)
                                                        L2=Label(f6,text=text,font="arial")
                                                        L2.grid(row =0,column=0)
                                                        E1.delete(0,'end')
                                                        E1.insert(0,'enter amount here')
                                                for i in conn.execute("select name,balance,ac_no from atm where ac_no = ?",(acno,)):
                                                    if i[2]==acno:
                                                            m = '''{}, RS.{} Deposited Successfully'''.format(i[0],amt)
                                                            messagebox.showinfo("Money Deposite !", m)
                                            
                                        except:
                                            messagebox.showwarning("Failed","Error !")
                                            conn.rollback()
                                            
                                    else:
                                        
                                        messagebox.showinfo("imformation",'''Dear User !
Entered Amount Should be Multiple of 500
please Enter Your Amount Again''')
                                else:
                                    messagebox.showwarning("warning","Invalid Amount Try again")
                            else:
                                messagebox.showinfo("Deposite Amount","Please Enter Your Amount You want to Deposit")
                except:
                    E1.delete(0,'end')
                    E1.insert(0,'enter amount here')
                    messagebox.showinfo("Deposite Amount","Error ! Please enter a valid amount")

                
            L1=Label(f4,text="Amount",font=("arial",15,"bold"))
            L1.grid(row=0,column=0)
            L1=Label(f4,text="       ",font=("arial",15,"bold"),bg="grey")
            L1.grid(row=0,column=1)
            E1=Entry(f4,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
            E1.grid(row=0,column=2)
            E1.insert(0,'enter amount here')
            B1=Button(f4,text="Submit",font=("arial",10,"bold"),bg="grey",fg="white",bd=10,padx=40,relief = GROOVE,activebackground="red",command=execute_deposit)
            B1.grid(row=2,column=2)
        def sentrywin():
            def execute_deposit():
                global bal
                global acno
                try:
                            amt=E1.get()
                            if amt!='enter amount here':
                                amt=int(E1.get())
                                if amt>0:
                                    if amt%500==0:
                                        try:
                                                conn.execute("update atm set balance = balance + ? where ac_no = ?",(amt,acno))
                                                conn.commit()
                                                acc_list=[]
                                                for i in conn.execute("select name,balance,ac_no from atm where ac_no = ?",(acno,)):
                                                    bal=i[1]
                                                    if i[2]==acno:
                                                        acc_list.append("{}".format(i[0]))
                                                        text='''{}, RS.{} Deposited Successfully'''.format(i[0],amt)
                                                        L2=Label(f6,text=text,font="arial")
                                                        L2.grid(row =0,column=0)
                                                        E1.delete(0,'end')
                                                        E1.insert(0,'enter amount here')
                                                for i in conn.execute("select name,balance,ac_no from atm where ac_no = ?",(acno,)):
                                                    if i[2]==acno:
                                                            m = '''{}, RS.{} Deposited Successfully'''.format(i[0],amt)
                                                            messagebox.showinfo("Money Deposite !", m)
                                            
                                        except:
                                            messagebox.showwarning("Failed","Error !")
                                            conn.rollback()
                                            
                                    else:
                                        
                                        messagebox.showinfo("imformation",'''Dear User !
Entered Amount Should be Multiple of 500
please Enter Your Amount Again''')
                                else:
                                    messagebox.showwarning("warning","Invalid Amount Try again")
                            else:
                                messagebox.showinfo("Deposite Amount","Please Enter Your Amount You want to Deposit")
                    
                except:
                    E1.delete(0,'end')
                    E1.insert(0,'enter amount here')
                    messagebox.showinfo("Deposite Amount","Error ! Please enter a valid amount")

                
            L1=Label(f4,text="Amount",font=("arial",15,"bold"))
            L1.grid(row=0,column=0)
            L1=Label(f4,text="       ",font=("arial",15,"bold"),bg="grey")
            L1.grid(row=0,column=1)
            E1=Entry(f4,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
            E1.grid(row=0,column=2)
            E1.insert(0,'enter amount here')
            B1=Button(f4,text="Submit",font=("arial",10,"bold"),bg="grey",fg="white",bd=10,padx=40,relief = GROOVE,activebackground="red",command=execute_deposit)
            B1.grid(row=2,column=2)
        global img
        atm_7=Tk()
        atm_7.title("Deposite")
        atm_7.geometry("1366x768")
        atm_7.configure(background="Light grey")

        #path="C:/Users/mayan/Desktop/Python/ATM PROJECT FRAMES/img1.gif"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(atm_7, image = img)
        panel.place(x=0,y=0)

        f1=Frame(atm_7,height=800,width=400,relief="raise",bd=5,bg="grey")
        f1.pack(side=TOP)
        L1=Label(f1,text="Please Choose Your Account Type",font=("arial",25,"bold"))
        L1.grid(columnspan=2)

        f2=Frame(atm_7,height=800,width=400,relief="raise",bd=5,bg="grey")
        f2.pack(side=RIGHT)
        L2=Label(f2,text="",bg="grey")
        L2.grid(row=1,column=0)        
        B1=Button(f2,text="CURRENT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=59,relief = GROOVE,activebackground="red",command=call_centrywin)
        B2=Button(f2,text="SAVING",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=70,relief = GROOVE,activebackground="red",command=call_sentrywin)

        f3=Frame(atm_7,height=800,width=400,relief="raise",bd=5,bg="grey")
        f3.pack(side=LEFT)
        L3=Label(f3,text="",bg="grey")
        L3.grid(row=1,column=0)
        B3=Button(f3,text="BACK",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=70,relief = GROOVE,activebackground="red",command=openwin)
        B4=Button(f3,text="QUIT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=72,relief = GROOVE,activebackground="red",command=quitwin)
        B1.grid(row=0,column=0)
        B2.grid(row=2,column=0)
        B3.grid(row=0,column=0)
        B4.grid(row=2,column=0)

        f4=Frame(atm_7,height=0,width=0,relief="raise",bd=5,bg="grey")
        f4.pack(side=TOP)

        f5=Frame(atm_7,height=0,width=0,relief="flat",bd=5,bg="grey")
        f5.pack(side=TOP)
        
        f6=Frame(atm_7,height=0,width=0,relief="flat",bd=5,bg="grey")
        f6.pack(side=TOP)

        atm_7.mainloop()

def Transfer():
        def call_centrywin():
            ac=False
            global acno
            ac_type='CURRENT'
            for i in conn.execute("select ac_type from atm where ac_no=?",(acno,)):
                if i[0]==ac_type:
                    ac=True
                    centrywin()
                else:
                    pass
            if not ac:
                    messagebox.showinfo("imformation",'''Dear User !
you do not have Current Account''')
        def call_sentrywin():
            ac=False
            global acno
            ac_type='SAVING'
            for i in conn.execute("select ac_type from atm where ac_no=?",(acno,)):
                if i[0]==ac_type:
                    ac=True
                    sentrywin()
                else:
                    pass
            if not ac:
                    messagebox.showinfo("imformation",'''Dear User !
you do not have Saving Account''')
        def openwin():
            atm_8.destroy()
            call_MainWindow()
            
        def quitwin():
            messagebox.showinfo("Exit","Thanks for using our ATM Service")
            atm_8.destroy()
        def centrywin():

            def call_trans():
                try:
                    global acno
                    global Name
                    ac_no=E1.get()
                    amt=E2.get()
                    if ac_no!='enter account no. here':
                        ac_no=int(E1.get())
                        if ac_no>=100000000 and ac_no<=1000000000000000000:
                            if amt!='enter amount here':
                                amt=int(E2.get())
                                if amt>0:
                                    if amt%100==0:
                                        try:
                                            ac=False
                                            for i in conn.execute("select ac_no from atm"):
                                                if i[0]==ac_no:
                                                    ac=True
                                                    conn.execute("update atm set balance=balance + ? where ac_no = ?",(amt,ac_no))
                                                    conn.execute("update atm set balance = balance - ? where ac_no = ?",(amt,acno))
                                                    conn.commit()
                                                    for i in conn.execute("select balance from atm where ac_no = ?",(acno,)):
                                                        global bal
                                                        bal=i[0]
                                                
                                                    m="{} Rs.{}, Successfully Transfered to Account No. '{}'".format(Name,amt,ac_no)
                                                    L1=Label(f5,text=m,font=("arial",15,"bold"))
                                                    L1.grid(row=0 ,column=0)
                                                    E1.delete(0,'end')
                                                    E1.insert(0,'enter account no. here')
                                                    E2.delete(0,'end')
                                                    E2.insert(0,'enter amount here')
                                                    messagebox.showinfo("Money Transfer",m)
                                            if not ac:
                                                    E1.delete(0,'end')
                                                    E1.insert(0,'enter account no. here')
                                                    messagebox.showinfo("Money Transfer","Account number not Exist !")
                                        except:
                                            conn.rollback()
                                            conn.close()
                                            E1.delete(0,'end')
                                            E1.insert(0,'enter account no. here')
                                            messagebox.showinfo("Money Transfer","Error !")
                                    else:
                                       messagebox.showinfo("imformation",'''Dear User !
Entered Amount Should be Multiple of 100
please Enter Your Amount Again''')
                                else:
                                    messagebox.showinfo("Money Transfer","Invalid amount")
                                
                            else:
                                E2.delete(0,'end')
                                E2.insert(0,'enter amount here')
                                messagebox.showinfo("Money Transfer","Please enter amount")
                        else:
                            E1.delete(0,'end')
                            E1.insert(0,'enter account no. here')
                            messagebox.showwarning("Money Transfer","Invalid account number")
                    else:
                        messagebox.showinfo("Money Transfer","Please enter receiver's account number")
                except:
                    E1.delete(0,'end')
                    E1.insert(0,'enter account no. here')
                    E2.delete(0,'end')
                    E2.insert(0,'enter amount here')
                    messagebox.showwarning("Money Transfer","Invalid Entries")
                    


            L1=Label(f4,text="Please Enter Receiver Account Number",font=("arial",12,"bold"))
            L1.grid(columnspan=3)
            L2=Label(f4,text="Account No.",font=("arial",15,"bold"))
            L2.grid(row=1,column=0)
            L3=Label(f4,text="       ",font=("arial",15,"bold"),bg="grey")
            L3.grid(row=1,column=1)
            E1=Entry(f4,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
            E1.grid(row=1,column=2)
            E1.insert(0,'enter account no. here')
            L3=Label(f4,text="       ",font=("arial",15,"bold"),bg="grey")
            L3.grid(row=2,column=0)
            L4=Label(f4,text="Amount",font=("arial",15,"bold"))
            L4.grid(row=3,column=0)
            E2=Entry(f4,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
            E2.grid(row=3,column=2)
            E2.insert(0,'enter amount here')
            L5=Label(f4,text="       ",font=("arial",15,"bold"),bg="grey")
            L5.grid(row=4,column=2)
            B1=Button(f4,text="Submit",font=("arial",10,"bold"),bg="grey",fg="white",bd=10,padx=40,relief = GROOVE,activebackground="red",command=call_trans)
            B1.grid(row=5,column=2)

        def sentrywin():

            def call_trans():
                try:
                    global acno
                    global Name
                    ac_no=E1.get()
                    amt=E2.get()
                    if ac_no!='enter account no. here':
                        ac_no=int(E1.get())
                        if ac_no>=100000000 and ac_no<=1000000000000000000:
                            if amt!='enter amount here':
                                amt=int(E2.get())
                                if amt>0:
                                    if amt%100==0:
                                        try:
                                            ac=False
                                            for i in conn.execute("select ac_no from atm"):
                                                if i[0]==ac_no:
                                                    ac=True
                                                    conn.execute("update atm set balance=balance + ? where ac_no = ?",(amt,ac_no))
                                                    conn.execute("update atm set balance = balance - ? where ac_no = ?",(amt,acno))
                                                    conn.commit()
                                                    for i in conn.execute("select balance from atm where ac_no = ?",(acno,)):
                                                        global bal
                                                        bal=i[0]
                                                
                                                    m="{} Rs.{}, Successfully Transfered to Account No. '{}'".format(Name,amt,ac_no)
                                                    L1=Label(f5,text=m,font=("arial",15,"bold"))
                                                    L1.grid(row=0 ,column=0)
                                                    E1.delete(0,'end')
                                                    E1.insert(0,'enter account no. here')
                                                    E2.delete(0,'end')
                                                    E2.insert(0,'enter amount here')
                                                    messagebox.showinfo("Money Transfer",m)
                                            if not ac:
                                                    E1.delete(0,'end')
                                                    E1.insert(0,'enter account no. here')
                                                    messagebox.showinfo("Money Transfer","Account number not Exist !")
                                        except:
                                            conn.rollback()
                                            conn.close()
                                            E1.delete(0,'end')
                                            E1.insert(0,'enter account no. here')
                                            messagebox.showinfo("Money Transfer","Error !")
                                    else:
                                       messagebox.showinfo("imformation",'''Dear User !
Entered Amount Should be Multiple of 100
please Enter Your Amount Again''')
                                else:
                                    messagebox.showinfo("Money Transfer","Invalid amount")
                                
                            else:
                                E2.delete(0,'end')
                                E2.insert(0,'enter amount here')
                                messagebox.showinfo("Money Transfer","Please enter amount")
                        else:
                            E1.delete(0,'end')
                            E1.insert(0,'enter account no. here')
                            messagebox.showwarning("Money Transfer","Invalid account number")
                    else:
                        messagebox.showinfo("Money Transfer","Please enter receiver's account number")
                except:
                    E1.delete(0,'end')
                    E1.insert(0,'enter account no. here')
                    E2.delete(0,'end')
                    E2.insert(0,'enter amount here')
                    messagebox.showwarning("Money Transfer","Invalid Entries")
                    


            L1=Label(f4,text="Please Enter Receiver Account Number",font=("arial",12,"bold"))
            L1.grid(columnspan=3)
            L2=Label(f4,text="Account No.",font=("arial",15,"bold"))
            L2.grid(row=1,column=0)
            L3=Label(f4,text="       ",font=("arial",15,"bold"),bg="grey")
            L3.grid(row=1,column=1)
            E1=Entry(f4,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
            E1.grid(row=1,column=2)
            E1.insert(0,'enter account no. here')
            L3=Label(f4,text="       ",font=("arial",15,"bold"),bg="grey")
            L3.grid(row=2,column=0)
            L4=Label(f4,text="Amount",font=("arial",15,"bold"))
            L4.grid(row=3,column=0)
            E2=Entry(f4,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
            E2.grid(row=3,column=2)
            E2.insert(0,'enter amount here')
            L5=Label(f4,text="       ",font=("arial",15,"bold"),bg="grey")
            L5.grid(row=4,column=2)
            B1=Button(f4,text="Submit",font=("arial",10,"bold"),bg="grey",fg="white",bd=10,padx=40,relief = GROOVE,activebackground="red",command=call_trans)
            B1.grid(row=5,column=2)

        global img
        atm_8=Tk()
        atm_8.title("Transfer")
        atm_8.geometry("1366x768")
        atm_8.configure(background="Light grey")

        #path="C:/Users/mayan/Desktop/Python/ATM PROJECT FRAMES/img1.gif"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(atm_8, image = img)
        panel.place(x=0,y=0)

        f1=Frame(atm_8,height=800,width=400,relief="raise",bd=5,bg="grey")
        f1.pack(side=TOP)
        L1=Label(f1,text="Please Choose Your Account Type",font=("arial",25,"bold"))
        L1.grid(columnspan=2)

        f2=Frame(atm_8,height=800,width=400,relief="raise",bd=5,bg="grey")
        f2.pack(side=RIGHT)
        L2=Label(f2,text="",bg="grey")
        L2.grid(row=1,column=0)        
        B1=Button(f2,text="CURRENT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=59,relief = GROOVE,activebackground="red",command=call_centrywin)
        B2=Button(f2,text="SAVING",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=70,relief = GROOVE,activebackground="red",command=call_sentrywin)

        f3=Frame(atm_8,height=800,width=400,relief="raise",bd=5,bg="grey")
        f3.pack(side=LEFT)
        L3=Label(f3,text="",bg="grey")
        L3.grid(row=1,column=0)
        B3=Button(f3,text="BACK",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=70,relief = GROOVE,activebackground="red",command=openwin)
        B4=Button(f3,text="QUIT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=72,relief = GROOVE,activebackground="red",command=quitwin)
        B1.grid(row=0,column=0)
        B2.grid(row=2,column=0)
        B3.grid(row=0,column=0)
        B4.grid(row=2,column=0)

        f5=Frame(atm_8,height=0,width=0,relief="flat",bd=5,bg="grey")
        f5.pack(side=TOP)
        
        f4=Frame(atm_8,height=0,width=0,relief="raise",bd=5,bg="grey")
        f4.pack(side=TOP)

        atm_8.mainloop()
    
def call_MainWindow():
    def update_pin():
        def update():
            global p
            global acno
            cpin=E1.get()
            npin=E2.get()
            cnpin=E3.get()
            try:
                if cpin!='enter current pin here':
                    cpin=int(E1.get())
                    if npin!='enter new pin here':
                        npin=int(E2.get())
                        if cnpin!='enter confirm pin here':
                            cnpin=int(E3.get())
                            if cpin>1000 and npin>1000 and cnpin>1000:
                                if cpin==p:
                                    if npin!=cpin:
                                        if npin==cnpin:
                                            try:
                                                conn.execute("update atm set pin = ? where ac_no=?",(cnpin,acno))
                                                conn.commit()
                                                p=cnpin
                                                E1.delete(0,'end')
                                                E1.insert(0,'enter current pin here')
                                                E2.delete(0,'end')
                                                E2.insert(0,'enter new pin here')
                                                E3.delete(0,'end')
                                                E3.insert(0,'enter confirm pin here')
                                                messagebox.showinfo("PIN changed","""Dear User !
PIN Updated Successfully""")
                                            except:
                                                conn.rollback()
                                                messagebox.showwarning("Change PIN","Error ! Please try again")
                                        else:
                                            messagebox.showwarning("Change PIN","PIN not match with Comfirm PIN Please Enter PIN again")
                                    else:
                                        messagebox.showwarning("Change PIN","""Dear User !
Both Current and New PIN are Same
Please Enter New PIN other than Current PIN again""")
                                else:
                                    messagebox.showwarning("Change PIN","""Wrong Current PIN""")
                            else:
                                messagebox.showwarning("Change PIN","""pin should be of 4 digits or greater""")
                        else:
                            E3.delete(0,'end')
                            E3.insert(0,'enter comfirm pin here')
                            messagebox.showinfo("PIN change","Please Enter Comfirm PIN")
                    else:
                        E2.delete(0,'end')
                        E2.insert(0,'enter new pin here')
                        messagebox.showinfo("PIN change","Please Enter Your New PIN")
                                                  
                else:
                    E1.delete(0,'end')
                    E1.insert(0,'enter current pin here')
                    messagebox.showinfo("PIN change","Please Enter Your Current PIN")
            except:
                E1.delete(0,'end')
                E1.insert(0,'enter current pin here')
                E2.delete(0,'end')
                E2.insert(0,'enter new pin here')
                E3.delete(0,'end')
                E3.insert(0,'enter confirm pin here')
                messagebox.showwarning("Error ! ","Error ! Invalid Entery of PIN Numbers")
        
        L1=Label(f5,text="Current PIN",font=("arial",15,"bold"))
        L1.grid(row=0,column=0)
        L2=Label(f5,text="                   ",font=("arial",15,"bold"),bg="grey")
        L2.grid(row=0,column=1)
        E1=Entry(f5,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
        E1.grid(row=0,column=2)
        E1.insert(0,'enter current pin here')
        L3=Label(f5,text="       ",font=("arial",15,"bold"),bg="grey")
        L3.grid(row=1,column=0)
        L4=Label(f5,text="New PIN",font=("arial",15,"bold"),padx=20)
        L4.grid(row=2,column=0)
        E2=Entry(f5,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
        E2.grid(row=2,column=2)
        E2.insert(0,'enter new pin here')
        L5=Label(f5,text="       ",font=("arial",15,"bold"),bg="grey")
        L5.grid(row=3,column=0)
        L6=Label(f5,text="Confirm PIN",font=("arial",15,"bold"))
        L6.grid(row=4,column=0)
        E3=Entry(f5,font=("arial",15,"bold"),bg="white",fg="black",bd=5)
        E3.grid(row=4,column=2)
        E3.insert(0,'enter confirm pin here')
        L7=Label(f5,text="       ",font=("arial",15,"bold"),bg="grey")
        L7.grid(row=5,column=2)
        B1=Button(f5,text="Submit",font=("arial",10,"bold"),bg="grey",fg="white",bd=10,padx=40,relief = GROOVE,activebackground="red",command=update)
        B1.grid(row=6,column=2)
    
    def Ac_Details():
        
        acc_list=[]
        for i in conn.execute("select name,ac_no,ac_type,p_no,email,age,gender,balance from atm where ac_no = ?",(acno,)):
            acc_list.append("Name:  {}".format(i[0]))
            acc_list.append("Account no.: {}".format(i[1]))
            acc_list.append("Account type: {}".format(i[2]))
            acc_list.append("Phone NO.: {}".format(i[3]))
            acc_list.append("E-Mail: {}".format(i[4]))
            acc_list.append("Age: {}".format(i[5]))
            acc_list.append("Gender: {}".format(i[6]))
            text = acc_list[0]+"\n"+acc_list[1]+"\n"+acc_list[2]+"\n"+acc_list[3]+"\n"+acc_list[4]+"\n"+acc_list[5]+"\n"+acc_list[6]
            L1=Label(f4,text=text,font="arial")
            L1.grid(row=0,column=0)
        for i in conn.execute("select name,ac_no,ac_type,p_no,email,age,gender from atm where ac_no = ?",(acno,)):
            m='''Name:  {}
Account no.: {}
Account type: {}
Phone NO.: {}
E-Mail: {}
Age: {}
Gender: {}'''.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
        messagebox.showinfo("Account Details",m)

    def Call_Transfer():
        atm_4.destroy()
        Transfer()
    
    def Call_Deposit():
        atm_4.destroy()
        Deposit()
    
    def Call_BalCheck():
        atm_4.destroy()
        BalCheck()

    def openwin():
        atm_4.destroy()
        call_StartWindow()
        
    def openwin2():
        atm_4.destroy()
        call_withdraw()
        
    def quitwin():
        messagebox.showinfo("information","Thanks for using our ATM Service")
        atm_4.destroy()
    global img
    atm_4=Tk()
    atm_4.title("Transactional Menu")
    atm_4.geometry("1366x768")
    atm_4.configure(background="light grey")

    #path="C:/Users/mayan/Desktop/Python/ATM PROJECT FRAMES/img1.gif"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(atm_4, image = img)
    panel.place(x=0,y=0)

    f1=Frame(atm_4,height=800,width=400,relief="raise",bd=5,bg="grey")
    f1.pack(side=TOP)
    L1=Label(f1,text="Select Your Transaction",font=("arial",25,"bold"))
    L1.grid(columnspan=2)

    f2=Frame(atm_4,height=800,width=400,relief="raise",bd=5,bg="grey")
    f2.pack(side=RIGHT)
    B1=Button(f2,text="WITHDRAWAL",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=40,relief = GROOVE,activebackground="red",command=openwin2)
    B1.grid(row=0,column=0)
    L2=Label(f2,text="",bg="grey")
    L2.grid(row=1,column=0)
    B2=Button(f2,text="BALANCE CHECK",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=25,relief = GROOVE,activebackground="red",command=Call_BalCheck)
    B2.grid(row=2,column=0)
    L3=Label(f2,text="",bg="grey")
    L3.grid(row=3,column=0)
    B3=Button(f2,text="DEPOSIT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=65,relief = GROOVE,activebackground="red",command=Call_Deposit)
    B3.grid(row=4,column=0)
    L4=Label(f2,text="",bg="grey")
    L4.grid(row=5,column=0)
    B4=Button(f2,text="TRANSFER",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=55,relief = GROOVE,activebackground="red",command=Call_Transfer)
    B4.grid(row=6,column=0)

    f3=Frame(atm_4,height=800,width=400,relief="raise",bd=5,bg="grey")
    f3.pack(side=LEFT)
    L5=Label(f3,text="",bg="grey")
    L5.grid(row=1,column=0)
    B5=Button(f3,text="CHANGE PIN",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=37,relief = GROOVE,activebackground="red",command=update_pin)
    B5.grid(row=2,column=0)
    L6=Label(f3,text="",bg="grey")
    L6.grid(row=3,column=0)
    B6=Button(f3,text="BACK",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=70,relief = GROOVE,activebackground="red",command=openwin)
    B6.grid(row=4,column=0)
    L7=Label(f3,text="",bg="grey")
    L7.grid(row=5,column=0)
    B7=Button(f3,text="QUIT",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=74,relief = GROOVE,activebackground="red",command=quitwin)
    B7.grid(row=6,column=0)
    B8=Button(f3,text="ACCOUNT DETAIL",font=("arial",15,"bold"),bg="grey",fg="white",bd=10,padx=10,relief = GROOVE,activebackground="red",command=Ac_Details)
    B8.grid(row=0,column=0)

    f4=Frame(atm_4,height=0,width=0,relief="flat",bd=5,bg="grey")
    f4.pack(side=TOP)

    f5=Frame(atm_4,height=0,width=0,relief="raise",bd=5,bg="grey")
    f5.pack(side=TOP)

    atm_4.mainloop()

call_StartWindow()
