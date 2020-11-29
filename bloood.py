from tkinter import *
from PIL import Image,ImageTk
from functools import partial
import mysql.connector
import tkinter.messagebox as box


db = mysql.connector.connect(host='localhost',
                                         database='blood19',
                                         user='root',
                                         password='@Nikitamankar123')

cursor = db.cursor()
root = Tk()
#image1 = PhotoImage(file="blllld.png")
#anel = Label(root, image=image1, bg="black").place(x=0, y=0, relwidth=1, relheight=1)
load = Image.open("wallpaper.jpg")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.place(x=0, y=0,relheight=1,relwidth=1)
root.title("BLOOD BANK")
root.geometry("1920x1080")
root.configure(background='black')
#frame2 = PhotoImage(file='giphy.gif', format="gif -index 2")
l3 = Label(root, text="BLOOD BANK SYSTEM", font="Courier 24 italic bold",borderwidth=3,relief='flat').place(x=550, y=40, w=450, h=62)
a2abel=Label(root,text="I AM ADMIN",bg='white',font="Helvetica 12 bold").place(x=60,y=200,w=300,h=40)
abutton=Button(root,text="Click to login",command=lambda:admin()).place(x=370,y=200,h=40,w=100)


#button = Button(root).place(x=80,y=250)
#img = PhotoImage(file="login.png") # make sure to add "/" not "\"
#button.config(image=img)
#button.pack()

   # Displaying the button
"""
from tkinter import *
import imageio
from PIL import Image, ImageTk
def stream():
    try:
        image = video.get_next_data()
        frame_image = Image.fromarray(image)
        frame_image=ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = frame_image
        l1.after(delay, lambda: stream())
    except:
        video.close()
        return   
########### Main Program ############
root = Tk()
root.title('Video in a Frame')
f1=Frame()
l1 = Label(f1)
l1.pack()
f1.pack()
video_name = "Futurama.mkv"   #Image-path
video = imageio.get_reader(video_name)
delay = int(1000 / video.get_meta_data()['fps'])
stream()
root.mainloop()

"""

l1 = Label(root, text="DONOR'S FORM ", bg='white', font="Helvetica 12 bold").place(x=60, y=300, w=300, h=40)
b1 = Button(root, text="Fill the form", command=lambda: donorinfo()).place(x=370, y=300,h=40,w=100)

#l2 = Label(root, text="Click to enter the details of the blood", bg='white', font="Helvetica 12").place(x=80, y=300,w=300, h=40)
#b2 = Button(root, text="Blood Details", command=lambda: blooddetails()).place(x=80, y=350)
#l3 = Label(root, text="Click to make a request for blood", bg='white', font="Helvetica 12").place(x=80, y=400, w=300,h=40)
#b3 = Button(root, text="Blood Request", command=lambda: requestblood()).place(x=80, y=450)

fbut = Button(root, text="Feedback", command=lambda: feedback_page()).place(x=370, y=400,h=40,w=100)
l3 = Label(root, text="FILL THE FEEDBACK", bg='white', font="Helvetica 12 bold").place(x=60,y=400, w=300,
                                                                                                  h=40)
b2 = Button(root, text="Exit", command=lambda: stop(root)).place(x=220, y=500,w=100,h=40)
v = StringVar()



def insertDonor(adminx,name,age, gender, address, contactno,bloodgroup):
    try:
        cursor.execute("INSERT INTO donor1(Admin_id,dname,bloodgroup,gender,address,phoneno) values(%s,%s,%s,%s,%s,%s)",[adminx,name,bloodgroup,gender,address,contactno])
        db.commit()
    except:
        db.rollback()


def insertDon(name,age,gender,address,contactno,bloodgroup):
    try:
        cursor.execute("INSERT INTO donor3(doname,bgp,Gen,adr,pno) values(%s,%s,%s,%s,%s)",[name,bloodgroup,gender,address,contactno])
        db.commit()
    except:
        db.rollback()    

def insertBlood(donor_id,bloodgroup, platelet, rbc):
    insert = "INSERT INTO blood(bloodgroup,platelet,rbc,date) VALUES('" + bloodgroup + "'," + "'" + platelet + "'," + "'" + rbc + "'," + "CURDATE())"

    try:
        cursor.execute(insert)
        db.commit()
    except:
        db.rollback()

