import cv2
import os
import numpy as np

IMG_PATH = "test_images/matching/001.jpg"

def createLaplacian(img_path):
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    img_laplacian = cv2.Laplacian(img_gray, cv2.CV_32F, ksize=3)

    output_path = os.path.dirname(img_path) + "/laplacian.png"
    cv2.imwrite(output_path, img_laplacian)
    return output_path

def createSobel(img_path):
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_sobel_x = cv2.Sobel(img_gray, cv2.CV_32F, 1, 0, ksize=3)
    img_sobel_y = cv2.Sobel(img_gray, cv2.CV_32F, 0, 1, ksize=3)

    img_sobel = np.sqrt(img_sobel_x ** 2 + img_sobel_y ** 2)

    output_path = os.path.dirname(img_path) + "/sobel.png"
    cv2.imwrite(output_path, img_sobel)
    return output_path

def extractSaturation(img_path):
    img = cv2.imread(img_path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img_saturation = img_hsv[:, :, 1]

    output_path = os.path.dirname(img_path) + "/saturation.png"
    cv2.imwrite(output_path, img_saturation)
    return output_path

def templateMatching(img_path, template_path):

    return img_path

if __name__ == '__main__':
    saturation_path = extractSaturation(IMG_PATH)
    createLaplacian(saturation_path)
    createSobel(saturation_path)
