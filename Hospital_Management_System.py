from tkinter import *
from tkinter import messagebox
import mysql.connector as my
from tkinter import ttk

def doctor_panel():
    global dt_pn
    dt_pn=Toplevel(ad_screen)
    dt_pn.geometry("1350x950")
    dt_pn.configure(background="PaleVioletRed1")
    
    Label(dt_pn,text="DOCTOR PANEL",background="PaleVioletRed1" ,fg="black",font=("arial black",40,"bold")).place(x=500,y=10)
    Label(dt_pn,text=" ENTER ID :",font=("arial black",20)).place(x=50,y=100)
    Label(dt_pn,text=" NAME : ",font=("arial black",20)).place(x=50,y=150)
    Label(dt_pn,text="SPECIALIZATION :",font=("arial black",20)).place(x=50,y=200)
    Label(dt_pn,text=" CONTACT :",font=("arial black",20)).place(x=50,y=250)
    large_font = ('arial black',20)

    e_id=Entry(dt_pn,font=large_font)
    e_id.place(x=400,y=100)

    e_name=Entry(dt_pn,font=large_font)
    e_name.place(x=400,y=150)

    e_specialization=Entry(dt_pn,font=large_font)
    e_specialization.place(x=400,y=200)

    e_contact=Entry(dt_pn,font=large_font)
    e_contact.place(x=400,y=250)
    def insert():
        d_id=e_id.get()
        d_name=e_name.get()
        specialization=e_specialization.get()
        contact=e_contact.get()
        if(d_id=="" or d_name=="" or specialization=="" or contact==""):
            messagebox.showinfo("Insert status","All fields are required")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("insert into doctor_panel values('"+d_id+"','"+d_name+"','"+specialization+"','"+contact+"')")
            mycursor.execute("commit");

            e_id.delete(0,'end')
            e_name.delete(0,'end')
            e_specialization.delete(0,'end')
            e_contact.delete(0,'end')
            
            messagebox.showinfo("Insert status","inserted successfullly")
            mydb.close();

    def delete():
        if(e_id.get()==""):
            messagebox.showinfo("Delete status","id is compulsory for delete")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("delete from doctor_panel where d_id='"+e_id.get()+"'")
            mycursor.execute("commit");
            e_id.delete(0,'end')
            e_name.delete(0,'end')
            e_specialization.delete(0,'end')
            e_contact.delete(0,'end')
            show()
            messagebox.showinfo("delete status","deleted successfullly");
            mydb.close();

    def update():
        d_id=e_id.get()
        d_name=e_name.get()
        specialization=e_specialization.get()
        contact=e_contact.get()

        if(d_id=="" or d_name=="" or specialization=="" or contact==""):
            messagebox.showinfo("update status","All fields are required")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("update doctor_panel set d_name='"+ d_name +"',specialization='"+specialization+"',contact='"+ contact +"' where d_id='"+d_id+"'")           
            mycursor.execute("commit");

            e_id.delete(0,'end')
            e_name.delete(0,'end')
            e_specialization.delete(0,'end')
            e_contact.delete(0,'end')
            show()
            messagebox.showinfo("update status","updated successfullly");
            mydb.close();
            
        
    def search():
        if(e_id.get()==""):
            messagebox.showinfo("fetch status","id is compulsory to get all records")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("select * from doctor_panel where d_id='"+e_id.get()+"'")
            rows=mycursor.fetchall()
            for row in rows:
                e_name.insert(0,row[1])
                e_specialization.insert(0,row[2])
                e_contact.insert(0,row[3])
            mydb.close();

        

    def show():
        mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
        mycursor=mydb.cursor()
        mycursor.execute("select * from doctor_panel")
        rows=mycursor.fetchall()
        list.delete(0, list.size())

        for row in rows:
            insertData=str(row[0])+'      '+row[1]+'       '+row[2]+'       '+str(row[3])
            list.insert(list.size()+1,insertData)
        mydb.close();


    def back():
        global ad_screen
        ad_screen=Toplevel(w)
        ad_screen.geometry("1350x950")
        ad_screen.configure(background="PaleVioletRed1")

        Label(ad_screen,text="ADMIN PANEL",bg="PaleVioletRed1" , fg="black",font=("arial black",40)).place(x=500,y=70)

        Button(ad_screen, text="Doctor", bg="yellow",fg="red",font=("aerial black",40),command=doctor_panel).place(x=300,y=200)
        Button(ad_screen, text="Patient", bg="yellow",fg="red",font=("aerial black",40),command=patient_panel).place(x=900,y=200)
        Button(ad_screen, text="Appointment", bg="yellow",fg="red",font=("aerial black",40),command=appointment_panel).place(x=250,y=400)
        Button(ad_screen, text="Help", bg="yellow",fg="red",font=("aerial black",40),command=helpline).place(x=930,y=400)
        dt_pn.withdraw()
    
        
        
    Button(dt_pn, text="INSERT", bg="yellow",fg="red",font=("aerial black",18),command=insert).place(x=10,y=420)
    Button(dt_pn, text="UPDATE", bg="yellow",fg="red",font=("aerial black",18),command=update).place(x=120,y=420)
    Button(dt_pn, text="VIEW", bg="yellow",fg="red",font=("aerial black",18),command=show).place(x=240,y=420)
    Button(dt_pn, text="DELETE", bg="yellow",fg="red",font=("aerial black",18),command=delete).place(x=325,y=420)
    Button(dt_pn, text="BACK", bg="yellow",fg="red",font=("aerial black",18),command=back).place(x=442,y=420)
    Button(dt_pn, text="SEARCH", bg="yellow",fg="red",font=("aerial black",18),command=search).place(x=530,y=420)
    ad_screen.withdraw()
    list=Listbox(dt_pn,width=70,height=35)
    list.place(x=800,y=100)
    show()


    
    
   
