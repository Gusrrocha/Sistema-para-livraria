from qt_core import *
class AddProP(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/add_prop.ui', self)