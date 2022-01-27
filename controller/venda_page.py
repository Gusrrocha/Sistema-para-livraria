from qt_core import *
class VendaPg(QWidget):
    def __init__(self, user_logged):
        super().__init__()
        uic.loadUi('view/venda_pg.ui', self)




        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()


    def showtime(self):
        tempo = QTime.currentTime()
        text = tempo.toString("hh:mm:ss")
        self.label_date.setText(text)