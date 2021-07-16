import time
import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
from MyVideoCapture import *


class App:
    def __init__(self, window, window_title, video_source):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.vid = MyVideoCapture(video_source)
        self.canvas = tk.Canvas(window,
                                width=self.vid.width,
                                height=self.vid.height)
        self.canvas.pack()

        self.btn_snapshot = tk.Button(window,text="Snapshot",width=50,command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.delay = 15
        self.update()

        self.window.mainloop()

    def snapshot(self):
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-"+time.strftime("%d-%m-%Y-%H-%M-%S")+".jpg",
                        cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            # 파이썬 이미지 랭귀지 (비디오 정보를 Canvas에 넣기위한 처리작업)
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update)


App(tk.Tk(), "Tkinter an Opencv", 0)
