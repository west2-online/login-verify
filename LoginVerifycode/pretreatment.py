import cv2

codes = ["7532", "2183", "3744", "6388", "1320"]
width = 6
height = 10
site = [2, 12, 32, 42]

for n in range(1, 6):
    img = cv2.imread(f'data/{n}.bmp', cv2.IMREAD_GRAYSCALE)
    img = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY_INV)[1]
    code = codes[n - 1]
    for i in range(4):
        s = site[i]
        c = code[i]
        cv2.imwrite(f"data/num_{c}.bmp", img[:, s:s + width])
