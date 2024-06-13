import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui
from Designs.design_MainWindow import *
from py.queries_db import *
from py.MenuTheoryWidget import MenuTheory
from py.MenuQuestion import MenuQuestion
from py.MenuStatistic import MenuStatistic


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, desktop):
        super().__init__()
        self.setupUi(self)

        self.desktop = desktop

        # Выравниваем форму по центру
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

        self.login = self.password = ''

        # Нужные инструменты, чтобы перемещать форму по экрану.
        self.move_x = self.move_y = self.old_x = self.old_y = 0
        self.press = False

        # Устанавливаем аватар. Корректируем его размеры.
        image = QtGui.QPixmap('image/avatar.jpg')
        height = self.avatar.height()
        width = self.avatar.width()
        self.avatar.setPixmap(image.scaled(width, height, QtCore.Qt.KeepAspectRatio))

        # Подключаем нужные функции к кнопкам и устанавливаем иконки к некоторым кнопкам.
        self.statisticButton.clicked.connect(self.show_menu_statistic)

        self.exitButton.clicked.connect(self.exit)
        self.exitButton.setIcon(QtGui.QIcon('icon/exit_to_app.png'))

        self.theoryButton.clicked.connect(self.show_menu_theory)
        self.practiceButton.clicked.connect(self.show_menu_question)

        # Служебные инструмены, чтобы убрать встроенные рамки формы.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    # Показываем соответствующие формы, которые были выбраны в меню навигации.
    def show_menu_theory(self):
        self.menu_theory = MenuTheory(self.desktop, self)
        self.menu_theory.show()
        self.hide()

    def show_menu_question(self):
        self.menu_question = MenuQuestion(self.desktop, self.login, self.password, self)
        self.menu_question.show()
        self.hide()

    def show_menu_statistic(self):
        self.menu_statistic = MenuStatistic(self.desktop, self.login, self.password, self)
        self.menu_statistic.show()
        self.hide()

    # При создании формы нам нужно указать имя и фамилию пользователя.
    def paintEvent(self, event):
        name, surname = query_data(self.login, self.password)[0]
        self.name.setText(name)
        self.surname.setText(surname)

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

    # Функция для выхода из приложения.
    def exit(self):
        sys.exit()
