from PyQt5 import QtCore, QtGui, QtWidgets
import helperFunctions as hf
import os

class Ui_loginScreen(object):

    def login(self):
        email = self.emailFeild.text()
        password = self.passFeild.text()

        hf.auth.sign_in_with_email_and_password(email, password)
        print("logged in")
        os.system("python NMS.py")


    def setupUi(self, loginScreen):
        loginScreen.setObjectName("loginScreen")
        loginScreen.resize(800, 599)
        loginScreen.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(loginScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 781, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pics//abc.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.passFeild = QtWidgets.QLineEdit(self.centralwidget)
        self.passFeild.setGeometry(QtCore.QRect(270, 350, 251, 41))
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
        self.loginBtn.clicked.connect(self.login)
        self.emailFeild = QtWidgets.QLineEdit(self.centralwidget)
        self.emailFeild.setGeometry(QtCore.QRect(270, 300, 251, 41))
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
        loginScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        loginScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginScreen)
        self.statusbar.setObjectName("statusbar")
        loginScreen.setStatusBar(self.statusbar)

        self.retranslateUi(loginScreen)
        QtCore.QMetaObject.connectSlotsByName(loginScreen)

    def retranslateUi(self, loginScreen):
        _translate = QtCore.QCoreApplication.translate
        loginScreen.setWindowTitle(_translate("loginScreen", "MainWindow"))
        self.passFeild.setPlaceholderText(_translate("loginScreen", "Password"))
        self.loginBtn.setText(_translate("loginScreen", "Log in"))
        self.emailFeild.setPlaceholderText(_translate("loginScreen", "Email"))
        self.heading.setText(_translate("loginScreen", "Final Year Project"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginScreen = QtWidgets.QMainWindow()
    ui = Ui_loginScreen()
    ui.setupUi(loginScreen)
    loginScreen.show()
    sys.exit(app.exec_())
