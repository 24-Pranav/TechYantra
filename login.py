import sqlite3
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
# from main import Face_Recognition_System


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")

        print("Path to colorful.png:", "Resources/colorful.png")
        print("Path to images.jfif:", "Resources/images.jfif")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        # Background
        img1 = Image.open("Resources/colorful.png")
        img1 = img1.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        # Login Frame
        main_frame = Frame(bg_img, bd=2, bg="lightgreen")
        main_frame.place(x=515, y=130, width=500, height=560)

        imglogo = Image.open("Resources/login.png")
        imglogo = imglogo.resize((80, 80), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(imglogo)
        lbl_img = Label(self.root, image=self.photoimg2)
        lbl_img.place(x=735, y=150, width=80, height=80)

        student_label = Label(main_frame, text="Get Started...", bg="lightgreen", font=("times new roman", 30, "bold"),
                              fg="purple")
        student_label.place(x=150, y=100)

        student_label = Label(main_frame, text="Username ", bg="lightgreen", font=("times new roman", 20, "bold"), )
        student_label.place(x=180, y=160)

        # User name
        self.txtuser = ttk.Entry(main_frame, width=24, font=("times new roman", 20, "bold"))
        self.txtuser.place(x=80, y=200)

        student_label = Label(main_frame, text="Password ", bg="lightgreen", font=("times new roman", 20, "bold"), )
        student_label.place(x=180, y=260)

        # Password
        self.txtpwd = ttk.Entry(main_frame, width=24, font=("times new roman", 20, "bold"))
        self.txtpwd.place(x=80, y=300)

        # login btn
        self.loginbtn = Button(main_frame, width=8, text="Login", command=self.login, bg="magenta",
                               font=("times new roman", 18, "bold"), activeforeground="white",
                               activebackground="magenta")
        self.loginbtn.place(x=180, y=350)

        # register btn
        self.regbtn = Button(main_frame, text="New User Register", bg="lightgreen",
                             font=("times new roman", 16, "bold"),
                             activeforeground="black", activebackground="lightgreen", border=0,
                             command=self.reg)
        self.regbtn.place(x=150, y=410)

        # forget password btn
        self.btn = Button(main_frame, text="Forget Password", bg="lightgreen", font=("times new roman", 16, "bold"),
                          activeforeground="black", activebackground="lightgreen", border=0,
                          command=self.forget_pwd)
        self.btn.place(x=150, y=450)

    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = sqlite3.connect(r"database.db")
            cursor = conn.cursor()
            cursor.execute("select * from regteach where email='"+self.txtuser.get()+"' and pwd='"+self.txtpwd.get()+"'")
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = sqlite3.connect(r"database.db")
            cursor = conn.cursor()
            query=("select * from regteach where email='"+self.txtuser.get()+"' and ss_que='"+self.var_ssq.get()+"' and s_ans='"+self.var_sa.get()+"'")
            cursor.execute(query)
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd='"+self.var_pwd.get()+"' where email='"+self.txtuser.get()+"'")
                cursor.execute(query)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = sqlite3.connect(r"database.db")
            cursor = conn.cursor()
            query=("select * from regteach where email='"+self.txtuser.get()+"'")
            cursor.execute(query)
            row=cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)
            conn.commit()
            conn.close()


if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.state('zoomed')
    root.mainloop()