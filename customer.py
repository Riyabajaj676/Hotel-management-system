from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox



class Cust_win:
        def __init__(self,root):
          self.root = root
          self.root.title("Hotel Management System")  # Corrected usage of title method
          self.root.geometry("1295x550+220+220")


#============Variable===========
          self.var_ref=StringVar()
          x=random.randint(1000,9999)
          self.var_ref.set(str(x))


          self.var_cust_name=StringVar()
          self.var_Mother=StringVar()
          self.var_gender=StringVar()
          self.var_post=StringVar()
          self.var_mobile=StringVar()
          self.var_email=StringVar()
          self.var_nationality=StringVar()
          self.var_address=StringVar()
          self.var_id_Proof=StringVar()
          self.var_id_number=StringVar()





         #============TITLE====================
          lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
          lbl_title.place(x=0,y=0,width=1295,height=50)

         #==============LOGO=====================
          img2=Image.open ("/Users/riya/Desktop/ Hotel Management System/images/gh.jpeg")
          img2 = img2.resize((100, 40), Image.BOX)
          self.photoimg2 = ImageTk.PhotoImage(img2)

        
          lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
          lblimg.place(x=5, y=2, width=230, height=40)

          #============LABEL FRAME========================
          labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",18,"bold"),padx=2,)
          labelframeleft.place(x=5,y=50,width=425,height=490)

          #===========LABELS and ENTRY=================
          #customer_ref
          lbl_cust_ref=Label(labelframeleft,text="Customer Reference",font=("times new roman",12,"bold"),padx=2,pady=6)
          lbl_cust_ref.grid(row=0,column=0,sticky=W)

          entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_ref,font=("arial",13,"bold"),state="readonly")
          entry_ref.grid(row=0,column=1)
          
          #customer name
          cname=Label(labelframeleft,text="Customer Name",font=("aria",12,"bold"),padx=2,pady=6)
          cname.grid(row=1,column=0,sticky=W)

          txtcname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_name,font=("arial",13,"bold"))
          txtcname.grid(row=1,column=1)

          # mother name

          lblmname=Label(labelframeleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=6)
          lblmname.grid(row=2,column=0,sticky=W)

          txtmname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_Mother,font=("arial",13,"bold"))
          txtmname.grid(row=2,column=1)
          #gender combobox

          label_gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
          label_gender.grid(row=3,column=0,sticky=W)
          combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
          combo_gender["value"]=("Male","Female","Other")
          combo_gender.current(0)
          combo_gender.grid(row=3,column=1)



           #postcode
          lblpostcode=Label(labelframeleft,text="Post Code",font=("arial",12,"bold"),padx=2,pady=6)
          lblpostcode.grid(row=4,column=0,sticky=W)

          txtpostcode=ttk.Entry(labelframeleft,width=29,textvariable=self.var_post,font=("arial",13,"bold"))
          txtpostcode.grid(row=4,column=1)
       
         #Mobile number
          lblMobile=Label(labelframeleft,text="Mobile",font=("arial",12,"bold"),padx=2,pady=6)
          lblMobile.grid(row=5,column=0,sticky=W)

          txtMobile=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=("arial",13,"bold"))
          txtMobile.grid(row=5,column=1)
          
          #email
       
          lblEmail=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
          lblEmail.grid(row=6,column=0,sticky=W)

          txtEmail=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("arial",13,"bold"))
          txtEmail.grid(row=6,column=1)
        
        #nationality
          lblNationality=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
          lblNationality.grid(row=7,column=0,sticky=W)
          combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
          combo_nationality["value"]=("Indian","American","British")
          combo_nationality.current(0)
          combo_nationality.grid(row=7,column=1)




          #idproof type combobox
          lblIdProof=Label(labelframeleft,text="Id Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
          lblIdProof.grid(row=8,column=0,sticky=W)
          combo_Id=ttk.Combobox(labelframeleft,textvariable=self.var_id_Proof,font=("arial",12,"bold"),width=27,state="readonly")
          combo_Id["value"]=("Age proof","DrivingLicence","Passport")
          combo_Id.current(0)
          combo_Id.grid(row=8,column=1)






        # id number
          lblIdNumber=Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
          lblIdNumber.grid(row=9,column=0,sticky=W)
          
          txtIdNumber=ttk.Entry(labelframeleft,width=29,textvariable=self.var_id_number,font=("arial",13,"bold"))
          txtIdNumber.grid(row=9,column=1)


       #address

          lblAddress=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
          lblAddress.grid(row=10,column=0,sticky=W)

          txtAddress=ttk.Entry(labelframeleft,width=29,textvariable=self.var_address,font=("arial",13,"bold"))
          txtAddress.grid(row=10,column=1)
   


   #=====Buttons
          btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
          btn_frame.place(x=0,y=400,width=412,height=40)

          btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
          btnAdd.grid(row=0,column=0,padx=1)

          btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
          btnUpdate.grid(row=0,column=1,padx=1)

          btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="Black",fg="gold",width=10)
          btnDelete.grid(row=0,column=2,padx=1)

          btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="brown",fg="gold",width=10)
          btnReset.grid(row=0,column=3,padx=1)


          #=================Table Frame============
          Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",18,"bold"),padx=2,)
          Table_frame.place(x=435,y=50,width=860,height=490)
 
  
          lblSearchBy=Label(Table_frame,text="Search By:",font=("arial",12,"bold"),bg="Red",fg="White")
          lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
          self.search_var=StringVar()
          combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
          combo_Search["value"]=("Mobile","Ref")
          combo_Search.current(0)
          combo_Search.grid(row=0,column=1,padx=2)

          self.txt_search=StringVar()

          txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
          txtSearch.grid(row=0,column=2,padx=2)


          btnSearch=Button(Table_frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=8)
          btnSearch.grid(row=0,column=3,padx=1)

          btnUpdate=Button(Table_frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=8)
          btnUpdate.grid(row=0,column=4,padx=1)


          #=================SHOW DATA TABLE==============
          
          TableDetail_frame=Frame(Table_frame,bd=2,relief=RIDGE)
          TableDetail_frame.place(x=0,y=50,width=860,height=350)

          scroll_x=ttk.Scrollbar(TableDetail_frame,orient=HORIZONTAL)
          scroll_y=ttk.Scrollbar(TableDetail_frame,orient=VERTICAL)

          self.Cust_details_table=ttk.Treeview(TableDetail_frame,columns=("ref","name","Mothername","gender","post","Mobile","Email","Nationality","IdProof","IdNumber","Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
          
          scroll_x.pack(side=BOTTOM,fill=X)
          scroll_y.pack(side=RIGHT,fill=Y)
          self.Cust_details_table.pack(fill=BOTH, expand=True)


          scroll_x.config(command=self.Cust_details_table.xview)
          scroll_y.config(command=self.Cust_details_table.yview)

          self.Cust_details_table.heading("ref",text="Reference No")
          self.Cust_details_table.heading("name",text="Name")
          self.Cust_details_table.heading("Mothername",text="Mother Name")
          self.Cust_details_table.heading("gender",text="Gender")
          self.Cust_details_table.heading("post",text="PostCode")
          self.Cust_details_table.heading("Mobile",text="Mobile")
          self.Cust_details_table.heading("Email",text="Email")
          self.Cust_details_table.heading("Nationality",text="Nationality")
          self.Cust_details_table.heading("IdProof",text="Id Proof")
          self.Cust_details_table.heading("IdNumber",text="Id Number")
          self.Cust_details_table.heading("Address",text="Address")

          self.Cust_details_table["show"]="headings"

          self.Cust_details_table.column("ref",width=100)
          self.Cust_details_table.column("name",width=100)
          self.Cust_details_table.column("Mothername",width=100)
          self.Cust_details_table.column("gender",width=100)
          self.Cust_details_table.column("post",width=100)
          self.Cust_details_table.column("Mobile",width=100)
          self.Cust_details_table.column("Email",width=100)
          self.Cust_details_table.column("Nationality",width=100)
          self.Cust_details_table.column("IdProof",width=100)
          self.Cust_details_table.column("IdNumber",width=100)
          self.Cust_details_table.column("Address",width=100)
          
          self.Cust_details_table.pack(fill=BOTH,expand=1)
          self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
          self.fetch_data()

 #add data
        def add_data(self):
             if self.var_mobile.get()==""or self.var_Mother.get()=="":
                 messagebox.showerror("Error","All fields are required",parent=self.root)
             else:
                     
                     try:
                        
                           conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
                           my_cursor=conn.cursor()
                           my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                             self.var_ref.get(),
                                                                                             self.var_cust_name.get(),
                                                                                             self.var_Mother.get(),
                                                                                             self.var_gender.get(),
                                                                                             self.var_post.get(),
                                                                                             self.var_mobile.get(),
                                                                                             self.var_email.get(),
                                                                                             self.var_nationality.get(),
                                                                                             self.var_id_Proof.get(),
                                                                                             self.var_id_number.get(),
                                                                                             self.var_address.get()
                   ))
                           conn.commit()
                           self.fetch_data()
                           conn.close()
                           

                           messagebox.showinfo("Success","customer has been added")  
                     except Exception as es:
                           messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)

        def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from customer")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
           self.Cust_details_table.delete(*self.Cust_details_table.get_children())
           for i in rows:
                   self.Cust_details_table.insert("",END,values=i)
                   conn.commit()
           conn.close()
