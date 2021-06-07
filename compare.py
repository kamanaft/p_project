import PySimpleGUI as sg

layout = [
    [sg.Text('File 1'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('MD5'), sg.Checkbox('SHA1')
     ],
    [sg.Text('File 2'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('SHA256')
     ],
    [sg.Output(size=(80, 20))],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('File Compare', layout)
while True:
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break


