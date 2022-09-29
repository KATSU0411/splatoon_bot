import PySimpleGUI as SG
from ahk import AHK

import ctypes
from ctypes.wintypes import HWND, DWORD, RECT

# window位置とサイズ取得
# todo: クラス化

def getWindowRect(window_title):
    target_window_handle = ctypes.windll.user32.FindWindowW(0, window_title)
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(
            target_window_handle, ctypes.pointer(rect))
    print((rect.left, rect.top, rect.right, rect.bottom))
    return (rect.left, rect.top, rect.right, rect.bottom)



SG.theme('LightBlue1')

ahk = AHK()
window_infos = list(ahk.windows())
window_titles = [info.title.decode('utf-8', errors='ignore') for info in window_infos]

layout = [  
            [SG.Text('line text')],
            [SG.Combo(window_titles, default_value='キャプチャする対象を選択', key='WINDOW_TITLE')],
            [SG.Button(button_text='キャプチャ開始', key='START')]
        ]

window = SG.Window(title='splatoon auto move voice chat tool', layout=layout)

while True:
    event, values = window.read()
    if event == SG.WIN_CLOSED:
        break

    if event == 'START':
        title = values['WINDOW_TITLE']
        print(title)

        getWindowRect(title)


window.close
