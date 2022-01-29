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
        self.item_atual = None
        self.valor = None
        self.valor_total = 0
        self.falta = 0
        self.user_logged = user_logged
        self.fun_atual_v.setText(user_logged)
        self.val_total.setText("R$ 0,00")
        self.valor_item.setText("R$ 0,00")
        self.troco.setText("R$ 0,00")
        self.falta_lineEdit.setText("R$ 0,00")
        self.table_item.verticalHeader().setVisible(False)
        self.table_item.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_item.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.removerItem_btn.setEnabled(False)
        self.cancel_item_btn.hide()
        self.addItem_btn.clicked.connect(self.addItem)
        self.pag_comboBox.currentIndexChanged.connect(self.pagamento)
        self.inserir_din.clicked.connect(self.mCl)
        self.table_item.clicked.connect(self.ckl)
        self.removerItem_btn.clicked.connect(self.removeItem)
        
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
        self.load()
        self.load_prd()
    
    def pagamento(self):
        if self.pag_comboBox.currentIndex() == 1:
            self.troco_label.hide()
            self.troco.hide()
            self.pag_groupBox.setTitle("Cartão")
        else:
            self.troco_label.show()
            self.troco.show()
            self.pag_groupBox.setTitle("Dinheiro")

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
        locale.setlocale(locale.LC_ALL, '')
        id_prd = self.prd_atual.id
        nome = self.prd_atual.nome
        qt = self.quant_produto.value()
        valor = self.prd_atual.valor_venda*qt

        item_dao.add(Item(None, id_prd, nome, qt, valor))
        id_item = item_dao.selectRecent()
        self.lista_item.append(Item(id_item[0][0], id_prd, nome, qt, valor))
        self.valor_total += valor
        val_format = locale.currency(self.valor_total, grouping=True)
        self.val_total.setText(val_format)
        self.falta_lineEdit.setText(str(locale.currency(self.valor_total, grouping=True)))
        self.load_item()
    
    def removeItem(self):
        locale.setlocale(locale.LC_ALL, '')
        self.valor_total -= self.item_atual.produto_valor
        self.val_total.setText(locale.currency(self.valor_total, grouping=True))
        self.falta_lineEdit.setText(str(locale.currency(self.valor_total, grouping=True)))
        item_dao.remove(self.item_atual.id)
        self.lista_item.remove(self.item_atual)
        self.removerItem_btn.setEnabled(False)
        self.cancel_item_btn.hide()
        self.addItem_btn.setEnabled(True)
        self.produto_comboBox.setEnabled(True)
        self.quant_produto.setEnabled(True)
        self.valor_item.setEnabled(True)
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
        self.valor_item.setText("R$ 0,00")

    def prdSelected(self, index):
        locale.setlocale(locale.LC_ALL, '')
        self.prd_atual = self.lista_prd[index]
        self.valor = locale.currency(self.prd_atual.valor_venda, grouping=True)
        self.valor_item.setText(str(self.valor))
        
    def ckl(self):
        self.removerItem_btn.setEnabled(True)
        self.cancel_item_btn.show()
        self.addItem_btn.setEnabled(False)
        self.produto_comboBox.setEnabled(False)
        self.quant_produto.setEnabled(False)
        self.valor_item.setEnabled(False)
        row = self.table_item.currentRow()
        self.item_atual = self.lista_item[row]



    def mCl(self):
        locale.setlocale(locale.LC_ALL, '')
        if self.valor_total != 0:
            dinheiro_recebido = int(self.din_lineEdit.text())
            self.falta += dinheiro_recebido
            falta = self.valor_total - self.falta
            falta_f = locale.currency(falta, grouping=True)
            if self.falta < self.valor_total:
                self.falta_lineEdit.setText(falta_f)
            else:
                troco = self.falta - self.valor_total
                troco_f = locale.currency(troco, grouping=True)
                self.troco.setText(troco_f)
                self.falta_lineEdit.setText("R$ 0,00")
        else:
            QMessageBox.warning(self, "Aviso!", "Você ainda não adicionou nenhum produto!")


    def showtime(self):
        tempo = QTime.currentTime()
        text = tempo.toString("hh:mm:ss")
        self.label_date.setText(text)