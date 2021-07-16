import cv2
from openCV.Common.utils import put_string
from tkinter import *


class Video_frame:

    def zoom_bar(self, value):
        self.vcap.set(cv2.CAP_PROP_ZOOM, value)  # 줌 설정

    def focus_bar(self, value):
        print(value)
        self.vcap.set(cv2.CAP_PROP_FOCUS, value)

    def __init__(self, title):
        self.vcap = cv2.VideoCapture(0)  # 0번 카메라 연결
        if self.vcap.isOpened() is None: raise Exception("카메라 연결 안됨")

        cv2.namedWindow(title)  # 윈도우 생성 - 반드시 생성 해야함
        cv2.createTrackbar("zoom", title, 0, 10, self.zoom_bar)
        cv2.createTrackbar("focus", title, 0, 40, self.focus_bar)

        while True:
            ret, frame = self.vcap.read()  # 카메라 영상 받기
            if not ret: break
            if cv2.waitKey(30) >= 0: break

            zoom = int(self.vcap.get(cv2.CAP_PROP_ZOOM))
            focus = int(self.vcap.get(cv2.CAP_PROP_FOCUS))
            put_string(frame, "zoom : ", (10, 240), zoom)  # 줌 값 표시
            put_string(frame, "focus : ", (10, 270), focus)  # 초점 값 표시
            cv2.imshow(title, frame)

        self.vcap.release()


Video_frame("시벌")
root = Tk()
root.title("SiSO")
root.geometry("300x200+1000+100")
root.resizable(True, True)

frame1 = Frame(root, relief="solid", bd=2)
frame1.pack(side="left", fill="both", expand=True)

frame2 = Frame(root, relief="solid", bd=2)
frame2.pack(side="right", fill="both", expand=True)

frame3 = Frame(root, relief="solid", bd=2)
frame3.pack(side="right", fill="both", expand=True)

label1 = Label(frame1, text='Hello')
label1.pack()

label2 = Label(frame2, text='World!')
label2.pack()

root.mainloop()
