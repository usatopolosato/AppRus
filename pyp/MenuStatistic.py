import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore, QtGui
from Designs.design_MainWindow import *
from pyp.queries_db import *
from pyp.DiagramWidget import Diagram
from Designs.design_MenuStatistic import Ui_MenuStatistic


class MenuStatistic(QWidget, Ui_MenuStatistic):
    def __init__(self, desktop, login, password, main_window):
        super().__init__()
        self.setupUi(self)

        self.desktop = desktop

        # Сохраняем нужную информацию о пользователе.
        self.login = login
        self.password = password

        # Выравнивание по центру.
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

        # Нужные инструменты, чтобы перемещать форму по экрану.
        self.move_x = self.move_y = self.old_x = self.old_y = 0
        self.press = False

        # Подключение функций к кнопкам
        for i in range(1, 27):
            eval(f'''self.statisticButton{i}.clicked.connect(self.show_diagram)''')

        # Сохранение навигационной формы для последующего показа
        self.main_window = main_window

        # Подключения функций к кнопкам и установка на кнопки иконок.
        self.exitButton.clicked.connect(self.exit)
        self.exitButton.setIcon(QtGui.QIcon('icon/exit_to_app.png'))

        # Служебные инструмены, чтобы убрать встроенные рамки формы.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    # Функция для показа статистики по выбранному вопросу.
    def show_diagram(self):
        self.diagram_widget = Diagram(self.desktop, self.login, self.password,
                                      int(self.sender().text().split()[1]), self)
        self.diagram_widget.show()
        self.hide()

    # Реагируем на нажатие ESC, чтобы выполнить выход из формы
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.exit()

    # Функция для выхода из формы
    def exit(self):
        self.main_window.show()
        self.hide()

    # Функции для передвижения формы по экрану.
    def mousePressEvent(self, event):
        self.old_x, self.old_y = (event.x(), event.y())
        self.press = True

    def mouseReleaseEvent(self, event):
        self.press = False

    def mouseMoveEvent(self, event):
        if self.press:
            self.move_x = event.x()
            self.move_y = event.y()
            self.move(self.x() + (self.move_x - self.old_x), self.y() + (self.move_y - self.old_y))
