from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from time import strptime
from datetime import datetime
import mysql.connector
import random
from tkinter import messagebox

class roombooking:
        def __init__(self,root):
          self.root = root
          self.root.title("Hotel Management System")  # Corrected usage of title method
          self.root.geometry("1295x550+220+220")

          #VAriables
          self.var_contact=StringVar()
          self.var_checkout=StringVar()
          self.var_checkin=StringVar()
          self.var_roomtype=StringVar()
          self.var_roomavailable=StringVar()
          self.var_meal=StringVar()
          self.var_noOfdays=StringVar()
          self.var_paidtax=StringVar()
          self.var_actualtotal=StringVar()
          self.var_total=StringVar()

          lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
          lbl_title.place(x=0,y=0,width=1295,height=50)

         #==============LOGO=====================
          img2=Image.open ("/Users/riya/Desktop/ Hotel Management System/images/gh.jpeg")
          img2 = img2.resize((100, 40), Image.BOX)
          self.photoimg2 = ImageTk.PhotoImage(img2)

        
          lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
          lblimg.place(x=5, y=2, width=230, height=40)

#============LABEL FRAME========================
          labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",18,"bold"),padx=2,)
          labelframeleft.place(x=5,y=50,width=425,height=490)


 #===========LABELS and ENTRY=================
          #customer_ref
          lbl_cust_cont=Label(labelframeleft,text="Customer Contact",font=("times new roman",13,"bold"),padx=2,pady=6)
          lbl_cust_cont.grid(row=0,column=0,sticky=W)

          entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
          entry_contact.grid(row=0,column=1)

#Fetch Data ++++++++++


          btnfetch=Button(labelframeleft,text="Fetch",command=self.Fetch_contact,font=("arial",12,"bold"),bg="black",fg="gold",width=4)
          btnfetch.place(x=330,y=4)



         #Check_in_Date
          check_in_date=Label(labelframeleft,text="Check_in Date :",font=("aria",12,"bold"),padx=2,pady=6)
          check_in_date.grid(row=1,column=0,sticky=W)

          txtcheck=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
          txtcheck.grid(row=1,column=1)



#Check_out_date
          lbl_check_out=Label(labelframeleft,text="Check_Out_Date",font=("arial",12,"bold"),padx=2,pady=6)
          lbl_check_out.grid(row=2,column=0,sticky=W)

          txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
          txt_Check_out.grid(row=2,column=1)

          

#Room Type
          lbl_romm_type=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
          lbl_romm_type.grid(row=3,column=0,sticky=W)
          conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
          my_cursor=conn.cursor()
          my_cursor.execute("select RoomType from Details")
          ide=my_cursor.fetchall()
          combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
          combo_nationality["value"]=ide
          combo_nationality.current(0)
          combo_nationality.grid(row=3,column=1)

#Available Room
          lblRoomAvailable=Label(labelframeleft,text="Available Room",font=("arial",12,"bold"),padx=2,pady=6)
          lblRoomAvailable.grid(row=4,column=0,sticky=W)

          #txtAvailableRoom=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
          #txtAvailableRoom.grid(row=4,column=1)

          conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
          my_cursor=conn.cursor()
          my_cursor.execute("select RoomNo from Details")
          rows=my_cursor.fetchall()
          combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
          combo_nationality["value"]=rows
          combo_nationality.current(0)
          combo_nationality.grid(row=4,column=1)








#Meal
          lblMeal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
          lblMeal.grid(row=5,column=0,sticky=W)

          txt_Meal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
          txt_Meal.grid(row=5,column=1)



#No of Days
          lblNoOfDays=Label(labelframeleft,text="No Of Days",font=("arial",12,"bold"),padx=2,pady=6)
          lblNoOfDays.grid(row=6,column=0,sticky=W)

          txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noOfdays,width=29,font=("arial",13,"bold"))
          txtNoOfDays.grid(row=6,column=1)

#Paid Tax

          lblPaidTax=Label(labelframeleft,text="Paid Tax :",font=("arial",12,"bold"),padx=2,pady=6)
          lblPaidTax.grid(row=7,column=0,sticky=W)

          txtPaidTax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
          txtPaidTax.grid(row=7,column=1)



#Sub Total

          lblSubtotal=Label(labelframeleft,text="Sub Total :",font=("arial",12,"bold"),padx=2,pady=6)
          lblSubtotal.grid(row=8,column=0,sticky=W)

          txtSubtotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
          txtSubtotal.grid(row=8,column=1)



