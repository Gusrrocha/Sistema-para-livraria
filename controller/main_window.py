from controller.funcionario import FunOP
from controller.produto_page import ProP
from qt_core import *
from controller.cliente_page import ClientePage
class MainWindow(QMainWindow):
    def __init__(self, user_logged):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        self.user_logged = user_logged

        self.funcionario_label.setText(user_logged+"!")
        self.clientes_btn.clicked.connect(self.showCliente)
        self.produto_btn.clicked.connect(self.produto_page)

        menu = QMenu()
        self.mais_fun.setMenu(menu)
        action_um = menu.addAction('Editar funcionário')
        action_um.triggered.connect(self.edit_fun)
        action_dois = menu.addAction('Sair')
        action_dois.triggered.connect(self.sair)

    def showCliente(self):
        self.tabela.insertWidget(1, ClientePage())
        self.tabela.setCurrentIndex(1)

    def sair(self):
        pass

    def edit_fun(self):
        self.tabela.insertWidget(2, FunOP(self.user_logged))
        self.tabela.setCurrentIndex(2)

    def produto_page(self):
        self.tabela.insertWidget(3, ProP(self))
        self.tabela.setCurrentIndex(3)
        

        
        
