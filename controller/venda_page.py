from re import S
from qt_core import *
import locale
import model.cliente_dao as cl
import model.prop_dao as pr
import model.item_dao as item_dao
import model.venda_dao as sale
import model.storage_dao as st
from model.venda import Venda
from model.item import Item
from model import dbase
class VendaPg(QWidget):
    def __init__(self, user_logged, mainWindow, tabela, action):
        super().__init__()
        uic.loadUi('view/venda_pg.ui', self)
        self.mainWindow = mainWindow
        self.tabela = tabela
        self.action = action
        self.lista_prd = None
        self.lista = None
        self.lista_item = []
        self.lista_iditem = []
        self.cl_atual = None
        self.prd_atual = None
        self.item_atual = None
        self.parcela_at = None
        self.valor = None
        self.valor_total = 0
        self.falta = 0
        self.i = 0
        self.q = 0
        self.go = 0
        self.other = 0
        self.tabela.currentChanged.connect(self.deleteChanges)
        self.user_logged = user_logged
        self.action.triggered.connect(self.deleteChanges)
        self.fun_atual_v.setText(user_logged)
        self.val_total.setText("R$ 0,00")
        self.valor_item.setText("R$ 0,00")
        self.troco.setText("R$ 0,00")
        self.falta_lineEdit.setText("R$ 0,00")
        self.table_item.verticalHeader().setVisible(False)
        self.table_item.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_item.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.final_btn.setEnabled(False)
        self.removerItem_btn.setEnabled(False)
        self.addItem_btn.setEnabled(False)
        self.inserir_din.setEnabled(False)
        self.final_in_btn.setEnabled(False)
        self.cancel_item_btn.hide()
        self.parcela_label.hide()
        self.parcelas.hide()
        self.label_im.hide()
        self.label_par.hide()
        self.label_po.hide()
        self.par.hide()
        self.cela.hide()
        self.addItem_btn.clicked.connect(self.addItem)
        self.pag_comboBox.currentIndexChanged.connect(self.pagamento)
        self.inserir_din.clicked.connect(self.mCl)
        self.table_item.clicked.connect(self.ckl)
        self.final_btn.clicked.connect(self.final)
        self.removerItem_btn.clicked.connect(self.removeItem)
        self.cancel_item_btn.clicked.connect(self.cancelItem)
        self.final_in_btn.clicked.connect(self.fechar)
        self.parcelas.currentIndexChanged.connect(self.parcela)
        qApp.aboutToQuit.connect(self.close)
        self.BOTT = 0.00
        self.TOP = 99999.00
        self.valid = QDoubleValidator(self.BOTT, self.TOP, 2, notation=QDoubleValidator.StandardNotation)
        self.din_lineEdit.setValidator(self.valid)
        self.din_lineEdit.textChanged.connect(self.formatd)
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
        self.load()
        self.load_prd()
    
    def close(self):
        for item in self.lista_item:
            for produto in self.lista_prd:
                if produto.id == item.produto_id:
                    qt = produto.quantidade
                    qt += item.quantidade
                    st.update(item.produto_id, qt)
                    qt = 0
    def deleteChanges(self):
        if self.other == 1:
            pass
            
        else: 
            for item in self.lista_item:
                for produto in self.lista_prd:
                    if produto.id == item.produto_id:
                        qt = produto.quantidade
                        qt += item.quantidade
                        st.update(item.produto_id, qt)
                        qt = 0
    def formatd(self):
        s = self.din_lineEdit.text()
        self.valid.validate(s, 14)[0]
         
    def fechar(self):
        quest = QMessageBox.question(self, "Fechar", "Você tem certeza que quer fechar?", QMessageBox.Yes| QMessageBox.No)
        
        if quest == QMessageBox.Yes:
            self.final_in_btn.setEnabled(False)
            if self.pag_comboBox.currentText() == 'DINHEIRO':
                self.inserir_din.setEnabled(True)
            elif self.parcela_at != None:
                self.inserir_din.setEnabled(True)
            self.addItem_btn.setEnabled(False)
            self.produto_comboBox.setEnabled(False)
            self.quant_produto.setEnabled(False)
            self.valor_item.setEnabled(False)
            self.table_item.setEnabled(False)
            self.pag_comboBox.setEnabled(False)
            self.din_lineEdit.returnPressed.connect(self.mCl)
    
    def pagamento(self):
        if self.pag_comboBox.currentIndex() == 1:
            self.troco_label.hide()
            self.troco.hide()
            self.parcelas.show()
            self.parcela_label.show()
            self.din_lineEdit.hide()
            self.din_label.hide()
            self.label_im.show()
            self.label_par.show()
            self.label_po.show()
            self.falta_label.hide()
            self.falta_lineEdit.hide()
            self.par.show()
            self.cela.show()
            self.cela.setText("R$ 0,00")
            self.pag_groupBox.setTitle("Cartão")
        else:
            self.troco_label.show()
            self.troco.show()
            self.inserir_din.show()
            self.parcelas.hide()
            self.parcela_label.hide()
            self.din_lineEdit.show()
            self.din_label.show()
            self.label_im.hide()
            self.label_par.hide()
            self.label_po.hide()
            self.falta_label.show()
            self.falta_lineEdit.show()
            self.par.hide()
            self.cela.hide()
            self.pag_groupBox.setTitle("Dinheiro")


    def load_prd(self):
        self.lista_prd = pr.selectAll()
        if self.q == 0:
            i = 0
            self.q += 1
            for p in self.lista_prd:
                self.produto_comboBox.insertItem(i, p.nome)
                i += 1
        self.produto_comboBox.currentIndexChanged.connect(self.prdSelected)

    def load(self):
        self.lista = cl.selectAll()
        i = 0
        for c in self.lista:
            self.cliente_comboBox.insertItem(i, c.nome)
            i += 1
        self.cliente_comboBox.currentIndexChanged.connect(self.clSelected)

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
        qt_sql = self.prd_atual.quantidade-qt
        self.go = 0
        for i in self.lista_item:
            if i.produto_id == id_prd:
                self.go += 1
        if self.go == 0:
            st.update(self.prd_atual.id, qt_sql)
            item_dao.add(Item(None, id_prd, None, nome, qt, valor))
            id_item = item_dao.selectRecent()
            self.lista_item.append(Item(id_item[0][0], id_prd, None, nome, qt, valor))
            self.lista_iditem.append(id_item[0][0])
            self.valor_total += valor
            val_format = locale.currency(self.valor_total, grouping=True)
            self.val_total.setText(val_format)
            self.falta_lineEdit.setText(str(locale.currency(self.valor_total, grouping=True)))
            self.final_in_btn.setEnabled(True)
            self.load_item()
            self.load_prd()
        else:
            QMessageBox.warning(self, "Erro!", "Remova o item primeiro, para inseri-lo de novo!")
    
    def cancelItem(self):
        self.removerItem_btn.setEnabled(False)
        self.cancel_item_btn.hide()
        self.final_in_btn.show()
        self.addItem_btn.setEnabled(True)
        self.produto_comboBox.setEnabled(True)
        self.quant_produto.setEnabled(True)
        self.valor_item.setEnabled(True)
        self.item_atual = None
        
    def removeItem(self):
        locale.setlocale(locale.LC_ALL, '')
        self.valor_total -= self.item_atual.produto_valor
        self.val_total.setText(locale.currency(self.valor_total, grouping=True))
        self.falta_lineEdit.setText(str(locale.currency(self.valor_total, grouping=True)))
        qt_sql = self.item_atual.quantidade
        st.updateM(self.item_atual.produto_id, qt_sql)
        item_dao.remove(self.item_atual.id)
        self.lista_item.remove(self.item_atual)
        self.removerItem_btn.setEnabled(False)
        self.cancel_item_btn.hide()
        self.final_in_btn.show()
        self.addItem_btn.setEnabled(True)
        self.produto_comboBox.setEnabled(True)
        self.quant_produto.setEnabled(True)
        self.valor_item.setEnabled(True)
        self.load_item()
        self.load_prd()
        
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
        c = 0
        for item in self.lista_prd:
            c += 1
        self.produto_comboBox.setCurrentIndex(c)
        self.quant_produto.setValue(1)
        self.valor_item.setText("R$ 0,00")
    
    def clSelected(self, index):
        if self.cliente_comboBox.currentText() != "Escolha o cliente":
            self.cl_atual = self.lista[index]

    def prdSelected(self, index):
        locale.setlocale(locale.LC_ALL, '')
        if self.produto_comboBox.currentText() != "Escolha o produto":
            self.prd_atual = self.lista_prd[index]
            self.quant_produto.setMaximum(self.prd_atual.quantidade)
            self.valor = locale.currency(self.prd_atual.valor_venda, grouping=True)
            self.valor_item.setText(str(self.valor))
            if self.prd_atual.quantidade != 0:
                self.addItem_btn.setEnabled(True)
                self.quant_produto.setValue(1)
            else:
                self.addItem_btn.setEnabled(False)
                QMessageBox.information(self, 'Sem itens', 'O estoque de itens do produto "{}" acabou'.format(self.prd_atual.nome))
        else:
            self.valor_item.setText("R$ 0,00")
            self.addItem_btn.setEnabled(False)
        
        
    def ckl(self):
        self.removerItem_btn.setEnabled(True)
        self.cancel_item_btn.show()
        self.final_in_btn.hide()
        self.addItem_btn.setEnabled(False)
        self.produto_comboBox.setEnabled(False)
        self.quant_produto.setEnabled(False)
        self.valor_item.setEnabled(False)
        row = self.table_item.currentRow()
        self.item_atual = self.lista_item[row]


    def mCl(self):
        locale.setlocale(locale.LC_ALL, '')
        
        if self.pag_comboBox.currentIndex() != 1:
            if self.valid.validate(self.din_lineEdit.text(), 14)[0] == QValidator.Acceptable:
                d = self.din_lineEdit.text()
                z = d.replace(',', '.')
                if self.valor_total != 0:
                    dinheiro_recebido = float(z)
                    self.falta += dinheiro_recebido
                    falta = self.valor_total - self.falta
                    falta_f = locale.currency(falta, grouping=True)
                    self.din_lineEdit.clear()
                    if self.falta < self.valor_total:
                        self.falta_lineEdit.setText(falta_f)
                    else:
                        self.din_lineEdit.setEnabled(False)
                        self.inserir_din.setEnabled(False)
                        self.final_btn.setEnabled(True)
                        troco = self.falta - self.valor_total
                        troco_f = locale.currency(troco, grouping=True)
                        self.troco.setText(troco_f)
                        self.falta_lineEdit.setText("R$ 0,00")
                else:
                    QMessageBox.warning(self, "Aviso!", "Você ainda não adicionou nenhum produto!")
            else:
                QMessageBox.warning(self, "Erro!", "Insira corretamente os dados!")
        else:
            if self.parcela_at > 1 and self.parcela_at < 4:
                self.valor_total += (self.valor_total * 5/100)
                val_cort = self.valor_total / self.parcela_at
                self.par.setText(f"Valor parcelado em ({self.parcela_at}x):")
                self.val_total.setText(locale.currency(self.valor_total, grouping=True))
                self.cela.setText(locale.currency(val_cort, grouping=True))
                self.inserir_din.setEnabled(False)
                self.parcelas.setEnabled(False)
                self.final_btn.setEnabled(True)
            
            elif self.parcela_at >= 4:
                self.valor_total += (self.valor_total*15/100)
                val_cort = self.valor_total / self.parcela_at
                self.par.setText(f"Valor parcelado em ({self.parcela_at}x):")
                self.val_total.setText(locale.currency(self.valor_total, grouping=True))
                self.cela.setText(locale.currency(val_cort, grouping=True))
                self.inserir_din.setEnabled(False)
                self.parcelas.setEnabled(False)
                self.final_btn.setEnabled(True)
        

    def parcela(self):
        self.parcela_at = self.parcelas.currentText()
        self.inserir_din.setEnabled(True)
        match(self.parcela_at):
            case "2x": self.parcela_at = 2
            case "3x": self.parcela_at = 3
            case "4x": self.parcela_at = 4
            case "5x": self.parcela_at = 5
            case "6x": self.parcela_at = 6
            case "7x": self.parcela_at = 7
            case "8x": self.parcela_at = 8
         
    def final(self):
        try:
            if self.cl_atual != None:
                for i in self.lista_item:
                    for p in self.lista_prd:
                        if p.id == i.produto_id:
                            st.storage(i.produto_id, i.quantidade)
                sale.add(Venda(None, self.cl_atual.nome, self.user_logged, self.valor_total, QDateTime.currentDateTime().toString('dd/MM/yyyy '+' hh:mm:ss')))
                QMessageBox.information(self, "Finalizado!", "Compra finalizada com sucesso!")
                id_venda = sale.selectRecent()
                for itemid in self.lista_iditem:
                    conn = dbase.connect()
                    cursor = conn.cursor()
                    sql = f"""UPDATE ItemVenda SET id_venda={id_venda[0]} WHERE id=?"""
                    cursor.execute(sql, [itemid])
                    conn.commit()
                    conn.close()
                
                self.other += 1
                self.mainWindow.mainPage()
            else:
                QMessageBox.warning(self, "Erro!", "Insira um cliente!")
        except Exception as b:
            print(b)

        

    def showtime(self):
        tempo = QTime.currentTime()
        text = tempo.toString("hh:mm:ss")
        self.label_date.setText(text)
        data = QDate.currentDate()
        texto = data.toString("dd/MM/yyyy")
        self.data_label.setText(texto)

