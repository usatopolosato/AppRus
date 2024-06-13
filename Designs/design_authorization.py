# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_authorization.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Authorization(object):
    def setupUi(self, Authorization):
        Authorization.setObjectName("Authorization")
        Authorization.resize(591, 477)
        self.content = QtWidgets.QFrame(Authorization)
        self.content.setGeometry(QtCore.QRect(10, 20, 571, 441))
        self.content.setStyleSheet("QFrame {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(161, 161, 161);\n"
"}\n"
"QPushButton {\n"
"    cursor: pointer;\n"
"}")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.label_authorization = QtWidgets.QLabel(self.content)
        self.label_authorization.setGeometry(QtCore.QRect(6, 19, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(22)
        self.label_authorization.setFont(font)
        self.label_authorization.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.label_authorization.setAlignment(QtCore.Qt.AlignCenter)
        self.label_authorization.setObjectName("label_authorization")
        self.loginButton = QtWidgets.QPushButton(self.content)
        self.loginButton.setGeometry(QtCore.QRect(150, 310, 281, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(12)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.registrationButton = QtWidgets.QPushButton(self.content)
        self.registrationButton.setGeometry(QtCore.QRect(150, 360, 281, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(12)
        self.registrationButton.setFont(font)
        self.registrationButton.setObjectName("registrationButton")
        self.errorLabel = QtWidgets.QLabel(self.content)
        self.errorLabel.setGeometry(QtCore.QRect(16, 250, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("QLabel {\n"
"    color: red;\n"
"}")
        self.errorLabel.setText("")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.content)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 401, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_login = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.horizontalLayout.addWidget(self.label_login)
        self.login = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setMaximumSize(QtCore.QSize(400, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.login.setFont(font)
        self.login.setText("")
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.content)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 170, 401, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_password = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_2.addWidget(self.label_password)
        self.password = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMaximumSize(QtCore.QSize(400, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setText("")
        self.password.setObjectName("password")
        self.horizontalLayout_2.addWidget(self.password)
        self.visibilityButton = QtWidgets.QPushButton(self.content)
        self.visibilityButton.setGeometry(QtCore.QRect(430, 180, 41, 31))
        self.visibilityButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/visibility_off.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon/visibility.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.visibilityButton.setIcon(icon)
        self.visibilityButton.setCheckable(True)
        self.visibilityButton.setChecked(False)
        self.visibilityButton.setObjectName("visibilityButton")
        self.exitButton = QtWidgets.QPushButton(self.content)
        self.exitButton.setGeometry(QtCore.QRect(510, 0, 61, 51))
        self.exitButton.setStyleSheet("QPushButton{\n"
"    border-radius: 30px;\n"
"}")
        self.exitButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/exit_to_app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon1)
        self.exitButton.setIconSize(QtCore.QSize(64, 64))
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(Authorization)
        QtCore.QMetaObject.connectSlotsByName(Authorization)

    def retranslateUi(self, Authorization):
        _translate = QtCore.QCoreApplication.translate
        Authorization.setWindowTitle(_translate("Authorization", "Authorization"))
        self.label_authorization.setText(_translate("Authorization", "Авторизация"))
        self.loginButton.setText(_translate("Authorization", "SIGN IN"))
        self.registrationButton.setText(_translate("Authorization", "SIGN UP"))
        self.label_login.setText(_translate("Authorization", "Логин:"))
        self.login.setPlaceholderText(_translate("Authorization", "Логин"))
        self.label_password.setText(_translate("Authorization", "Пароль:"))
        self.password.setPlaceholderText(_translate("Authorization", "Пароль"))
