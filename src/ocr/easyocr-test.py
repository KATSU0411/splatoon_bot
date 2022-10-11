import easyocr
import os
import skeleton

ocr_reader = easyocr.Reader(['ja'])

IMG_PATH_BEFORE = os.getcwd() + "/test_images/before_grouping/cut_001.jpg"
img_binary, img_erosion, img_path1, img_path2, img_path3 = skeleton.createSkeltonImage()

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


IMG_PATH1 = os.getcwd() + "/test_images/matching/001.jpg"
IMG_PATH2 = os.getcwd() + "/test_images/matching/002.jpg"

result = ocr_reader.readtext(IMG_PATH1, detail=0)
print(result)
result = ocr_reader.readtext(IMG_PATH2, detail=0)
print(result)
