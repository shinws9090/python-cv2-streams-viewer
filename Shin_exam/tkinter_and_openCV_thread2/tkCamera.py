import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from MyVideoCapture import MyVideoCapture


class tkCamera(tkinter.Frame):

    def __init__(self, window, source=('0',0), width=None, height=None):
        super().__init__(window)

        self.window = window

        # self.window.title(window_title)
        self.title_name , self.video_source = source
        self.vid = MyVideoCapture(self.video_source, width, height)

        self.title_label = tkinter.Label(self,text=self.title_name)
        self.title_label.pack()

        self.canvas = tkinter.Canvas(self, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot = tkinter.Button(self, text="Snapshot", width=10, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, side="left")

        self.btn_start = tkinter.Button(self, text="start", command=self.video_start)
        self.btn_start.pack(anchor=tkinter.CENTER, side="left")

        self.btn_stop = tkinter.Button(self, text="stop", command=self.video_stop)
        self.btn_stop.pack(anchor=tkinter.CENTER, side="left")

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 100

        self.running = True
        self.update_widget()

    def video_start(self):
        if not self.running:
            self.running = True
            self.update_widget()

    def video_stop(self):
        if self.running:
            self.running = False

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update_widget(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        if self.running:
            self.window.after(self.delay, self.update_widget)
