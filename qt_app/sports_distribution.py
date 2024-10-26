from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 800)
        MainWindow.setStyleSheet("background-color: rgb(121,189,143);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 79, 1051, 311))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Tennis = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tennis.sizePolicy().hasHeightForWidth())
        self.Tennis.setSizePolicy(sizePolicy)
        self.Tennis.setMinimumSize(QtCore.QSize(300, 300))
        self.Tennis.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Tennis.setFont(font)
        self.Tennis.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Tennis.setObjectName("Tennis")
        self.horizontalLayout.addWidget(self.Tennis)
        self.Football = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.Football.setMinimumSize(QtCore.QSize(300, 300))
        self.Football.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Football.setFont(font)
        self.Football.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Football.setObjectName("Football")
        self.horizontalLayout.addWidget(self.Football)
        self.Bascketball = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.Bascketball.setMinimumSize(QtCore.QSize(300, 300))
        self.Bascketball.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Bascketball.setFont(font)
        self.Bascketball.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Bascketball.setObjectName("Bascketball")
        self.horizontalLayout.addWidget(self.Bascketball)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 390, 1051, 311))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.Volleyball = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.Volleyball.setMinimumSize(QtCore.QSize(300, 300))
        self.Volleyball.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Volleyball.setFont(font)
        self.Volleyball.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.Volleyball.setObjectName("Volleyball")
        self.horizontalLayout_2.addWidget(self.Volleyball)
        self.Hockey = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.Hockey.setMinimumSize(QtCore.QSize(300, 300))
        self.Hockey.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Hockey.setFont(font)
        self.Hockey.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Hockey.setObjectName("Hockey")
        self.horizontalLayout_2.addWidget(self.Hockey)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Tennis.setText(_translate("MainWindow", "Теннис"))
        self.Football.setText(_translate("MainWindow", "Футбол"))
        self.Bascketball.setText(_translate("MainWindow", "Баскетбол"))
        self.Volleyball.setText(_translate("MainWindow", "Воллейбол"))
        self.Hockey.setText(_translate("MainWindow", "Хоккей"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
