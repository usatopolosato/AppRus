# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_theory.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TheoryWidget(object):
    def setupUi(self, TheoryWidget):
        TheoryWidget.setObjectName("TheoryWidget")
        TheoryWidget.resize(661, 608)
        self.centralwidget = QtWidgets.QWidget(TheoryWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.contentWidget = QtWidgets.QFrame(self.centralwidget)
        self.contentWidget.setGeometry(QtCore.QRect(40, 0, 571, 561))
        self.contentWidget.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"    border-radius: 20px;\n"
"}")
        self.contentWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentWidget.setObjectName("contentWidget")
        self.content = QtWidgets.QTextBrowser(self.contentWidget)
        self.content.setGeometry(QtCore.QRect(30, 40, 521, 491))
        self.content.setStyleSheet("")
        self.content.setObjectName("content")
        self.exitButton = QtWidgets.QPushButton(self.contentWidget)
        self.exitButton.setGeometry(QtCore.QRect(510, 0, 61, 51))
        self.exitButton.setStyleSheet("QPushButton{\n"
"    border-radius: 30px;\n"
"    background-color: none;\n"
"}")
        self.exitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/exit_to_app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon)
        self.exitButton.setIconSize(QtCore.QSize(64, 64))
        self.exitButton.setObjectName("exitButton")
        TheoryWidget.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TheoryWidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 21))
        self.menubar.setObjectName("menubar")
        TheoryWidget.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TheoryWidget)
        self.statusbar.setObjectName("statusbar")
        TheoryWidget.setStatusBar(self.statusbar)

        self.retranslateUi(TheoryWidget)
        QtCore.QMetaObject.connectSlotsByName(TheoryWidget)

    def retranslateUi(self, TheoryWidget):
        _translate = QtCore.QCoreApplication.translate
        TheoryWidget.setWindowTitle(_translate("TheoryWidget", "Виджет для теории"))
        self.content.setHtml(_translate("TheoryWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
