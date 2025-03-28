from tkinter import*
from PIL import Image,ImageTk
import sqlite3
import cv2
from datetime import datetime


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Pannel")

        # baground image
        img1 = Image.open("Resources/colorful.png")
        img1 = img1.resize((1600, 800), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1600, height=800)

        main_frame = Frame(bg_img, bd=2, bg="lightyellow")
        main_frame.place(x=-5, y=80, width=1600, height=720)

        img_left = Image.open("Resources/Header03.png")
        img_left = img_left.resize((1515, 680), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        bg_img = Label(self.root, image=self.photoimg_left)
        bg_img.place(x=10, y=100, width=1515, height=680)

        title_lbl = Label(text="  ---- FACE RECOGNITION ----  ", font=("times new roman", 30, "bold"), bg="gold",
                          fg="black")
        title_lbl.place(x=490, y=20)


        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # Detect Face
        img3 = Image.open("Resources/scan.png")
        img3 = img3.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img3)
        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.face_recog)
        b1.place(x=660, y=200, width=220, height=220)
        b1_1 = Button(bg_img, text="Face Detector", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="lightpink")
        b1_1.place(x=660, y=400, width=220, height=40)

    # =====================Attendance===================

    def mark_attendance(self, i, r, n):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])

            if ((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"{i}, {r}, {n}, {dtString}, {d1}, Present\n")

    # ================face recognition==================

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            featuers = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in featuers:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                # messagebox.showinfo("Hello", id)
                confidence = int((100*(1-predict/300)))

                conn = sqlite3.connect(r"database.db")
                cursor = conn.cursor()

                cursor.execute(
                    "select Name from student where Student_ID="+str(id))
                n = cursor.fetchone()
                # messagebox.showinfo("Hello", n)
                n = str(n[0])

                cursor.execute(
                    "select Roll_No from student where Student_ID="+str(id))
                r = cursor.fetchone()
                r = str(r[0])
                cursor.execute(
                    "select Student_ID from student where Student_ID="+str(id))
                i = cursor.fetchone()
                i = str(i[0])

                if confidence > 77:
                    cv2.putText(
                        img, f"Student_ID : {i}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(
                        img, f"Name : {n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(
                        img, f"Roll-No : {r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i, r, n)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, y]

            return coord

        # ==========
        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1,
                                  10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.state('zoomed')
    root.mainloop()