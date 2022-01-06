from PyQt5 import QtCore, QtGui, QtWidgets
import helperFunctions as hf
from loginScreen import Ui_loginScreen
class Ui_regScreen(object):

    def register(self):
        email = self.emailFeild.text()
        pass1 = self.passFeild.text()
        pass2 = self.retypePass.text()

        if pass1 == pass2:
            hf.auth.create_user_with_email_and_password(email,pass1)
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_loginScreen()
        self.ui.setupUi(self.window)
        self.window.show()
        regScreen.hide()


    def setupUi(self, regScreen):
        regScreen.setObjectName("regScreen")
        regScreen.resize(800, 599)
        regScreen.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(regScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 781, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pics//abc.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.passFeild = QtWidgets.QLineEdit(self.centralwidget)
        self.passFeild.setGeometry(QtCore.QRect(270, 300, 251, 41))
        self.passFeild.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.passFeild.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passFeild.setAlignment(QtCore.Qt.AlignCenter)
        self.passFeild.setObjectName("passFeild")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(330, 400, 121, 41))
        self.loginBtn.setStyleSheet("QPushButton {\n"
                                    "background-color: rgb(214, 214, 214);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "background-color: rgb(173, 173, 173);\n"
                                    "}")
        self.loginBtn.setObjectName("loginBtn")
        self.emailFeild = QtWidgets.QLineEdit(self.centralwidget)
        self.emailFeild.setGeometry(QtCore.QRect(270, 250, 251, 41))
        self.emailFeild.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.emailFeild.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.emailFeild.setAlignment(QtCore.Qt.AlignCenter)
        self.emailFeild.setObjectName("emailFeild")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(0, 30, 801, 91))
        self.heading.setStyleSheet("QLabel\n"
                                    "{\n"
                                    "color: white;\n"
                                    "font: 36pt ;\n"
                                    "}")
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.retypePass = QtWidgets.QLineEdit(self.centralwidget)
        self.retypePass.setGeometry(QtCore.QRect(270, 350, 251, 41))
        self.retypePass.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.retypePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retypePass.setAlignment(QtCore.Qt.AlignCenter)
        self.retypePass.setObjectName("retypePass")
        regScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(regScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        regScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(regScreen)
        self.statusbar.setObjectName("statusbar")
        regScreen.setStatusBar(self.statusbar)

        self.retranslateUi(regScreen)
        QtCore.QMetaObject.connectSlotsByName(regScreen)

    def retranslateUi(self, regScreen):
        _translate = QtCore.QCoreApplication.translate
        regScreen.setWindowTitle(_translate("regScreen", "MainWindow"))
        self.passFeild.setPlaceholderText(_translate("regScreen", "Password"))
        self.loginBtn.setText(_translate("regScreen", "Register"))
        self.emailFeild.setPlaceholderText(_translate("regScreen", "Email"))
        self.heading.setText(_translate("regScreen", "Final Year Project"))
        self.retypePass.setPlaceholderText(_translate("regScreen", "Retype Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    regScreen = QtWidgets.QMainWindow()
    ui = Ui_regScreen()
    ui.setupUi(regScreen)
    regScreen.show()
    sys.exit(app.exec_())
