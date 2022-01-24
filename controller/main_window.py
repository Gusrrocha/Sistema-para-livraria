from qt_core import *
from controller.cliente_page import ClientePage
class MainWindow(QMainWindow):
    def __init__(self, user_logged):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        self.funcionario_label.setText(user_logged)
        self.clientes_btn.clicked.connect(self.showCliente)





    def showCliente(self):
        self.tabela.insertWidget(1, ClientePage())
        self.tabela.setCurrentIndex(1)