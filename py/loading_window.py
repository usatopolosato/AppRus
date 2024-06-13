import time
from Designs.design_loadingWindow import Ui_LoadingWindow
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui


# Класс, предназначенный для заполнения ProgressBar
class ProgressHandler(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)

    def run(self):
        # Замедлим заполнения ProgressBar
        for step in range(1, 101):
            self.signal.emit(['progress_increment', step])
            time.sleep(0.02)


class Loading(QWidget, Ui_LoadingWindow):
    def __init__(self, desktop, window):
        super().__init__()
        self.setupUi(self)

        # После заполнения ProgressBar покажем форму авторизации.
        self.authorization = window

        # Выравниваем форму по центру.
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

        # Устанавливаем логотип ЕГЭ. Корректируем его размеры под форму.
        image = QtGui.QPixmap('image/EGE.png')
        height = self.image.height()
        width = self.image.width()
        self.image.setPixmap(image.scaled(width, height, QtCore.Qt.KeepAspectRatio))

        # Создания обработчика ProgressBar
        self.handler = ProgressHandler()
        self.handler.signal.connect(self.signal_handler)
        self.handler.start()

        # Служебные инструмены, чтобы убрать встроенные рамки формы.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    # Заполняем ProgressBar и при заполнении в 100 % показываем форму авторизации.
    def signal_handler(self, value):
        if value[1] == 100:
            self.authorization.show()
            self.close()
        if value[0] == 'progress_increment':
            self.progressBar.setValue(self.progressBar.value() + 1)
