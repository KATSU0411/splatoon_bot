import skeleton
from google_drive_ocr import GoogleOCRApplication

app = GoogleOCRApplication('gcp-key.json')

img_binary, img_erosion, img_path1, img_path2, img_path3 = skeleton.createSkeltonImage()

app.perform_ocr(img_binary)
app.perform_ocr(img_erosion)
app.perform_ocr(img_path1)
app.perform_ocr(img_path2)
app.perform_ocr(img_path3)