def retrieve(bg):
    request = "select * from donor1 where bloodgroup='" + bg + "'"

    try:
        cursor.execute(request)
        rows = cursor.fetchall()
        db.commit()
        return rows
    except:
        db.rollback()


def sel():      

    selection = "You selected the option " + v.get()
    print
    selection


def donordetails(adminx):
    # global v
    root = Toplevel()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="Name:", bg='white', font="Helvetica 12").place(x=40, y=40)
    l2 = Label(root, text="Age:", bg='white', font="Helvetica 12").place(x=40, y=80)
    l3 = Label(root, text="Gender:", bg='white', font="Helvetica 12").place(x=40, y=120)
    l4 = Label(root, text="Address:", bg='white', font="Helvetica 12").place(x=40, y=220)
    l5 = Label(root, text="Contact:", bg='white', font="Helvetica 12").place(x=40, y=260)
    l6= Label(root, text="blood group",bg='white',font="Helvetica 12").place(x=40,y=300)
    e1 = Entry(root)
    e1.place(x=140, y=40)
    e2 = Entry(root)
    e2.place(x=140, y=80)
    e3=Entry(root)
    e3.place(x=140,y=120)
    e4 = Entry(root)
    e4.place(x=140, y=220)
    e5 = Entry(root)
    e5.place(x=140, y=260)
    e6=Entry(root)
    e6.place(x=140,y=300)
    b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=340)
    b1=Button(root,text="Submit",command=lambda : insertDonor(adminx,e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())).place(x=160,y=340)
    root.mainloop()


def donorinfo():
    # global v
    root = Toplevel()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="Name:", bg='white', font="Helvetica 12").place(x=40, y=40)
    l2 = Label(root, text="Age:", bg='white', font="Helvetica 12").place(x=40, y=80)
    l3 = Label(root, text="Gender:", bg='white', font="Helvetica 12").place(x=40, y=120)
    l4 = Label(root, text="Address:", bg='white', font="Helvetica 12").place(x=40, y=220)
    l5 = Label(root, text="Contact:", bg='white', font="Helvetica 12").place(x=40, y=260)
    l6= Label(root, text="blood group",bg='white',font="Helvetica 12").place(x=40,y=300)
    l7=Label(root,text="")
    e1 = Entry(root)
    e1.place(x=140, y=40)
    e2 = Entry(root)
    e2.place(x=140, y=80)
    e3=Entry(root)
    e3.place(x=140,y=120)
    e4 = Entry(root)
    e4.place(x=140, y=220)
    e5 = Entry(root)
    e5.place(x=140, y=260)
    e6=Entry(root)
    e6.place(x=140,y=300)
    b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=340)
    b1=Button(root,text="Submit",command=lambda : insertDon(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())).place(x=160,y=340)
    root.mainloop()






def blooddetails():
    root = Tk()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="Blood Group:", font="Helvetica 12").place(x=40, y=40, w=250, h=20)
    l2 = Label(root, text="PLatetelet count (in 100 thousands):", font="Helvetica 12").place(x=40, y=80, w=250, h=20)
    l3 = Label(root, text="RBC count (in millions):", font="Helvetica 12").place(x=40, y=120, w=250, h=20)
    # l4=Label(root,text="Date Of Entry count:").place(x=40,y=160)
    e1 = Entry(root)
    e1.place(x=350, y=40)
    e2 = Entry(root)
    e2.place(x=350, y=80)
    e3 = Entry(root)
    e3.place(x=350, y=120)
    b2 = Button(root, text="Back", command=lambda: stop(root)).place(x=200, y=160)
    b1 = Button(root, text="Submit", command=lambda: insertBlood(e1.get(), e2.get(), e3.get())).place(x=40, y=160)
    root.mainloop()
    

   


