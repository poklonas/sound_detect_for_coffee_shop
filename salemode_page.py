# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salemode_page_hot.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1298, 669)
        MainWindow.setMinimumSize(QtCore.QSize(0, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(20, 20, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.icemenu_button = QtWidgets.QPushButton(self.centralwidget)
        self.icemenu_button.setGeometry(QtCore.QRect(220, 20, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.icemenu_button.setFont(font)
        self.icemenu_button.setObjectName("icemenu_button")
        self.hotmenu_button = QtWidgets.QPushButton(self.centralwidget)
        self.hotmenu_button.setGeometry(QtCore.QRect(480, 20, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hotmenu_button.setFont(font)
        self.hotmenu_button.setObjectName("hotmenu_button")
        self.frapemenu_button = QtWidgets.QPushButton(self.centralwidget)
        self.frapemenu_button.setGeometry(QtCore.QRect(740, 20, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.frapemenu_button.setFont(font)
        self.frapemenu_button.setObjectName("frapemenu_button")
        self.etcmenu_button = QtWidgets.QPushButton(self.centralwidget)
        self.etcmenu_button.setGeometry(QtCore.QRect(1000, 20, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.etcmenu_button.setFont(font)
        self.etcmenu_button.setObjectName("etcmenu_button")
        self.menu_scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.menu_scroll.setEnabled(True)
        self.menu_scroll.setGeometry(QtCore.QRect(270, 90, 981, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_scroll.sizePolicy().hasHeightForWidth())
        self.menu_scroll.setSizePolicy(sizePolicy)
        self.menu_scroll.setAutoFillBackground(False)
        self.menu_scroll.setLineWidth(1)
        self.menu_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.menu_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.menu_scroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.menu_scroll.setWidgetResizable(True)
        self.menu_scroll.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.menu_scroll.setObjectName("menu_scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -74, 962, 513))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.menu_scroll.setWidget(self.scrollAreaWidgetContents)
        
        self.bill_scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.bill_scroll.setGeometry(QtCore.QRect(20, 90, 231, 321))
        self.bill_scroll.setWidgetResizable(True)
        self.bill_scroll.setObjectName("bill_scroll")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 229, 319))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        #############################################################################
        self.tableView = QtWidgets.QTableView(self.scrollAreaWidgetContents_2)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 231, 321))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableView.setFont(font)
        self.tableView.AdjustToContents = True
        self.tableView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tableView.setObjectName("tableView")
        ####################################################################################
        self.bill_scroll.setWidget(self.scrollAreaWidgetContents_2)

        self.price_lcd_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.price_lcd_number.setGeometry(QtCore.QRect(90, 420, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_lcd_number.setFont(font)
        self.price_lcd_number.setProperty("intValue", 0)
        self.price_lcd_number.setObjectName("price_lcd_number")
        self.cost_label = QtWidgets.QLabel(self.centralwidget)
        self.cost_label.setGeometry(QtCore.QRect(20, 420, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cost_label.setFont(font)
        self.cost_label.setObjectName("cost_label")
        self.get_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.get_label_2.setGeometry(QtCore.QRect(20, 460, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.get_label_2.setFont(font)
        self.get_label_2.setObjectName("get_label_2")
        self.get_lcd_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.get_lcd_number.setGeometry(QtCore.QRect(90, 460, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.get_lcd_number.setFont(font)
        self.get_lcd_number.setProperty("intValue", 0)
        self.get_lcd_number.setObjectName("get_lcd_number")
        self.change_lcd_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.change_lcd_number.setGeometry(QtCore.QRect(90, 500, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.change_lcd_number.setFont(font)
        self.change_lcd_number.setProperty("intValue", 0)
        self.change_lcd_number.setObjectName("change_lcd_number")
        self.change_label = QtWidgets.QLabel(self.centralwidget)
        self.change_label.setGeometry(QtCore.QRect(10, 500, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.change_label.setFont(font)
        self.change_label.setObjectName("change_label")
        self.bill_button = QtWidgets.QPushButton(self.centralwidget)
        self.bill_button.setGeometry(QtCore.QRect(130, 550, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bill_button.setFont(font)
        self.bill_button.setObjectName("bill_button")
        self.sound_detect_button = QtWidgets.QPushButton(self.centralwidget)
        self.sound_detect_button.setGeometry(QtCore.QRect(700, 550, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sound_detect_button.setFont(font)
        self.sound_detect_button.setObjectName("sound_detect_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.icemenu_button.setText(_translate("MainWindow", "Ice"))
        self.hotmenu_button.setText(_translate("MainWindow", "Hot"))
        self.frapemenu_button.setText(_translate("MainWindow", "Frappe "))
        self.etcmenu_button.setText(_translate("MainWindow", "Other"))
        self.cost_label.setText(_translate("MainWindow", "Total"))
        self.get_label_2.setText(_translate("MainWindow", "Get"))
        self.change_label.setText(_translate("MainWindow", "Change"))
        self.bill_button.setText(_translate("MainWindow", "Payment"))
        self.sound_detect_button.setText(_translate("MainWindow", "Start order by voice"))


