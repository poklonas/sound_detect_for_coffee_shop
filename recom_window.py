# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recom_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QGraphicsScene
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap 

class Recom_window(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.recommend = ['./image/hot/Hot_Latte.GIF','./image/hot/Hot_Cappuccino.GIF']
        self.index = 0
        self.set_action()
        self.update_pic()
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.show_recommend = QtWidgets.QGraphicsView(self.centralwidget)
        self.show_recommend.setGeometry(QtCore.QRect(290, 20, 681, 471))
        self.show_recommend.setObjectName("show_recommend")
        self.order_table = QtWidgets.QTableView(self.centralwidget)
        self.order_table.setGeometry(QtCore.QRect(30, 20, 250, 370))
        self.order_table.setObjectName("order_table")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(640, 500, 331, 61))
        self.next.setObjectName("next")
        self.before = QtWidgets.QPushButton(self.centralwidget)
        self.before.setGeometry(QtCore.QRect(290, 500, 331, 61))
        self.before.setObjectName("before")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.price_lcd_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.price_lcd_number.setGeometry(QtCore.QRect(110, 420, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_lcd_number.setFont(font)
        self.price_lcd_number.setProperty("intValue", 0)
        self.price_lcd_number.setObjectName("price_lcd_number")
        self.cost_label = QtWidgets.QLabel(self.centralwidget)
        self.cost_label.setGeometry(QtCore.QRect(40, 420, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cost_label.setFont(font)
        self.cost_label.setObjectName("cost_label")
        self.get_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.get_label_2.setGeometry(QtCore.QRect(40, 460, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.get_label_2.setFont(font)
        self.get_label_2.setObjectName("get_label_2")
        self.get_lcd_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.get_lcd_number.setGeometry(QtCore.QRect(110, 460, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.get_lcd_number.setFont(font)
        self.get_lcd_number.setProperty("intValue", 0)
        self.get_lcd_number.setObjectName("get_lcd_number")
        self.change_lcd_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.change_lcd_number.setGeometry(QtCore.QRect(110, 500, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.change_lcd_number.setFont(font)
        self.change_lcd_number.setProperty("intValue", 0)
        self.change_lcd_number.setObjectName("change_lcd_number")
        self.change_label = QtWidgets.QLabel(self.centralwidget)
        self.change_label.setGeometry(QtCore.QRect(30, 500, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.change_label.setFont(font)
        self.change_label.setObjectName("change_label")



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_recom(self, set_rec):
        self.recommend = set_rec
        self.index = 0
        self.update_pic()

    def update_pic(self):
        scene = QGraphicsScene()
        path = self.recommend[self.index]
        scene.addPixmap(QPixmap(path))
        self.show_recommend.setScene(scene)

    def set_action(self):
        self.next.clicked.connect(self.next_click)
        self.before.clicked.connect(self.prev_click)

    def next_click(self):
        if(self.index < len(self.recommend)-1):
            self.index +=1
        else:
            self.index = 0
        self.update_pic()

    def prev_click(self):
        if(self.index > 0):
            self.index -=1
        else:
            self.index = len(self.recommend)-1
        self.update_pic()


    def adjust_header(self):
        header = self.order_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    def closeEvent(self,event):
        self.parent.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next.setText(_translate("MainWindow", ">"))
        self.before.setText(_translate("MainWindow", "<"))
        self.cost_label.setText(_translate("MainWindow", "Total"))
        self.get_label_2.setText(_translate("MainWindow", "Get"))
        self.change_label.setText(_translate("MainWindow", "Change"))