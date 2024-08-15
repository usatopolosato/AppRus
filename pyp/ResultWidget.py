import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QSpinBox, QLabel, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtGui
from Designs.design_result import *
from pyp.queries_db import make_up_exem
from pyp.queries_db import html_quastion
from pyp.add_db import new_statistic


class Result(QMainWindow, Ui_resultWidget):
    def __init__(self, desktop, user_answer, answer, login, password, window):
        super().__init__()
        self.setupUi(self)

        self.desktop = desktop

        # Для показа меню вопросы, осуществляется показ после закрытия формы.
        self.menu_window = window

        # Сохраняем нужную информацию о пользователе.
        self.login = login
        self.password = password

        # Загрузка результатов
        self.load_content(user_answer, answer)

        # Подключения функций к кнопкам и установка на кнопки иконок.
        self.exitButton.setIcon(QtGui.QIcon('icon/exit_to_app.png'))
        self.exitButton.clicked.connect(self.exit)

        # Выравнивание по центру
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

    # Результаты мы будем выводить в таблицу.
    # Сравнение ответов пользователя с корректным ответами и выделение нужным цветом строки таблицы
    # в зависимости от того, правильно ответил пользователь или нет.
    def load_content(self, user_answer, answer):
        self.result.setRowCount(0)
        for i, el in enumerate(user_answer):
            self.result.setRowCount(self.result.rowCount() + 1)
            self.result.setItem(i, 0, QTableWidgetItem(el[1]))
            # Получения списка корректных ответов
            correct = answer[i].split(' ИЛИ ')
            # После каждой проверки обновляется статистика пользователя
            if el[0] in [8, 25, 26, 6, 7, 1, 5]:
                if el[1] in correct:
                    # Обновление статистики
                    new_statistic(self.login, self.password, el[0] - 1, True)
                    self.result.setItem(i, 1, QTableWidgetItem(el[1]))
                    self.result.item(i, 0).setBackground(QColor(107, 255, 66))
                    self.result.item(i, 1).setBackground(QColor(107, 255, 66))
                else:
                    # Обновление статистики
                    new_statistic(self.login, self.password, el[0] - 1, False)
                    self.result.setItem(i, 1, QTableWidgetItem(correct[0]))
                    self.result.item(i, 0).setBackground(QColor(255, 80, 83))
                    self.result.item(i, 1).setBackground(QColor(255, 80, 83))
            else:
                if ''.join(sorted(el[1])) in correct:
                    # Обновление статистики
                    new_statistic(self.login, self.password, el[0] - 1, True)
                    self.result.setItem(i, 1, QTableWidgetItem(el[1]))
                    self.result.item(i, 0).setBackground(QColor(107, 255, 66))
                    self.result.item(i, 1).setBackground(QColor(107, 255, 66))
                else:
                    # Обновление статистики
                    new_statistic(self.login, self.password, el[0] - 1, False)
                    self.result.setItem(i, 1, QTableWidgetItem(correct[0]))
                    self.result.item(i, 0).setBackground(QColor(255, 80, 83))
                    self.result.item(i, 1).setBackground(QColor(255, 80, 83))
        self.result.resizeColumnsToContents()
        self.contentWidget.resize(self.result.width() + 30, self.result.height() + 70)
        # Сделано для того, чтобы нельзя было изменять элементы таблицы.
        self.result.setEditTriggers(QAbstractItemView.NoEditTriggers)

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

    # Выход из формы результат и показ меню вопросы
    def exit(self):
        self.menu_window.show()
        self.hide()

    # Реагируем на нажатие ESC, чтобы выполнить выход из формы
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.exit()
