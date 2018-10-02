# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1298, 669)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_group = QtWidgets.QGroupBox(self.centralwidget)
        self.login_group.setGeometry(QtCore.QRect(160, 270, 961, 331))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.login_group.setFont(font)
        self.login_group.setAutoFillBackground(False)
        self.login_group.setObjectName("login_group")
        self.username_edit = QtWidgets.QTextEdit(self.login_group)
        self.username_edit.setGeometry(QtCore.QRect(230, 90, 631, 61))
        self.username_edit.setObjectName("username_edit")
        self.password_edit = QtWidgets.QTextEdit(self.login_group)
        self.password_edit.setGeometry(QtCore.QRect(230, 190, 631, 61))
        self.password_edit.setObjectName("password_edit")
        self.login_button = QtWidgets.QPushButton(self.login_group)
        self.login_button.setGeometry(QtCore.QRect(450, 270, 221, 51))
        self.login_button.setObjectName("login_button")
        self.username_label = QtWidgets.QLabel(self.login_group)
        self.username_label.setGeometry(QtCore.QRect(16, 90, 181, 61))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.login_group)
        self.password_label.setGeometry(QtCore.QRect(20, 190, 181, 61))
        self.password_label.setObjectName("password_label")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(840, 10, 451, 21))
        self.error_label.setObjectName("error_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_group.setTitle(_translate("MainWindow", "LOGIN"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.username_label.setText(_translate("MainWindow", "User name"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.error_label.setText(_translate("MainWindow", "Error"))