#*******************************************************************************PATIENT WINDOW***************************************************************************************


def patient_panel():
    global pt_pn
    pt_pn=Toplevel(ad_screen)
    pt_pn.geometry("1350x950")
    pt_pn.configure(bg="PaleVioletRed1")
    
    large_font = ('arial black',20)
    Label(pt_pn,text="ADMIT PATIENT FORM AND DETAILS",bg="PaleVioletRed1",fg="black",font=("aerial black",40,"bold")).place(x=250,y=10)
    Label(pt_pn,text="NAME :",font=("arial black",15,"bold")).place(x=50,y=70)
    e_name=Entry(pt_pn,font=large_font)
    e_name.place(x=300,y=75)
    
    Label(pt_pn,text="AGE :",font=("arial black",15,"bold")).place(x=50,y=120)
    e_age=Entry(pt_pn,font=large_font)
    e_age.place(x=300,y=125)
    
    Label(pt_pn,text="GENDER :",font=("arial black",15,"bold")).place(x=50,y=170)
    e_gender=ttk.Combobox(pt_pn,font=("arial black",15,"bold"))
    e_gender["values"]=("male","female","other")
    e_gender.place(x=300,y=175)
    
    Label(pt_pn,text="CONTACT",font=("arial black",15,"bold")).place(x=50,y=220)
    e_contact=Entry(pt_pn,font=large_font)
    e_contact.place(x=300,y=225)
    
    Label(pt_pn,text="DISEASE",font=("arial black",15,"bold")).place(x=50,y=270)
    e_disease=Entry(pt_pn,font=large_font)
    e_disease.place(x=300,y=275)
    
    Label(pt_pn,text="DOCTOR NAME",font=("arial black",15,"bold")).place(x=50,y=320)
    e_doctor=Entry(pt_pn,font=large_font)
    e_doctor.place(x=300,y=325)
    
    Label(pt_pn,text="ADMIT DATE",font=("arial black",15,"bold")).place(x=50,y=370)
    e_admit=Entry(pt_pn,font=large_font)
    e_admit.place(x=300,y=375)
    
    Label(pt_pn,text="DISCHARGE DATE",font=("arial black",15,"bold")).place(x=50,y=420)
    e_discharge=Entry(pt_pn,font=large_font)
    e_discharge.place(x=300,y=425)



    def insert():
        name=e_name.get()
        age=e_age.get()
        gender=e_gender.get()
        contact=e_contact.get()
        disease=e_disease.get()
        d_name=e_doctor.get()
        admit_date=e_admit.get()
        discharge_date=e_discharge.get()
        
        if(name=="" or age=="" or gender=="" or contact=="" or disease=="" or d_name==""):
            messagebox.showinfo("Insert status","All fields are required")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("insert into patient_panel values('"+name+"','"+age+"','"+gender+"','"+contact+"','"+disease+"','"+d_name+"','"+admit_date+"','"+discharge_date+"')")
            mycursor.execute("commit");

            e_name.delete(0,'end')
            e_age.delete(0,'end')
            e_gender.delete(0,'end')
            e_contact.delete(0,'end')
            e_disease.delete(0,'end')
            e_doctor.delete(0,'end')
            e_admit.delete(0,'end')
            e_discharge.delete(0,'end')
            
            messagebox.showinfo("Insert status","inserted successfullly")
            mydb.close();
    def delete():
        if(e_name.get()==""):
            messagebox.showinfo("Delete status","name is compulsory for delete")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("delete from patient_panel where name='"+e_name.get()+"'")
            mycursor.execute("commit");

            e_name.delete(0,'end')
            e_age.delete(0,'end')
            e_gender.delete(0,'end')
            e_contact.delete(0,'end')
            e_disease.delete(0,'end')
            e_doctor.delete(0,'end')
            e_admit.delete(0,'end')
            e_discharge.delete(0,'end')
            show()
            messagebox.showinfo("delete status","deleted successfullly");
            mydb.close();

    def update():
        name=e_name.get()
        age=e_age.get()
        gender=e_gender.get()
        contact=e_contact.get()
        disease=e_disease.get()
        d_name=e_doctor.get()
        admit_date=e_admit.get()
        discharge_date=e_discharge.get()

        if(name=="" or age=="" or gender=="" or contact=="" or disease=="" or d_name=="" or admit_date=="" or discharge_date==""):
            messagebox.showinfo("update status","All fields are required")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("update patient_panel set age='"+age+"',gender='"+gender+"',contact='"+ contact +"',disease='"+disease+"',d_name='"+d_name+"',admit_date='"+admit_date+"',discharge_date='"+ discharge_date +"' where name='"+name+"'")           
            mycursor.execute("commit");

            e_name.delete(0,'end')
            e_age.delete(0,'end')
            e_gender.delete(0,'end')
            e_contact.delete(0,'end')
            e_disease.delete(0,'end')
            e_doctor.delete(0,'end')
            e_admit.delete(0,'end')
            e_discharge.delete(0,'end')
            show()
            messagebox.showinfo("update status","updated successfullly");
            mydb.close();
        
    def search():
        if(e_name.get()==""):
            messagebox.showinfo("fetch status","name is compulsory for delete")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("select * from patient_panel where name='"+e_name.get()+"'")
            rows=mycursor.fetchall()
            for row in rows:
                e_age.insert(0,row[1])
                e_gender.insert(0,row[2])
                e_contact.insert(0,row[3])
                e_disease.insert(0,row[4])
                e_doctor.insert(0,row[5])
                e_admit.insert(0,row[6])
                e_discharge.insert(0,row[7])
            mydb.close();

    def show():
        mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
        mycursor=mydb.cursor()
        mycursor.execute("select * from patient_panel")
        rows=mycursor.fetchall()
        list.delete(0, list.size())

        for row in rows:
            insertData=row[0]+'          '+str(row[1])+'           '+row[2]+'          '+str(row[3])+'              '+row[4]+'       '+row[5]+'       '+row[6]+'       '+row[7]
            list.insert(list.size()+1,insertData)
        mydb.close();
        
    def back():
        global ad_screen
        ad_screen=Toplevel(w)
        ad_screen.geometry("1350x950")
        ad_screen.configure(background="PaleVioletRed1")

        Label(ad_screen,text="ADMIN PANEL",bg="PaleVioletRed1" , fg="black",font=("arial black",40)).place(x=500,y=70)
        Button(ad_screen, text="Doctor", bg="yellow",fg="red",font=("aerial black",40),command=doctor_panel).place(x=300,y=200)
        Button(ad_screen, text="Patient", bg="yellow",fg="red",font=("aerial black",40),command=patient_panel).place(x=900,y=200)
        Button(ad_screen, text="Appointment", bg="yellow",fg="red",font=("aerial black",40),command=appointment_panel).place(x=250,y=400)
        Button(ad_screen, text="Help", bg="yellow",fg="red",font=("aerial black",40),command=helpline).place(x=930,y=400)

        pt_pn.withdraw()

    Button(pt_pn, text="INSERT", bg="yellow",fg="red",font=("aerial black",18),command=insert).place(x=10,y=550)
    Button(pt_pn, text="UPDATE", bg="yellow",fg="red",font=("aerial black",18),command=update).place(x=120,y=550)
    Button(pt_pn, text="VIEW", bg="yellow",fg="red",font=("aerial black",18),command=show).place(x=240,y=550)
    Button(pt_pn, text="DELETE", bg="yellow",fg="red",font=("aerial black",18),command=delete).place(x=325,y=550)
    Button(pt_pn, text="BACK", bg="yellow",fg="red",font=("aerial black",18),command=back).place(x=442,y=550)
    Button(pt_pn, text="SEARCH", bg="yellow",fg="red",font=("aerial black",18),command=search).place(x=530,y=550)
    ad_screen.withdraw()
    list=Listbox(pt_pn,width=95,height=35)
    list.place(x=750,y=100)
    show()


