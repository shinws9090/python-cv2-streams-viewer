import cv2
import numpy as np

image = np.zeros((300, 400), np.uint8)
image.fill(226)
print(image)


title1, title2 = "ddd", "sss"
cv2.namedWindow(title1,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2,cv2.WINDOW_NORMAL)

cv2.imshow(title1, image) # 창 띄우기
cv2.imshow(title2, image)

cv2.resizeWindow(title1,100,100)
cv2.resizeWindow(title2,100,100)

vcap = cv2.VideoCapture(0)
vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 세로 사이즈
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while True:
    ret, frame = vcap.read()
    cv2.imshow("titled2", frame)


cv2.waitKey(0)  # 0 = 엔터키
cv2.destroyWindow()  # 누르면 닫으라는 이벤트
