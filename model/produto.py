from qt_core import *
class Produto():
    def __init__(self, id, img, nome, quantidade, autor, valor_venda, valor_compra):
        self.id = id
        self.img = img
        self.nome = nome
        self.quantidade = quantidade
        self.autor = autor
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        
    def getProd(self):
        return [self.img, self.nome, self.quantidade, self.autor, self.valor_venda, self.valor_compra]
