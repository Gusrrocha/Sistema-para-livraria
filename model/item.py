class Item():
    def __init__(self, id, produto_id, id_venda, produto_nome, quantidade, produto_valor):
        self.id = id
        self.produto_id = produto_id
        self.id_venda = id_venda
        self.produto_nome = produto_nome
        self.quantidade = quantidade
        self.produto_valor = produto_valor
    
    def getItem(self):
        return [self.produto_nome, self.quantidade, self.produto_valor]