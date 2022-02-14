from qt_core import *
import model.prop_dao as prop_dao
from model.produto import Produto
import locale
import os
class ProP(QWidget):
    l_p = []
    prod_at = None
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/produto.ui', self)
        self.mainWindow = mainWindow
        self.img = None
        self.remover_btn.hide()
        self.cancelar_btn.hide()
        self.remover_btn.clicked.connect(self.remover)
        self.cancelar_btn.clicked.connect(self.cancelar)
        self.salvar_btn.clicked.connect(self.salvar)
        self.validator = QDoubleValidator(0.00, 9999.00, 2, notation=QDoubleValidator.StandardNotation)
        self.est_prop.setValidator(self.validator)
        self.valor_prop.setValidator(self.validator)
        self.valor_prop.textChanged.connect(self.forn)
        self.est_prop.textChanged.connect(self.form)
        self.img_btn.clicked.connect(self.imageFinder)
        self.img_label.setPixmap(QPixmap('assets/icons/placeholder_img3.png'))
        self.quant_prop.setValue(1)
        self.painel_produtos.verticalHeader().setVisible(False)
        self.painel_produtos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.painel_produtos.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.painel_produtos.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.painel_produtos.clicked.connect(self.click)
        self.load()

    def forn(self):
        self.validator.validate(self.valor_prop.text(), 14)[0]
    def form(self):
        self.validator.validate(self.est_prop.text(), 14)[0]

    def remover(self):
        prop_dao.removeP(self.prod_at.id)
        self.remover_btn.hide()
        self.cancelar_btn.hide()
        self.load()

    def cancelar(self):
        self.clear()
        self.cancelar_btn.hide()
        self.remover_btn.hide()

    def salvar(self):
        nome = self.nome_prop.text()
        qt = self.quant_prop.value()
        autor = self.au.text()
        valor = self.valor_prop.text()
        valor_c = self.est_prop.text()

        try:
            if nome != '' and qt != 0 and autor != '' and valor != '' and valor_c != '':
                if self.validator.validate(valor, 14)[0] == QValidator.Acceptable and self.validator.validate(valor_c, 14)[0] == QValidator.Acceptable:
                    val_ = valor.replace(',','.')
                    val_c = valor_c.replace(',','.')
                    if self.prod_at != None:
                        prop_dao.editProd(Produto(self.prod_at.id, self.img, nome, qt, autor, val_, val_c))
                        self.load()
                    else:
                        prop_dao.addProd(Produto(None, self.img, nome, qt, autor, val_, val_c))
                        self.load()
                else:
                    QMessageBox.warning(self, "Erro!", "Apenas números inteiros nas lacunas de valores!")              
            else:
                QMessageBox.warning(self, "Erro!", "Insira todos os dados!")
        except Exception as w:
            print(w)
    

    def load(self):
        self.l_p = prop_dao.selectAll()
        self.clear()
        self.painel_produtos.setRowCount(0)
        for produto in self.l_p:
            self.table(produto)

    def table(self, produto):
        locale.setlocale(locale.LC_ALL, '')
        rowCount = self.painel_produtos.rowCount()
        self.painel_produtos.insertRow(rowCount)
        val_p = locale.currency(produto.valor_venda, grouping=True)
        val_c = locale.currency(produto.valor_compra, grouping=True)
        luc_pre = locale.currency(produto.valor_venda-produto.valor_compra, grouping=True)
        
        id = QTableWidgetItem(str(produto.id))
        nome = QTableWidgetItem(produto.nome)
        qtd = QTableWidgetItem(str(produto.quantidade))
        if produto.quantidade <= 10:
            qtd = QTableWidgetItem(str(f'{produto.quantidade}'+' (Pouco estoque!)'))
        valor_ = QTableWidgetItem(str(val_p))
        valor_co = QTableWidgetItem(str(val_c))
        lucr_prej = QTableWidgetItem(str(luc_pre))

        self.painel_produtos.setItem(rowCount, 0, id)
        self.painel_produtos.setItem(rowCount, 1, nome)
        self.painel_produtos.setItem(rowCount, 2, qtd)
        self.painel_produtos.setItem(rowCount, 3, valor_)
        self.painel_produtos.setItem(rowCount, 4, valor_co)
        self.painel_produtos.setItem(rowCount, 5, lucr_prej)
    
    def click(self):
        self.cancelar_btn.show()
        self.remover_btn.show()
        row = self.painel_produtos.currentRow()
        self.prod_at = self.l_p[row]
        if self.prod_at.img == None:
            self.img_label.setPixmap(QPixmap('assets/icons/placeholder_img3.png'))
        else:
            self.img = self.prod_at.img
            self.img_label.setPixmap(QPixmap(self.prod_at.img))
        self.nome_prop.setText(self.prod_at.nome)
        self.au.setText(self.prod_at.autor)
        self.quant_prop.setValue(self.prod_at.quantidade)
        self.valor_prop.setText(str(self.prod_at.valor_venda).replace('.',','))
        self.est_prop.setText(str(self.prod_at.valor_compra).replace('.',','))


    def clear(self):
        self.img_label.setPixmap(QPixmap('assets/icons/placeholder_img3.png'))
        self.nome_prop.clear()
        self.quant_prop.clear()
        self.au.clear()
        self.valor_prop.clear()
        self.est_prop.clear()
        self.img = None
        self.prod_at = None

    def imageFinder(self):
        filt = 'File (*.jpg, *.jpeg, *.png)'
        request = QFileDialog.getOpenFileName(self, "Escolha uma imagem", os.getcwd(), filt)
        self.img = request[0]
        if self.img != '':
            self.img_label.setPixmap(QPixmap(self.img))
        