def grid1(bg):
    root = Tk()
    root.title("LIST OF MATCHING DONORS")
    root.geometry("750x500")
    root.configure(background='#FF8F8F')
    rows = retrieve(bg)
    x = 0
    for row in rows:
        l1 = Label(root, text=row[0], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=0, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l2 = Label(root, text=row[1], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=1, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l3 = Label(root, text=row[2], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=2, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l4 = Label(root, text=row[3], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=3, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l5 = Label(root, text=row[4], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=4, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l6 = Label(root, text=row[5], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=5, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l7 = Label(root, text=row[6], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=6, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        x = x + 1
    root.mainloop()


def grid2():
    root = Tk()
    root.title("LIST OF DONORS")
    root.geometry("750x500")
    root.configure(background='#ffeadb')
    rows = retrieve1()
    x = 0
    for row in rows:
        l1 = Label(root, text=row[0], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=0, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l2 = Label(root, text=row[1], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=1, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l3 = Label(root, text=row[2], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=2, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l4 = Label(root, text=row[3], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=3, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l5 = Label(root, text=row[4], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=4, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l6 = Label(root, text=row[5], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=5, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l7 = Label(root, text=row[6], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=6, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        x = x + 1
    root.mainloop()




def grid3():
    root = Tk()
    root.title("LIST OF DONORS")
    root.geometry("750x500")
    root.configure(background='#ffeadb')
    rows = retrieve2()
    x = 0
    for row in rows:
        l1 = Label(root, text=row[0], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=0, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l2 = Label(root, text=row[1], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=1, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l3 = Label(root, text=row[2], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=2, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l4 = Label(root, text=row[3], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=3, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l5 = Label(root, text=row[4], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=4, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l6 = Label(root, text=row[5], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=5, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        x = x + 1
    root.mainloop()


def grid4():
    root = Tk()
    root.title("LIST OF Feedback's")
    root.geometry("750x500")
    root.configure(background='#ffeadb')
    rows = retrieve3()
    x = 0
    for row in rows:
        l1 = Label(root, text=row[0], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=0, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l2 = Label(root, text=row[1], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=1, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l3 = Label(root, text=row[2], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=2, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        x=x+1
    root.mainloop()


def retrieve3():
    request = "select * from feedback"
    try:
        cursor.execute(request)
        rows = cursor.fetchall()
        db.commit()
        return rows
    except:
        db.rollback()


def retrieve1():
    request = "select * from donor1"
    try:
        cursor.execute(request)
        rows = cursor.fetchall()
        db.commit()
        return rows
    except:
        db.rollback()

def retrieve2():
    request = "select * from donor3"
    try:
        cursor.execute(request)
        rows = cursor.fetchall()
        db.commit()
        return rows
    except:
        db.rollback()





def requestblood():
    root = Tk()
    root.title("BLOOD BANK")
    root.geometry("1920x1080")
    root.configure(background='#ffeadb')
    l = Label(root, text="Enter the blood group").place(x=50, y=50, w=400, h=40)
    e = Entry(root)
    e.place(x=500, y=50)
    b2 = Button(root, text="Back", command=lambda: stop(root)).place(x=500, y=250,w=50)
    #b = Button(root, text="ENTER", command=lambda: grid1(e.get())).place(x=500, y=100)
    l1=Label(root,text="Enter the city name").place(x=50,y=150,w=400,h=40)
    e1 = Entry(root)
    e1.place(x=500, y=150)
    #b3 = Button(root, text="Back", command=lambda: stop(root)).place(x=800, y=100)
    b31 = Button(root, text="ENTER", command=lambda:add_count(e.get(),e1.get())).place(x=500, y=200)
    root.mainloop()


def LoginPage():
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter login details").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable="username")
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password__login_entry = Entry(login_screen, textvariable="password", show= '*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1).pack()
    login_screen.mainloop()

def add_count(bloodgroup,city):
    number_of_rows=cursor.execute('SELECT count(*) FROM availability where city=%s and Blood_group=%s',[city,bloodgroup])
    nor=cursor.fetchone()[0]
    print(nor)
    if(int(nor)>0):
        grid8(bloodgroup,city) 
        db.commit()


    elif(int(nor)==0):
        box.showinfo('info','Blood not available')
        db.rollback()




import tkinter.messagebox as box


def dialog1(entry1,entry2):
    username=entry1.get()
    password = entry2.get()
    
    cursor.execute("select admin_id from admin1 where username=%s and password=%s", [username,password])
    adminx=cursor.fetchone()

    if(adminx==None):
         box.showinfo('info','Invalid Login')
    else:
        admin_next_page(str(adminx[0]))

    
    """
    if ( == 'admin' and  password == 'secret'):
        admin_next_page()
    else:
        box.showinfo('info','Invalid Login')
    """
def admin():
    window = Tk()
    window.title('Admin')
    window.geometry("400x300")
    frame = Frame(window)
    Label1 = Label(window,text = 'Username:')
    Label1.pack(padx=15,pady= 5)
    entry1 = Entry(window,bd =5)
    entry1.pack(padx=15, pady=5)
    Label2 = Label(window,text = 'Password: ')
    Label2.pack(padx = 15,pady=6)
    entry2 = Entry(window, bd=5,show='*')
    entry2.pack(padx = 15,pady=7)
    btn = Button(frame, text = 'Login',command =lambda:dialog1(entry1,entry2))
    btn.pack(side = RIGHT , padx =5)
    frame.pack(padx=100,pady = 19)
    window.mainloop()

def feedback():
    root=Tk()
    root.title('Feedback')
    l7 = Label(root, text="Feedback:", bg='white', font="Helvetica 12").place(x=40, y=220)
    b11 = Button(root, text="Submit", command=lambda:feedback_page()).place(x=40, y=300)
    root.mainloop()


def feedback_page():
    root=Tk()
    root.geometry("750x500")
    root.title('Feedback')
    l2=Label(root,text="Name",bg='pink',font="Helvetica 12").place(x=40,y=40)
    e2 = Entry(root)
    e2.place(x=40, y=80)
    l1 = Label(root, text="Give Feedback",bg='pink',font="Helvetica 12").place(x=40, y=120, w=300, h=20)
    e1 = Entry(root)
    e1.place(x=40,y=160,w=300,h=100)
    b11 = Button(root, text="Submit", command=lambda:insert_feedback(e2.get(),e1.get())).place(x=40, y=300)
    b2 = Button(root, text="Close", command=lambda: stop(root)).place(x=100, y=300)
    root.mainloop()


def insert_feedback(name,feedback_data):
    try:
        cursor.execute("INSERT INTO feedback(dname,feedback_data) values(%s,%s)",[name,feedback_data])
        db.commit()
    except:
        db.rollback()
#create table feedback(feedback_id int primary key auto_increment, dname varchar(30),feedback_data varchar(100));


def admin_next_page(adminx):
    root=Tk()

    root.title("BLOOD BANK")
    root.geometry("1920x1080")
    root.configure(background='#FF8F8F')

    tit = Label(root, text="Welcome to Admin's Page", bg='white', font="Helvetica 15 bold").place(x=600, y=40, w=300, h=42)

    l0 = Label(root, text="Donate blood", bg='white', font="Helvetica 12").place(x=350, y=200, w=300, h=40)
    b0 = Button(root, text="donor click", command=lambda:insert2()).place(x=470, y=250)

    l1 = Label(root, text="Add donor", bg='white', font="Helvetica 12").place(x=350, y=300, w=300, h=40)
    b1 = Button(root, text="donor click", command=lambda: donordetails(adminx)).place(x=470, y=350)

    l2 = Label(root, text="Update donor details", bg='white', font="Helvetica 12").place(x=350, y=400,w=300, h=40)
    b2 = Button(root, text="donor click", command=lambda:admin_update_page()).place(x=470, y=450)

    l3 = Label(root, text="Click to make a request for blood", bg='white', font="Helvetica 12").place(x=580, y=500, w=300,
                                                                                                  h=40)
    b3 = Button(root, text="Blood Request", command=lambda: requestblood()).place(x=670, y=550)

    l4 = Label(root, text="Donor's list", bg='white', font="Helvetica 12").place(x=800, y=200, w=300,
                                                                                                  h=40)
    b4 = Button(root, text="Request list", command=lambda: donor_list()).place(x=920, y=250)


    l5 = Label(root, text="View feedback", bg='white', font="Helvetica 12").place(x=800, y=300, w=300,
                                                                                                  h=40)
    b5 = Button(root, text="Request feedback", command=lambda: grid4()).place(x=910, y=350)


    l6 = Label(root, text="History", bg='white', font="Helvetica 12").place(x=800, y=400, w=300,
                                                                                                  h=40)
    b6 = Button(root, text="Request History", command=lambda: grid7()).place(x=910, y=450)


    b2 = Button(root, text="Exit", command=lambda: stop(root)).place(x=700, y=600)
    v = StringVar()
    root.mainloop()



"""
def historypart():
    root=Tk()

    root.title("BLOOD BANK")
    root.geometry("1920x1080")
    root.configure(background='#FF8F8F')

    l6 = Label(root, text="View History", bg='white', font="Helvetica 12").place(x=80, y=200, w=300,
                                                                                                  h=40)
    b6 = Button(root, text="Request History", command=lambda: grid7()).place(x=80, y=250)



    l7 = Label(root, text="Put History", bg='white', font="Helvetica 12").place(x=80, y=400, w=300,
                                                                                                  h=40)
    b7 = Button(root, text="Fill History", command=lambda:donor_history()).place(x=80, y=450)

    v = StringVar()
    root.mainloop()
"""




def donor_list():
    root=Tk()

    root.title("BLOOD BANK")
    root.geometry("1024x720")
    l1 = Label(root, text="List of Donors(made by Admin)", bg='white', font="Helvetica 12").place(x=80, y=200,w=300, h=40)

    b1 = Button(root, text="donor click", command=lambda: grid2()).place(x=80, y=250)

    l2 = Label(root, text="List of Donors(filled via GUI)", bg='white', font="Helvetica 12").place(x=80, y=300,w=300, h=40)

    b2 = Button(root, text="donor click", command=lambda:grid3()).place(x=80, y=350)

    root.mainloop()




def admin_update_page():
    root=Tk()
    root.title("BLOOD BANK")
    root.geometry("1024x720")
    root.configure(background='#FF8F8F')
    l1=Label(root, text="Update the blood info",bg='white',font="Helvetica 12").place(x=80,y=200,w=300,h=40)
    b1=Button(root, text="donor click",command= lambda:blood_info_page()).place(x=80,y=250)
    l2=Label(root,text="Update the contact info",bg='white',font="Helvetica 12").place(x=80,y=300,w=300,h=40)
    b2=Button(root,text="donor click",command=lambda:contact_info_page()).place(x=80,y=350)
    v=StringVar()
    root.mainloop()

def contact_info_page():
    root = Toplevel()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="Name:", bg='white', font="Helvetica 12").place(x=40, y=40)
    l2 = Label(root, text="Donor_id:", bg='white', font="Helvetica 12").place(x=40, y=80)
    l3=  Label(root, text="Admin_id",bg='white',font="Helvetica 12").place(x=40,y=120)
    l4=  Label(root, text="phoneno ",bg='white',font="Helvetica 12").place(x=40,y=160)
    l5=  Label(root, text="address",bg='white',font="Helvetica 12").place(x=40,y=200)
    e1 = Entry(root)
    e1.place(x=140, y=40)
    e2 = Entry(root)
    e2.place(x=140, y=80)
    e3=Entry(root)
    e3.place(x=140,y=120)
    e4=Entry(root)
    e4.place(x=140,y=160)
    e5=Entry(root)
    e5.place(x=140,y=200)
    b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=340)
    b1=Button(root,text="Submit",command=lambda : update_contact_info(e1.get(),e2.get(),e3.get(),e4.get(),e5.get())).place(x=160,y=340)

    #create table Contact_info(dname varchar(30), Donor_id int primary key, Admin_id int, phoneno varchar(30), address varchar(30), foreign key (Donor_id) references donor1(Donor_id),foreign key(Admin_id) references admin1(Admin_id));

def blood_info_page():
    root = Toplevel()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="Name:", bg='white', font="Helvetica 12").place(x=40, y=40)
    l2 = Label(root, text="Donor_id:", bg='white', font="Helvetica 12").place(x=40, y=80)
    l3=  Label(root, text="blood group",bg='white',font="Helvetica 12").place(x=40,y=120)
    l4=  Label(root, text="Admin id ",bg='white',font="Helvetica 12").place(x=40,y=160)
    e1 = Entry(root)
    e1.place(x=140, y=40)
    e2 = Entry(root)
    e2.place(x=140, y=80)
    e3=Entry(root)
    e3.place(x=140,y=120)
    e4=Entry(root)
    e4.place(x=140,y=160)
    b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=340)
    b1=Button(root,text="Submit",command=lambda : update_blood_info(e1.get(),e2.get(),e3.get(),e4.get())).place(x=160,y=340)



def update_blood_info(name,donor_id,blood_group,adminid):
    try:
        cursor.execute("INSERT INTO Blood_info(dname,Donor_id,Blood_group,Admin_id) values(%s,%s,%s,%s)",[name,donor_id,blood_group,adminid])
        db.commit()
        update_donor1(blood_group,donor_id)
    except:
        db.rollback()

def update_contact_info(name,donor_id,admin_id,phoneno,address):
    try:
        cursor.execute("INSERT INTO Contact_info(dname,Donor_id,Admin_id,phoneno,address) values(%s,%s,%s,%s,%s)", [name,donor_id,admin_id,phoneno,address])
        db.commit()
        update_donor1_contact(name,donor_id,admin_id,phoneno,address)
    except:
        db.rollback()

    #create table Contact_info(dname varchar(30), Donor_id int primary key, Admin_id int, phoneno varchar(30), address varchar(30), foreign key (Donor_id) references donor1(Donor_id),foreign key(Admin_id) references admin1(Admin_id));


def update_donor1(blood_group,donor_id):
    try:
        cursor.execute("UPDATE donor1 set bloodgroup=%s where Donor_id=%s",[blood_group,donor_id])
        db.commit()
    except:
        db.rollback()


def update_donor1_contact(name,donor_id,admin_id,phoneno,address):
    try:
        cursor.execute("UPDATE donor1 set phoneno=%s,address=%s where Donor_id=%s",[phoneno,address,donor_id])
        db.commit()
    except:
        db.rollback()







#history
"""
def insert_history(name,donor_id,date1):
    try:
        cursor.execute("INSERT INTO history1(dname,date1) values(%s,%s)",[name,date1])
        db.commit()
    except:
        db.rollback()
"""

def grid7():
    root = Tk()
    root.title("LIST OF DONORS")
    root.geometry("750x500")
    root.configure(background='#ffeadb')
    rows = retrieve7()
    x = 0
    for row in rows:
        l1 = Label(root, text=row[0], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=0, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l2 = Label(root, text=row[1], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
        l3 = Label(root, text=row[2], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=2, sticky='E', padx=5,pady=5, ipadx=5, ipady=5)
        
        x = x + 1
    root.mainloop()


def retrieve7():
    request = "select * from history1"
    try:
        cursor.execute(request)
        rows = cursor.fetchall()
        db.commit()
        return rows
    except:
        db.rollback()


"""
def donor_history():
    root = Tk()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="Name:", bg='white', font="Helvetica 12").place(x=40, y=40)
    l2 = Label(root, text="Donor_id:", bg='white', font="Helvetica 12").place(x=40, y=80)
    l3=  Label(root, text="Date",bg='white',font="Helvetica 12").place(x=40,y=120)
    e1 = Entry(root)
    e1.place(x=140, y=40)
    e2 = Entry(root)
    e2.place(x=140, y=80)
    e3=Entry(root)
    e3.place(x=140,y=120)
    b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=340)
    b1=Button(root,text="Submit",command=lambda:insert_history(e1.get(),e2.get(),e3.get())).place(x=160,y=340)
    root.mainloop()
"""


"""
def insert_history(name,donor_id,date1):
    try:
        cursor.execute("INSERT INTO history1(Donor_id,dname,date1) values(%s,%s,%s)",[Donor_id,name,date1])
        db.commit()
    except:
        db.rollback()
"""
def insert_click(dname,donor_id):
    try:
        cursor.execute("INSERT INTO history1(dname,Donor_id) values(%s,%s)",[dname,donor_id])
        db.commit()
    except:
        db.rollback()


def insert2():
    root = Toplevel()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="Name:", bg='white', font="Helvetica 12").place(x=40, y=40)
    l2 = Label(root, text="Donor_id:", bg='white', font="Helvetica 12").place(x=40, y=80)
    e1 = Entry(root)
    e1.place(x=140, y=40)
    e2 = Entry(root)
    e2.place(x=140, y=80)
    b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=340)
    b1=Button(root,text="Submit",command=lambda : insert_click(e1.get(),e2.get())).place(x=160,y=340)

"""
def insert1():
    root = Toplevel()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="insert:", bg='white', font="Helvetica 12").place(x=40, y=40)
    l2 = Label(root, text="view insert:", bg='white', font="Helvetica 12").place(x=40, y=80)
    e1 = Entry(root)
    e1.place(x=140, y=40)
    e2 = Entry(root)
    e2.place(x=140, y=80)
    b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=340)
    b1=Button(root,text="Submit",command=lambda :insert2()).place(x=160,y=340)
"""

def retrieve8(bloodgroup,city):
    try:
        cursor.execute("select quantity from availability where city= %s and Blood_group=%s",[city,bloodgroup])
        rows = cursor.fetchall()
        db.commit()
        return rows
    except:
        db.rollback()


def grid8(bloodgroup,city):
    root = Tk()
    root.title("LIST OF DONORS")
    root.geometry("750x500")
    root.configure(background='#ffeadb')
    rows = retrieve8(bloodgroup,city)
    x = 0
    for row in rows:
        l1 = Label(root, text=row[0], bg="#d9adad", font="Verdana 15 bold").grid(row=x, column=0, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        #l2 = Label(root, text=row[1], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=1, sticky='E', padx=5,pady=5, ipadx=5, ipady=5)
        # l3 = Label(root, text=row[2], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=2, sticky='E', padx=5,pady=5, ipadx=5, ipady=5)
        b1=Button(root,text="Submit",command=lambda :request88(bloodgroup,city)).place(x=50,y=20)

        
        x = x + 1
    root.mainloop()

def request88(bloodgroup,city):
    try:
        cursor.execute("UPDATE availability set quantity=quantity-1 where city=%s and Blood_group=%s",[city,bloodgroup])
        box.showinfo("info","Requested")
        db.commit()
    except:
        db.rollback()



def stop(root):
    root.destroy()


root.mainloop()





"""

root = Toplevel()

root.title("Admin for filling the forms")root.geometry("1024x768")
    
root.configure(background='#FF8F8F')
l1 = Label(root, text="Name:", bg='white', font="Helvetica 12").place(x=40, y=40)
l2 = Label(root, text="Age:", bg='white', font="Helvetica 12").place(x=40, y=80)
l3 = Label(root, text="Gender:", bg='white', font="Helvetica 12").place(x=40, y=120)
l4 = Label(root, text="Address:", bg='white', font="Helvetica 12").place(x=40, y=220)
l5 = Label(root, text="Contact:", bg='white', font="Helvetica 12").place(x=40, y=260)
e1 = Entry(root)
e1.place(x=120, y=40)
e2 = Entry(root)
e2.place(x=120, y=80)
r1 = Radiobutton(root, text="Male", variable=v, value="Male", command=sel).place(x=120, y=120)
r2 = Radiobutton(root, text="Female", variable=v, value="Female", command=sel).place(x=120, y=150) r3 = Radiobutton(root, text="Other", variable=v, value="Other", command=sel).place(x=120, y=180)
    # e3=Entry(root)
    # e3.place(x=100,y=120)
e4 = Entry(root)
e4.place(x=120, y=220)
e5 = Entry(root)
e5.place(x=120, y=260)
b21 = Button(root, text="Back", command=lambda: stop(root)).place(x=80, y=300)
b11 = Button(root, text="Submit", command=lambda: insertBlood(e1.get(), e2.get(), e3.get())).place(x=150, y=300)

    # b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=300)

    # b1=Button(root,text="Submit",command=lambda : insertDonor(e1.get(),e2.get(),gen,e4.get(),e5.get())).place(x=40,y=300)

root.mainloop()
"""
#1] blood banks near me
