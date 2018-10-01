# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manual_menu_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(677, 514)
        self.manuname_label = QtWidgets.QLabel(Form)
        self.manuname_label.setGeometry(QtCore.QRect(20, 20, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.manuname_label.setFont(font)
        self.manuname_label.setObjectName("manuname_label")
        self.option_scroll = QtWidgets.QScrollArea(Form)
        self.option_scroll.setGeometry(QtCore.QRect(20, 60, 631, 341))
        self.option_scroll.setWidgetResizable(True)
        self.option_scroll.setObjectName("option_scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 339))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.nosugar_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.nosugar_radio.setGeometry(QtCore.QRect(10, 10, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nosugar_radio.setFont(font)
        self.nosugar_radio.setObjectName("nosugar_radio")
        self.sweet_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.sweet_radio.setGeometry(QtCore.QRect(10, 40, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sweet_radio.setFont(font)
        self.sweet_radio.setObjectName("sweet_radio")
        self.option_scroll.setWidget(self.scrollAreaWidgetContents)
        self.add_button = QtWidgets.QPushButton(Form)
        self.add_button.setGeometry(QtCore.QRect(20, 410, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.cancle_button = QtWidgets.QPushButton(Form)
        self.cancle_button.setGeometry(QtCore.QRect(380, 410, 271, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.cancle_button.setFont(font)
        self.cancle_button.setObjectName("cancle_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.manuname_label.setText(_translate("Form", "Menu Name"))
        self.nosugar_radio.setText(_translate("Form", "No sugar"))
        self.sweet_radio.setText(_translate("Form", "sweet"))
        self.add_button.setText(_translate("Form", "Add"))
        self.cancle_button.setText(_translate("Form", "Cancle"))

