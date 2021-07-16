import tkinter
from tkCamera import *


class App:

    def __init__(self, window, window_title, video_source):
        self.window = window

        self.window.title(window_title)

        # open video source (by default this will try to open the computer webcam)
        self.vids = []
        # columns=2
        for idx , source in enumerate(video_source):
            vid = tkCamera(self.window, source,40,30)
            # x = idx % columns
            # y = idx // columns
            # vid.grid(row=y, column=x)
            vid.pack()
            self.vids.append(vid)

        # Create a canvas that can fit the above video source size

        self.window.mainloop()


if __name__ == '__main__':
    sources = [
        0,
        # 'https://imageserver.webcamera.pl/rec/krupowki-srodek/latest.mp4',
        # 'https://imageserver.webcamera.pl/rec/skolnity/latest.mp4',
        'https://imageserver.webcamera.pl/rec/krakow4/latest.mp4',
    ]

    # Create a window and pass it to the Application object
    App(tkinter.Tk(), "Tkinter and OpenCV", sources)