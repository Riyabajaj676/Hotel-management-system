from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install Pillow
from PIL import Image
from tkinter import messagebox
import mysql.connector


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




if __name__=="__main__":
            root=Tk()
            app=Register(root)
            root.mainloop()