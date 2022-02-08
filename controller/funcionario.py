from qt_core import *
class FunOP(QWidget):
    def __init__(self, user_logged):
        super().__init__()
        uic.loadUi('view/fun.ui', self)

        self.user_logged = user_logged
        

