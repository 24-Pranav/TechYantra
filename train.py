from tkinter import*
from PIL import Image,ImageTk
import os
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Train Pannel")

        # baground image
        img1 = Image.open("Resources/colorful.png")
        img1 = img1.resize((1600, 800), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1600, height=800)

        title_lbl = Label(bg_img, text="  ---- TRAIN DATASET ----  ", font=("times new roman", 30, "bold"), bg="gold",
                          fg="black")
        title_lbl.place(x=510, y=20)

        img_left = Image.open("Resources/peoples.jpg")
        img_left = img_left.resize((1550, 690), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        bg_img = Label(self.root, image=self.photoimg_left)
        bg_img.place(x=-5, y=100, width=1550, height=690)

        # Create buttons below the section
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button
        img6 = Image.open("Resources/traindata.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.train_classifier)
        b1.place(x=670, y=200, width=220, height=220)
        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_classifier,
                      font=("times new roman", 20, "bold"), bg="lightpink")
        b1_1.place(x=670, y=380, width=220, height=40)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.state('zoomed')
    root.mainloop()