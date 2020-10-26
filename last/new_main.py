# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import  QApplication,QMainWindow,QWidget,QPalette,QColor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        p=QPalette()
        p.setColor(QPalette.Window,QColor(192,253,123))
        MainWindow.setObjectName("1")
        MainWindow.resize(288, 202)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 288, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_6.setOpenExternalLinks(True)
        self.pushButton_6.setText("<a href=https://sort.hust.cc >-----------------参考书推荐-----------------</a>")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "算法内容简介"))
        self.pushButton_3.setText(_translate("MainWindow", "算法动态图展示"))
        self.pushButton_4.setText(_translate("MainWindow", "算法演示"))
        self.pushButton_5.setText(_translate("MainWindow", "算法比较"))



import sys
import text
import do_it
import comp
import move

def main():
    app = QApplication(sys.argv)
    QW=QMainWindow()
    zhu=Ui_MainWindow()
    zhu.setupUi(QW)

    # inruduction
    w1 = QWidget()
    word = text.Ui_Form()
    word.setupUi(w1)
    zhu.pushButton_2.clicked.connect(w1.show)

    # move
    w6 = QWidget()
    m = move.Ui_Form()
    m.setupUi(w6)
    zhu.pushButton_3.clicked.connect(w6.show)

    # do it
    w2 = QWidget()
    di = do_it.Ui_Form()
    di.setupUi(w2)
    zhu.pushButton_4.clicked.connect(w2.show)

    # compare
    w3 = QWidget()
    comp1 = comp.Ui_Form()
    comp1.setupUi(w3)
    zhu.pushButton_5.clicked.connect(w3.show)


    QW.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()