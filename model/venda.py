from qt_core import *
class Venda():
    def __init__(self, id, cliente, funcionario, item_venda, valor):
        self.id = id
        self.cliente = cliente
        self.funcionario = funcionario
        self.item_venda = item_venda
        self.valor = valor