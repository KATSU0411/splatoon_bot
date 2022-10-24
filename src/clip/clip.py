import cv2

# 様々な解像度で対応できるよう割合表記
CLIP_START_POS = {'x': 0.01, 'y': 0.17}
WAITING_PLYER_NAME_SIZE = {'width': 0.25, 'height': 0.068}
def clipWaitingPlayerName(originImg, playerNum):
    originHeight, originWidth = img.shape[:2]

    nameSizeWidth = int(originWidth * WAITING_PLYER_NAME_SIZE['width'])
    nameSizeHeight = int(originHeight * WAITING_PLYER_NAME_SIZE['height'])

    startposX = int(originWidth * CLIP_START_POS['x'])
    startposY = int(originHeight * CLIP_START_POS['y']) + nameSizeHeight * playerNum

    clipImg = originImg[startposY : startposY + nameSizeHeight, startposX : startposX + nameSizeWidth]

    return clipImg

def clipWaitingAllPlayerName(originImg):
    originHeight, originWidth = img.shape[:2]

    nameSizeWidth = int(originWidth * WAITING_PLYER_NAME_SIZE['width'])
    nameSizeHeight = int(originHeight * WAITING_PLYER_NAME_SIZE['height'])

    startposX = int(originWidth * CLIP_START_POS['x'])
    startposY = int(originHeight * CLIP_START_POS['y'])

    clipImg = originImg[startposY : startposY + nameSizeHeight * 10, startposX : startposX + nameSizeWidth]

    return clipImg


if __name__ == '__main__':
    img = cv2.imread('test_images/before_grouping/001.jpg')

    for i in range(10):
        clipImg = clipWaitingPlayerName(img, i)
        cv2.imwrite('test_images/before_grouping/clip_00' + str(i) + '.png', clipImg)

    clipImg = clipWaitingAllPlayerName(img)
    cv2.imwrite('test_images/before_grouping/clip_all.png', clipImg)
