from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install Pillow
from PIL import Image
from tkinter import messagebox
import mysql.connector
import random
import time
import datetime
from hotel import HotelManagementSystem



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0") 

        self.bg=ImageTk.PhotoImage(file="/Users/riya/Desktop/ Hotel Management System/images/ff1.jpeg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=1,y=1,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        

        img1=Image.open ("/Users/riya/Desktop/ Hotel Management System/images/login.jpeg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimg1,background="Black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)





        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="White",background="Black")
        get_str.place(x=100,y=100)

        #label
        username=Label(frame,bd=2,text="Username",font=("times new roman",15,"bold"),fg="White",background="Black")
        username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        password=Label(frame,bd=2,text="Password",font=("times new roman",15,"bold"),fg="White",background="Black")
        password.place(x=70,y=225)
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        



        img2=Image.open ("/Users/riya/Desktop/ Hotel Management System/images/pass1.jpeg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimg2,background="Black", borderwidth=0)
        lblimg2.place(x=650, y=395, width=25, height=25)


        



        img3=Image.open ("/Users/riya/Desktop/ Hotel Management System/images/icon1.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimg3,background="Black", borderwidth=0)
        lblimg3.place(x=650, y=323, width=25, height=25)


#loginbutton
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="Blue",bg="Yellow",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
 




#register button
        loginregister=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="blue",background="Black",activeforeground="yellow",activebackground="pink")
        loginregister.place(x=20,y=350,width=160)


        #forgetbutton
        loginforget=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="blue",background="Black",activeforeground="yellow",activebackground="pink")
        loginforget.place(x=20,y=370,width=160)

#login window

    def login (self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
              messagebox.showerror("Error","all field required")

        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
              messagebox.showinfo("Success","Welcome ")
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                         self.txtuser.get(),
                                                                                         self.txtpass.get()
             ))
             
             row=my_cursor.fetchone()
             if row!=None:
                  messagebox.showerror("Error","Invalid Username & password")
             else:   
                  open_main=messagebox.askyesno("YesNo","Access only admin")
                  if open_main>0:
                       self.new_window=Toplevel(self.root)
                       self.app=HotelManagementSystem(self.new_window)
                  else:
                       if not open_main:
                            return
                       conn.commit()
                       conn.close()



#==================RESEt password Window
    def reset_pass(self):
         if self.combo_security_Q.get()=="Select":
              messagebox.showerror("Error","Select security Questions",parent=self.root2)
         elif self.txt_security.get()=="":
              messagebox.showerror("Error","Please enter the answer",parent=self.root2)
         elif self.txt_new_pass.get()=="":
              messagebox.showerror("Error","Please enter the new password",parent=self.root2)
         else:
               conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
               my_cursor=conn.cursor()
               query=("Select * from register where email=%s and securityQ=%s and securityA=%s")
               value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
               my_cursor.execute(query,value)
               row=my_cursor.fetchone()
               if row==None:
                    messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
               else:
                    query=("Update register set  password=%s where email=%s")
                    value=(self.txt_new_pass.get(),self.txtuser.get())
                    my_cursor.execute(query,value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info", "Your password has been reset , please login new password",parent=self.root2)
                    self.root2.destroy()
         






#forgetpassword
    def forgot_password_window(self):
         if self.txtuser.get()=="":
              messagebox.showerror("Error","Please Enter the Email address to reset password")
         else:
               conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
               my_cursor=conn.cursor()  
               query=("select * from register where email=%s")
               value=(self.txtuser.get(),)
               my_cursor.execute(query,value)
               row=my_cursor.fetchone()
               #print(row)

               if row==None:
                    messagebox.showerror("My Error," "Please enter the valid user name")
               else:
                    conn.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget password")
                    self.root2.geometry("340x450+610+170")

                    l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),foreground="Blue",background="White")
                    l.place(x=0,y=10,relwidth=1)


                    security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),background="White",foreground="black")
                    security_Q.place(x=50,y=80)
                    self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                    self.combo_security_Q["values"]=("Select","Your Birth Place","Your GirlFriend name","Your Pet Name")
                    self.combo_security_Q.place(x=50,y=110,width=250)
                    self.combo_security_Q.current(0)
            


                    security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),background="White",foreground="black")
                    security_A.place(x=50,y=150)

                    self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                    self.txt_security.place(x=50,y=180,width=250)



                    newpassword=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),background="White",foreground="black")
                    newpassword.place(x=50,y=220)

                    self.txt_new_pass=ttk.Entry(self.root2,font=("times new roman",15))
                    self.txt_new_pass.place(x=50,y=250,width=250)


                    resetbtn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),foreground="Blue",background="yellow")
                    resetbtn.place(x=100,y=290)
 






              #function

    def register_window(self):
         self.new_window=Toplevel(self.root)
         self.app=Register(self.new_window)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("REGISTER")
        self.root.geometry("1600x900+0+0")



        #varibales
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

