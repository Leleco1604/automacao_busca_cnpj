import PySimpleGUI as sg
from time import sleep 

sg.theme('reddit')

#Layout 

tela_login = [
    [sg.Text('Usuário')],
    [sg.Input(key= 'usuario')],
    [sg.Text('Senha')],
    [sg.Input(password_char='*', key= 'senha')],
    [sg.Button('Enviar')],
    [sg.Output(size =(43,10))]
]

# Criar a janela 
janela = sg.Window('Login', layout = tela_login)

#Ler os eventos 
while True:
    event,values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enviar':
        usurario_digitado = values['usuario']
        senha_digitado = values['senha']

        print('Passo 1 feito')
        sleep(5)
        print('Passo 2 feito')
        sleep(5)
        print('Passo 3 feito')
        sleep(5)
