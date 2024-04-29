from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from time import strptime
from datetime import datetime
import mysql.connector
import random
from tkinter import messagebox

class DetailsRoom:
        def __init__(self,root):
          self.root = root
          self.root.title("Hotel Management System")  # Corrected usage of title method
          self.root.geometry("1295x550+220+220")



          lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
          lbl_title.place(x=0,y=0,width=1295,height=50)

         #==============LOGO=====================
          img2=Image.open ("/Users/riya/Desktop/ Hotel Management System/images/gh.jpeg")
          img2 = img2.resize((100, 40), Image.BOX)
          self.photoimg2 = ImageTk.PhotoImage(img2)

        
          lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
          lblimg.place(x=5, y=2, width=230, height=40)

#============LABEL FRAME========================
          labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",18,"bold"),padx=2,)
          labelframeleft.place(x=5,y=50,width=540,height=350)




          #===========LABELS and ENTRY=================
          #Floor
          lbl_floor=Label(labelframeleft,text="Floor",font=("times new roman",13,"bold"),padx=2,pady=6)
          lbl_floor.grid(row=0,column=0,sticky=W,padx=20)
           
          self.var_floor=StringVar()
          
          entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
          entry_floor.grid(row=0,column=1,sticky=W)


          #RoomNo

          lbl_floor=Label(labelframeleft,text="Room No: ",font=("times new roman",13,"bold"),padx=2,pady=6)
          lbl_floor.grid(row=1,column=0,sticky=W,padx=20)
  
          self.var_roomNo=StringVar()
          entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=20,font=("arial",13,"bold"))
          entry_floor.grid(row=1,column=1,sticky=W)
          

          #roomtype


          lbl_floor=Label(labelframeleft,text="Room Type",font=("times new roman",13,"bold"),padx=2,pady=6)
          lbl_floor.grid(row=2,column=0,sticky=W,padx=20)
          self.var_RoomType=StringVar()
          entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("arial",13,"bold"))
          entry_floor.grid(row=2,column=1,sticky=W)




          #BUTTON

          btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
          btn_frame.place(x=0,y=200,width=412,height=40)

          btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
          btnAdd.grid(row=0,column=0,padx=1)

          btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
          btnUpdate.grid(row=0,column=1,padx=1)

          btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="Black",fg="gold",width=10)
          btnDelete.grid(row=0,column=2,padx=1)

          btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="brown",fg="gold",width=8)
          btnReset.grid(row=0,column=3,padx=1)




#TableFrame

          Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",18,"bold"),padx=2,)
          Table_frame.place(x=600,y=55,width=600,height=350)



          scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
          scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
          self.room_table=ttk.Treeview(Table_frame,columns=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
          
          scroll_x.pack(side=BOTTOM,fill=X)
          scroll_y.pack(side=RIGHT,fill=Y)
          self.room_table.pack(fill=BOTH, expand=True)


          scroll_x.config(command=self.room_table.xview)
          scroll_y.config(command=self.room_table.yview)
 
          self.room_table.heading("floor",text="Floor")
          self.room_table.heading("roomno",text="Room No")
          self.room_table.heading("roomtype",text="Room Type")
         
          
          self.room_table["show"]="headings"

          self.room_table.column("floor",width=100)
          self.room_table.column("roomno",width=100)
          self.room_table.column("roomtype",width=100)
          
          self.room_table.pack(fill=BOTH,expand=1)
          self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
          self.fetch_data()
     



     #ADD DATA
        def add_data(self):
             if self.var_floor.get()==""or self.var_RoomType.get()=="":
                 messagebox.showerror("Error","All fields are required",parent=self.root)
             else:
                     
                     try:
                        
                           conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
                           my_cursor=conn.cursor()
                           my_cursor.execute("insert into Details values(%s,%s,%s)" , (
                               
                                                                                              self.var_floor.get(),
                                                                                              self.var_roomNo.get(),
                                                                                              self.var_RoomType.get()
                        ))
                           
                           
                           
                           conn.commit()
                           self.fetch_data()
                           conn.close()
                           

                           messagebox.showinfo("Success","New Room Added Successfully")  
                     except Exception as es:
                           messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)










 #========Fetch Data====

        def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from Details")
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



                       
            self.var_floor.set(row[0])
            self.var_roomNo.set(row[1])
            self.var_RoomType.set(row[2])
            
                                        

#Update

        def update(self):
                                if self.var_floor.get()=="":
                                      messagebox.showerror("Error","Please Enter Floor Number",parent=self.root)
                                else:
                                   conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
                                   my_cursor=conn.cursor()
                                   my_cursor.execute("update Details set Floor=%s,RoomType=%s where RoomNo=%s",(

                                                                                                                                           
                                                                                                                                           
                                                                                                                                           self.var_floor.get(),
                                                                                                                                           self.var_RoomType.get(),
                                                                                                                                           self.var_roomNo.get()
                                                                                                                                           
                                                                                                                                                         ))
                                                                                                                                                        
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("UPDATES","New Room details has been updated succesfully",parent=self.root)

#delete Function
        def mDelete(self):
                                        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)        
                                        if mDelete>0:                                 
                                                conn=mysql.connector.connect(host="localhost",username="root",password="Riy@1234",database="Management")
                                                my_cursor=conn.cursor()
                                   #my_cursor.execute("delete customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where Ref=%s",(
                                                query="delete from Details where RoomNo=%s"
                                                value=(self.var_roomNo.get(),)
                                                my_cursor.execute(query,value)
                                        else:
                                       
                                         if not mDelete:
                                            return
                                        conn.commit()
                                        self.fetch_data()
                                        conn.close()

          



#reset function
        def reset(self):   
               
                        self.var_roomNo.set("")
                        self.var_floor.set("")
                        self.var_RoomType.set("")
                        









if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()