#Total cost

          lbltotalcost=Label(labelframeleft,text="Total Cost :",font=("arial",12,"bold"),padx=2,pady=6)
          lbltotalcost.grid(row=9,column=0,sticky=W)

          txttotalcost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
          txttotalcost.grid(row=9,column=1)

#BILL COST BUTTON
          btnbill=Button(labelframeleft,text="BILL COST",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
          btnbill.grid(row=10,column=0,padx=1)




#BUTTON

          btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
          btn_frame.place(x=0,y=400,width=412,height=40)

          btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
          btnAdd.grid(row=0,column=0,padx=1)

          btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
          btnUpdate.grid(row=0,column=1,padx=1)

          btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="Black",fg="gold",width=10)
          btnDelete.grid(row=0,column=2,padx=1)

          btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="brown",fg="gold",width=8)
          btnReset.grid(row=0,column=3,padx=1)


          img3=Image.open ("/Users/riya/Desktop/ Hotel Management System/images/bed1.jpeg")
          img3 = img3.resize((520, 300), Image.BOX)
          self.photoimg3 = ImageTk.PhotoImage(img3)

        
          lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
          lblimg.place(x=760, y=55, width=520, height=200)



#TABLE FRAME====

          Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",18,"bold"),padx=2,)
          Table_frame.place(x=435,y=280,width=860,height=260)
 
  
          lblSearchBy=Label(Table_frame,text="Search By:",font=("arial",12,"bold"),bg="Red",fg="White")
          lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
          self.search_var=StringVar()
          combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
          combo_Search["value"]=("Contact","Room")
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
          TableDetail_frame.place(x=0,y=50,width=860,height=180)

          scroll_x=ttk.Scrollbar(TableDetail_frame,orient=HORIZONTAL)
          scroll_y=ttk.Scrollbar(TableDetail_frame,orient=VERTICAL)

          self.room_table=ttk.Treeview(TableDetail_frame,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
          
          scroll_x.pack(side=BOTTOM,fill=X)
          scroll_y.pack(side=RIGHT,fill=Y)
          self.room_table.pack(fill=BOTH, expand=True)


          scroll_x.config(command=self.room_table.xview)
          scroll_y.config(command=self.room_table.yview)

          self.room_table.heading("contact",text="Contact")
          self.room_table.heading("checkin",text="Check-in")
          self.room_table.heading("checkout",text="Check-out")
          self.room_table.heading("roomtype",text="Room Type")
          self.room_table.heading("roomavailable",text="Room No")
          self.room_table.heading("meal",text="Meal")
          self.room_table.heading("noOfdays",text="NoOfDays")
          
          self.room_table["show"]="headings"

          self.room_table.column("contact",width=100)
          self.room_table.column("checkin",width=100)
          self.room_table.column("checkout",width=100)
          self.room_table.column("roomtype",width=100)
          self.room_table.column("roomavailable",width=100)
          self.room_table.column("meal",width=100)
          self.room_table.column("noOfdays",width=100)
          self.room_table.pack(fill=BOTH,expand=1)
          self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
          self.fetch_data()

       
#ADD DATA
        def add_data(self):
             if self.var_contact.get()==""or self.var_checkin.get()=="":
                 messagebox.showerror("Error","All fields are required",parent=self.root)
             else:
                     
                     try:
                        
                           conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
                           my_cursor=conn.cursor()
                           my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)" , (
                               
                                                                                              self.var_contact.get(),
                                                                                              self.var_checkin.get(),
                                                                                              self.var_checkout.get(),
                                                                                              self.var_roomtype.get(),
                                                                                              self.var_roomavailable.get(),
                                                                                              self.var_meal.get(),
                                                                                              self.var_noOfdays.get()
                                                                                              
                    
                        ))
                           
                           
                           
                           conn.commit()
                           self.fetch_data()
                           conn.close()
                           

                           messagebox.showinfo("Success","Room Booked")  
                     except Exception as es:
                           messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)

  #========Fetch Data====

        def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from room")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
           self.room_table.delete(*self.room_table.get_children())
           for i in rows:
                   self.room_table.insert("",END,values=i)
                   conn.commit()
           conn.close()

#getcursor
        def get_cursor( self,event=""):
            cursor_row=self.room_table.focus()
            content=self.room_table.item(cursor_row)
            row=content["values"]



                       
            self.var_contact.set(row[0])
            self.var_checkin.set(row[1])
            self.var_checkout.set(row[2])
            self.var_roomtype.set(row[3])
            self.var_roomavailable.set(row[4]),
            self.var_meal.set(row[5])
            self.var_noOfdays.set(row[6])
                                                                                              

