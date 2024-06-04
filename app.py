import PySimpleGUI as sg

sg.theme('reddit')

#Layout 

tela_login = [
    [sg.Text('Usuário')],
    [sg.Input(key= 'usuario')],
    [sg.Text('Senha')],
    [sg.Input(password_char='*', key= 'senha')],
    [sg.Button('Enviar')]
]

#
