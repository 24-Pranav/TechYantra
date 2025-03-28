from tkinter import *
from tkinter import ttk
from train import Train
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1800x900+0+0")
        self.root.title("Face Recogonition System")

# This part is image labels setting start
        # first header image
        img = Image.open(r"Resources\colorful.png")
        img = img.resize((1600, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1600, height=130)

        # backgorund image
        bg1 = Image.open("Resources/bg4.png")
        bg1 = bg1.resize((1600, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1600, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Developer Panel", font=(
            "verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1560, height=45)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # student button 1
        std_img_btn = Image.open(
            r"Resources\Pranav.jpg")
        std_img_btn = std_img_btn.resize((220, 220), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, image=self.std_img1, cursor="hand2")
        std_b1.place(x=130, y=200, width=220, height=220)

        std_b1_1 = Button(bg_img, text="Pranav Rajput", cursor="hand2", font=(
            "tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=130, y=380, width=220, height=45)

        # Detect Face  button 2
        det_img_btn = Image.open(
            r"Resources\Pranav.jpg")
        det_img_btn = det_img_btn.resize((220, 220), Image.LANCZOS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, image=self.det_img1, cursor="hand2",)
        det_b1.place(x=385, y=200, width=220, height=220)

        det_b1_1 = Button(bg_img, text="Pranav Rajput", cursor="hand2", font=(
            "tahoma", 15, "bold"), bg="white", fg="navyblue")
        det_b1_1.place(x=385, y=380, width=220, height=45)

        # Attendance System  button 3
        att_img_btn = Image.open(
            r"Resources\Pranav.jpg")
        att_img_btn = att_img_btn.resize((220, 220), Image.LANCZOS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, image=self.att_img1, cursor="hand2",)
        att_b1.place(x=645, y=200, width=220, height=220)

        att_b1_1 = Button(bg_img, text="Pranav Rajput", cursor="hand2", font=(
            "tahoma", 15, "bold"), bg="white", fg="navyblue")
        att_b1_1.place(x=645, y=380, width=220, height=45)

        # Help  Support  button 4
        hlp_img_btn = Image.open(
            r"Resources\Pranav.jpg")
        hlp_img_btn = hlp_img_btn.resize((220, 220), Image.LANCZOS)
        self.hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img, image=self.hlp_img1, cursor="hand2",)
        hlp_b1.place(x=900, y=200, width=220, height=220)

        hlp_b1_1 = Button(bg_img, text="Pranav Rajput", cursor="hand2", font=(
            "tahoma", 15, "bold"), bg="white", fg="navyblue")
        hlp_b1_1.place(x=900, y=380, width=220, height=45)

        # Help  Support  button 4
        hlp_img_btn2 = Image.open(
            r"Resources\Pranav.jpg")
        hlp_img_btn2 = hlp_img_btn2.resize((220, 220), Image.LANCZOS)
        self.hlp_img2 = ImageTk.PhotoImage(hlp_img_btn2)

        hlp_b2 = Button(bg_img, image=self.hlp_img2, cursor="hand2",)
        hlp_b2.place(x=1160, y=200, width=220, height=220)

        hlp_b1_2 = Button(bg_img, text="Pranav Rajput", cursor="hand2", font=(
            "tahoma", 15, "bold"), bg="white", fg="navyblue")
        hlp_b1_2.place(x=1160, y=380, width=220, height=45)

        title_lb1 = Label(bg_img, text="Team TechYantra", font=(
            "verdana", 20, "bold"), bg="white", fg="salmon")
        title_lb1.place(x=0, y=500, width=1560, height=45)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.state('zoomed')
    root.mainloop()