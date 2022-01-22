from http.client import ACCEPTED
from sys import argv
from qt_core import *
from controller.main_window import MainWindow
from controller.login import Login


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    win = Login()
    win.show()
sys.exit(app.exec())


