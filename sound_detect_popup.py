# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sound_detect_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(410, 360)
        self.picture_view = QtWidgets.QGraphicsView(Form)
        self.picture_view.setGeometry(QtCore.QRect(40, 20, 321, 231))
        self.picture_view.setObjectName("picture_view")
        self.start_stop_button = QtWidgets.QPushButton(Form)
        self.start_stop_button.setGeometry(QtCore.QRect(40, 270, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.start_stop_button.setFont(font)
        self.start_stop_button.setObjectName("start_stop_button")
        self.cancle_button = QtWidgets.QPushButton(Form)
        self.cancle_button.setGeometry(QtCore.QRect(200, 270, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.cancle_button.setFont(font)
        self.cancle_button.setObjectName("cancle_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.start_stop_button.setText(_translate("Form", "Start/Stop"))
        self.cancle_button.setText(_translate("Form", "Cancle"))

