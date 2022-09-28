import PySimpleGUI as SG

SG.theme('LightBlue1')

layout = [  [SG.Text('line text')],
        [SG.Text('input'), SG.InputText()],
        [SG.Button('OK'), SG.Button('Cancel')] ]

window = SG.Window(title='splatoon auto move voice chat tool', layout=layout)

while True:
    event, values = window.read()
    if event == SG.WIN_CLOSED:
        break

window.close
