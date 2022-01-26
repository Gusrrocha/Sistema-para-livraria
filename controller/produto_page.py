from qt_core import *
class ProP(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/produto.ui', self)
        self.mainWindow = mainWindow

        self.painel_produtos.verticalHeader().setVisible(False)
        self.painel_produtos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.painel_produtos.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.add_produto_btn.clicked.connect(self.add_produto)

    
    def add_produto(self):
        self.mainWindow.showAdd()
