import cv2
import numpy as np


nums = np.array([(cv2.imread(f"./LoginVerifycode/data/num_{i}.bmp", cv2.IMREAD_GRAYSCALE)).flatten() for i in range(9)])
site = [2, 12, 32, 42]
width = 6


def get_cos_similar_multi(v1, v2):  # 余弦相似度
    num = np.dot([v1], np.array(v2).T)  # 向量点乘
    denom = np.linalg.norm(v1) * np.linalg.norm(v2, axis=1)  # 求模长的乘积
    res = num / denom
    res[np.isneginf(res)] = 0
    return 0.5 + 0.5 * res


def recognize_login_verify_code(img):
    img = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY_INV)[1]
    return [np.argmax(get_cos_similar_multi(img[:, s:s + width].flatten(), nums)) for s in site]


if __name__ == '__main__':
    print(recognize_login_verify_code(cv2.imread("data/2.bmp")))
