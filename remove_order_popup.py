# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remove_order_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(653, 204)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.labelQty = QtWidgets.QLabel(Form)
        self.labelQty.setGeometry(QtCore.QRect(30, 40, 601, 71))
        self.labelQty.setFont(font)
        self.labelQty.setObjectName("labelQty")

        self.yesButton = QtWidgets.QPushButton(Form)
        self.yesButton.setGeometry(QtCore.QRect(300, 140, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yesButton.setFont(font)
        self.yesButton.setObjectName("yesButton")
        self.noButton = QtWidgets.QPushButton(Form)
        self.noButton.setGeometry(QtCore.QRect(480, 140, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.noButton.setFont(font)
        self.noButton.setObjectName("noButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.yesButton.setText(_translate("Form", "Yes"))
        self.noButton.setText(_translate("Form", "No , and close this popup"))

