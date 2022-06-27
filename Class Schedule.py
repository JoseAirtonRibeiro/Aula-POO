from Contact import *

class Schedule:
    def __init__(self):
        self.contact_list = []

    def save_contact(self):
        ent_cod = input('Insira o código: ')
        ent_name = input('Insira o nome: ')
        ent_phone = input('Insira o telefone: ')
        self.contact_list.append(Contact(ent_cod, ent_name, ent_phone))
        print('DATA SAVED!')

    def list_cont_all(self):
        for i in range(len(self.contact_list))
        print('Nome: ',self.contact_list[i].name, 'Telefone: ',self.contact_list[i].phone,'Código: ',self.contact_list[i].cod)

    def change_phone(self):
        entrada2 = input('Informe o código do contato')
        for i in range(len(self.contact_list)):
            if entrada1 == self.contact_list[i].cod:
                self.contact_list[i].phone = input('Novo Numero: ')
            else:
                print('Contato não encontrado')