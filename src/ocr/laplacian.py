import pyocr
import cv2
import os
import numpy as np

IMG_PATH1 = os.path.dirname(__file__) + "test_images/before_grouping/cut_001.jpg"
IMG_PATH2 = os.path.dirname(__file__) + "test_images/grouped/cut_001.jpg"

engine = pyocr.get_available_tools()[0]

img = cv2.imread(IMG_PATH1)
cv2.imshow('gray', img)

img_gray =  cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img_lap = cv2.Laplacian(img_gray, cv2.CV_32F, ksize=3)

cv2.imshow('lap', np.uint8(img_lap))

cv2.waitKey(0)

cv2.imwrite("test_images/out/test.png", img_lap)
