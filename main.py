import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
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

    def set_login_page_action(self):
        self.login_p.login_button.clicked.connect(self.login)

    def login(self):
        self.user = self.login_p.username_edit.toPlainText()
        self.pas = self.login_p.password_edit.toPlainText()
        # easy for check at frist
        if(self.user != "admin"):
            self.login_p.error_label.setText("dont exit user name : "+self.user)
            return
        elif(self.pas != "123456"):
            self.login_p.error_label.setText("password wrong for user name : "+self.user)
            return
        else:
            self.open_select_page()

    def open_select_page(self):
        self.select_p.setupUi(self)
        self.select_p.userinfo_label.setText(self.user)  ##### fix at first
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
        self.set_sale_page_action()
        self.show()

    def set_sale_page_action(self):
        self.sale_p.back_button.clicked.connect(self.open_select_page)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())