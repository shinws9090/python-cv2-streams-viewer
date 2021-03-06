import cv2


class MyVideoCapture:
    def __init__(self, video_source=0,width=None, height=None):
        self.vid = cv2.VideoCapture(video_source)

        if not self.vid.isOpened():
            raise ValueError("영상을 열수 없", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.width = width
        self.height = height

        # 크기값이 없다면
        if not self.width:
            self.width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        if not self.height:
            self.height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.flip(frame, 1)
                frame = cv2.resize(frame, (self.width, self.height))
                return ret, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            else:
                return ret, None
        # else:
        #     return (ret, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        # self.window.mainloop()
