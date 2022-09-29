import PySimpleGUI as SG
from ahk import AHK

import ctypes
from ctypes.wintypes import HWND, DWORD, RECT

import mss

# window位置とサイズ取得
# todo: クラス化

def getWindowRect(window_title):
    target_window_handle = ctypes.windll.user32.FindWindowW(0, window_title)
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(
            target_window_handle, ctypes.pointer(rect))
    return (rect.left, rect.top, rect.right, rect.bottom)

# スクショ撮影
# todo: クラス化
def getScreenShot(rect):
    with mss.mss() as sct:
        img = sct.grab(rect)
        raw_image = mss.tools.to_png(img.rgb, img.size)

    return raw_image



SG.theme('LightBlue1')

ahk = AHK()
window_infos = list(ahk.windows())
window_titles = [info.title.decode('utf-8', errors='ignore') for info in window_infos]

layout = [  
            [SG.Text('line text')],
            [SG.Combo(window_titles, default_value='キャプチャする対象を選択', key='WINDOW_TITLE')],
            [SG.Button(button_text='キャプチャ開始', key='START')],
            [SG.Image(key='CAPTURE_IMAGE')]
        ]

window = SG.Window(title='splatoon auto move voice chat tool', layout=layout)

window_title = ''

while True:
    event, values = window.read(timeout=100)
    if event == SG.WIN_CLOSED:
        break

    if event == 'START':
        window_title = values['WINDOW_TITLE']

    if window_title != '':
        rect = getWindowRect(window_title)
        img = getScreenShot(rect)

        window['CAPTURE_IMAGE'].Update(source=img)


window.close
