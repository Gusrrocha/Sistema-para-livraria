from sys import argv
from qt_core import *
from controller.main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())
