import io
import sys
from PyQt5 import QtCore, QtGui
from PyQt5 import uic
from pyp.queries_db import html_theory
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser
from Designs.design_theory import Ui_TheoryWidget


class Theory(QMainWindow, Ui_TheoryWidget):
    def __init__(self, desktop, task, menu_window):
        super().__init__()
        self.setupUi(self)

        # Выравнивание по центру
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

        # Нужные инструменты, чтобы перемещать форму по экрану.
        self.move_x = self.move_y = self.old_x = self.old_y = 0
        self.press = False

        # Показываем теорию в форме
        self.content.setHtml(html_theory(task))

        # Для показа меню теория, осуществляется показ после закрытия формы.
        self.menu_window = menu_window

        # Подключения функций к кнопкам и установка на кнопки иконок.
        self.exitButton.clicked.connect(self.exit)
        self.exitButton.setIcon(QtGui.QIcon('icon/exit_to_app.png'))

        # Служебные инструмены, чтобы убрать встроенные рамки формы.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    # Реагируем на нажатие ESC, чтобы выполнить выход из формы
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.exit()

    # Функция для выхода из формы
    def exit(self):
        self.menu_window.show()
        self.close()

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
