import numpy as np, cv2

image = cv2.imread("images/bit_test.jpg", cv2.IMREAD_COLOR)  # 원본 영상 읽기
logo2 = cv2.imread("images/img.png", cv2.IMREAD_COLOR)  # 로고 영상 읽기
logo = cv2.resize(logo2, dsize=(300, 300), interpolation=cv2.INTER_AREA)
if image is None or logo is None: raise Exception("영상 파일 읽기 오류 ")

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY_INV)[1]  # 로고 영상 이진화
masks = cv2.split(masks)
# print(masks)
cv2.imshow("s1", masks[0])
cv2.imshow("s2", masks[1])
cv2.imshow("s3", masks[2])
fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])  # 전경 통과 마스크
cv2.imshow("sss2", fg_pass_mask)
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
cv2.imshow("sss3", fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)  # 배경 통과 마스크
cv2.imshow("sss4", bg_pass_mask)

(H, W), (h, w) = image.shape[:2], logo.shape[:2]  # 로고 영상 크기
x, y = (W - w) // 2, (H - h) // 2
roi = image[y:y + h, x:x + w]  # 관심 영역(roi) 지정
cv2.imshow("sss5", roi)

# 행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)  # 로고의 전경 복사
cv2.imshow("forground", foreground)
background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)  # roi에 원본배경만 복사
cv2.imshow("background", background)

dst = cv2.add(background, foreground)  # 로고 전경과 원본 배경 간 합성

cv2.imshow("dst", dst)
image[y:y + h, x:x + w] = dst  # 합성 영상을 원본에 복사

cv2.imshow("image", image)

cv2.waitKey()