#*****************************************************************************APPOINTMENT WINDOW*****************************************************************************************


def appointment_panel():
    global at_pn
    at_pn=Toplevel(ad_screen)
    at_pn.geometry("1350x950")
    at_pn.configure(bg="PaleVioletRed1")
    large_font = ('arial black',20)
    
    Label(at_pn,text="PATIENT  DETAILS",bg="PaleVioletRed1",fg="black",font=("arial black",40)).place(x=400,y=10)
    Label(at_pn,text="NAME :",font=("arial black",20,"bold")).place(x=50,y=100)
    e_name=Entry(at_pn,font=large_font)
    e_name.place(x=250,y=100)
    
    Label(at_pn,text="AGE :",font=("arial black",20,"bold")).place(x=50,y=170)
    e_age=Entry(at_pn,font=large_font)
    e_age.place(x=250,y=170)
   
    Label(at_pn,text="GENDER :",font=("arial black",20,"bold")).place(x=50,y=240)
    e_gender=ttk.Combobox(at_pn,font=("arial black",20,"bold"))
    e_gender["values"]=("male","female","other")
    e_gender.place(x=250,y=240)
    
    Label(at_pn,text="CONTACT :",font=("arial black",20,"bold")).place(x=50,y=310)
    e_contact=Entry(at_pn,font=large_font)
    e_contact.place(x=250,y=310)
    
    Label(at_pn,text="ADDRESS :",font=("arial black",20,"bold")).place(x=50,y=380)
    e_address=Entry(at_pn,font=large_font)
    e_address.place(x=250,y=380)
    
    Label(at_pn,text="DOCTOR :",font=("arial black",20,"bold")).place(x=50,y=450)
    e_doctor=Entry(at_pn,font=large_font)
    e_doctor.place(x=250,y=450)

    def insert():
        name=e_name.get()
        age=e_age.get()
        gender=e_gender.get()
        contact=e_contact.get()
        address=e_address.get()
        d_name=e_doctor.get()
        
        if(name=="" or age=="" or gender=="" or contact=="" or address=="" or d_name==""):
            messagebox.showinfo("Insert status","All fields are required")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("insert into appointments values('"+name+"','"+age+"','"+gender+"','"+contact+"','"+address+"','"+d_name+"')")
            mycursor.execute("commit");

            e_name.delete(0,'end')
            e_age.delete(0,'end')
            e_gender.delete(0,'end')
            e_contact.delete(0,'end')
            e_address.delete(0,'end')
            e_doctor.delete(0,'end')
            
            messagebox.showinfo("Insert status","inserted successfullly")
            mydb.close();

    def delete():
        if(e_name.get()==""):
            messagebox.showinfo("Delete status","id or name is compulsory for delete")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("delete from appointments where name='"+e_name.get()+"'")
            mycursor.execute("commit");
            e_name.delete(0,'end')
            e_age.delete(0,'end')
            e_gender.delete(0,'end')
            e_contact.delete(0,'end')
            e_address.delete(0,'end')
            e_doctor.delete(0,'end')
            show()
            messagebox.showinfo("delete status","deleted successfullly");
            mydb.close();
    def update():
        name=e_name.get()
        age=e_age.get()
        gender=e_gender.get()
        contact=e_contact.get()
        address=e_address.get()
        d_name=e_doctor.get()

        if(name=="" or age=="" or gender=="" or contact=="" or address=="" or d_name==""):
            messagebox.showinfo("update status","All fields are required")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("update appointments set age='"+age+"',gender='"+gender+"',contact='"+ contact +"',address='"+address+"',d_name='"+d_name+"' where name='"+name+"'")           
            mycursor.execute("commit");

            e_name.delete(0,'end')
            e_age.delete(0,'end')
            e_gender.delete(0,'end')
            e_contact.delete(0,'end')
            e_address.delete(0,'end')
            e_doctor.delete(0,'end')
            show()
            messagebox.showinfo("update status","updated successfullly");
            mydb.close();
        
    def search():
        if(e_name.get()==""):
            messagebox.showinfo("fetch status","name is compulsory for delete")
        else:
            mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
            mycursor=mydb.cursor()
            mycursor.execute("select * from appointments where name='"+e_name.get()+"'")
            rows=mycursor.fetchall()
            for row in rows:
                e_age.insert(0,row[1])
                e_gender.insert(0,row[2])
                e_contact.insert(0,row[3])
                e_address.insert(0,row[4])
                e_doctor.insert(0,row[5])
            mydb.close();

    def show():
        mydb=my.connect(host="localhost",
                    user="root",
                    password="",
                    database="hms")
        mycursor=mydb.cursor()
        mycursor.execute("select * from appointments")
        rows=mycursor.fetchall()
        list.delete(0, list.size())

        for row in rows:
            insertData=row[0]+'       '+str(row[1])+'          '+row[2]+'           '+str(row[3])+'            '+row[4]+'          '+row[5]
            list.insert(list.size()+1,insertData)
        mydb.close();
        
   
    def back():
        global ad_screen
        ad_screen=Toplevel(w)
        ad_screen.geometry("1350x950")
        ad_screen.configure(background="PaleVioletRed1")

        Label(ad_screen,text="ADMIN PANEL",bg="PaleVioletRed1" , fg="black",font=("arial black",40)).place(x=500,y=70)

        Button(ad_screen, text="Doctor", bg="yellow",fg="red",font=("aerial black",40),command=doctor_panel).place(x=300,y=200)
        Button(ad_screen, text="Patient", bg="yellow",fg="red",font=("aerial black",40),command=patient_panel).place(x=900,y=200)
        Button(ad_screen, text="Appointment", bg="yellow",fg="red",font=("aerial black",40),command=appointment_panel).place(x=250,y=400)
        Button(ad_screen, text="Help", bg="yellow",fg="red",font=("aerial black",40),command=helpline).place(x=930,y=400)
        at_pn.withdraw()
        

    Button(at_pn, text="INSERT", bg="yellow",fg="red",font=("aerial black",18),command=insert).place(x=10,y=550)
    Button(at_pn, text="UPDATE", bg="yellow",fg="red",font=("aerial black",18),command=update).place(x=120,y=550)
    Button(at_pn, text="VIEW", bg="yellow",fg="red",font=("aerial black",18),command=show).place(x=240,y=550)
    Button(at_pn, text="DELETE", bg="yellow",fg="red",font=("aerial black",18),command=delete).place(x=325,y=550)
    Button(at_pn, text="BACK", bg="yellow",fg="red",font=("aerial black",18),command=back).place(x=442,y=550)
    Button(at_pn, text="SEARCH", bg="yellow",fg="red",font=("aerial black",18),command=search).place(x=530,y=550)
    ad_screen.withdraw()
    
    list=Listbox(at_pn,width=95,height=30)
    list.place(x=700,y=100)
    show()
    


