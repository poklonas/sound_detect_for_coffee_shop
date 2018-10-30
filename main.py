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
from functools import partial

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.login_p = login_p()
        self.sale_p = sale_p()
        self.select_p = select_p()
        self.feed_pop = feedback_pop()
        self.manual_mpop = manual_pop()
        self.sound_detect_pop = sound_detect_pop()
        self.warning_pop = warn_pop()
        self.popup = MyPopup()
        self.open_login_page()
        self.hotmenu_len = 9
        self.icemenu_len = 17
        self.frapmenu_len = 12
        self.etcmenu_len = 8
        self.order_list = []
        ### temp menu
        self.menu = ["เอสเพรสโซ","คาปูชิโน","ลาเต้","มอคค่า","ชา","ชาเขียวนม","ชานม","ดาร์คช็อกโกแลต","นมสด","ช็อกโกแลต"]
        self.price = [40,40,35,30,25,25,30,45,40,45]

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

    def set_select_page_action(self):
        self.select_p.logout_button.clicked.connect(self.open_login_page)
        self.select_p.salemode_button.clicked.connect(self.open_sale_page)

    def open_login_page(self):
        self.login_p.setupUi(self)
        self.set_login_page_action()
        self.show()

    def open_sale_page(self):
        self.sale_p.setupUi(self)
        self.set_hot_drink()
        self.set_sale_page_action()
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
                i.setStyleSheet("background-image:url('./image/hot/"+str(count)+".GIF')")
                i.clicked.connect(partial( self.manual_add_popup,self.menu[count], self.price[count]))
                count += 1         

    def set_ice_drink(self):
        self.remove_button()
        self.add_button(self.icemenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url('./image/ice/"+str(count)+".GIF')")
                i.clicked.connect(lambda: self.manual_add_popup(self.menu[count], self.price[count]))
                count += 1

    def set_frappe_drink(self):
        self.remove_button()
        self.add_button(self.frapmenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url('./image/frappe/"+str(count)+".GIF')")
                i.clicked.connect(lambda: self.manual_add_popup(self.menu[count], self.price[count]))
                count += 1

    def set_etc_menu(self):
        self.remove_button()
        self.add_button(self.etcmenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url('./image/etc/"+str(count)+".GIF')")
                i.clicked.connect(lambda: self.manual_add_popup(self.menu[count], self.price[count]))
                count += 1

    def sound_detect_menu(self):
        self.popup = MyPopup()
        self.sound_detect_pop.setupUi(self.popup)
        self.sound_detect_pop.cancle_button.clicked.connect(self.close_popup)
        self.sound_detect_pop.start_stop_button.clicked.connect(self.start_detect_sound)
        self.state = 0
        self.set_disable_salemode_button()
        self.popup.show()

    def start_detect_sound(self):
        if(self.state == 0):
            self.state = 1
            self.sound_detect_pop.picture_view.setStyleSheet("background-image:url('./image/general/start_sound_record.gif')")
        else:
            self.sound_detect_pop.picture_view.setStyleSheet("background-image:url('./image/general/stop_sound_record.gif')")
            self.state = 0

    def close_popup(self):
        self.set_enabled_salemode_button()
        self.popup.close()

    def manual_add_popup(self, name, price):
        self.popup = MyPopup()
        self.manual_mpop.setupUi(self.popup)
        self.set_disable_salemode_button()
        self.manual_mpop.manuname_label.setText(name)
        self.manual_mpop.cancle_button.clicked.connect(self.close_popup)
        self.manual_mpop.add_button.clicked.connect(lambda: self.add_order(name,price))
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


    def set_sale_page_action(self):
        self.sale_p.back_button.clicked.connect(self.open_select_page)
        self.sale_p.icemenu_button.clicked.connect(self.set_ice_drink)
        self.sale_p.hotmenu_button.clicked.connect(self.set_hot_drink)
        self.sale_p.frapemenu_button.clicked.connect(self.set_frappe_drink)
        self.sale_p.etcmenu_button.clicked.connect(self.set_etc_menu)
        self.sale_p.sound_detect_button.clicked.connect(self.sound_detect_menu)

    #def set_button_salemanual(self):
    #    items = self.sale_p.scrollAreaWidgetContents.children()
    #    count = 0
    #    for i in items:
    #        if isinstance(i, QtWidgets.QPushButton):
    #            i.clicked.connect(lambda: self.manual_add_popup(self.menu[count], self.price[count]))
    #            count = count + 1

    def add_order(self, name, price):
        order = Order(name, price)
        self.order_list.append(order)
        sum_price = 0
        order_model = QStandardItemModel()
        for i in self.order_list:
            sum_price += i.price
            order_model.appendRow(QStandardItem(i.name+"       :      "+str(i.price)))
        self.sale_p.listView.setModel(order_model)
        self.sale_p.price_lcd_number.setProperty("intValue", sum_price)
        self.close_popup()
        
class Order():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class MyPopup(QMainWindow):
    def __init__(self, parent=None):
        super(MyPopup, self).__init__(parent)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())