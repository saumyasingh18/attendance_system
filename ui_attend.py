from tkinter import *
import cv2
import face_recognition
from tkinter import messagebox
import os
from datetime import datetime
import numpy as np
from PIL import Image, ImageTk
class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance System")
        self.root.resizable(True, True)
        # Initialize variables
        self.cap = None
        self.encode_list_known = []
        self.person_names = []
        self.match_found = False

        self.frame = Frame(self.root, height=400, width=400, highlightthickness=5)
        self.frame.pack(side=TOP)
        head = Label(self.frame, text="ATTENDANCE SYSTEM", font="Arial")
        head.grid(row=0, column=0, columnspan=3)
        self.menu = Menu(self.frame)
        self.root.config(menu=self.menu)
        self.menu.add_command(label="Check attendance", command=NONE)
        self.start_button = Button(self.frame, text="Start Attendance", command=self.start_attendance)
        self.start_button.grid(row=2, column=0, columnspan=1)
        self.mark_attendance_button = Button(self.frame, text="Mark Attendance", command=self.mark_attendance, state=DISABLED)
        self.mark_attendance_button.grid(row=2, column=1)
        self.stop_button = Button(self.frame, text="Stop Attendance", command=self.stop_attendance, state=DISABLED)
        self.stop_button.grid(row=2, column=3, columnspan=1, pady=5)
        self.camera_label = Label(self.frame, text="Camera")
        self.camera_label.grid(row=1, column=0, columnspan=3)

    def load_images_and_encode(self, path):
        images = []
        person_names = []
        my_list = os.listdir(path)
        for cu_img in my_list:
            current_img = cv2.imread(f'{path}/{cu_img}')
            images.append(current_img)
            person_names.append(os.path.splitext(cu_img)[0])
        encode_list_known = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encode_list_known.append(encode)
        return encode_list_known, person_names
    def start_attendance(self):

        self.start_button.config(state=DISABLED)
        self.mark_attendance_button.config(state=NORMAL)
        self.stop_button.config(state=NORMAL)
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
        self.encode_list_known, self.person_names = self.load_images_and_encode('images')

        while True:
            ret, frame= self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (640, 480))
                # Detecting face in current camera frame
                faces_current_frame = face_recognition.face_locations(frame)
                encodes_current_frame = face_recognition.face_encodings(frame, faces_current_frame)
                # Iterate over each face in the current frame
                for encode_face, face_loc in zip(encodes_current_frame, faces_current_frame):
                    # Compare the current face with known faces
                    matches = face_recognition.compare_faces(self.encode_list_known, encode_face)
                    face_dis = face_recognition.face_distance(self.encode_list_known, encode_face)
                    match_index = np.argmin(face_dis)

                    if matches[match_index]:
                        self.match_found = True
                        self.match_name = self.person_names[match_index].upper()

                        y1, x2, y2, x1 = face_loc
                        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

                        # Draw rectangle around the face
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                        # Draw name below the face rectangle
                        cv2.putText(frame, self.match_name, (x1 + 6, y2 + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                        self.mark_attendance_button.config(state=NORMAL)
                    else:
                        self.match_found = False
                        self.mark_attendance_button.config(state=DISABLED)

                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.camera_label.imgtk = imgtk
                self.camera_label.configure(image=imgtk)
                self.camera_label.update()

                if cv2.waitKey(1) == 13:
                    break
    def mark_attendance(self):
        with open('Attendance.csv', 'a') as f:
            time_now = datetime.now()
            t_str = time_now.strftime('%H:%M:%S')
            d_str = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{self.match_name},{t_str},{d_str}')
        messagebox.showinfo("Attendance Marked", f"Attendance marked for {self.match_name}")
        self.mark_attendance_button.config(state=DISABLED)

    def stop_attendance(self):
        if self.cap is not None:
            self.cap.release()
            cv2.destroyAllWindows()
        self.start_button.config(state=NORMAL)
        self.stop_button.config(state=DISABLED)
        self.mark_attendance_button.config(state=DISABLED)
if __name__ == "__main__":
   root = Tk()
   app = AttendanceSystem(root)
   root.mainloop()
