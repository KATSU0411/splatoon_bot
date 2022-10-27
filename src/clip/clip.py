import cv2
import numpy as np

# 様々な解像度で対応できるよう割合表記
WAITING_PLAYER_CLIP_START_POS = {'x': 0.01, 'y': 0.17}
WAITING_PLAYER_NAME_SIZE = {'width': 0.25, 'height': 0.068}

MATCHING_PLAYER_LEFT_START_POS = {'x': 0.01, 'y': 0.27}
MATCHING_PLAYER_RIGHT_START_POS = {'x': 0.77, 'y': 0.27}
MATCHING_PLYER_NAME_SIZE = {'width': 0.25, 'height': 0.14}

MATCHING_PLAYER_CLIP_AREA = {'height': 0.06, 'y':0.03}

def clipWaitingPlayerName(originImg, playerNum):
    originHeight, originWidth = img.shape[:2]

    nameSizeWidth = int(originWidth * WAITING_PLAYER_NAME_SIZE['width'])
    nameSizeHeight = int(originHeight * WAITING_PLAYER_NAME_SIZE['height'])

    startposX = int(originWidth * WAITING_PLAYER_CLIP_START_POS['x'])
    startposY = int(originHeight * WAITING_PLAYER_CLIP_START_POS['y']) + nameSizeHeight * playerNum 

    clipImg = originImg[startposY : startposY + nameSizeHeight, startposX : startposX + nameSizeWidth]

    return clipImg

def clipWaitingAllPlayerNames(originImg):
    allClipImg = None
    for i in range(10):
        clipImg = clipWaitingPlayerName(img, i)
        if(allClipImg is None):
            allClipImg = clipImg
        else:
            allClipImg = np.vstack([allClipImg, clipImg])

    return allClipImg

def clipMatchingPlayerName(originImg, playerNum, direction="left"):
    originHeight, originWidth = img.shape[:2]

    if(direction == "right") : 
        startPos = MATCHING_PLAYER_RIGHT_START_POS
    elif(direction == "left") :
        startPos = MATCHING_PLAYER_LEFT_START_POS

    nameSizeWidth = int(originWidth * MATCHING_PLYER_NAME_SIZE['width'])
    nameSizeHeight = int(originHeight * MATCHING_PLYER_NAME_SIZE['height'])

    clipAreaHeight = int(originHeight * MATCHING_PLAYER_CLIP_AREA['height'])
    clipAreaStartYOffset = int(originHeight * MATCHING_PLAYER_CLIP_AREA['y'])

    startposX = int(originWidth * startPos['x'])
    startposY = int(originHeight * startPos['y']) + nameSizeHeight * playerNum + clipAreaStartYOffset

    clipImg = originImg[startposY : startposY + clipAreaHeight, startposX : startposX + nameSizeWidth]

    return clipImg

def clipMatchingTeamPlayerNames(originImg, direction="left"):
    allClipImg = None
    for i in range(4):
        clipImg = clipMatchingPlayerName(img, i, direction)
        if(allClipImg is None):
            allClipImg = clipImg
        else:
            allClipImg = np.vstack([allClipImg, clipImg])

        _, width = clipImg.shape[:2]
        padding = np.zeros((50, width, 3), dtype=int)
        allClipImg = np.vstack([allClipImg, padding])

    return allClipImg

if __name__ == '__main__':
    img = cv2.imread('test_images/before_grouping/001.jpg')

    for i in range(10):
        clipImg = clipWaitingPlayerName(img, i)
        cv2.imwrite('test_images/before_grouping/clip_00' + str(i) + '.png', clipImg)

    clipImg = clipWaitingAllPlayerNames(img)
    cv2.imwrite('test_images/before_grouping/clip_all.png', clipImg)

    img = cv2.imread('test_images/matching/001.jpg')
    for i in range(4):
        clipImg = clipMatchingPlayerName(img, i)
        cv2.imwrite('test_images/matching/clip_00' + str(i) + '.png', clipImg)

    clipImg = clipMatchingTeamPlayerNames(img, "left")
    cv2.imwrite('test_images/matching/clip_left.png', clipImg)
    clipImg = clipMatchingTeamPlayerNames(img, "right")
    cv2.imwrite('test_images/matching/clip_right.png', clipImg)
