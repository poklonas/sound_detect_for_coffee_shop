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
import collections

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.setWindowTitle('CoffeeNLP')
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

        self.startDate.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.stopDate.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.startDate.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.stopDate.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
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
        self.tableWidget.setGeometry(QtCore.QRect(340, 10, 931, 531))
        self.tableWidget.setMaximumSize(QtCore.QSize(931, 621))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4) # chang to 5 if need qty too
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1279, 21))
        self.menubar.setObjectName("menubar")
        self.tableWidget.verticalHeader().setVisible(False)
        MainWindow.setMenuBar(self.menubar)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 550, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cup_m_count = QtWidgets.QLabel(self.centralwidget)
        self.cup_m_count.setGeometry(QtCore.QRect(340, 580, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cup_m_count.setFont(font)
        self.cup_m_count.setObjectName("cup_m_count")
        self.cup_l_count = QtWidgets.QLabel(self.centralwidget)
        self.cup_l_count.setGeometry(QtCore.QRect(430, 580, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cup_l_count.setFont(font)
        self.cup_l_count.setObjectName("cup_l_count")
        self.cup_total_count = QtWidgets.QLabel(self.centralwidget)
        self.cup_total_count.setGeometry(QtCore.QRect(640, 580, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cup_total_count.setFont(font)
        self.cup_total_count.setObjectName("cup_total_count")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(780, 550, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.price_m_count = QtWidgets.QLabel(self.centralwidget)
        self.price_m_count.setGeometry(QtCore.QRect(780, 580, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_m_count.setFont(font)
        self.price_m_count.setObjectName("price_m_count")
        self.price_l_count = QtWidgets.QLabel(self.centralwidget)
        self.price_l_count.setGeometry(QtCore.QRect(900, 580, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_l_count.setFont(font)
        self.price_l_count.setObjectName("price_l_count")
        self.price_total_count = QtWidgets.QLabel(self.centralwidget)
        self.price_total_count.setGeometry(QtCore.QRect(1130, 580, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_total_count.setFont(font)
        self.price_total_count.setObjectName("price_total_count")
        self.price_n_count = QtWidgets.QLabel(self.centralwidget)
        self.price_n_count.setGeometry(QtCore.QRect(990, 580, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_n_count.setFont(font)
        self.price_n_count.setObjectName("price_n_count")
        self.cup_n_count = QtWidgets.QLabel(self.centralwidget)
        self.cup_n_count.setGeometry(QtCore.QRect(520, 580, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cup_n_count.setFont(font)
        self.cup_n_count.setObjectName("cup_n_count")

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
        #item = self.tableWidget.horizontalHeaderItem(3)
        #item.setText(_translate("MainWindow", "Qty"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Items"))
        self.label_3.setText(_translate("MainWindow", "Count Cup Size"))
        self.cup_m_count.setText(_translate("MainWindow", "M : "))
        self.cup_l_count.setText(_translate("MainWindow", "L : "))
        self.cup_total_count.setText(_translate("MainWindow", "Total : "))
        self.label_7.setText(_translate("MainWindow", "Price"))
        self.price_m_count.setText(_translate("MainWindow", "M : "))
        self.price_l_count.setText(_translate("MainWindow", "L : "))
        self.price_total_count.setText(_translate("MainWindow", "Total : "))
        self.price_n_count.setText(_translate("MainWindow", "other : "))
        self.cup_n_count.setText(_translate("MainWindow", "Other : "))

    def update_table(self, path, dic_menu):
        conn = sqlite3.connect(path)
        query = """ SELECT o.id, o.time, f.name, op.name AS option , do.orderDetailID, f.size FROM DetailOrder d
                    LEFT JOIN Detailorder_option do ON do.orderDetailID == d.id
                    LEFT JOIN Optional op ON op.id == do.optionalID
                    INNER JOIN FOOD f ON f.id == d.foodID
                    INNER JOIN Orders o ON o.id == d.orderID
                    WHERE strftime('%Y-%m-%d', o.time) between ? AND ?
                """
        start = self.format_date((self.startDate.selectedDate()))
        stop = self.format_date((self.stopDate.selectedDate()).addDays(1))
        start_stop = ( start, stop, )
        result = conn.execute(query, start_stop)
        self.tableWidget.setRowCount(0)
        last_id = None
        last_item = None
        last_row = -1
        span_row = None
        last_detail_id = None
        last_menu = None
        count = 1
        #########
        size_m = 0
        size_l = 0
        size_n = 0
        price_m = 0
        price_l = 0
        price_n = 0
        price_current = 0

        #order_set = {
        #    date:"",
        #    time:"",
        #    start_row:"",
        #    end_row:"",
        #    span_row:"",
        #    menu : collections.defaultdict(str),
        #}
        for row_data in list(result):
            if(row_data[3] == None): # none option
                size = str(row_data[5])
                raw_name = str(row_data[2])
                menu = raw_name + '[' + size + ']'
                head = menu[0:3]
                price_current = dic_menu[raw_name, size][1]
                if( size == "M" ):
                    size_m += 1
                    price_m += price_current
                elif( size == "L" ):
                    size_l += 1
                    price_l += price_current
                else:
                    size_n += 1
                    price_n += price_current
            else: # has option
                if(last_detail_id != row_data[4]):  # new detail order?
                    size = str(row_data[5])
                    raw_name = str(row_data[2])
                    menu = raw_name + '[' + size + ']' + " and " + str(row_data[3])
                    head = menu[0:3]
                    price_current = dic_menu[raw_name, size][1]
                    if( size == "M" ):
                        size_m += 1
                        price_m += price_current
                    elif( size == "L" ):
                        size_l += 1
                        price_l += price_current
                    else:
                        size_n += 1
                        price_n += price_current
                else:
                    menu = last_menu + " and " + str(row_data[3])
                last_menu = menu
            if(last_id == row_data[0]): # old order ?
                if( last_detail_id != row_data[4] or row_data[3] == None):
                    last_row += 1
                    self.tableWidget.insertRow(last_row)
                    count += 1
                    #order_set["count"] = count
                    #order_set["end_row"] = last_row
                if(count > 1):
                    self.tableWidget.setSpan(span_row, 0, count, 1)
                    self.tableWidget.setSpan(span_row, 1, count, 1)
                    self.tableWidget.setSpan(span_row, 2, count, 1)                
                    #self.tableWidget.setItem(last_row, 3, QtWidgets.QTableWidgetItem('1'))
                    self.tableWidget.setItem(last_row, 3, QtWidgets.QTableWidgetItem(menu))
            else: # new order
                last_row += 1
                self.tableWidget.insertRow(last_row)
                count = 1
                span_row = last_row
                date_time_obj = datetime.datetime.strptime(row_data[1], '%Y-%m-%d %H:%M:%S')
                self.tableWidget.setItem(last_row, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))
                self.tableWidget.setItem(last_row, 1, QtWidgets.QTableWidgetItem(str(date_time_obj.date())))
                self.tableWidget.setItem(last_row, 2, QtWidgets.QTableWidgetItem(str(date_time_obj.time())))
                #self.tableWidget.setItem(last_row, 3, QtWidgets.QTableWidgetItem('1'))
                self.tableWidget.setItem(last_row, 3, QtWidgets.QTableWidgetItem(menu))
                #order_set = {
                #    date:date_time_obj.date(),
                #    time:date_time_obj.time(),
                #    start_row:last_row,
                #    end_row:last_row,
                #    span_row:span_row,
                #    count:count,
                #    menu : collections.defaultdict(str),
                #}
                #order_set["menu"][str(menu)] = 1
            last_detail_id = row_data[4]
            last_id = row_data[0]
        _translate = QtCore.QCoreApplication.translate
        self.cup_m_count.setText(_translate("MainWindow", "M : " + str(size_m)))
        self.cup_l_count.setText(_translate("MainWindow", "L : " + str(size_l)))
        self.cup_total_count.setText(_translate("MainWindow", "Total : " + str(size_n + size_m + size_l)))
        self.price_m_count.setText(_translate("MainWindow", "M : " + str(price_m)))
        self.price_l_count.setText(_translate("MainWindow", "L : " + str(price_l)))
        self.price_total_count.setText(_translate("MainWindow", "Total : " + str(price_l + price_m + price_n)))
        self.price_n_count.setText(_translate("MainWindow", "other : "+ str(price_n)))
        self.cup_n_count.setText(_translate("MainWindow", "Other : "+ str(size_n)))

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