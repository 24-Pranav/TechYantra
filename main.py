from tkinter import*
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from helpsupport import Helpsupport

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("STUDENT TRACKING PROGRESS SYSTEM")

# This part is image labels setting start 
        # baground image
        img1 = Image.open("Resources/colorful.png")
        img1 = img1.resize((1920, 1080), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        title_lbl = Label(bg_img, text="  ---- STUDENT ATTENDENCE DASHBOARD ----  ", font=("times new roman", 35, "bold"),
                          bg="gold", fg="black")
        title_lbl.place(x=265, y=90)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 

        # student details button
        img2 = Image.open("Resources/images.jfif")
        img2 = img2.resize((220, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)
        b1 = Button(bg_img, image=self.photoimg3, cursor="hand2", command=self.student_pannels)
        b1.place(x=265, y=200, width=220, height=220)
        b1_1 = Button(bg_img, text="Student Details", command=self.student_pannels, cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="lightpink")
        b1_1.place(x=265, y=400, width=220, height=40)

        # Detect face
        img3 = Image.open("Resources/scan.png")
        img3 = img3.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img3)
        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.face_rec)
        b1.place(x=515, y=200, width=220, height=220)
        b1_1 = Button(bg_img, text="Face Detector", command=self.face_rec, cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="lightpink")
        b1_1.place(x=515, y=400, width=220, height=40)

        # Attendence
        img4 = Image.open("Resources/attendence.png")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg5, command=self.attendance_pannel, cursor="hand2")
        b1.place(x=765, y=200, width=220, height=220)
        b1_1 = Button(bg_img, text="Attendance", command=self.attendance_pannel, cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="lightpink")
        b1_1.place(x=765, y=400, width=220, height=40)

        # help desk
        img5 = Image.open("Resources/helpdesk.png")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.helpSupport, )
        b1.place(x=1015, y=200, width=220, height=220)
        b1_1 = Button(bg_img, text="Help desk", cursor="hand2", command=self.helpSupport,
                      font=("times new roman", 20, "bold"), bg="lightpink")
        b1_1.place(x=1015, y=400, width=220, height=40)
        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........

        # Train face button
        img6 = Image.open("Resources/traindata.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.train_pannels)
        b1.place(x=265, y=450, width=220, height=220)
        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_pannels,
                      font=("times new roman", 20, "bold"), bg="lightpink")
        b1_1.place(x=265, y=650, width=220, height=40)

        # Photos button
        img7 = Image.open("Resources/pics.png")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.open_img)
        b1.place(x=515, y=450, width=220, height=220)
        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img,
                      font=("times new roman", 20, "bold"), bg="lightpink")
        b1_1.place(x=515, y=650, width=220, height=40)

        # Developer button
        img8 = Image.open("Resources/developer.png")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.developr)
        b1.place(x=765, y=450, width=220, height=220)
        b1_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developr,
                      font=("times new roman", 20, "bold"), bg="lightpink")
        b1_1.place(x=765, y=650, width=220, height=40)

        # Exit button
        img9 = Image.open("Resources/exit.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.Close)
        b1.place(x=1015, y=450, width=220, height=220)
        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 20, "bold"), bg="lightpink",command=self.Close)
        b1_1.place(x=1015, y=650, width=220, height=40)

# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    def Close(self):
        root.destroy()
    
    def open_img(self):
        os.startfile("data_img")



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.state('zoomed')
    root.mainloop()
