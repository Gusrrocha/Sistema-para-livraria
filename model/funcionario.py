from qt_core import *
class Funcionario():
    def __init__(self, id, nome_de_usuario, senha, email):
        self.id = id
        self.nome_de_usuario = nome_de_usuario
        self.senha = senha
        self.email = email
    
    def getWorker(self):
        return [self.nome_de_usuario, self.senha, self.email]
        
        