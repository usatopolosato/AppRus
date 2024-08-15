import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QSpinBox, QLabel, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui
from Designs.design_question import *
from pyp.queries_db import make_up_exem
from pyp.queries_db import html_quastion


class Question(QMainWindow, Ui_questionWidget):
    def __init__(self, desktop, html, window):
        super().__init__()
        self.setupUi(self)

        self.desktop = desktop

        # Для показа меню вопросы, осуществляется показ после закрытия формы.
        self.menu_window = window

        # Показываем задание в форме
        self.content.setHtml(html)

        # Подключения функций к кнопкам и установка на кнопки иконок.
        self.exitButton.setIcon(QtGui.QIcon('icon/exit_to_app.png'))
        self.exitButton.clicked.connect(self.exit)

        # Выравниваем по центру
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

        # Нужные инструменты, чтобы перемещать форму по экрану.
        self.move_x = self.move_y = self.old_x = self.old_y = 0
        self.press = False

        # Служебные инструмены, чтобы убрать встроенные рамки формы.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

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

    # Функция для выхода из варианта. Вывод предупреждения. Диалоговое окно
    def exit(self):
        dialog = QMessageBox(self)
        dialog.setText('''Вы действительно хотите выйти?\n Учтите, что статистика не сохранится.''')
        dialog.setWindowTitle('Close')
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.buttonClicked.connect(self.close_question)
        dialog.exec_()

    # Если при диалоге получен ответ: Yes, выходим из варианта
    def close_question(self, button):
        if button.text() == '&Yes':
            self.hide()
            self.menu_window.show()
