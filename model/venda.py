from qt_core import *
class Venda():
    def __init__(self, id, cliente, funcionario, valor, item_venda=[]):
        self.id = id
        self.cliente = cliente
        self.funcionario = funcionario
        self.valor = valor
        self.item_venda = item_venda
        
    def getSale(self):
        return [self.cliente, self.funcionario, self.valor]

    def getList(self):
        newlist = []
        self.item_venda.extend(newlist)
        return [newlist]