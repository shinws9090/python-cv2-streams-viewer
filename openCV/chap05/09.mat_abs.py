import numpy as np, cv2

image1 = cv2.imread("images/abs_test1.jpg", cv2.IMREAD_GRAYSCALE)  # 명암도 영상 읽기
image2 = cv2.imread("images/abs_test2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")

dif_img1 = cv2.subtract(image1, image2)  # 차분 연산
"""
[dif_img1(roi) uint8] = 
[[ 0  0  0  0  9 12  7]
 [ 0  0  0  0  4  9  3]
 [ 0  0  0 15  0  4  0]]  바로 차분하면 재대로 합성이안됨
"""
dif_img2 = cv2.subtract(np.int16(image1), np.int16(image2))  # 음수 보전 위해
"""
[dif_img2(roi) int16]  = 
[[-100 -106  -80   -6    9   12    7]
 [-105 -109  -72   -4    4    9    3]
 [-106 -109  -58   15   -1    4    0]]  행렬로 변환하여 차분 후 
"""
abs_dif1 = np.absolute(dif_img2).astype('uint8')  # 절댓값 계산
"""
[abs_dif1(roi)] = 
[[100 106  80   6   9  12   7]
 [105 109  72   4   4   9   3]
 [106 109  58  15   1   4   0]] 행렬 차분된것에 대하여 절대값 계산한 이미지가 지대로 합성됨
"""

abs_dif2 = cv2.absdiff(image1, image2)  # 차분 절댓값 계산(다른방식, 차분하고 절대값계산 통합)
"""
[abs_dif2(roi)] = 
[[100 106  80   6   9  12   7]
 [105 109  72   4   4   9   3]
 [106 109  58  15   1   4   0]]  차분하고 절대값 계산된것이 바로나옴
"""

x, y, w, h = 100, 100, 7, 3
print("[dif_img1(roi) uint8] = \n%s\n" % dif_img1[y:y + h, x:x + w])
print("[dif_img2(roi) int16]  = \n%s\n" % dif_img2[y:y + h, x:x + w])
print("[abs_dif1(roi)] = \n%s\n" % abs_dif1[y:y + h, x:x + w])
print("[abs_dif2(roi)] = \n%s\n" % abs_dif2[y:y + h, x:x + w])

titles = ['image1', 'image2', 'dif_img1', 'abs_dif1', 'abs_dif2']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)
