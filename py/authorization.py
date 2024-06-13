import sys
from Designs.design_authorization import Ui_Authorization
from PyQt5.QtWidgets import QWidget, QLineEdit, QInputDialog
from PyQt5 import QtCore, QtGui
from py.queries_db import *
from py.add_db import *
from py.check_mail import *


class Authorization(QWidget, Ui_Authorization):
    def __init__(self, desktop, main_window):
        super().__init__()
        self.setupUi(self)

        # Выравниваем форму по центру.
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

        # Для последующего показа навигационной формы.
        self.main_window = main_window

        # Нужные инструменты, чтобы перемещать форму по экрану.
        self.move_x = self.move_y = self.old_x = self.old_y = 0
        self.press = False

        # Подключения функций к кнопкам и установка на кнопки иконок.
        self.exitButton.clicked.connect(self.exit)
        self.exitButton.setIcon(QtGui.QIcon('icon/exit_to_app.png'))

        self.visibilityButton.setIcon(QtGui.QIcon('icon/visibility_off.png'))
        self.visibilityButton.clicked.connect(self.visible_password)

        self.loginButton.clicked.connect(self.sign_in)
        self.registrationButton.clicked.connect(self.sign_up)

        # При изменении информации в полях логин и пароль очищаем сообщения об ошибке.
        self.login.textChanged.connect(self.clear_errorLabels)
        self.password.textChanged.connect(self.clear_errorLabels)

        # Сделано для того, чтобы пароль нельзя было видеть.
        self.password.setEchoMode(QLineEdit.Password)

        # Служебные инструмены, чтобы убрать встроенные рамки формы.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    # Функция для изменения видимости пароля и изменения иконки кнопки видимости.
    def visible_password(self):
        if self.visibilityButton.isChecked():
            self.visibilityButton.setIcon(QtGui.QIcon('icon/visibility.png'))
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.visibilityButton.setIcon(QtGui.QIcon('icon/visibility_off.png'))
            self.password.setEchoMode(QLineEdit.Password)

    # Функция, предназначенная для входа в аккаунт.
    def sign_in(self):
        login = self.login.text()
        password = self.password.text()
        ERROR = 0
        # Исключения для того, чтобы сообщить, что ключевые поля пустые.
        try:
            assert len(login) != 0
        except AssertionError:
            ERROR = 1
            self.errorLabel.setText('Для начала введите логин и пароль')
        try:
            assert len(password) != 0
        except AssertionError:
            ERROR = 1
            self.errorLabel.setText('Для начала введите логин и пароль')
        if not ERROR:
            # Существует ли пользователь с таким логином?
            query = check_db(login, password)
            ''' Если да, то мы входим в аккаунт, скрываем форму авторизации и показываем 
                навигационную форму. Если нет, то сообщаем пользователю об ошибке.'''
            try:
                assert len(query) != 0
                self.main_window.login = login
                self.main_window.password = password
                self.main_window.show()
                self.close()
            except AssertionError:
                self.errorLabel.setText('Неверный логин или пароль')

    # Функция, предназначенная для регистрации в системе.
    def sign_up(self):
        self.errorLabel.clear()
        i = 0
        ''' Существует цикл, состоящий из 7 вопросов, которые соберут нужную информацию о 
        пользователе. Если был дан ответ на все вопросы, то пользователь успешно зарегистрируется в 
        системе.'''
        while i != 7:
            ERROR = 0
            if i == 0:
                email, ok_pressed = QInputDialog.getText(self, "Введите почту", '''
Введите свой почтовый адрес(поддерживаются yandex, gmail, mail, icloud)''')
                if ok_pressed:
                    # Вызываем функцию для проверки правильности email.
                    email, diagnostics = check_mail(email)
                    if not diagnostics:
                        # Сообщаем об ошибке.
                        self.errorLabel.setText(email)
                        ERROR = 1
            elif i == 1:
                name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                        "Назовите свое имя:")
                # Проверяем непустое ли поле имя.
                try:
                    assert len(name.replace(' ', '')) != 0 or not ok_pressed
                except AssertionError:
                    # Сообщаем об ошибке.
                    ERROR = 1
                    self.errorLabel.setText('Имя не может быть пустой строкой.')
            elif i == 2:
                surname, ok_pressed = QInputDialog.getText(self, "Введите фамилию",
                                                           "Назовите свою фамилию:")
                # Проверяем непустое ли поле фамилия.
                try:
                    assert len(surname.replace(' ', '')) != 0 or not ok_pressed
                except AssertionError:
                    # Сообщаем об ошибке.
                    ERROR = 1
                    self.errorLabel.setText('Фамилия не может быть пустой строкой.')
            elif i == 3:
                clas, ok_pressed = QInputDialog.getInt(
                    self, "Введите свой класс", "В каком классе ты учишься?",
                    10, 1, 11, 1)
            elif i == 4:
                login, ok_pressed = QInputDialog.getText(self, "Введите логин",
                                                         "Придумай себе логин")
                # Проверяем правильность заполнения поля логин.
                try:
                    assert len(login) != 0 or not ok_pressed
                    if ' ' in login:
                        # Сообщаем об ошибке.
                        self.errorLabel.setText('Логин содержит запрещенные символы')
                        ERROR = 1
                except AssertionError:
                    # Сообщаем об ошибке.
                    ERROR = 1
                    self.errorLabel.setText('Логин не может быть пустой строкой.')
                try:
                    assert len(check_login(login)) == 0 or not ok_pressed
                except AssertionError:
                    # Сообщаем об ошибке.
                    self.errorLabel.setText('Пользователь с таким логином уже существует')
                    ERROR = 1
            elif i == 5:
                password, ok_pressed = QInputDialog.getText(self, "Введите пароль",
                                                            "Придумай себе пароль(от 9 символов)",
                                                            QLineEdit.Password)
                # Проверяем правильность заполнения поля пароль.
                try:
                    assert len(password) >= 9 or not ok_pressed
                except AssertionError:
                    # Сообщаем об ошибке.
                    ERROR = 1
                    self.errorLabel.setText('Пароль содержит слишком мало символов.')
            elif i == 6:
                new_password, ok_pressed = QInputDialog.getText(self, "Повтори пароль",
                                                         "Повторите пароль", QLineEdit.Password)
                # Проверяем совпадает ли повторный ввод пароля.
                if new_password != password and ok_pressed:
                    # Сообщаем об ошибке.
                    self.errorLabel.setText('Пароли не совпадают.')
                    ERROR = 1
                    i -= 1
            ''' Если пользователь нажал кнопку ок, то проверяем на наличия ошибок. Если нет,
                завершаем регистрацию.'''
            if ok_pressed:
                # Если все хорошо, то продолжаем работу.Если нет, просим пользователя повторить ввод
                if not ERROR:
                    self.errorLabel.clear()
                    i += 1
            else:
                self.errorLabel.clear()
                break
        if i == 7:
            '''Если пользователь ответил на все вопросы исправно, то регистрируем его в базу 
               данных.'''
            id_data = add_data(name, email, surname, clas)
            id_statistic = add_statistic()
            add_account(login, password, id_data, id_statistic)
            self.errorLabel.setText('Регистрация прошла успешно')

    # Функция для очистки сообщения об ошибке.
    def clear_errorLabels(self):
        self.errorLabel.clear()

    # Функция для выхода из приложения.
    def exit(self):
        sys.exit()

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
