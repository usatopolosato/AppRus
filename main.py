from pyp.loading_window import *
from pyp.authorization import *
from pyp.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    desktop = app.desktop()
    authorization = Authorization(desktop, MainWindow(desktop))
    loading = Loading(desktop, authorization)
    loading.show()
    sys.exit(app.exec())
