# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saleinfo_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
import sqlite3
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1279, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 10, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(10, 550, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")

        self.startDate = QtWidgets.QCalendarWidget(self.centralwidget)
        self.startDate.setGeometry(QtCore.QRect(10, 120, 312, 183))
        self.startDate.setObjectName("startDate")
        self.startDate.setMaximumDate(QDate.currentDate())
        self.stopDate = QtWidgets.QCalendarWidget(self.centralwidget)
        self.stopDate.setGeometry(QtCore.QRect(10, 360, 312, 183))
        self.stopDate.setObjectName("stopDate")
        self.stopDate.setMaximumDate(QDate.currentDate())
        self.startDate.clicked.connect(self.startDateClicked)
        self.stopDate.clicked.connect(self.stopDateClicked)
        self.stopDate.setSelectedDate(QDate.currentDate())

        self.startDateVal = self.startDate.selectedDate()
        self.stopDateVal = self.stopDate.selectedDate()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(340, 10, 931, 621))
        self.tableWidget.setMaximumSize(QtCore.QSize(931, 621))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1279, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Start Date"))
        self.label_2.setText(_translate("MainWindow", "Stop Date"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Items"))

    def update_table(self, path):
        conn = sqlite3.connect(path)
        query = """ SELECT o.id, o.time, f.name, op.name FROM DetailOrder d
                    INNER JOIN Optional op ON op.id == d.optionalID
                    INNER JOIN FOOD f ON f.id == d.foodID
                    INNER JOIN Orders o ON o.id == d.orderID
                    WHERE strftime('%Y-%m-%d', o.time) between ? AND ?
                """
        start = self.format_date((self.startDate.selectedDate()))
        stop = self.format_date((self.stopDate.selectedDate()).addDays(1))
        start_stop = ( start, stop, )
        print(start_stop)
        result = conn.execute(query, start_stop)
        self.tableWidget.setRowCount(0)
        last_id = None
        last_item = None
        last_row = -1
        span_row = None
        count = 1
        for row_data in list(result):
            last_row += 1
            self.tableWidget.insertRow(last_row)
            if(row_data[3] == "Normal"):
                menu = str(row_data[2])
            else:
                menu = str(row_data[2]) + " and " + str(row_data[3])
            if(last_id == row_data[0]):
                count += 1
                self.tableWidget.setSpan(span_row, 0, count, 1)
                self.tableWidget.setSpan(span_row, 1, count, 1)
                self.tableWidget.setSpan(span_row, 2, count, 1)
                self.tableWidget.setItem(last_row, 3, QtWidgets.QTableWidgetItem(menu))
            else:
                count = 1
                span_row = last_row
                date_time_obj = datetime.datetime.strptime(row_data[1], '%Y-%m-%d %H:%M:%S')
                self.tableWidget.setItem(last_row, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))
                self.tableWidget.setItem(last_row, 1, QtWidgets.QTableWidgetItem(str(date_time_obj.date())))
                self.tableWidget.setItem(last_row, 2, QtWidgets.QTableWidgetItem(str(date_time_obj.time())))
                self.tableWidget.setItem(last_row, 3, QtWidgets.QTableWidgetItem(menu))
            last_id = row_data[0]

    def startDateClicked(self):
        if(self.startDate.selectedDate() > self.stopDate.selectedDate()):
            self.startDate.setSelectedDate(self.startDateVal)
        else:
            self.startDateVal = self.startDate.selectedDate()

    def stopDateClicked(self):
        if(self.startDate.selectedDate() > self.stopDate.selectedDate()):
            self.stopDate.setSelectedDate(self.stopDateVal)
        else:
            self.stopDateVal = self.stopDate.selectedDate()

    def format_date(self, datetext):
        y = str(datetext.year())
        if datetext.month() < 10:
            m = '0'+str(datetext.month())
        else:
            m = str(datetext.month())
        if datetext.day() < 10:
            d = '0'+str(datetext.day())
        else:
            d = str(datetext.day())
        return y + '-' + m + '-' + d