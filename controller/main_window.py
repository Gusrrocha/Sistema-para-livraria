from qt_core import *
import locale
from controller.funcionario import FunOP
from controller.produto_page import ProP
from controller.cliente_page import ClientePage
from controller.venda_page import VendaPg
from controller.estoque import Storage
import model.venda_dao as Sale
import model.item_dao as item_dao
class MainWindow(QMainWindow):
    def __init__(self, user_logged):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        self.user_logged = user_logged
        self.l = []
        self.funcionario_label.setText(user_logged+"!")
        self.clientes_btn.clicked.connect(self.showCliente)
        self.produto_btn.clicked.connect(self.produto_page)
        self.venda_btn.clicked.connect(self.venda_pg)
        self.estoque_btn.clicked.connect(self.estoque)
        self.home_btn.clicked.connect(self.mainPage)
        self.table_venda.verticalHeader().setVisible(False)
        self.table_venda.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_venda.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table_venda.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        menu = QMenu()
        self.mais_fun.setMenu(menu)
        action_um = menu.addAction('Editar funcionário')
        action_um.triggered.connect(self.edit_fun)
        action_dois = menu.addAction('Sair')
        action_dois.triggered.connect(self.sair)
        self.loadSale()

    def mainPage(self):
        item_dao.deleteNull()
        self.tabela.setCurrentIndex(0)
        self.loadSale()

    def showCliente(self):
        item_dao.deleteNull()
        self.tabela.insertWidget(1, ClientePage())
        self.tabela.setCurrentIndex(1)

    def sair(self):
        pass

    def edit_fun(self):
        item_dao.deleteNull()
        self.tabela.insertWidget(2, FunOP(self.user_logged))
        self.tabela.setCurrentIndex(2)

    def produto_page(self):
        item_dao.deleteNull()
        self.tabela.insertWidget(3, ProP(self))
        self.tabela.setCurrentIndex(3)
    
    def venda_pg(self):
        item_dao.deleteNull()
        self.tabela.insertWidget(4, VendaPg(self.user_logged, self))
        self.tabela.setCurrentIndex(4)

    def estoque(self):
        item_dao.deleteNull()
        self.tabela.insertWidget(5, Storage())
        self.tabela.setCurrentIndex(5)
        
    def loadSale(self):
        self.l = Sale.selectAll()
        self.table_venda.setRowCount(0)
        for v in self.l:
            self.addVenda(v)
        for i in range(self.table_venda.rowCount()):
            if self.table_venda.rowCount() > -1:
                button = QPushButton(self.table_venda)
                button.setText('...')
                button.setGeometry(30,30,30,30)
                button.setFixedSize(30,30)
                button.setToolTip('Visualizar Itens')
                button.setCursor(Qt.PointingHandCursor)
                button.clicked.connect(self.ver_mais)
                self.table_venda.setCellWidget(i, 5, button)
    
    def addVenda(self, v):
        locale.setlocale(locale.LC_ALL, '')
        row = self.table_venda.rowCount()
        self.table_venda.insertRow(row)
        list = item_dao.selectAllOne(v.id)
        val = locale.currency(v.valor, grouping=True)
        id = QTableWidgetItem(str(v.id))
        cliente = QTableWidgetItem(v.cliente)
        funcionario = QTableWidgetItem(v.funcionario)
        quant_item = QTableWidgetItem(str(len(list)))
        valor = QTableWidgetItem(str(val))

        self.table_venda.setItem(row, 0, id)
        self.table_venda.setItem(row, 1, cliente)
        self.table_venda.setItem(row, 2, funcionario)
        self.table_venda.setItem(row, 3, quant_item)
        self.table_venda.setItem(row, 4, valor)
        
    def ver_mais(self):
        locale.setlocale(locale.LC_ALL, '')
        r = self.table_venda.currentRow()
        i = self.table_venda.item(r, 0).text()
        it = item_dao.selectAllOne(i)
        l = []
        for item in it:
            string = f"Nome: {item.produto_nome}\n Quantidade: {item.quantidade}\n Valor(un): {locale.currency(item.produto_valor, grouping=True)}\n"
            l.append(string)
        
        l_format = '\n'.join(l)
        QMessageBox.information(self, "Lista de itens", f"{l_format}")



        
