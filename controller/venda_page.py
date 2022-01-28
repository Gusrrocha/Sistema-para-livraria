from qt_core import *
import locale
import model.cliente_dao as cl
import model.prop_dao as pr
import model.item_dao as item_dao
from model.item import Item
class VendaPg(QWidget):
    def __init__(self, user_logged):
        super().__init__()
        uic.loadUi('view/venda_pg.ui', self)

        self.lista_prd = None
        self.lista = None
        self.lista_item = []
        self.prd_atual = None
        self.valor = None
        self.user_logged = user_logged
        self.fun_atual_v.setText(user_logged)
        self.valor_item.setText("R$ 0")
        self.table_item.verticalHeader().setVisible(False)
        self.table_item.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_item.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.removerItem_btn.hide()
        self.addItem_btn.clicked.connect(self.addItem)

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
        self.load()
        self.load_prd()
    
    def load_prd(self):
        self.lista_prd = pr.selectAll()
        for p in self.lista_prd:
            self.produto_comboBox.addItem(p.nome)
        self.produto_comboBox.currentIndexChanged.connect(self.prdSelected)

    def load(self):
        self.lista = cl.selectAll()
        for c in self.lista:
            self.cliente_comboBox.addItem(c.nome)
        # self.cliente_comboBox.currentIndexChanged.connect(self.clSelected)

    def load_item(self):
        cont = 0
        self.table_item.setRowCount(0)
        for item in self.lista_item:
            cont += 1
            self.tb(item, cont)

    
    def addItem(self, index):
        id_prd = self.prd_atual.id
        nome = self.prd_atual.nome
        qt = self.quant_produto.value()
        valor = self.prd_atual.valor_venda*qt

        item_dao.add(Item(None, id_prd, nome, qt, valor))
        self.lista_item.append(Item(None, id_prd, nome, qt, valor))
        self.load_item()

    def tb(self, item, cont):
        locale.setlocale(locale.LC_ALL, '')
        row = self.table_item.rowCount()
        self.table_item.insertRow(row)

        val_item = locale.currency(item.produto_valor, grouping=True)
        qt_item = QTableWidgetItem(str(cont))
        id = QTableWidgetItem(str(item.produto_id))
        nome = QTableWidgetItem(item.produto_nome)
        quant = QTableWidgetItem(str(item.quantidade))
        valor = QTableWidgetItem(str(val_item))

        self.table_item.setItem(row, 0, qt_item)
        self.table_item.setItem(row, 1, id)
        self.table_item.setItem(row, 2, nome)
        self.table_item.setItem(row, 3, quant)
        self.table_item.setItem(row, 4, valor)
        self.clear()

    def clear(self):
        self.quant_produto.setValue(1)
        self.valor_item.setText("R$ 0")

    def prdSelected(self, index):
        locale.setlocale(locale.LC_ALL, '')
        self.prd_atual = self.lista_prd[index]
        self.valor = locale.currency(self.prd_atual.valor_venda, grouping=True)
        self.valor_item.setText(str(self.valor))
        

    def showtime(self):
        tempo = QTime.currentTime()
        text = tempo.toString("hh:mm:ss")
        self.label_date.setText(text)