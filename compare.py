import PySimpleGUI as sg
import hashlib
import re

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

# Function to work with hashfiles
def hash(file, alg):
    if alg == 'MD5':
        hash = hashlib.md5()
    elif alg == 'SHA1':
        hash = hashlib.sha1()
    elif alg == 'SHA256':
        hash = hashlib.sha256()
    with open(file) as set:
        for str in set:
            hash.update(str.encode(encoding='utf-8'))
    return hash.hexdigest()

window = sg.Window('File Compare', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        file1 = file2 = flag = None
        if values[0] and values[3]:
            file1 = re.findall('.', values[0])
            file2 = re.findall('.', values[3])
            flag = 1
            if not file1 and file1 is not None:
                print('Error: File 1 path is not valid.')
                flag = 0
            elif not file2 and file2 is not None:
                print('Error: File 2 path is not valid.')
                flag = 0
            elif values[1] is not True and values[2] is not True and values[4] is not True:
                print('Error: Choose at least one encryption algorithm')
            elif flag == 1:
                print('Info: Filepaths were defined.')
                algs = []
                if values[1] == True: algs.append('MD5')
                if values[2] == True: algs.append('SHA1')
                if values[4] == True: algs.append('SHA256')
                filepaths = []
                filepaths.append(values[0])
                filepaths.append(values[3])
                print('Info: File comparison using:', algs)
                for alg in algs:
                    print(alg, ':')
                    print(filepaths[0], ':', hash(filepaths[0], alg))
                    print(filepaths[1], ':', hash(filepaths[1], alg))
                    if hash(filepaths[0], alg) == hash(filepaths[1], alg):
                        print('Files match for ', alg)
                    else:
                        print('Files do NOT match for ', alg)
        else:
            print('Please choose 2 files.')
window.close()


