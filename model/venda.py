from dataclasses import dataclass
from qt_core import *
class Venda():
    def __init__(self, id, cliente, funcionario, valor, data, parcela):
        self.id = id
        self.cliente = cliente
        self.funcionario = funcionario
        self.valor = valor
        self.data = data
        self.parcela = parcela
        
    def getSale(self):
        return [self.cliente, self.funcionario, self.valor, self.data, self.parcela]
