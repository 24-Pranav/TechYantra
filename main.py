from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1520x800+0+0")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()


        #
        # baground image
        img1 = Image.open("Resources/colorful.png")
        img1 = img1.resize((1540, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1540, height=800)

        imglogo = Image.open("Resources/register.png")
        imglogo = imglogo.resize((500, 620), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(imglogo)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=140, y=80, width=500, height=640)

        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=640, y=80, width=760, height=640)

        register_label = Label(frame, text="REGISTER HERE ", bg="white", font=("times new roman", 25, "bold"),
                               fg="magenta")
        register_label.place(x=20, y=20)

        # labels and entry
        fname = Label(frame, text="First Name", bg="white", font=("times new roman", 16, "bold"), )
        fname.place(x=60, y=80)

        self.fname_entry = ttk.Entry(frame, font=("times new roman", 16, "bold",), textvariable=self.var_fname)
        self.fname_entry.place(x=60, y=120)

        lname = Label(frame, text="Last Name", bg="white", font=("times new roman", 16, "bold"), )
        lname.place(x=380, y=80)

        self.lname_entry = ttk.Entry(frame, font=("times new roman", 16, "bold"), textvariable=self.var_lname)
        self.lname_entry.place(x=380, y=120)

        contact = Label(frame, text="Contact No", bg="white", font=("times new roman", 16, "bold"), )
        contact.place(x=60, y=180)

        self.contact_entry = ttk.Entry(frame, font=("times new roman", 16, "bold"), textvariable=self.var_cnum)
        self.contact_entry.place(x=60, y=220)

        email = Label(frame, text="Email", bg="white", font=("times new roman", 16, "bold"), )
        email.place(x=380, y=180)

        self.email_entry = ttk.Entry(frame, font=("times new roman", 16, "bold"), textvariable=self.var_email)
        self.email_entry.place(x=380, y=220)

        security = Label(frame, text="Select Security Questions", bg="white", font=("times new roman", 16, "bold"), )
        security.place(x=60, y=280)

        self.combo_security_Q = ttk.Combobox(frame, font=("times new roman", 16, "bold"), state="readonly",
                                             textvariable=self.var_ssq)
        self.combo_security_Q["values"] = ("Select", "Your Birth Place ", "Your Pet name")
        self.combo_security_Q.place(x=60, y=320, width=230)
        self.combo_security_Q.current(0)

        security_ans = Label(frame, text="Security Answer", bg="white", font=("times new roman", 16, "bold"), )
        security_ans.place(x=380, y=280)

        self.security_entry = ttk.Entry(frame, font=("times new roman", 16, "bold"), textvariable=self.var_sa)
        self.security_entry.place(x=380, y=320)

        password = Label(frame, text="Password", bg="white", font=("times new roman", 16, "bold"), )
        password.place(x=60, y=380)

        self.password_entry = ttk.Entry(frame, font=("times new roman", 16, "bold"), textvariable=self.var_pwd)
        self.password_entry.place(x=60, y=420)

        Confirm_password = Label(frame, text="Confirm Password", bg="white", font=("times new roman", 14, "bold"), )
        Confirm_password.place(x=380, y=380)

        self.confirm_entry = ttk.Entry(frame, font=("times new roman", 16, "bold"), textvariable=self.var_cpwd)
        self.confirm_entry.place(x=380, y=420)

        # checkbutton
        self.checkBtn = Checkbutton(frame, bg="white", text="I Agree The Terms &  Condition",
                                    font=("times new roman", 16, "bold"), variable=self.var_check)
        self.checkBtn.place(x=60, y=470)

        term = Label(frame, text="I Agree The Terms &  Condition", bg="white", font=("times new roman", 14, "bold"), )
        term.place(x=85, y=475)

        self.btn = Button(frame, text="Register Now ", bg="lightgreen", font=("times new roman", 16, "bold"),
                          command=self.reg)
        self.btn.place(x=60, y=530, width=225, height=40)

        self.btn = Button(frame, text="Login Now ", bg="slateblue", font=("times new roman", 16, "bold"), command=lambda :self.register("login"))
        self.btn.place(x=380, y=530, width=225, height=40)

        # end






    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = sqlite3.connect(r"database.db")
                mycursor = conn.cursor()
                query="select * from regteach where email='"+self.var_email.get()+"'"
                mycursor.execute(query)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into regteach values('"+self.var_fname.get()+"','"+self.var_lname.get()+"','"+self.var_cnum.get()+"','"+self.var_email.get()+"','"+self.var_ssq.get()+"','"+self.var_sa.get()+"','"+self.var_pwd.get()+"')")
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.state('zoomed')
    root.mainloop()