#Update

        def update(self):
                                if self.var_contact.get()=="":
                                      messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
                                else:
                                   conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
                                   my_cursor=conn.cursor()
                                   my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(

                                                                                                                                           
                                                                                                                                           
                                                                                                                                           self.var_checkin.get(),
                                                                                                                                           self.var_checkout.get(),
                                                                                                                                           self.var_roomtype.get(),
                                                                                                                                           self.var_roomavailable.get(),
                                                                                                                                           self.var_meal.get(),
                                                                                                                                           self.var_noOfdays.get(),
                                                                                                                                           self.var_contact.get()
                                                                                                                                                         ))
                                                                                                                                                        
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("UPDATES","Room details has been updated succesfully",parent=self.root)
          
          
#delete Function
        def mDelete(self):
                                        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)        
                                        if mDelete>0:                                 
                                                conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
                                                my_cursor=conn.cursor()
                                   #my_cursor.execute("delete customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where Ref=%s",(
                                                query="delete from room where Contact=%s"
                                                value=(self.var_contact.get(),)
                                                my_cursor.execute(query,value)
                                        else:
                                       
                                         if not mDelete:
                                            return
                                        conn.commit()
                                        self.fetch_data()
                                        conn.close()


#reset function
        def reset(self):   
               
                        self.var_contact.set("")
                        self.var_checkin.set("")
                        self.var_checkout.set("")
                        self.var_roomtype.set("")
                        self.var_roomavailable.set(""),
                        self.var_meal.set("")
                        self.var_noOfdays.set("")
                        self.var_paidtax.setset("")
                        self.var_actualtotal.set("")
                        self.var_total.set("")
               


#========================= All Data Fetch=================

        def Fetch_contact(self):
         if self.var_contact.get()=="":
          messagebox.showerror("Error","Please enter contact no",parent=self.root)
            
         else:

            conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
               messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
               conn.commit()
               conn.close()
            showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
            showDataframe.place(x=450,y=55,width=300,height=180)
            
            lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)
            

            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=0)
     


#gender

            conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
            my_cursor=conn.cursor()
            query=("select Gender from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
      

            lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=30)
            

            lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl2.place(x=90,y=30)




#email

            conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
            my_cursor=conn.cursor()
            query=("select Email from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
      

            lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=60)
            

            lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl3.place(x=90,y=60)

#nationality

            conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
            my_cursor=conn.cursor()
            query=("select Nationality from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
      

            lblGender=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=90)
            

            lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl4.place(x=90,y=90)
#address

            conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
            my_cursor=conn.cursor()
            query=("select Address from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
      

            lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=120)
            

            lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl5.place(x=90,y=120)


            conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
            my_cursor=conn.cursor()
            query=("select Mother from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
      

            lblMother=Label(showDataframe,text="Mother:",font=("arial",12,"bold"))
            lblMother.place(x=0,y=140)
            

            lbl6=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl6.place(x=90,y=140)

#search system

        def search(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
           my_cursor=conn.cursor()
           my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
           rows=my_cursor.fetchall()
           if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
             self.room_table.insert("",END,values=i)
            conn.commit()
           conn.close()


#totaldata

        def total(self):
                   inDate=self.var_checkin.get()
                   outDate=self.var_checkout.get()
                   inDate=datetime.strptime(inDate,"%d/%m/%Y")
                   outDate=datetime.strptime(outDate,"%d/%m/%Y")
                   self.var_noOfdays.set(abs(outDate - inDate).days)
                
                   if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxary"):
                    q1=float(300)
                   q2=float(700)
                   q3=float(self.var_noOfdays.get())
                   q4=float(q1+q2)
                   q5=float(q3+q4)
                   Tax="Rs."+str("%.2f"%((q5)))
                   ST="Rs."+str("%.2f"%((q5)))
                   TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
                   self.var_paidtax.set(Tax)
                   self.var_actualtotal.set(ST)
                   self.var_total.set(TT)\


            #elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxary"):
                        #q1=float(300)
                        #q2=float(700)
                        #q3=float(self.var_noOfdays.get())
                        #q4=float(q1+q2)
                        #q5=float(q3+q4)
                        #Tax="Rs."+str("%.2f"%((q5)))
                         #ST="Rs."+str("%.2f"%((q5)))
                   #TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
                   #self.var_paidtax.set(Tax)
                   #self.var_actualtotal.set(ST)
                   #self.var_total.set(TT)




       





if __name__ == "__main__":
    root=Tk()
    obj=roombooking(root)
    root.mainloop()