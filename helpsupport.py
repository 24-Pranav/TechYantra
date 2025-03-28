from tkinter import*
from PIL import Image,ImageTk


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1082+0+0")
        self.root.title("Face Recognition System")

        # baground image
        img1 = Image.open("Resources/colorful.png")
        img1 = img1.resize((1600, 900), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1600, height=900)

        title_lbl = Label(bg_img, text="  ---- DEVELOPER HELP EMAIL ----  ", font=("times new roman", 30, "bold"),
                          bg="gold", fg="black")
        title_lbl.place(x=450, y=20)

        main_frame = Frame(bg_img, bd=2, bg="lightyellow")
        main_frame.place(x=20, y=80, width=1490, height=690)

        img_left = Image.open("Resources/desk.jpg")
        img_left = img_left.resize((1410, 620), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        bg_img = Label(self.root, image=self.photoimg_left)
        bg_img.place(x=60, y=120, width=1410, height=620)

        l4 = Label(bg_img,
                   text="Email: rajputpranav996@gmail.com" + "\n" + "         rajputpranav996@gmail.com" + "\n" + "        rajputpranav996@gmail.com" + "\n" + "               rajputpranav996@gmail.com" + "\n" + "              rajputpranav996@gmail.com",
                   font=("times new roman", 15, "bold"), fg="purple")
        l4.place(x=450, y=250, width=500, height=150)




if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.state('zoomed')
    root.mainloop()