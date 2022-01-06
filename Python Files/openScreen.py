from PyQt5 import QtCore, QtGui, QtWidgets
from loginScreen import Ui_loginScreen
from regScreen import Ui_regScreen

class Ui_openScreen(object):

    def openLogin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_loginScreen()
        self.ui.setupUi(self.window)
        self.window.show()
        openScreen.hide()

    def openReg(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_regScreen()
        self.ui.setupUi(self.window)
        self.window.show()
        openScreen.hide()

    def setupUi(self, openScreen):
        openScreen.setObjectName("openScreen")
        openScreen.resize(800, 599)
        openScreen.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(openScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 781, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pics//abc.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(320, 230, 151, 51))
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
        self.loginBtn.clicked.connect(self.openLogin)
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(0, 30, 801, 91))
        self.heading.setStyleSheet("QLabel\n"
                                    "{\n"
                                    "color: white;\n"
                                    "font: 36pt ;\n"
                                    "}")
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.regBtn = QtWidgets.QPushButton(self.centralwidget)
        self.regBtn.setGeometry(QtCore.QRect(320, 290, 151, 51))
        self.regBtn.setStyleSheet("QPushButton {\n"
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
        self.regBtn.setObjectName("regBtn")
        self.regBtn.clicked.connect(self.openReg)
        openScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(openScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        openScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(openScreen)
        self.statusbar.setObjectName("statusbar")
        openScreen.setStatusBar(self.statusbar)

        self.retranslateUi(openScreen)
        QtCore.QMetaObject.connectSlotsByName(openScreen)

    def retranslateUi(self, openScreen):
        _translate = QtCore.QCoreApplication.translate
        openScreen.setWindowTitle(_translate("openScreen", "MainWindow"))
        self.loginBtn.setText(_translate("openScreen", "Log in"))
        self.heading.setText(_translate("openScreen", "Final Year Project"))
        self.regBtn.setText(_translate("openScreen", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    openScreen = QtWidgets.QMainWindow()
    ui = Ui_openScreen()
    ui.setupUi(openScreen)
    openScreen.show()
    sys.exit(app.exec_())
