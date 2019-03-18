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
from other_module.pjvoice import Recogning
from thread import * 
from my_association import update_rule 
from recom_window import Recom_window 
import pickle 
import collections
import sqlite3
import datetime
import csv

class MyApp(QMainWindow):
    def __init__(self, parent=None, recom_window=None):
        QWidget.__init__(self, parent)
        self.login_p = login_p()
        self.sale_p = sale_p()
        self.select_p = select_p()
        self.saleinfo_p = saleinfo_p()
        self.feed_pop = feedback_pop()
        self.manual_mpop = manual_pop()
        self.popup = MyPopup()
        self.open_login_page()
        self.dbname = 'newDB3.db'
        self.food_id_and_price = collections.defaultdict(int)
        self.optional_id = collections.defaultdict(int)
        self.set_optional_id_dic()
        self.menu_pic = collections.defaultdict(str)
        self.menu_dic = {
                    ("menu_hot", "M")   : self.set_drink_to_list('Hot','M'),
                    ("menu_ice", "M")   : self.set_drink_to_list('Ice','M'),
                    ("menu_ice", "L")   : self.set_drink_to_list('Ice','L'),
                    ("menu_frap", "M")   : self.set_drink_to_list('Frappe','M'),
                    ("menu_frap", "L")   : self.set_drink_to_list('Frappe','L'),
                    ("menu_snack", "N")   : self.set_snack_to_list(),
                    }
        self.hotmenu_len = len(self.menu_dic[("menu_hot", "M")])
        self.icemenu_len = len(self.menu_dic[("menu_ice", "M")])
        self.frapmenu_len = len(self.menu_dic[("menu_frap", "M")])
        self.etcmenu_len = len(self.menu_dic[("menu_snack", "N")])
        self.order = {}
        self.order_tuple = ()
        self.price = 0
        self.rc = Recogning()
        self.threadpool = QThreadPool()
        with open('rule.result', 'rb') as file:
            self.rule_and_header = pickle.load(file)
        self.recom = recom_window
        self.recom.set_parent(self)
        self.status = QtGui.QStandardItemModel()

    def set_drink_to_list(self, typeIn, size):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        drinks = c.execute("SELECT f.id, f.name, f.price, f.size, f.path From Food f WHERE f.size == ? and f.name LIKE ?", (size,typeIn+"_%",))
        conn.commit()
        result = []
        for drink in list(drinks):
            self.food_id_and_price[(drink[1], drink[3])] = [drink[0], drink[2]]
            self.menu_pic[drink[1]] = drink[4]
            menu = {
                    'size'  : drink[3],
                    'name'  : drink[1],
                    'price' : drink[2],
                    'pic'   : drink[4],
                }
            if( menu['name'][0:3] == "Hot" ):
                menu['optional'] = ['y','y','y','n']
            else:
                menu['optional'] = ['y','y','y','y']
            result.append(menu)
        return result

    def set_snack_to_list(self):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        snacks = c.execute("SELECT f.id, f.name, f.price, f.size, f.path From Food f WHERE f.size == 'N'")
        conn.commit()
        result = []
        for snack in list(snacks):
            self.food_id_and_price[(snack[1], snack[3])] = [snack[0], snack[2]]
            self.menu_pic[snack[1]] = snack[4]
            menu = {
                    'size'  : snack[3],
                    'name'  : snack[1],
                    'price' : snack[2],
                    'pic'   : snack[4],
                    'optional' : ['n','n','n','n'],
                }
            result.append(menu)
        return result

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
        order = {
            "status" : None,
            "item" : [],
        }
        self.update_list_order(order)
        self.sale_p.status.setModel(self.status)
        self.show()

    def open_select_page_from_sale(self):
        self.reset_order()
        self.reset_status()
        self.open_select_page()

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

    def set_hot_drink(self):
        self.remove_button()
        self.add_button(self.hotmenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url("+str(self.menu_dic[("menu_hot","M")][count]['pic'])+")")
                i.clicked.connect(partial( self.manual_add_popup,self.menu_dic[("menu_hot","M")][count]))
                count += 1         

    def set_ice_drink(self):
        self.remove_button()
        self.add_button(self.icemenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url("+str(self.menu_dic[("menu_ice","M")][count]['pic'])+")")
                i.clicked.connect(partial( self.manual_add_popup,self.menu_dic[("menu_ice","M")][count]))
                count += 1

    def set_frappe_drink(self):
        self.remove_button()
        self.add_button(self.frapmenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url("+str(self.menu_dic[("menu_frap","M")][count]['pic'])+")")
                i.clicked.connect(partial( self.manual_add_popup,self.menu_dic[("menu_frap","M")][count]))
                count += 1

    def set_etc_menu(self):
        self.remove_button()
        self.add_button(self.etcmenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url("+str(self.menu_dic[("menu_snack","N")][count]['pic'])+")")
                i.clicked.connect(partial( self.manual_add_popup,self.menu_dic[("menu_snack","N")][count]))
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
           
    def update_list_order(self, item_and_status):
        for item in item_and_status["item"]:
            total_in = int(item[1])
            name = item[0]
            price_in = int(self.food_id_and_price[(name,item[3])][1])
            self.price +=  price_in * total_in
            if name in self.order:
                total = int(self.order[name][1]) + int(total_in)
                self.order.update({name : [name,str(total),str(price_in)]})
            else:
                self.order[name] = [name, str(total_in), str(price_in)]
        order = []
        for i in self.order.values():
            order.append(i)
        if order != []:
            order_model = MyOrderTableModel(order, self)
        else:
            order_model = MyOrderTableModel([[None,None,None]], self)
        self.sale_p.tableView.setModel(order_model)
        self.adjust_header()
        self.recom.order_table.setModel(order_model)
        self.recom.adjust_header()
        self.sale_p.tableView.setWordWrap(True)
        self.sale_p.price_lcd_number.setProperty("intValue", self.price)
        self.recom.price_lcd_number.setProperty("intValue", self.price)
        if(item_and_status["status"] != None):
            self.add_status(item_and_status["status"])

    def close_popup(self):
        self.set_enabled_salemode_button()
        self.rc.on = False
        self.popup.close()

    def manual_add_popup(self, menu):
        self.popup = MyPopup(myCloseEvent = self.set_enabled_salemode_button)
        self.manual_mpop.setupUi(self.popup)
        self.set_disable_salemode_button()
        self.manual_mpop.manuname_label.setText(menu["name"])
        self.manual_mpop.cancle_button.clicked.connect(self.close_popup)
        if(menu['optional'][0] == 'n'):
            self.manual_mpop.set_sugar_disable()
        if(menu['optional'][1] == 'n'):
            self.manual_mpop.set_milk_disable()
        if(menu['optional'][2] == 'n'):
            self.manual_mpop.set_cream_disable()
        if(menu['optional'][3] == 'n'):
            self.manual_mpop.set_whipcream_disable()
        if(menu['name'][0:3] == "Hot"):
            self.manual_mpop.set_size_disable()
        if(menu['name'][0:3] not in ["Hot", "Ice", "Frap"]):
            self.manual_mpop.set_size_disable()
        self.manual_mpop.add_button.clicked.connect(lambda: self.add_order(menu["name"], self.manual_mpop.get_qty(), self.manual_mpop.get_size(), self.manual_mpop.get_option()))
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
        self.sale_p.back_button.clicked.connect(self.open_select_page_from_sale)
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
        self.saleinfo_p.update_table(self.dbname, self.food_id_and_price)

    def add_order_to_db(self):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        dateT = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO Orders (time) VALUES (?)", ( dateT, ))
        order_id = c.lastrowid
        for (menu, qty, price) in self.order.values():
            split_menu = menu.split('.') # => ['menu[M]', option1, option2 , ...]
            foodname = split_menu[0]
            optional = split_menu[1:]
            foodname = foodname.split('[') # => ['menu', 'M]']
            if(len(foodname) < 2):
                foodid = self.food_id_and_price[(foodname[0],'N')][0]    
            else:
                foodid = self.food_id_and_price[(foodname[0],foodname[1][0])][0]
            if optional != []:
                 for i in range(0,int(qty)):
                    c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  order_id,  foodid,) )
                    last_detail_id = c.lastrowid
                    for option in optional:
                        optionID = self.optional_id[option]
                        c.execute("INSERT INTO Detailorder_option (orderDetailID,optionalID) VALUES (?,?)", (last_detail_id, optionID,))
            else:
                for i in range(0,int(qty)):
                    c.execute("INSERT INTO DetailOrder (orderID, foodID) VALUES (?,?)", (  order_id,  foodid,) )
        conn.commit()
        self.reset_order()
        self.add_status(str("add order id : "+ str(order_id) + " to database complete"))

    def reset_order(self):
        self.order = {}
        self.price = 0
        order_model = MyOrderTableModel([[None,None,None]], self)
        self.sale_p.tableView.setModel(order_model)
        self.adjust_header()
        self.sale_p.price_lcd_number.setProperty("intValue", self.price)
        self.order_tuple = ()
        self.recom.order_table.setModel(order_model)
        self.recom.adjust_header()
        self.recom.price_lcd_number.setProperty("intValue", self.price)

    def update_rule(self):
        update_rule(self.dbname, 'rule.result')
        with open('rule.result', 'rb') as file:
            self.rule_and_header = pickle.load(file)
        print("update rule complete")
        
    def add_order(self, name, total_in, size, options):
        self.order_tuple += (self.rule_and_header[2][name],)
        if(self.food_id_and_price[(name,size)] != 0):
            price_in = self.food_id_and_price[(name,size)][1]
            name += '['+size+'] '
        else:
            price_in = self.food_id_and_price[(name,'N')][1]
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
        order_model = MyOrderTableModel(order, self)
        self.sale_p.tableView.setModel(order_model)
        self.adjust_header()
        self.sale_p.price_lcd_number.setProperty("intValue", self.price)
        self.show_recommend()
        self.recom.order_table.setModel(order_model)
        self.recom.adjust_header()
        self.recom.price_lcd_number.setProperty("intValue", self.price)
        self.close_popup()
        
    def show_recommend(self):
        order_in = frozenset(self.order_tuple)
        show_set = ()
        for i in self.rule_and_header[0]:
            if(order_in == i[0]):
                for j in i[1]:
                    show_set += (self.rule_and_header[1][j],)
        if(show_set == ()):
            return None
        rec_list = []
        for i in frozenset(show_set):   
            rec_list.append(self.menu_pic[i])
        self.recom.update_recom(rec_list)


    def adjust_header(self):
        header = self.sale_p.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    def closeEvent(self,event):
        self.recom.close()

    def add_status(self, status):
        item = QtGui.QStandardItem(status)
        self.status.insertRow(0, item)

    def reset_status(self):
        self.status = QtGui.QStandardItemModel()

class MyPopup(QMainWindow):
    def __init__(self, parent=None, myCloseEvent=None):
        super(MyPopup, self).__init__(parent)
        self.myevent = myCloseEvent

    def closeEvent(self,event):
        self.myevent() 

class MyOrderTableModel(QAbstractTableModel):
    def __init__(self, dataIn, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = dataIn
        self.headerdata = ['Name','Qty','Price']

    def rowCount(self, parent):
        if(self.arraydata == [[None,None,None]]):
            return 0
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
    recom_window_new = Recom_window()
    recom_window_new.show()
    myapp = MyApp(recom_window = recom_window_new)
    myapp.show()
    sys.exit(app.exec_())