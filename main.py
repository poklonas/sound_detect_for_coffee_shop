import sys
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5 import QtGui , QtCore, QtWidgets
from login_page import Ui_MainWindow as login_p
from salemode_page import Ui_MainWindow as sale_p
from selectmode_page import Ui_MainWindow as select_p 
from feedback_popup import Ui_Form as feedback_pop
from manual_menu_popup import Ui_Form as manual_pop 
from sound_detect_popup import Ui_Form as sound_detect_pop 
from warning_popup import Ui_Form as warn_pop 
from saleinfo_page import Ui_MainWindow as saleinfo_p
from functools import partial
from pjvoice import Recogning
from thread import * 
import collections
import sqlite3
import datetime
import csv

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.login_p = login_p()
        self.sale_p = sale_p()
        self.select_p = select_p()
        self.saleinfo_p = saleinfo_p()
        self.feed_pop = feedback_pop()
        self.manual_mpop = manual_pop()
        #self.sound_detect_pop = sound_detect_pop()
        #self.warning_pop = warn_pop()
        self.popup = MyPopup()
        self.open_login_page()
        self.dbname = 'newDB2.db'
        #####################################################
        # menu dic each menu has a list of these component
        # string of name_th  name_en   price    pic    
        # and list string of optional
        # menu_dic_price is for sound process only
        #####################################################
        self.menu_dic_price = collections.defaultdict(int)
        self.menu_dic = {
                    "menu_hot"   : self.set_menu_to_list('menu_config/menu_hot.csv'),
                    "menu_ice"   : self.set_menu_to_list('menu_config/menu_ice.csv'),
                    "menu_frap"  : self.set_menu_to_list('menu_config/menu_frap.csv'),
                    "menu_snack" : self.set_menu_to_list('menu_config/menu_snack.csv'),
                    }
        ### count menu in each type
        self.hotmenu_len = len(self.menu_dic["menu_hot"])
        self.icemenu_len = len(self.menu_dic["menu_ice"])
        self.frapmenu_len = len(self.menu_dic["menu_frap"])
        self.etcmenu_len = len(self.menu_dic["menu_snack"])
        ### food and optional id from db 
        self.food_id = collections.defaultdict(int)
        self.set_food_id_dic()
        self.optional_id = collections.defaultdict(int)
        self.set_optional_id_dic()
        ##############################################
        self.order = {}
        self.price = 0
        ### temp menu wait for delete
        #self.menu_list = ["เอสเพรสโซ","คาปูชิโน","ลาเต้","มอคค่า","ชา","ชาเขียวนม","ชานม","ดาร์คช็อกโกแลต","นมสด","ช็อกโกแลต"]
        #self.price_list = [40,40,35,30,25,25,30,45,40,45]
        #self.menu_dic = {
        #    "เอสเพรสโซ" : 40,
        #    "คาปูชิโน" : 40,
        #    "ลาเต้" : 35,
        #    "มอคค่า" : 30,
        #    "ชา" : 25,
        #    "ชาเขียวนม" : 25,
        #    "ชานม" : 30,
        #    "ดาร์คช็อกโกแลต" : 45,
        #    "นมสด" : 40,
        #    "ช็อกโกแลต" : 45
        #}
        ## cound rc
        self.rc = Recogning()
        #thered
        self.threadpool = QThreadPool()

    def set_menu_to_list(self, path_file):
        result = []
        with open (path_file, 'r',encoding='utf-8') as  csvf:
            reader = csv.reader(csvf)
            header = next(reader, None)
            for row in reader:
                option = list(row[-1].split("-"))
                menu = {
                    header[0] : row[0],
                    header[1] : row[1],
                    header[2] : row[2],
                    header[3] : row[3],
                    header[4] : option,
                }
                result.append(menu)
                self.menu_dic_price[row[1]] = (row[2])
        return result

    def set_food_id_dic(self):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        foods = c.execute("SELECT Food.id, Food.name From Food")
        conn.commit()
        for food in list(foods):
            self.food_id[food[1]] = food[0]

    def set_optional_id_dic(self):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        optionals = c.execute("SELECT Optional.id, Optional.name From Optional")
        conn.commit()
        for optional in list(optionals):
            self.optional_id[optional[1]] = optional[0]


    def set_login_page_action(self):
        self.login_p.login_button.clicked.connect(self.login)

    def login(self):
        self.user = self.login_p.username_edit.toPlainText()
        self.pas = self.login_p.password_edit.toPlainText()
        # easy for check at frist
        if(self.user != ""):
            self.login_p.error_label.setText("dont exit user name : "+self.user)
            return
        elif(self.pas != ""):
            self.login_p.error_label.setText("password wrong for user name : "+self.user)
            return
        else:
            self.open_select_page()

    def open_select_page(self):
        self.select_p.setupUi(self)
        self.select_p.userinfo_label.setText(self.user) 
        self.set_select_page_action()
        self.show()

    def open_login_page(self):
        self.login_p.setupUi(self)
        self.set_login_page_action()
        self.show()

    def open_sale_page(self):
        self.sale_p.setupUi(self)
        self.set_hot_drink()
        self.set_sale_page_action()
        self.show()

    def open_saleinfo_page(self):
        self.saleinfo_p.setupUi(self)
        self.set_saleinfo_page_action()
        self.show()

    def remove_button(self):
        items = self.sale_p.scrollAreaWidgetContents.children()
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.deleteLater()

    def add_button(self, l):
        for i in range(l):
            menu = QtWidgets.QPushButton(self.sale_p.scrollAreaWidgetContents)
            menu.setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(menu.sizePolicy().hasHeightForWidth())
            menu.setSizePolicy(sizePolicy)
            menu.setMinimumSize(QtCore.QSize(0, 161))
            menu.setLayoutDirection(QtCore.Qt.LeftToRight)
            menu.setObjectName("button"+str(i))
            self.sale_p.gridLayout.addWidget(menu, i/4, i%4, 1, 1)
        self.sale_p.gridLayout.update()

    # ----- 232*161 for picture button
    def set_hot_drink(self):
        self.remove_button()
        self.add_button(self.hotmenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url("+str(self.menu_dic["menu_hot"][count]['pic'])+")")
                #i.setStyleSheet("background-image:url('"+str(self.menu_dic["menu_hot"][count]['pic'])+"')")
                #i.setStyleSheet("background-image:url('./image/hot/"+str(count)+".GIF')")
                i.clicked.connect(partial( self.manual_add_popup,self.menu_dic["menu_hot"][count]))
                count += 1         

    def set_ice_drink(self):
        self.remove_button()
        self.add_button(self.icemenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url("+str(self.menu_dic["menu_ice"][count]['pic'])+")")
                #i.setStyleSheet("background-image:url('./image/ice/"+str(count)+".GIF')")
                i.clicked.connect(partial( self.manual_add_popup,self.menu_dic["menu_ice"][count]))
                #i.clicked.connect(lambda: self.manual_add_popup(self.menu_dic["menu_ice"][count]))
                count += 1

    def set_frappe_drink(self):
        self.remove_button()
        self.add_button(self.frapmenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url("+str(self.menu_dic["menu_frap"][count]['pic'])+")")
                #i.setStyleSheet("background-image:url('./image/frappe/"+str(count)+".GIF')")
                i.clicked.connect(partial( self.manual_add_popup,self.menu_dic["menu_frap"][count]))
                #i.clicked.connect(lambda: self.manual_add_popup(self.menu_dic["menu_frap"][count]))
                count += 1

    def set_etc_menu(self):
        self.remove_button()
        self.add_button(self.etcmenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url("+str(self.menu_dic["menu_snack"][count]['pic'])+")")
                #i.setStyleSheet("background-image:url('./image/etc/"+str(count)+".GIF')")
                i.clicked.connect(partial( self.manual_add_popup,self.menu_dic["menu_snack"][count]))
                #i.clicked.connect(lambda: self.manual_add_popup(self.menu_dic["menu_snack"][count]))
                count += 1

    def sound_detect_menu(self):
        self.start_detect_sound()

    def start_detect_sound(self):
        if(not self.rc.on):
            if(self.threadpool.activeThreadCount() == 0):
                thread = Thread(self.detect)
                self.threadpool.start(thread)
        else:
            self.detect()
        
    def detect(self):
        if(not self.rc.on):
            self.sale_p.sound_detect_button.setText("Stop order by voice")
            self.rc.on = True
            return self.rc.listen(self.update_list_order)
        else:
            self.sale_p.sound_detect_button.setText("Start order by voice")
            self.rc.on = False
           
    def update_list_order(self, new_list):
        for item in new_list:
            total_in = int(item[1])
            price_in = int(self.menu_dic_price[item[0]])
            #price_in = total_in * self.menu_dic[item[0]]
            name = item[0]
            self.price +=  price_in * total_in
            if name in self.order:
                total = int(self.order[name][1]) + int(total_in)
                #price = int(self.order[name][2]) + int(price_in) 
                self.order.update({name : [name,str(total),str(price_in)]})
            else:
                self.order[name] = [name, str(total_in), str(price_in)]
        order = []
        for i in self.order.values():
            order.append(i)
        if order != []:
            order_model = MyOrderTableModel(order, self)
            self.sale_p.tableView.setModel(order_model)
            self.adjust_header()
            self.sale_p.price_lcd_number.setProperty("intValue", self.price)

    def close_popup(self):
        self.set_enabled_salemode_button()
        self.rc.on = False
        self.popup.close()

    def manual_add_popup(self, menu):
        self.popup = MyPopup()
        self.manual_mpop.setupUi(self.popup)
        self.set_disable_salemode_button()
        self.manual_mpop.manuname_label.setText(menu["name_en"])
        self.manual_mpop.cancle_button.clicked.connect(self.close_popup)
        if(menu['optional'][0] == 'n'):
            self.manual_mpop.set_sugar_disable()
        if(menu['optional'][1] == 'n'):
            self.manual_mpop.set_milk_disable()
        if(menu['optional'][2] == 'n'):
            self.manual_mpop.set_cream_disable()
        if(menu['optional'][3] == 'n'):
            self.manual_mpop.set_whipcream_disable()
        self.manual_mpop.add_button.clicked.connect(lambda: self.add_order(menu["name_en"], 1, menu["price"], self.manual_mpop.get_option()))
        self.popup.show()

    def set_disable_salemode_button(self):
        self.sale_p.hotmenu_button.setEnabled(False)
        self.sale_p.icemenu_button.setEnabled(False)
        self.sale_p.frapemenu_button.setEnabled(False)
        self.sale_p.etcmenu_button.setEnabled(False)
        self.sale_p.sound_detect_button.setEnabled(False)
        self.sale_p.bill_button.setEnabled(False)
        self.sale_p.back_button.setEnabled(False)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setEnabled(False)

    def set_enabled_salemode_button(self):
        self.sale_p.hotmenu_button.setEnabled(True)
        self.sale_p.icemenu_button.setEnabled(True)
        self.sale_p.frapemenu_button.setEnabled(True)
        self.sale_p.etcmenu_button.setEnabled(True)
        self.sale_p.sound_detect_button.setEnabled(True)
        self.sale_p.bill_button.setEnabled(True)
        self.sale_p.back_button.setEnabled(True)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setEnabled(True)

    def set_select_page_action(self):
        self.select_p.logout_button.clicked.connect(self.open_login_page)
        self.select_p.salemode_button.clicked.connect(self.open_sale_page)
        self.select_p.saleinfo_button.clicked.connect(self.open_saleinfo_page)
        self.select_p.update_rule_button.clicked.connect(self.update_rule)

    def set_sale_page_action(self):
        self.sale_p.back_button.clicked.connect(self.open_select_page)
        self.sale_p.icemenu_button.clicked.connect(self.set_ice_drink)
        self.sale_p.hotmenu_button.clicked.connect(self.set_hot_drink)
        self.sale_p.frapemenu_button.clicked.connect(self.set_frappe_drink)
        self.sale_p.etcmenu_button.clicked.connect(self.set_etc_menu)
        self.sale_p.sound_detect_button.clicked.connect(self.sound_detect_menu)
        self.sale_p.bill_button.clicked.connect(self.add_order_to_db)

    def set_saleinfo_page_action(self):
        self.saleinfo_p.back_button.clicked.connect(self.open_select_page)
        self.saleinfo_p.search_button.clicked.connect(self.update_table_saleinfo)

    def update_table_saleinfo(self):
        self.saleinfo_p.update_table(self.dbname)

    def add_order_to_db(self):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        dateT = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for (menu, qty, price) in self.order.values():
            c.execute("INSERT INTO Orders (time) VALUES (?)", ( dateT, ))
            order_id = c.lastrowid
            split_menu = menu.split('.')
            foodname = split_menu[0]
            optional = split_menu[1:]
            foodid = self.food_id[foodname]
            if optional != []:
                 for i in range(0,int(qty)):
                    c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  order_id,  foodid,) )
                    last_detail_id = c.lastrowid
                    for option in optional:
                        optionID = self.optional_id[option]
                        c.execute("INSERT INTO Detailorder_option (orderDetailID,optionalID) VALUES (?,?)", (last_detail_id, optionID,))
            else:
                for i in range(0,int(qty)):
                    print('add', order_id, foodid, 0)
                    c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  order_id,  foodid,) )
        conn.commit()
        self.order = {}
        self.price = 0
        order_model = MyOrderTableModel([[]], self)
        self.sale_p.tableView.setModel(order_model)
        self.adjust_header()
        self.sale_p.price_lcd_number.setProperty("intValue", self.price)

    def update_rule(self):
        print("wait update rule")

    def add_order(self, name, total_in, price_in, options):
        for option in options:
            if option != 'Normal':
                name += '.' + option
        if name in self.order:
            total = int(self.order[name][1]) + int(total_in)
            price = int(price_in * total)
            self.order.update({name : [name,str(total),str(price_in)]})
        else:
            self.order[name] = [name, str(total_in), str(price_in)]
        self.price += int(price_in) * int(total_in)
        order = []
        for i in self.order.values():
            order.append(i)
            print(order)
        order_model = MyOrderTableModel(order, self)
        self.sale_p.tableView.setModel(order_model)
        self.adjust_header()
        self.sale_p.price_lcd_number.setProperty("intValue", self.price)
        self.close_popup()

    def adjust_header(self):
        header = self.sale_p.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

class MyPopup(QMainWindow):
    def __init__(self, parent=None):
        super(MyPopup, self).__init__(parent)

class MyOrderTableModel(QAbstractTableModel):
    def __init__(self, dataIn, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = dataIn
        self.headerdata = ['Name','Qty','Price']

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])


    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())