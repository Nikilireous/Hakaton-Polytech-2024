# Form implementation generated from reading ui file 'reg_form.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 525)
        MainWindow.setStyleSheet("background-color: rgb(3, 177, 18);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 282, 500, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.password = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.password.setMinimumSize(QtCore.QSize(100, 40))
        self.password.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 0, 1, 1)
        self.login = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.login.setMinimumSize(QtCore.QSize(100, 40))
        self.login.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 0, 0, 1, 1)
        self.login_edit = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.login_edit.setMinimumSize(QtCore.QSize(350, 40))
        self.login_edit.setMaximumSize(QtCore.QSize(350, 40))
        self.login_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login_edit.setObjectName("login_edit")
        self.gridLayout.addWidget(self.login_edit, 0, 1, 1, 1)
        self.password_edit = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.password_edit.setMinimumSize(QtCore.QSize(350, 40))
        self.password_edit.setMaximumSize(QtCore.QSize(350, 40))
        self.password_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_edit.setObjectName("password_edit")
        self.gridLayout.addWidget(self.password_edit, 1, 1, 1, 1)
        self.submit_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_btn.setGeometry(QtCore.QRect(210, 410, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit_btn.setFont(font)
        self.submit_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.submit_btn.setObjectName("submit_btn")
        self.Logo_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Logo_label.setGeometry(QtCore.QRect(2, 2, 500, 100))
        self.Logo_label.setText("")
        self.Logo_label.setObjectName("Logo_label")
        self.pixmap = QPixmap('logo.png')
        self.Logo_label.setPixmap(self.pixmap)
        self.Logo_label.resize(self.pixmap.width(), self.pixmap.height())

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusBar.setFont(font)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.password.setText(_translate("MainWindow", "Password:"))
        self.login.setText(_translate("MainWindow", "Login: "))
        self.submit_btn.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
