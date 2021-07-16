import numpy as np, cv2

m = np.random.rand(3, 5) * 1000 // 10

reduce_sum = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_SUM)  # 0 - 열방향 축소 합
print(reduce_sum)
reduce_avg = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_AVG)  # 1 - 행방향 축소 평균
reduce_max = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_MAX)  # 열 최대값
reduce_min = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_MIN)  # 행 최소값

print("[m1] = \n%s\n" % m)
print("[m_reduce_sum] =", reduce_sum.flatten())
print("[m_reduce_avg] =", reduce_avg.flatten())
print("[m_reduce_max] =", reduce_max.flatten())
print("[m_reduce_min] =", reduce_min.flatten())