#*********************************************************************************HELPINE WINDOW*************************************************************************************



def helpline():
    global hp
    hp=Toplevel(ad_screen)
    hp.geometry("1350x950")
    hp.configure(background="PaleVioletRed1")
    Label(hp,text="ABC health foundation \n Helpline number and mail id \n contact:01788593780 \n mail id:abc123@yahoo.com ",font=("arial black",40)).place(x=350,y=100)

    def back():
        global ad_screen
        ad_screen=Toplevel(w)
        ad_screen.geometry("1350x950")
        ad_screen.configure(background="PaleVioletRed1")

        Label(ad_screen,text="ADMIN PANEL",bg="PaleVioletRed1" , fg="black",font=("arial black",40)).place(x=500,y=70)
        Button(ad_screen, text="Doctor", bg="yellow",fg="red",font=("aerial black",40),command=doctor_panel).place(x=300,y=200)
        Button(ad_screen, text="Patient", bg="yellow",fg="red",font=("aerial black",40),command=patient_panel).place(x=900,y=200)
        Button(ad_screen, text="Appointment", bg="yellow",fg="red",font=("aerial black",40),command=appointment_panel).place(x=250,y=400)
        Button(ad_screen, text="Help", bg="yellow",fg="red",font=("aerial black",40),command=helpline).place(x=930,y=400)
        hp.withdraw()
        
    Button(hp, text="BACK", bg="yellow",fg="red",font=("aerial black",12),command=back).place(x=0,y=0)
    ad_screen.withdraw()
    

