#Com modificação de fotos

from ctypes import alignment
from turtle import right
from PySimpleGUI import PySimpleGUI as sg
import csv, os

diretorio_csv = os.getcwd()
diretorio_save = os.getcwd()

sg.theme('Material1')
layout = [
    [sg.Text('Selecione o arquivo ".csv":')], 
    [sg.InputText(key='-FILE_PATH-'), 
    sg.FileBrowse(initial_folder =diretorio_csv, file_types = [("CSV Files", "*.csv")])],
    [sg.Text('Selecione o local da pasta:')],
    [sg.InputText(key='folder'), 
     sg.FolderBrowse()],
    [sg.Button('Iniciar Extração'), sg.Button('Sair')], 
    [sg.Image(filename="favicon-16x16.png", =(right))]
]

window = sg.Window("Extrator de Imagens - Betha Sistemas Ltda.", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Sair'):
        break
      
window.close()
