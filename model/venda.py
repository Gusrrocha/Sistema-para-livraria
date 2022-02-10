from dataclasses import dataclass
from qt_core import *
class Venda():
    def __init__(self, id, cliente, funcionario, valor, data):
        self.id = id
        self.cliente = cliente
        self.funcionario = funcionario
        self.valor = valor
        self.data = data
        
    def getSale(self):
        return [self.cliente, self.funcionario, self.valor, self.data]
