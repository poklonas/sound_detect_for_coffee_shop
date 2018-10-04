import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5 import QtGui , QtCore, QtWidgets
from login_page import Ui_MainWindow as login_p
from salemode_page import Ui_MainWindow as sale_p
from selectmode_page import Ui_MainWindow as select_p 
from feedback_popup import Ui_Form as feedback_pop
from manual_menu_popup import Ui_Form as manual_pop 
from sound_detect_popup import Ui_Form as sound_detect_pop 
from warning_popup import Ui_Form as warn_pop 

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
        self.open_login_page()
        self.hotmenu_len = 9
        self.icemenu_len = 17
        self.frapmenu_len = 12
        self.etcmenu_len = 8

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
                count += 1
                #i.setIcon(QtGui.QIcon('./image/coffeeA.GIF'))
                #i.setIconSize(QtCore.QSize(200,210))

    def set_ice_drink(self):
        self.remove_button()
        self.add_button(self.icemenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url('./image/ice/"+str(count)+".GIF')")
                count += 1

    def set_frappe_drink(self):
        self.remove_button()
        self.add_button(self.frapmenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url('./image/frappe/"+str(count)+".GIF')")
                count += 1

    def set_etc_menu(self):
        self.remove_button()
        self.add_button(self.etcmenu_len)
        items = self.sale_p.scrollAreaWidgetContents.children()
        count = 0
        for i in items:
            if isinstance(i, QtWidgets.QPushButton):
                i.setStyleSheet("background-image:url('./image/etc/"+str(count)+".GIF')")
                count += 1

    def set_sale_page_action(self):
        self.sale_p.back_button.clicked.connect(self.open_select_page)
        self.sale_p.icemenu_button.clicked.connect(self.set_ice_drink)
        self.sale_p.hotmenu_button.clicked.connect(self.set_hot_drink)
        self.sale_p.frapemenu_button.clicked.connect(self.set_frappe_drink)
        self.sale_p.etcmenu_button.clicked.connect(self.set_etc_menu)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())