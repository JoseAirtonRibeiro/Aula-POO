from Class Contact import *
from Class Schedule import *
from tkinter import *
import mysql.connector
#_______________________
class Menu
def __init__(self): 
    schedule_obj = Schedule()

    while True:
        start = input('Informe opção desejada\n
                       '[1] - Novo contato\n'
                       '[2] - Listar Contatos\n'
                       '[0] - Sair\n')
        if start == '1':
            schedule_obj.save_contact()
        elif start == '2':
            schedule_obj.list_cont_all()
        elif start == '0':
            break
        else:
            print('Opção Inválida')


