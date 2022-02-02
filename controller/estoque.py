from qt_core import *
class Storage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/estoque.ui", self)

        