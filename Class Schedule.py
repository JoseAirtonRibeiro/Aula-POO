from Class Contact import *

class Schedule:
    def __init__(self):
        self.contact_list = []

    def save_contact(self):
        ent_name = input('Insira o nome: ')
        ent_cod = input('Insira o código: ')
        ent_phone = input('Insira o telefone: ')
        self.contact_list.append(Contact(ent_cod, ent_name, ent_phone))
        print('DATA SAVED!')

    def list_cont_all(self):
        for i in range(len(self.contact_list))
        print('Nome: 'self.contact_list[i].name, 'Telefone: 'self.contact_list[i].phone,'Código: 'self.contact_list[i].cod)