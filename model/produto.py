from qt_core import *
class Produto():
    def __init__(self, id, nome, quantidade, valor_venda, valor_compra):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        
    def getProd(self):
        return [self.nome, self.quantidade, self.valor_venda, self.valor_compra]
