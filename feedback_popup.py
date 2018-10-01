# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedback_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 179)
        self.something_label = QtWidgets.QLabel(Form)
        self.something_label.setGeometry(QtCore.QRect(20, 10, 361, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.something_label.setFont(font)
        self.something_label.setObjectName("something_label")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(120, 120, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.something_label.setText(_translate("Form", "something"))
        self.back_button.setText(_translate("Form", "Back"))

