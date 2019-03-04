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

        self.sugarBox = QtWidgets.QComboBox(Form)
        self.sugarBox.setGeometry(QtCore.QRect(150, 100, 131, 16))
        self.sugarBox.setObjectName("sugarBox")
        self.sugarBox.addItem("")
        self.sugarBox.addItem("")
        self.sugarBox.addItem("")
        self.sugarBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 100, 71, 20))
        self.label.setObjectName("Sugar")

        self.milkBox = QtWidgets.QComboBox(Form)
        self.milkBox.setGeometry(QtCore.QRect(150, 150, 131, 16))
        self.milkBox.setObjectName("milkBox")
        self.milkBox.addItem("")
        self.milkBox.addItem("")
        self.milkBox.addItem("")
        self.milkBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 71, 20))
        self.label_2.setObjectName("Milk")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 71, 20))
        self.label_3.setObjectName("Cream")
        self.creamBox = QtWidgets.QComboBox(Form)
        self.creamBox.setGeometry(QtCore.QRect(150, 200, 131, 16))
        self.creamBox.setObjectName("creamBox")
        self.creamBox.addItem("")
        self.creamBox.addItem("")
        self.creamBox.addItem("")
        self.creamBox.addItem("")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 71, 20))
        self.label_4.setObjectName("Whip_Cream")
        self.whipCreamBox = QtWidgets.QComboBox(Form)
        self.whipCreamBox.setGeometry(QtCore.QRect(150, 250, 131, 16))
        self.whipCreamBox.setObjectName("whipCreamBox")
        self.whipCreamBox.addItem("")
        self.whipCreamBox.addItem("")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 300, 71, 20))
        self.label_5.setObjectName("Size")
        self.sizeBox = QtWidgets.QComboBox(Form)
        self.sizeBox.setGeometry(QtCore.QRect(150, 300, 131, 16))
        self.sizeBox.setObjectName("sizeBox")
        self.sizeBox.addItem("")
        self.sizeBox.addItem("")

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

    def get_option(self):
        val = []
        val.append(self.sugarBox.currentText())
        val.append(self.milkBox.currentText())
        val.append(self.creamBox.currentText())
        val.append(self.whipCreamBox.currentText())
        return val

    def get_size(self):
        return self.sizeBox.currentText()

    def set_sugar_disable(self):
        self.sugarBox.setEnabled(False)

    def set_milk_disable(self):
        self.milkBox.setEnabled(False)

    def set_cream_disable(self):
        self.creamBox.setEnabled(False)

    def set_whipcream_disable(self):
        self.whipCreamBox.setEnabled(False)

    def set_size_disable(self):
        self.sizeBox.setEnabled(False)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.manuname_label.setText(_translate("Form", "Menu Name"))
        self.add_button.setText(_translate("Form", "Add"))
        self.cancle_button.setText(_translate("Form", "Cancle"))

        self.sugarBox.setItemText(0, _translate("Form", "Normal"))
        self.sugarBox.setItemText(1, _translate("Form", "No_Sugar"))
        self.sugarBox.setItemText(2, _translate("Form", "Low_Sugar"))
        self.sugarBox.setItemText(3, _translate("Form", "Add_Sugar"))
        self.label.setText(_translate("Form", "Sugar"))
        self.milkBox.setItemText(0, _translate("Form", "Normal"))
        self.milkBox.setItemText(1, _translate("Form", "No_Milk"))
        self.milkBox.setItemText(2, _translate("Form", "Low_Milk"))
        self.milkBox.setItemText(3, _translate("Form", "Add_Milk"))
        self.label_2.setText(_translate("Form", "Milk"))
        self.label_3.setText(_translate("Form", "Cream"))
        self.creamBox.setItemText(0, _translate("Form", "Normal"))
        self.creamBox.setItemText(1, _translate("Form", "No_Cream"))
        self.creamBox.setItemText(2, _translate("Form", "Low_Cream"))
        self.creamBox.setItemText(3, _translate("Form", "Add_Cream"))
        self.label_4.setText(_translate("Form", "Whip_Cream"))
        self.whipCreamBox.setItemText(0, _translate("Form", "Normal"))
        self.whipCreamBox.setItemText(1, _translate("Form", "Whip_Cream"))
        self.label_5.setText(_translate("Form", "Size"))
        self.sizeBox.setItemText(0, _translate("Form", "M"))
        self.sizeBox.setItemText(1, _translate("Form", "L"))
