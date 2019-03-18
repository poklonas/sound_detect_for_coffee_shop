# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manual_menu_popup2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(677, 559)
        self.manuname_label = QtWidgets.QLabel(Form)
        self.manuname_label.setGeometry(QtCore.QRect(20, 20, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.manuname_label.setFont(font)
        self.manuname_label.setObjectName("manuname_label")
        self.option_scroll = QtWidgets.QScrollArea(Form)
        self.option_scroll.setGeometry(QtCore.QRect(20, 60, 631, 391))
        self.option_scroll.setWidgetResizable(True)
        self.option_scroll.setObjectName("option_scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 389))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.qtyBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.qtyBox.setGeometry(QtCore.QRect(100, 20, 101, 31))
        self.qtyBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.qtyBox.setMinimum(1)
        self.qtyBox.setObjectName("qtyBox")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.label.setObjectName("label")
        self.sugarGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.sugarGroup.setGeometry(QtCore.QRect(10, 60, 601, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sugarGroup.setFont(font)
        self.sugarGroup.setObjectName("sugarGroup")
        self.sugarNormal = QtWidgets.QRadioButton(self.sugarGroup)
        self.sugarNormal.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.sugarNormal.setChecked(True)
        self.sugarNormal.setObjectName("sugarNormal")
        self.sugarNone = QtWidgets.QRadioButton(self.sugarGroup)
        self.sugarNone.setGeometry(QtCore.QRect(130, 40, 91, 21))
        self.sugarNone.setObjectName("sugarNone")
        self.sugarLow = QtWidgets.QRadioButton(self.sugarGroup)
        self.sugarLow.setGeometry(QtCore.QRect(240, 40, 91, 21))
        self.sugarLow.setObjectName("sugarLow")
        self.sugarAdd = QtWidgets.QRadioButton(self.sugarGroup)
        self.sugarAdd.setGeometry(QtCore.QRect(330, 40, 91, 21))
        self.sugarAdd.setObjectName("sugarAdd")
        self.milkGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.milkGroup.setGeometry(QtCore.QRect(10, 140, 601, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.milkGroup.setFont(font)
        self.milkGroup.setObjectName("milkGroup")
        self.milkNormal = QtWidgets.QRadioButton(self.milkGroup)
        self.milkNormal.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.milkNormal.setChecked(True)
        self.milkNormal.setAutoRepeat(False)
        self.milkNormal.setObjectName("milkNormal")
        self.milkNone = QtWidgets.QRadioButton(self.milkGroup)
        self.milkNone.setGeometry(QtCore.QRect(130, 40, 91, 21))
        self.milkNone.setObjectName("milkNone")
        self.milkLow = QtWidgets.QRadioButton(self.milkGroup)
        self.milkLow.setGeometry(QtCore.QRect(240, 40, 91, 21))
        self.milkLow.setObjectName("milkLow")
        self.milkAdd = QtWidgets.QRadioButton(self.milkGroup)
        self.milkAdd.setGeometry(QtCore.QRect(330, 40, 91, 21))
        self.milkAdd.setObjectName("milkAdd")
        self.creamGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.creamGroup.setGeometry(QtCore.QRect(10, 220, 601, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.creamGroup.setFont(font)
        self.creamGroup.setObjectName("creamGroup")
        self.creamNormal = QtWidgets.QRadioButton(self.creamGroup)
        self.creamNormal.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.creamNormal.setChecked(True)
        self.creamNormal.setObjectName("creamNormal")
        self.creamNone = QtWidgets.QRadioButton(self.creamGroup)
        self.creamNone.setGeometry(QtCore.QRect(130, 40, 91, 21))
        self.creamNone.setObjectName("creamNone")
        self.creamLow = QtWidgets.QRadioButton(self.creamGroup)
        self.creamLow.setGeometry(QtCore.QRect(240, 40, 91, 21))
        self.creamLow.setObjectName("creamLow")
        self.creamAdd = QtWidgets.QRadioButton(self.creamGroup)
        self.creamAdd.setGeometry(QtCore.QRect(330, 40, 91, 21))
        self.creamAdd.setObjectName("creamAdd")
        self.whipGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.whipGroup.setGeometry(QtCore.QRect(10, 300, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.whipGroup.setFont(font)
        self.whipGroup.setObjectName("whipGroup")
        self.WhipNone = QtWidgets.QRadioButton(self.whipGroup)
        self.WhipNone.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.WhipNone.setChecked(True)
        self.WhipNone.setObjectName("WhipNone")
        self.whipAdd = QtWidgets.QRadioButton(self.whipGroup)
        self.whipAdd.setGeometry(QtCore.QRect(130, 40, 91, 21))
        self.whipAdd.setObjectName("whipAdd")
        self.sizeGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.sizeGroup.setGeometry(QtCore.QRect(310, 300, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sizeGroup.setFont(font)
        self.sizeGroup.setObjectName("sizeGroup")
        self.sizeM = QtWidgets.QRadioButton(self.sizeGroup)
        self.sizeM.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.sizeM.setChecked(True)
        self.sizeM.setObjectName("sizeM")
        self.sizeL = QtWidgets.QRadioButton(self.sizeGroup)
        self.sizeL.setGeometry(QtCore.QRect(130, 40, 91, 21))
        self.sizeL.setObjectName("sizeL")
        self.option_scroll.setWidget(self.scrollAreaWidgetContents)
        self.add_button = QtWidgets.QPushButton(Form)
        self.add_button.setGeometry(QtCore.QRect(20, 460, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.cancle_button = QtWidgets.QPushButton(Form)
        self.cancle_button.setGeometry(QtCore.QRect(380, 460, 271, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.cancle_button.setFont(font)
        self.cancle_button.setObjectName("cancle_button")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def get_option(self):
        val = []
        val.append(self.get_sugar_checked())
        val.append(self.get_milk_checked())
        val.append(self.get_cream_checked())
        val.append(self.get_whip_checked())
        return val

    def get_size(self):
        if( self.sizeL.isChecked() ):
            return "L"
        else:
            return "M"

    def get_sugar_checked(self):
        if( self.sugarAdd.isChecked() ):
            return "Add_Sugar"
        elif( self.sugarLow.isChecked() ):
            return "Low_Sugar"
        elif( self.sugarNone.isChecked() ):
            return "No_Sugar"
        else:
            return "Normal"
    
    def get_cream_checked(self):
        if( self.creamAdd.isChecked() ):
            return "Add_Cream"
        elif( self.creamLow.isChecked() ):
            return "Low_Cream"
        elif( self.creamNone.isChecked() ):
            return "No_Cream"
        else:
            return "Normal"

    def get_whip_checked(self):
        if( self.whipAdd.isChecked() ):
            return "Whip_Cream"
        else:
            return "Normal"

    def get_qty(self):
        return self.qtyBox.value()

    def get_milk_checked(self):
        if( self.milkAdd.isChecked() ):
            return "Add_Milk"
        elif( self.milkLow.isChecked() ):
            return "Low_Milk"
        elif( self.milkNone.isChecked() ):
            return "No_Milk"
        else:
            return "Normal"


    def set_sugar_disable(self):
        self.sugarAdd.setEnabled(False)
        self.sugarLow.setEnabled(False)
        self.sugarNone.setEnabled(False)
        self.sugarNormal.setEnabled(False)

    def set_milk_disable(self):
        self.milkAdd.setEnabled(False)
        self.milkLow.setEnabled(False)
        self.milkNone.setEnabled(False)
        self.milkNormal.setEnabled(False)

    def set_cream_disable(self):
        self.creamAdd.setEnabled(False)
        self.creamLow.setEnabled(False)
        self.creamNone.setEnabled(False)
        self.creamNormal.setEnabled(False)

    def set_whipcream_disable(self):
        self.whipAdd.setEnabled(False)
        self.WhipNone.setEnabled(False)

    def set_size_disable(self):
        self.sizeL.setEnabled(False)
        self.sizeM.setEnabled(False)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.manuname_label.setText(_translate("Form", "Menu Name"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Qty</span></p></body></html>"))
        self.sugarGroup.setTitle(_translate("Form", "Sugar"))
        self.sugarNormal.setText(_translate("Form", "Normal"))
        self.sugarNone.setText(_translate("Form", "None"))
        self.sugarLow.setText(_translate("Form", "Low"))
        self.sugarAdd.setText(_translate("Form", "Add"))
        self.milkGroup.setTitle(_translate("Form", "Milk"))
        self.milkNormal.setText(_translate("Form", "Normal"))
        self.milkNone.setText(_translate("Form", "None"))
        self.milkLow.setText(_translate("Form", "Low"))
        self.milkAdd.setText(_translate("Form", "Add"))
        self.creamGroup.setTitle(_translate("Form", "Cream"))
        self.creamNormal.setText(_translate("Form", "Normal"))
        self.creamNone.setText(_translate("Form", "None"))
        self.creamLow.setText(_translate("Form", "Low"))
        self.creamAdd.setText(_translate("Form", "Add"))
        self.whipGroup.setTitle(_translate("Form", "Whip Cream"))
        self.WhipNone.setText(_translate("Form", "None"))
        self.whipAdd.setText(_translate("Form", "Add"))
        self.sizeGroup.setTitle(_translate("Form", "Size"))
        self.sizeM.setText(_translate("Form", "M"))
        self.sizeL.setText(_translate("Form", "L"))
        self.add_button.setText(_translate("Form", "Add"))
        self.cancle_button.setText(_translate("Form", "Cancel"))

