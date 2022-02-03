from qt_core import *
from controller.main_window import MainWindow
from model.funcionario import Funcionario
import model.funcionario_dao as fun_dao
class Login(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/login.ui', self)


        self.senha.setEchoMode(QLineEdit.Password)
        self.label_email.hide()
        self.email.hide()
        self.cadastrar_btn.hide()
        self.cancelar_btn.hide()
        self.entrar_btn.clicked.connect(self.check)
        self.registrar_btn.clicked.connect(self.register)
        self.cadastrar_btn.clicked.connect(self.cadast)
        self.cancelar_btn.clicked.connect(self.cancelar)

    
    def check(self):
        us = self.usuario.text()
        se = self.senha.text()
        try:
            if us == '' and se == '':
                QMessageBox.about(self, "Erro!", "Insira os dados!")
            else:
                login = fun_dao.log(us, se)
                if login == None:
                    QMessageBox.about(self, "Erro!", "Usuário ou senha incorretos!")
                else:
                    QMessageBox.about(self, "Acesso aceito!", "Entrou com êxito!")
                    user_logged = us
                    self.mainWindow = MainWindow(user_logged)
                    self.mainWindow.show()
                    
                    self.hide()
        except Exception as e:
            print(e)


    def cadast(self):
        try:
            user = self.usuario.text()
            senha = self.senha.text()
            email = self.email.text()
            
            valid = QDoubleValidator(0, 100000000, 0)
            if user != '' and email != '':
                exist = fun_dao.selectOne(user)
                if exist == None:
                    if valid.validate(senha, 14)[0] == QValidator.Acceptable:
                        if len(str(senha)) == 8:
                            fun_dao.reg(Funcionario(None, user, senha, email))
                            self.cadastrar_btn.hide()
                            self.registrar_btn.show()
                            self.entrar_btn.show()
                            self.email.hide()
                            self.label_email.hide()
                            self.cancelar_btn.hide()
                            self.usuario.clear()
                            self.senha.clear()
                            self.email.clear()
                        else:
                            QMessageBox.about(self, "Erro!", "A senha deve possuir 8 dígitos!")
                    else:
                        QMessageBox.about(self, "Erro!", "A senha está incorreta!")
                else:
                    QMessageBox.warning(self, "Erro!", "O usuário já existe.")
            else:
                QMessageBox.warning(self, "Erro!", "Insira um nome!")
        except Exception as e:
            print(e)
        
    
    def register(self):
        self.entrar_btn.hide()
        self.registrar_btn.hide()
        self.cadastrar_btn.show()
        self.label_email.show()
        self.email.show()
        self.cancelar_btn.show()
    
    def cancelar(self):
        self.cancelar_btn.hide()
        self.label_email.hide()
        self.email.hide()
        self.cadastrar_btn.hide()
        self.entrar_btn.show()
        self.registrar_btn.show()