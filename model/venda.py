from qt_core import *
class Venda():
    def __init__(self, id, cliente, funcionario, valor):
        self.id = id
        self.cliente = cliente
        self.funcionario = funcionario
        self.valor = valor
        
    def getSale(self):
        return [self.cliente, self.funcionario, self.valor]
