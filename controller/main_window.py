from qt_core import *
import locale
import os
from controller.funcionario import FunOP
from controller.produto_page import ProP
from controller.cliente_page import ClientePage
from controller.venda_page import VendaPg
import model.venda_dao as Sale
import model.item_dao as item_dao
import model.funcionario_dao as fun
class MainWindow(QMainWindow):
    def __init__(self, user_logged, login):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)
        Sale.deletePastMonth()
        item_dao.delSNonExistance()
        self.user_logged = user_logged
        self.login = login
        self.setMouseTracking(True)
        
        self.l = []
        
        menu = QMenu()
        key = fun.selectOne(self.user_logged)[4]
        if key != 1:
            self.fun_btn.hide()
        else:
            self.fun_btn.show()
            action_um = menu.addAction('Gerenciar funcionários')
            action_um.triggered.connect(self.fun_page)
        self.funcionario_label.setText(user_logged+"!")
        self.clientes_btn.clicked.connect(self.showCliente)
        self.produto_btn.clicked.connect(self.produto_page)
        self.venda_btn.clicked.connect(self.venda_pg)
        self.home_btn.clicked.connect(self.mainPage)
        self.fun_btn.clicked.connect(self.fun_page)
        self.table_venda.verticalHeader().setVisible(False)
        self.table_venda.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_venda.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table_venda.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.table_venda.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.table_venda.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.mais_fun.setMenu(menu)
        self.action_dois = menu.addAction('Sair')
        self.action_dois.triggered.connect(self.sair)
        self.loadSale()

    
    
    def mainPage(self):
        item_dao.deleteNull()
        self.home_btn.setStyleSheet('border-style: inset; background-color: rgb(236, 157, 0);  border-width: 2px;'
                                    'border-radius: 10px;'
                                    'border-color: white;'
                                    'font: bold 12px;'
                                    'min-width: 1em;'
                                    'padding: 6px;'
        )
        self.tabela.setCurrentIndex(0)
        
        self.tabela.currentChanged.connect(self.button)
        self.loadSale()

    def showCliente(self):
        item_dao.deleteNull()
        self.tabela.insertWidget(1, ClientePage())
        self.tabela.setCurrentIndex(1)

    def sair(self):
        self.login.show()
        self.hide()

    def fun_page(self):
        item_dao.deleteNull()
        self.tabela.insertWidget(2, FunOP(self.user_logged))
        self.tabela.setCurrentIndex(2)

    def produto_page(self):
        item_dao.deleteNull()
        self.tabela.insertWidget(3, ProP(self))
        self.tabela.setCurrentIndex(3)
    
    def venda_pg(self):
        item_dao.deleteNull()
        self.tabela.insertWidget(4, VendaPg(self.user_logged, self, self.tabela, self.action_dois))
        self.tabela.setCurrentIndex(4)

        
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
                self.table_venda.setCellWidget(i, 6, button)
    
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
        f = v.data[:4]
        f_u = v.data[5:7]
        f_d = v.data[8:10]
        h = v.data[12:14]
        m = v.data[15:17]
        s = v.data[18:20]
        da = '{}-{}-{}  {}:{}:{}'.format(f_d,f_u,f,h,m,s)
        d = 0
        for i in list:
            d += i.produto_valor
        if d < v.valor:
            valor = QTableWidgetItem(str(val+' [COM JUROS DE ({}x)]'.format(v.parcela)))
            valor.setToolTip(val+' [COM JUROS DE ({}x)]'.format(v.parcela))
            

        else:
            valor = QTableWidgetItem(str(val))
            valor.setToolTip(val)
        if len(v.cliente) > 20: cliente.setToolTip(v.cliente)
        if len(v.funcionario) > 20: funcionario.setToolTip(v.funcionario)
        font = QFont()
        font.setBold(True)
        
        self.table_venda.setItem(row, 0, id)
        self.table_venda.setItem(row, 1, cliente)
        self.table_venda.setItem(row, 2, funcionario)
        self.table_venda.setItem(row, 3, quant_item)
        self.table_venda.setItem(row, 4, valor)
        self.table_venda.setItem(row, 5, QTableWidgetItem(da))
        # rect = self.table_venda.visualItemRect(self.table_venda.currentItem())
        # v = self.table_venda.viewport().update(rect)
        # print(v)
        
    def ver_mais(self):
        locale.setlocale(locale.LC_ALL, '')
        r = self.table_venda.currentRow()
        i = self.table_venda.item(r, 0).text()
        it = item_dao.selectAllOne(i)
        v = self.table_venda.item(r, 4).text()
        l = []
        for item in it:
            string = f"Nome: {item.produto_nome}\n Quantidade: {item.quantidade}\n Valor total: {locale.currency(item.produto_valor, grouping=True)}\n"
            l.append(string)
        
        l_format = '\n'.join(l)
        QMessageBox.information(self, "Lista de itens", f"{l_format}")

    def button(self):
        if self.tabela.currentIndex() != 0:
            self.home_btn.setStyleSheet('border-style: outset; background-color: orange; border-width: 2px;'
                                        'border-radius: 10px;'
                                        'border-color: white;'
                                        'font: bold 12px;'
                                        'min-width: 1em;'
                                        'padding: 6px;')
        else:
            self.home_btn.setStyleSheet('border-style: inset; background-color: rgb(236, 157, 0); border-width: 2px;'
                                        'border-radius: 10px;'
                                        'border-color: white;'
                                        'font: bold 12px;'
                                        'min-width: 1em;'
                                        'padding: 6px;')
    
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(119,255,183))
        painter.drawRect(0,0,100000000,105)
        # painter.setBrush(Qt.lightGray)
        # painter.drawRect(117,109,100000,100000)
        painter.end()
    
    def mouseMoveEvent(self, event):
        self.cord.setText('(%d : %d)'% (event.x(), event.y()))
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F5:
            self.loadSale()
            Sale.deletePastMonth()
            print("Você apertou o f5! Parabéns!")


        
