import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QSpinBox, QLabel, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView
from PyQt5 import QtCore, QtGui
from Designs.design_MenuQuestion import *
from py.queries_db import make_up_exem, html_quastion, number_quastion, answer_question
from py.QuestionWidget import *
from py.ResultWidget import *


class MenuQuestion(QMainWindow, Ui_Menu_questions):
    def __init__(self, desktop, login, password, main_window):
        super().__init__()
        self.setupUi(self)

        self.desktop = desktop

        # Сохраняем нужную информацию о пользователе.
        self.login = login
        self.password = password

        self.id_t = 0

        # Сохранение навигационной формы для последующего показа
        self.main_window = main_window

        # Выравниваем форму по центру.
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

        self.spinboxs = []

        # Подключения функций к кнопкам и установка на кнопки иконок.
        self.exitButton.setIcon(QtGui.QIcon('icon/exit_to_app.png'))
        self.allButton.setIcon(QtGui.QIcon('icon/all.png'))
        self.clearButton.setIcon(QtGui.QIcon('icon/clear.png'))

        self.exitButton.clicked.connect(self.exit)
        self.allButton.clicked.connect(self.choice_all)
        self.clearButton.clicked.connect(self.clear_choice)
        self.beginButton.clicked.connect(self.start)

        # Загрузка контента в форму.
        self.load_content()

        # Нужные инструменты, чтобы перемещать форму по экрану.
        self.move_x = self.move_y = self.old_x = self.old_y = 0
        self.press = False

        self.quantity = [0] * 26

        # Служебные инструмены, чтобы убрать встроенные рамки формы.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def load_content(self):
        # Создание таблицы для составления варианта, где можно указать нужное кол-во заданий.
        self.compiler_table.setColumnCount(2)
        self.compiler_table.setHorizontalHeaderLabels(['Название задания', 'КОЛ-ВО'])
        self.compiler_table.setRowCount(26)
        # Названия заданий
        labels = ['Средства связи предложений в тексте',
                  'Определение лексического значения слова',
                  'Стилистический анализ текстов',
                  'Постановка ударения',
                  'Употребление паронимов',
                  'Лексические нормы',
                  'Морфологические нормы (образование форм слова)',
                  'Синтаксические нормы. Нормы согласования. Нормы управления',
                  'Правописание корней',
                  'Правописание приставок',
                  'Правописание суффиксов (кроме -Н-/-НН-)',
                  'Правописание личных окончаний глаголов и суффиксов причастий',
                  'Правописание НЕ и НИ',
                  'Слитное, дефисное, раздельное написание слов',
                  'Правописание -Н- и -НН- в суффиксах',
                  '''Пунктуация в сложносочиненном предложении и
в предложении с однородными членами''',
                  'Знаки препинания в предложениях с обособленными членами',
                  '''Знаки препинания при словах и конструкциях,
не связанных с членами предложения''',
                  'Знаки препинания в сложноподчиненном предложении',
                  'Знаки препинания в сложных предложениях с разными видами связи',
                  'Постановка знаков препинания в различных случаях',
                  'Смысловая и композиционная целостность текста',
                  'Функционально-смысловые типы речи',
                  'Лексическое значение слова',
                  'Средства связи предложений в тексте',
                  'Языковые средства выразительности']
        for i in range(26):
            for j in range(2):
                if j == 0:
                    label = QLabel(labels[i], self)
                    # Запрет на изменение данного столбца
                    label.setEnabled(False)
                    self.compiler_table.setCellWidget(i, j, label)
                else:
                    # Максимальное кол-во заданий одного типа 10
                    spinbox = QSpinBox(self)
                    spinbox.setMaximum(10)
                    self.compiler_table.setCellWidget(i, j, spinbox)
                    self.spinboxs.append(spinbox)
        self.compiler_table.resizeColumnsToContents()
        self.compiler_table.resizeRowToContents(10)

    # Функция для очистки выбранного кол-ва заданий
    def clear_choice(self):
        for i in range(26):
            self.spinboxs[i].setValue(0)

    # Функция устанавливает 1 в значение кол-во, если кол-во не было указано.
    def choice_all(self):
        for i in range(26):
            if self.spinboxs[i].value() == 0:
                self.spinboxs[i].setValue(1)

    # Создание варианта.
    def start(self):
        self.quantity = list(map(lambda x: x.value(), self.spinboxs))
        self.exam = make_up_exem(self.quantity)
        self.next = 1
        self.answers = answer_question(self.exam)
        self.user_answer = []
        try:
            # Вывод вопроса на экран
            self.id_t = self.exam.pop(0)
            self.question = Question(self.desktop, html_quastion(self.id_t), self)
            self.question.nextButton.clicked.connect(self.next_question)
            self.question.number_task.setText(self.question.number_task.text() +
                                              str(number_quastion(self.id_t)))
            self.question.show()
            # Вывод неких предупреждений по заданию.
            if number_quastion(self.id_t) == 24:
                self.question.warning_2.setText('Ответ должен быть записан в такой же форме,'
                                                ' как в тексте.')
            else:
                self.question.warning_2.setText('')
            self.hide()
            if not self.exam:
                self.question.nextButton.setText('Завершить')
        except IndexError:
            ...

    def next_question(self):
        # Обработка нажатия на кнопку и последующая смена форм.
        if self.exam:
            # Вывод вопроса на экран, сохранение ответа на него
            self.user_answer.append((number_quastion(self.id_t),
                                     self.question.answer.text().lower()))
            self.id_t = self.exam.pop(0)
            self.question.answer.setText('')
            self.question.content.setHtml(html_quastion(self.id_t))
            if number_quastion(self.id_t) == 24:
                self.question.warning_2.setText('Ответ должен быть записан в такой же форме,'
                                                ' как в тексте.')
            else:
                self.question.warning_2.setText('')
            if not self.exam:
                self.question.nextButton.setText('Завершить')
            self.question.number_task.setText(self.question.number_task.text().split('№')[0] + '№' +
                                              str(number_quastion(self.id_t)))
        else:
            # Когда цикл вопросов завершился, приступаем к выводу результатов.
            self.user_answer.append((number_quastion(self.id_t),
                                     self.question.answer.text().lower()))
            self.question.close()
            # Форма для показа результатов
            self.result = Result(self.desktop, self.user_answer, self.answers, self.login,
                                 self.password, self)
            self.result.show()

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

    # Реагируем на нажатие ESC, чтобы выполнить выход из формы
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.exit()

    # Функция для выхода из формы
    def exit(self):
        self.main_window.show()
        self.hide()
