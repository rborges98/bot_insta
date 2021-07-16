from typing import Text
import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Column
from db import mycursor, conexao

while True:
    mycursor.execute("SELECT * FROM contas_seguir")
        
    myresult = mycursor.fetchall()
    lista = []

    for x in myresult:
        y = x[0]
        lista.append(y)
    
    print(lista)
    col = [[psg.Text('\n'.join(lista))]]

    layout = [
        [psg.Text('Usuario:'), psg.Input(key='usuario')],
        [psg.Text('Senha:  '), psg.Input(key='senha',password_char='*')],
        [psg.Text('Contas: '), psg.Column(col, element_justification = 'c', scrollable=True, vertical_scroll_only=True, size=(300,65))],
        [psg.Button('Rodar bot'), psg.Button('Adicionar conta'), psg.Button('Excluir conta')]
             ]
                
    janela = psg.Window('Bot Instagram', finalize=True, layout=layout)
    event, values = janela.Read()

    usuario = values['usuario']
    senha = values['senha'] 

    if event == 'Rodar bot':
        break

    if event == 'Adicionar conta':

        layout = [
                [psg.Text('Conta'), psg.Input(key='conta')],
                [psg.Button('adicionar'), psg.Button('voltar')]
                ]

        janela2 = psg.Window('Cadastrar conta', finalize=True, layout=layout)
        event, values = janela2.Read()
        conta = values['conta']
        janela.hide()

            
        if event == 'adicionar':
            val = conta
            sql = "INSERT INTO contas_seguir (contas) VALUES (?)"
            mycursor.execute(sql, (val,))
            conexao.commit()
            janela2.hide()

        if event == 'voltar':
            janela2.hide()
            

    if event == 'Excluir conta':

        layout = [
                [psg.Text('Conta'), psg.Input(key='conta')],
                [psg.Button('Excluir'), psg.Button('voltar')]
                 ]

        janela3 = psg.Window('Excluir conta', finalize=True, layout=layout)
        event, values = janela3.Read()
        conta = values['conta']

        janela.hide()
            
        if event == 'Excluir':
            sql = "DELETE FROM contas_seguir WHERE contas = (?);"
            val = conta
            mycursor.execute(sql, (val,))
            conexao.commit()
            janela3.hide()
            

        if event == 'voltar':
            janela3.hide()
            
                    
                

