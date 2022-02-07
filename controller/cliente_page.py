from qt_core import *
from model.cliente import Cliente
import model.cliente_dao as cliente_dao
class ClientePage(QWidget):
    l_c = []
    c_at = None
    def __init__(self):
        super().__init__()
        uic.loadUi('view/cliente.ui', self)
        
        self.remover_btn.hide()
        self.cancel_edit_btn.hide()
        self.remover_btn.clicked.connect(self.remover)
        self.salvar_btn.clicked.connect(self.salvar)
        self.painel_clientes.verticalHeader().setVisible(False)
        self.painel_clientes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.painel_clientes.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.lupa.clicked.connect(self.buscar)
        self.cancel_edit_btn.clicked.connect(self.stopEdit)
        self.cpf.setMaxLength(11)
        self.telefone.setMaxLength(11)
        self.load()
        self.painel_clientes.clicked.connect(self.cL)

    def load(self):
        self.l_c = cliente_dao.selectAll()
        self.clear_()
        self.painel_clientes.setRowCount(0)
        for cliente in self.l_c:
            self.add_cliente(cliente)

    def buscar(self):
        pass


    def remover(self):
        cliente_dao.removeC(self.c_at.id)
        self.remover_btn.hide()
        self.cancel_edit_btn.hide()
        self.load()

        

    def salvar(self):
        try:
            nome = self.nome.text()
            telefone = str(self.telefone.text())
            endereco = self.endereco.text()
            cpf = str(self.cpf.text())
            
            valid = QDoubleValidator(0, 100000000000, 0)
            if nome != '' and telefone != '' and endereco != '' and cpf != '':
                f_um = cpf[:3]
                f_dois = cpf[3:6]
                f_tres = cpf[6:9]
                f_quatro = cpf[9:]

                f_tum = str(telefone[:2])
                # f_td = str(telefone[2])
                f_ttt = str(telefone[3:7])
                f_tt = str(telefone[7:])
                formated = "{}.{}.{}-{}".format(f_um,f_dois,f_tres,f_quatro)
                formated_tel = "({}) 9 {}-{}".format(f_tum, f_ttt, f_tt)
                if valid.validate(telefone, 14)[0] == QValidator.Acceptable and valid.validate(cpf, 14)[0] == QValidator.Acceptable:
                    if len(str(telefone)) == 11 and len(str(cpf)) == 11:
                        if self.c_at == None:
                            cliente_dao.add(Cliente(None, nome, formated_tel, endereco, formated))
                            self.load()
                        else:
                            cliente_dao.edit(Cliente(self.c_at.id, nome, formated_tel, endereco, formated))
                            self.load()
                    else:
                        QMessageBox.about(self, "Erro!", "O número de telefone e CPF do cliente deve ter 11 dígitos!")
                else:
                    QMessageBox.about(self, "Erro!", "Telefone ou CPF inseridos estão incorretos!")
            else:
                QMessageBox.about(self, "Erro!", "Preencha todas as lacunas!")
            

        except Exception as e:
            QMessageBox.about(self, "Erro!", "Preencha todas as lacunas!")
            print(e)
        self.remover_btn.hide()
        self.cancel_edit_btn.hide()


    def stopEdit(self):
        self.clear_()
        self.remover_btn.hide()
        self.cancel_edit_btn.hide()

    def cL(self):
        self.remover_btn.show()
        self.cancel_edit_btn.show()

        row = self.painel_clientes.currentRow()
        self.c_at = self.l_c[row]
        cpf_c = str(self.c_at.cpf)
        f_u = cpf_c[:3]
        f_d = cpf_c[4:7]
        f_t = cpf_c[8:11]
        f_q = cpf_c[12:]
        cpf_cl = '{}{}{}{}'.format(f_u, f_d, f_t, f_q)
        tel_c = str(self.c_at.telefone)
        f_tu = tel_c[1:3]
        f_tdo = tel_c[5]
        f_tr = tel_c[7:11]
        f_tq = tel_c[12:]
        tel_cl = '{}{}{}{}'.format(f_tu, f_tdo, f_tr, f_tq)
        self.nome.setText(self.c_at.nome)
        self.telefone.setText(tel_cl)
        self.endereco.setText(self.c_at.endereco)
        self.cpf.setText(cpf_cl)

    def clear_(self):
        self.nome.clear()
        self.telefone.clear()
        self.endereco.clear()
        self.cpf.clear()
        self.c_at = None

    def add_cliente(self, cliente):
        rowCount = self.painel_clientes.rowCount()
        self.painel_clientes.insertRow(rowCount)


        id = QTableWidgetItem(str(cliente.id))
        nome = QTableWidgetItem(cliente.nome)
        telefone = QTableWidgetItem(str(cliente.telefone))
        endereco = QTableWidgetItem(cliente.endereco)
        cpf = QTableWidgetItem(cliente.cpf)

        self.painel_clientes.setItem(rowCount, 0, id)
        self.painel_clientes.setItem(rowCount, 1, nome)
        self.painel_clientes.setItem(rowCount, 2, telefone)
        self.painel_clientes.setItem(rowCount, 3, endereco)
        self.painel_clientes.setItem(rowCount, 4, cpf)




        