#getccursor

        def get_cursor( self,event=""):
                        cursor_row=self.Cust_details_table.focus()
                        content=self.Cust_details_table.item(cursor_row)
                        row=content["values"]



                        self.var_ref.set(row[0]),
                        self.var_cust_name.set(row[1]),
                        self.var_Mother.set(row[2]),
                        self.var_gender.set(row[3]),
                        self.var_post.set(row[4]),
                        self.var_mobile.set(row[5]),
                        self.var_email.set(row[6]),
                        self.var_nationality.set(row[7]),
                        self.var_id_Proof.set(row[8]),
                        self.var_id_number.set(row[9]),
                        self.var_address.set(row[10])

#update

        def update(self):
                                if self.var_mobile.get()=="":
                                      messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
                                else:
                                   conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
                                   my_cursor=conn.cursor()
                                   my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where Ref=%s",(

                                                                                                                                           
                                                                                                                                            self.var_cust_name.get(),
                                                                                                                                            self.var_Mother.get(),
                                                                                                                                            self.var_gender.get(),
                                                                                                                                            self.var_post.get(),
                                                                                                                                            self.var_mobile.get(),
                                                                                                                                            self.var_email.get(),
                                                                                                                                            self.var_nationality.get(),
                                                                                                                                            self.var_id_Proof.get(),
                                                                                                                                            self.var_id_number.get(),
                                                                                                                                            self.var_address.get(),
                                                                                                                                            self.var_ref.get()
                                                                                                                                                         ))
                                                                                                                                                        
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("UPDATES","Customer details has been updated succesfully",parent=self.root)
          
          
          
          
           #delete                                                                      
        def mDelete(self):
                                        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)        
                                        if mDelete>0:                                 
                                                conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
                                                my_cursor=conn.cursor()
                                   #my_cursor.execute("delete customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where Ref=%s",(
                                                query="delete from customer where Ref=%s"
                                                value=(self.var_ref.get(),)
                                                my_cursor.execute(query,value)
                                        else:
                                       
                                         if not mDelete:
                                            return
                                        conn.commit()
                                        self.fetch_data()
                                        conn.close()





        def reset(self):
                

                        #self.var_ref.set(""),
                        self.var_cust_name.set(""),
                        self.var_Mother.set(""),
                        #self.var_gender.set(""),
                        self.var_post.set(""),
                        self.var_mobile.set(""),
                        self.var_email.set(""),
                        #self.var_nationality.set(""),
                        #self.var_id_Proof.set(""),
                        self.var_id_number.set(""),
                        self.var_address.set("")
                        x=random.randint(1000,9999)
                        self.var_ref.set(str(x))



        def search(self):
                                 conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
                                 my_cursor=conn.cursor()
                                 my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
                                 rows=my_cursor.fetchall()
                                 if len(rows)!=0:
                                   self.Cust_details_table.delete(*self.Cust_details_table.get_children())
                                 for i in rows:
                                         self.Cust_details_table.insert("",END,values=i)
                                 conn.commit()
                                 conn.close()



if __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()