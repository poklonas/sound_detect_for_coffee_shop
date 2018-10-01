# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 299)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 210, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.warn_label = QtWidgets.QLabel(Form)
        self.warn_label.setGeometry(QtCore.QRect(20, 30, 351, 151))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.warn_label.setFont(font)
        self.warn_label.setObjectName("warn_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Yes"))
        self.pushButton_2.setText(_translate("Form", "No"))
        self.warn_label.setText(_translate("Form", "Warn"))

