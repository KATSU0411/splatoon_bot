import skeleton
import io
import os

from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError as HTTPError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']
MIME_TYPE = 'application/vnd.google-apps.document'
SHARE_FOLDER_ID = '1tNCvGuuldB5-mGm9q6f_dLRNLJsuspUr'
sa_creds = service_account.Credentials.from_service_account_file('gcp-key.json')
scoped_creds = sa_creds.with_scopes(SCOPES)
service = build('drive', 'v3', credentials=scoped_creds)


TEMPORARY_FILE_NAME = "ocr.png"
OCR_OUTPUT_FILE_NAME = "ocr.txt"

def ocrPngFile(filePath):
    media_body = MediaFileUpload(filePath, mimetype=MIME_TYPE, resumable=False)

    body = {
            'name': TEMPORARY_FILE_NAME,
            'mimeType': MIME_TYPE,
            'parents': [SHARE_FOLDER_ID],
            }

    drive_file = service.files().create(
            body=body,
            media_body=media_body,
            ocrLanguage='ja',
        ).execute()

    ocr_file_request = service.files().export_media(
            fileId=drive_file['id'],
            mimeType='text/plain',
        )

    ocr_file = io.FileIO(OCR_OUTPUT_FILE_NAME, 'wb')
    downloader = MediaIoBaseDownload(ocr_file, ocr_file_request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()

    service.files().delete(fileId=drive_file['id']).execute()

    result = None
    with open(OCR_OUTPUT_FILE_NAME, encoding='utf-8') as f:
        lines = f.read().splitlines()
        if len(lines) == 3: 
            result = lines[2]

    return result


if __name__ == '__main__':


    for i in range(10):

        IMG_PATH_BEFORE = os.getcwd() + '/test_images/before_grouping/clip_00' + str(i) +'.png'
        # img = cv2.imread(IMG_PATH_BEFORE)
        # img_binary, img_erosion, img_path1, img_path2, img_path3 = skeleton.createSkeltonImage(img)

        ocr_result = ocrPngFile(IMG_PATH_BEFORE)
        print(ocr_result)


