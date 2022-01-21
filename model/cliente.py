from qt_core import *
class Cliente():
    def __init__(self, id, nome, telefone, endereco, cpf):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cpf = cpf

    def getCostumer(self):
        return [self.nome, self.telefone, self.endereco, self.cpf]

