import easyocr
import os
import skeleton
import cv2

ocr_reader = easyocr.Reader(['ja'])


#for i in range(10):

i = 1

IMG_PATH_BEFORE = os.getcwd() + '/test_images/before_grouping/clip_00' + str(i) +'.png'
img = cv2.imread(IMG_PATH_BEFORE)
img_binary, img_erosion, img_path1, img_path2, img_path3 = skeleton.createSkeltonImage(img)

result = ocr_reader.readtext(IMG_PATH_BEFORE, detail=0)
print("元画像", result)
result = ocr_reader.readtext(img_binary, detail=0)
print("バイナリ画像", result)
result = ocr_reader.readtext(img_erosion, detail=0)
print("収縮画像", result)
result = ocr_reader.readtext(img_path1, detail=0)
print("スケルトン1", result)
result = ocr_reader.readtext(img_path2, detail=0)
print("スケルトン2", result)
result = ocr_reader.readtext(img_path3, detail=0)
print("スケルトン3", result)
print('\n')


