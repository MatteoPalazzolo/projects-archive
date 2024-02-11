FLAG = './images/flag.jpg'
LEMUR = './images/lemur.jpg'
RESULT = './images/result.jpg'

"""
from PIL import Image, ImageChops
import numpy as np
from matplotlib import cm

im1 = Image.open(FLAG)
im2 = Image.open(LEMUR)
"""

import cv2

img1 = cv2.imread(FLAG)
img2 = cv2.imread(LEMUR)
bitwise_xor = cv2.bitwise_xor(img2, img1)

cv2.imshow("bit_and", bitwise_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()