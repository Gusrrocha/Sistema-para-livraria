from qt_core import *
class ClientePage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/cliente.ui', self)

        self.cancel_edit_btn.hide()
        

        