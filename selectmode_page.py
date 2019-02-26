# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectmode_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1298, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userinfo_label = QtWidgets.QLabel(self.centralwidget)
        self.userinfo_label.setGeometry(QtCore.QRect(30, 30, 921, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.userinfo_label.setFont(font)
        self.userinfo_label.setObjectName("userinfo_label")
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(1030, 20, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.logout_button.setFont(font)
        self.logout_button.setObjectName("logout_button")
        self.salemode_button = QtWidgets.QPushButton(self.centralwidget)
        self.salemode_button.setGeometry(QtCore.QRect(60, 120, 1191, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.salemode_button.setFont(font)
        self.salemode_button.setObjectName("salemode_button")

        self.saleinfo_button = QtWidgets.QPushButton(self.centralwidget)
        self.saleinfo_button.setGeometry(QtCore.QRect(60, 200, 1191, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.saleinfo_button.setFont(font)
        self.saleinfo_button.setObjectName("saleinfo_button")

        self.update_rule_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_rule_button.setGeometry(QtCore.QRect(60, 280, 1191, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.update_rule_button.setFont(font)
        self.update_rule_button.setObjectName("update_rule_button")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.userinfo_label.setText(_translate("MainWindow", "User Info"))
        self.logout_button.setText(_translate("MainWindow", "Logout"))
        self.salemode_button.setText(_translate("MainWindow", "Sale Mode"))
        self.saleinfo_button.setText(_translate("MainWindow", "Sale Information"))
        self.update_rule_button.setText(_translate("MainWindow", "Update Rule"))

