import skeleton

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
SHARE_FOLDER_ID = '1tNCvGuuldB5-mGm9q6f_dLRNLJsuspUr'
sa_creds = service_account.Credentials.from_service_account_file('gcp-key.json')
scoped_creds = sa_creds.with_scopes(SCOPES)
drive_service = build('drive', 'v3', credentials=scoped_creds)


i = 1

IMG_PATH_BEFORE = os.getcwd() + '/test_images/before_grouping/clip_00' + str(i) +'.png'
img = cv2.imread(IMG_PATH_BEFORE)
img_binary, img_erosion, img_path1, img_path2, img_path3 = skeleton.createSkeltonImage(img)