#bg Image
     
        
        self.background = ImageTk.PhotoImage(file="/Users/riya/Desktop/ Hotel Management System/images/jp.jpeg")
        bg_lbl = Label(self.root, image=self.background)
        bg_lbl.grid(row=0, column=0, sticky="nsew")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #left image======



        self.bg1=ImageTk.PhotoImage(file="/Users/riya/Desktop/ Hotel Management System/images/q1.jpeg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=450,height=550)


        #======Main Frame====
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",background="White")
        register_lbl.place(x=20,y=20)

        #=========Label and entry====
        #ROW!
        framename=Label(frame,text="First Name",font=("times new roman",15,"bold"),background="White")
        framename.place(x=50,y=100)

        frame_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        frame_entry.place(x=50,y=130,width=250)


        l_Name=Label(frame,text="LastName",font=("times new roman",15,"bold"),background="White")
        l_Name.place(x=370,y=100)

        self.txt_l_name=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_l_name.place(x=370,y=130,width=250)

        
#Row2



        contact_no=Label(frame,text="ContactNo",font=("times new roman",15,"bold"),background="White")
        contact_no.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
  


        contact_no=Label(frame,text="Email",font=("times new roman",15,"bold"),background="White")
        contact_no.place(x=370,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_contact.place(x=370,y=200,width=250)



    #Row3

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),background="White",foreground="black")
        security_Q.place(x=50,y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your GirlFriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
   


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),background="White",foreground="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

 #Row4
        
        pasword=Label(frame,text="Password",font=("times new roman",15,"bold"),background="white",foreground="black")
        pasword.place(x=50,y=310)

        self.txt_password=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_password.place(x=50,y=340,width=250)

        confrim_password=Label(frame,text="Confrim Password",font=("times new roman",15,"bold"),background="white",foreground="Black")
        confrim_password.place(x=370,y=310)

        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_password.place(x=370,y=340,width=250)



 #checkbutton
        self.var_check=IntVar()
        self.checkbutton=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbutton.place(x=50,y=380)
        
        
#register button

        img1=Image.open ("/Users/riya/Desktop/ Hotel Management System/images/rgis.jpeg")
        img1 = img1.resize((200, 55), Image.BOX)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1=Button(frame,image=self.photoimg1,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),foreground="White")
        b1.place(x=10,y=420,width=200)
        
       #login button



        img2=Image.open ("/Users/riya/Desktop/ Hotel Management System/images/lg1.jpeg")
        img2 = img2.resize((200, 45), Image.BOX)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1=Button(frame,image=self.photoimg2,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),foreground="White")
        b1.place(x=330,y=420,width=200)



#function Declaration
    def register_data(self):
       if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
             messagebox.showerror("Error","All fields are required")
       elif self.var_pass.get()!=self.var_confpass.get():
             messagebox.showerror("Error","password & confirm password must be same")
       elif self.var_check.get()==0:
             messagebox.showerror("Error","Please agree our terms and conditions") 

       else:
             
       



          conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
          my_cursor=conn.cursor()
          query=("select * from register where email=%s")
          value=(self.var_email.get(),)
          my_cursor.execute(query,value)
          rows=my_cursor.fetchone()
       if rows!=None:
             messagebox.showerror("Error","User already exist, please try another email")
       else:   
             my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                  
                                                                                             self.var_fname.get(),
                                                                                             self.var_lname.get(),
                                                                                             self.var_contact.get(),
                                                                                             self.var_email.get(),
                                                                                             self.var_securityQ.get(),
                                                                                             self.var_SecurityA.get(),
                                                                                             self.var_pass.get()
                                                                                              ))   

                          
                          
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Success","customer has been added") 



if __name__ == "__main__":
        main()
        