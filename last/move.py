# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '文字介绍.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import  QApplication,QMainWindow,QWidget,QMovie
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(892, 559)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QLabel(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)


        def b2():
            m1 = QMovie('冒泡排序.gif')
            self.textBrowser.setMovie(m1)
            m1.start()
        self.pushButton_2.clicked.connect(b2)

        def b3():
            m1 = QMovie('快速排序.gif')
            self.textBrowser.setMovie(m1)
            m1.start()
        self.pushButton_3.clicked.connect(b3)

        def b4():
            m1 = QMovie('归并排序.gif')
            self.textBrowser.setMovie(m1)
            m1.start()
        self.pushButton_4.clicked.connect(b4)

        def b5():
            m1 = QMovie('选择排序.gif')
            self.textBrowser.setMovie(m1)
            m1.start()
        self.pushButton_5.clicked.connect(b5)

        def b6():
            m1 = QMovie('希尔排序.gif')
            self.textBrowser.setMovie(m1)
            m1.start()
        self.pushButton_6.clicked.connect(b6)

        def b9():
            m1 = QMovie('基数排序.gif')
            self.textBrowser.setMovie(m1)
            m1.start()
        self.pushButton_9.clicked.connect(b9)

        def b7():
            m1 = QMovie('插入排序.gif')
            self.textBrowser.setMovie(m1)
            m1.start()
        self.pushButton_7.clicked.connect(b7)

        def b8():
            m1 = QMovie('计数排序.gif')
            self.textBrowser.setMovie(m1)
            m1.start()
        self.pushButton_8.clicked.connect(b8)

        def b10():
            m1 = QMovie('堆排序.gif')
            self.textBrowser.setMovie(m1)
            m1.start()
        self.pushButton_10.clicked.connect(b10)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "冒泡排序"))
        self.pushButton_3.setText(_translate("Form", "快速排序"))
        self.pushButton_4.setText(_translate("Form", "归并排序"))
        self.pushButton_5.setText(_translate("Form", "选择排序"))
        self.pushButton_6.setText(_translate("Form", "希尔排序"))
        self.pushButton_7.setText(_translate("Form", "插入排序"))
        self.pushButton_8.setText(_translate("Form", "计数排序"))
        self.pushButton_9.setText(_translate("Form", "基数排序"))
        self.pushButton_10.setText(_translate("Form", "堆排序"))


def main():
    app = QApplication(sys.argv)
    QW=QWidget()
    zhu=Ui_Form()
    zhu.setupUi(QW)

    QW.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()