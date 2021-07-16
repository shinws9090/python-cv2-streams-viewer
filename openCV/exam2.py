import cv2
import numpy as np


def onChange(fg_pass_mask, logo):  # 트랙바 콜백 함수
    global frame
    global value1

    ret, frame = vcap.read()
    frame = cv2.flip(frame, 1)

    if frame is None or logo is None:
        print(logo)
        raise Exception("영상 파일 읽기 오류 ")

    (H, W), (h, w) = frame.shape[:2], logo.shape[:2]  # 로고 영상 크기
    x, y = (W - w) // 2, (H - h) // 2
    roi = frame[y:y + h, x:x + w]  # 관심 영역(roi) 지정

    bg_pass_mask = cv2.bitwise_not(fg_pass_mask)  # 배경 통과 마스크

    foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)  # 로고의 전경 복사

    background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)  # roi에 원본배경만 복사

    dst2 = cv2.add(background, foreground)  # 로고 전경과 원본 배경 간 합성
    a = 1.0 - value1 / 100
    dst = cv2.addWeighted(roi, value1 / 100, dst2, a, 0)
    frame[y:y + h, x:x + w] = dst  # 합성 영상을 원본에 복사

    # # cvs2.waitKey(1) 1은 밀리세컨으로 키입력값 대기 지연시간이다. ESC로 멈춤
    # if cv2.waitKey(1) == 27:
    #     vcap.release()  # 메모리 해제
    #     cv2.destroyAllWindows()  # 모든창 제거, 특정 창만듣을 경우 ("VideoFrame")


def track(value):
    global value1
    value1 = value


def track2(value):
    global value2
    value2 = value


def logoMask():
    img = cv2.imread("img.png", cv2.IMREAD_COLOR)
    logo = cv2.resize(img, dsize=(300, 300), interpolation=cv2.INTER_AREA)

    masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY_INV)[1]  # 로고 영상 이진화
    masks = cv2.split(masks)

    fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])  # 전경 통과 마스크
    return (cv2.bitwise_or(masks[2], fg_pass_mask), logo)


def ratios():
    global value2
    ret, frame = vcap.read()
    frame = cv2.flip(frame, 1)
    r, g, b = cv2.split(frame)

    (min_val1, max_val1, _, _) = cv2.minMaxLoc(r)  # 최솟값과 최댓값 가져오기
    (min_val2, max_val2, _, _) = cv2.minMaxLoc(g)  # 최솟값과 최댓값 가져오기
    (min_val3, max_val3, _, _) = cv2.minMaxLoc(b)  # 최솟값과 최댓값 가져오기
    # print(min_val, max_val)
    try:
        ratio_r = value2 / (max_val1 - min_val1)
        ratio_g = value2 / (max_val2 - min_val2)
        ratio_b = value2 / (max_val3 - min_val3)
    except ZeroDivisionError:
        pass

    r = np.round((r - min_val1) * ratio_r).astype('uint8')
    g = np.round((g - min_val2) * ratio_g).astype('uint8')
    b = np.round((b - min_val3) * ratio_b).astype('uint8')
    return cv2.merge((r, g, b))


if __name__ == "__main__":
    value1 = 0
    value2 = 0
    frame = None
    vcap = cv2.VideoCapture(0)

    fg_pass_mask, logo = logoMask()

    onChange(fg_pass_mask, logo)
    cv2.imshow("VideoFrame", frame)
    cv2.createTrackbar("Brightness", "VideoFrame", 0, 100, track)  # 트랙바 콜백 함수 등록

    dst = ratios()
    cv2.imshow("VideoFrame2", dst)
    cv2.createTrackbar("Brightness", "VideoFrame2", 0, 255, track2)  # 트랙바 콜백 함수 등록

    while True:
        onChange(fg_pass_mask, logo)
        cv2.imshow("VideoFrame", frame)

        dst = ratios()
        cv2.imshow("VideoFrame2", dst)

        if cv2.waitKey(1) == 27:
            vcap.release()  # 메모리 해제
            cv2.destroyAllWindows()  # 모든창 제거, 특정 창만듣을 경우 ("VideoFrame")