#***************************************************************************MAIN MENU WINDOW*******************************************************************************************

def login(): #main menu window
    global ad_screen
    ad_screen=Toplevel(w)       
    ad_screen.geometry("1350x950")
    ad_screen.configure(background="PaleVioletRed1")
    
    Label(ad_screen,text="ADMIN PANEL",bg="PaleVioletRed1" , fg="black",font=("arial black",40)).place(x=500,y=70)

    Button(ad_screen, text="Doctor", bg="yellow",fg="red",font=("aerial black",40),command=doctor_panel).place(x=300,y=200)
    Button(ad_screen, text="Patient", bg="yellow",fg="red",font=("aerial black",40),command=patient_panel).place(x=900,y=200)
    Button(ad_screen, text="Appointment", bg="yellow",fg="red",font=("aerial black",40),command=appointment_panel).place(x=250,y=400)
    Button(ad_screen, text="Help", bg="yellow",fg="red",font=("aerial black",40),command=helpline).place(x=930,y=400)
    w.withdraw()

        

#***********************************************************************************************************************************************************************
def command1():#to check username and password
    if userEntry.get()=="admin" and passEntry.get()=="admin@123":
        messagebox.showinfo("login","Successfully login",)
        login()
    
    else:
        messagebox.showinfo("invalid username or password","Please check username and password")
    
    
w = Tk()
w.geometry("1350x950")
w.title("Hospital management system")
w['bg'] = "PaleVioletRed1"

Label(w, text = "WELCOME TO ABC HOSPITAL" , bg="PaleVioletRed1",fg="black",font=("arial black",40,"bold")).place(x=250,y=50)
large_font = ('arial black',20)
userlabel  = Label(w, text = "USERNAME" , bg = "PaleVioletRed1" , fg = "black" , font = ("arial black" , 40,"bold"))#username entry
userlabel.place(x=500 , y=180)
username=StringVar
userEntry=Entry(w, textvariable = username , font = large_font)
userEntry.place(x=470,y=280)

passwordlabel = Label(w, text="PASSWORD * ", bg="PaleVioletRed1", fg = "black" , font = ("arial black",40,"bold"))#password entry
passwordlabel.place(x=470,y=380)
password=StringVar
passEntry= Entry(w, textvariable=password,font=large_font, show= '*')
passEntry.place(x=470,y=480)


Button(w, text="Login", bg="yellow",fg="red",font=("arial black",25),command=command1).place(x=600,y=600)#button for login 

w.mainloop()

