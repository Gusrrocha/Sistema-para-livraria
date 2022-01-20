from qt_core import *
class ClientePage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/cliente.ui', self)

        self.cancel_edit_btn.hide()
        self.remover_btn.clicked.connect(self.remover)
        self.salvar_btn.clicked.connect(self.salvar)
        self.painel_clientes.verticalHeader().setVisible(False)
        self.painel_clientes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.painel_clientes.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.cancel_edit.clicked.connect(self.stopEdit)
        self.load()
        self.painel_clientes.clicked.connect(self.cL)


    def remover(self):
        pass

    def salvar(self):
        pass

    def stopEdit(self):
        pass

    def cL(self):
        pass

    def clear_(self):
        pass

        