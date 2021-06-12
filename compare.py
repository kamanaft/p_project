import PySimpleGUI as sg
import hashlib

# Interface
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
    if event not in (None, 'Exit', 'Cancel'):
        continue
    break

# Function to work with hash
def hash(file, alg):
    if alg == 'MD5':
        hash = hashlib.md5()
    elif alg == 'SHA1':
        hash = hashlib.sha1()
    elif alg == 'SHA256':
        hash = hashlib.sha256()
    with open(file) as set:
        for str in set:
            hash.update(str.encode(encoding = 'utf-8'))
    return(hash.hexdigest())





