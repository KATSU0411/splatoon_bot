import cv2
import os
import numpy as np

IMG_OUT_PATH_BINARY = os.getcwd() + "/test_images/out/binary.png"
IMG_OUT_PATH_EROSION = os.getcwd() + "/test_images/out/erosion.png"
IMG_OUT_PATH1 = os.getcwd() + "/test_images/out/skelton_test1.png"
IMG_OUT_PATH2 = os.getcwd() + "/test_images/out/skelton_test2.png"
IMG_OUT_PATH3 = os.getcwd() + "/test_images/out/skelton_test3.png"

def createSkeltonImage(imgPath):
    img = cv2.imread(imgPath)
    img_gray =  cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, img_binary = cv2.threshold(img_gray, 180, 255, cv2.THRESH_BINARY)

    img_ske1 = cv2.ximgproc.thinning(img_binary, thinningType=cv2.ximgproc.THINNING_ZHANGSUEN)
    img_ske2 = cv2.ximgproc.thinning(img_binary, thinningType=cv2.ximgproc.THINNING_GUOHALL)

    kernel = np.ones((2, 2), np.uint8)
    img_erosion = cv2.erode(img_binary, kernel, iterations=1)

    img_ske3 = cv2.ximgproc.thinning(img_erosion, thinningType=cv2.ximgproc.THINNING_ZHANGSUEN)

    cv2.imwrite(IMG_OUT_PATH_BINARY, img_binary)
    cv2.imwrite(IMG_OUT_PATH_EROSION, img_erosion)
    cv2.imwrite(IMG_OUT_PATH1, img_ske1)
    cv2.imwrite(IMG_OUT_PATH2, img_ske2)
    cv2.imwrite(IMG_OUT_PATH3, img_ske3)

    return IMG_OUT_PATH_BINARY, IMG_OUT_PATH_EROSION, IMG_OUT_PATH1, IMG_OUT_PATH2, IMG_OUT_PATH3

