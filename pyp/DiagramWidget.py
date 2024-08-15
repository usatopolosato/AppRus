import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsScene, QGraphicsEllipseItem
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from Designs.design_MainWindow import *
from pyp.queries_db import *
from Designs.design_diagram import Ui_DiagramWidget


class Diagram(QWidget, Ui_DiagramWidget):
    def __init__(self, desktop, login, password, task, widget):
        super().__init__()

        self.setupUi(self)

        # Сохраняем нужную информацию о пользователе.
        self.login = login
        self.password = password
        self.task = task

        # Для показа меню статистика, осуществляется показ после закрытия формы.
        self.menu_statistic = widget

        # Указываем номер задания.
        self.number_task.setText(self.number_task.text().split('№')[0] + '№' +
                                 str(task))

        # Загружаем контент. Составляем диаграмму на основе статистики.
        self.load_content()

        # Выравниваем форму по центру.
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

        # Нужные инструменты, чтобы перемещать форму по экрану.
        self.move_x = self.move_y = self.old_x = self.old_y = 0
        self.press = False

        # Подключения функций к кнопкам и установка на кнопки иконок.
        self.exitButton.clicked.connect(self.exit)
        self.exitButton.setIcon(QtGui.QIcon('icon/exit_to_app.png'))

        # Служебные инструмены, чтобы убрать встроенные рамки формы.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def load_content(self):
        # Делаем запрос, чтобы узнать кол-во правильных и неправльных ответов пользователя
        # по данному заданию.
        segments = statistic_task(self.login, self.password, self.task)
        scene = QGraphicsScene()
        if not any(segments):
            segments = [1]
        total = sum(segments)
        step_angle = 0
        colours = [QColor(0, 255, 0), QColor(255, 0, 0), QColor(132, 132, 132)]
        if len(segments) == 1:
            # Если пользователь не давал ответов по данному заданию, то мы создадим диаграмму серого
            # цвета.
            # Создания сегмента диаграммы и установка этому сегменту нужного цвета.
            segment = QGraphicsEllipseItem(0, 0, 300, 300)
            segment.setPos(0, 0)
            segment.setStartAngle(step_angle)
            # Максимальный размах 5760. Вычисляем угол сегмента
            angle = int(float(segments[0] * 5760) / total)
            step_angle = angle
            segment.setSpanAngle(angle)
            segment.setBrush(colours[2])
            scene.addItem(segment)
        else:
            # Меньший сегмент должен создаваться в начале
            if segments[0] <= segments[1]:
                # Создания сегмента диаграммы и установка этому сегменту нужного цвета.
                for i in range(len(segments)):
                    segment = QGraphicsEllipseItem(0, 0, 300, 300)
                    segment.setPos(0, 0)
                    # Устанавливаем стартовый угол сегмента на графической сцене.
                    segment.setStartAngle(step_angle)
                    # Максимальный размах 5760. Вычисляем угол сегмента
                    angle = int(float(segments[i] * 5760) / total)
                    step_angle += angle
                    segment.setSpanAngle(angle)
                    segment.setBrush(colours[i])
                    scene.addItem(segment)
            else:
                for i in range(len(segments) - 1, -1, -1):
                    segment = QGraphicsEllipseItem(0, 0, 300, 300)
                    segment.setPos(0, 0)
                    # Устанавливаем стартовый угол сегмента на графической сцене.
                    segment.setStartAngle(step_angle)
                    # Максимальный размах 5760. Вычисляем угол сегмента
                    angle = int(float(segments[0] * 5760) / total)
                    step_angle += angle
                    segment.setSpanAngle(angle)
                    segment.setBrush(colours[i])
                    scene.addItem(segment)
        self.diagram.setScene(scene)
        if len(segments) == 1:
            # Если пользователь не давал ответа на данное задание total = 1, чтобы не возникло
            # ошибки ZeroDivisionError.
            segments[0] = 0
            total = 1
        # Установим процент выполнения данного задания.
        self.result.setText(f'{segments[0] / total * 100:.2f}%')

    # Реагируем на нажатие ESC, чтобы выполнить выход из формы
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.exit()

    # Функция для выхода из формы.
    def exit(self):
        self.menu_statistic.show()
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
