from statistic.LoginVerifycode import recognize_login_verify_code
import numpy as np
import base64
import cv2

def util_login_validateCode(image_string):
    image_bytes = base64.b64decode(image_string.split(',')[-1])
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    nums = recognize_login_verify_code(image)
    res = nums[0] * 10 + nums[1] + nums[2] * 10 + nums[3]
    return res
