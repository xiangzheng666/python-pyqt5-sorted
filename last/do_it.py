# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'do-it.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import power as p
import re


class MyFigure(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        super(MyFigure, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

    def plot(self,m,aa):
            plt.rcParams['font.family'] = ['SimHei']
            plt.rcParams['axes.unicode_minus'] = False
            NameList = len(m)
            AgeList = m
            self.x = np.arange(NameList) + 1
            self.y = np.array(AgeList)
            self.axes.clear()
            self.axes.bar(range(NameList), AgeList, color='green', width=0.5)
            for a, b in zip(self.x, self.y):
                self.axes.text(a - 1, b, '%d' % b, ha='center', va='bottom')
            plt.title("算法步骤")






class Ui_Form(object):
    def k(self):
        self.canvas = MyFigure()
        self.canvas.setParent(self.frame)

    def b(self):
        k = []
        kk = []
        xx = self.lineEdit.text()
        for i in list(re.split('[^\w]', xx)):
                if i.isalnum():
                    kk.append(int(i))
                    k.append(i)
                else:
                   pass
        self.data = kk.copy()
        self.pushButton.setText('==='.join(k))

    def draw1(self,m):
        a=self.tt
        self.canvas.close_event()
        self.canvas.plot(m,a)
        self.canvas.draw()

    def p2(self):
        c1 = self.comboBox_2.currentText()
        if self.data and c1 != 'null':
            self.num=0
            max1 = max(self.data)
            cc1 = str(c1)
            cc2 = self.data.copy()
            out, process1, ti1, we1, n1 = p.k(cc1, cc2, max1)
            self.maxx=len(process1)
            mt = process1[self.num]
            self.t = process1
            self.draw1(self.data)

    def p3(self):
        c1 = self.comboBox_2.currentText()
        if self.data and c1 != 'null':
            if self.num > 0:
                self.num = self.num - 1
                mt = self.t[self.num]
                self.draw1(mt)
                st1='这是'+str(self.num+1)+'步,总共'+str(self.maxx+1)+'步'
                self.pushButton_3.setText(st1)

    def p4(self):
        c1 = self.comboBox_2.currentText()
        if self.data and c1 != 'null':
            if self.num < self.maxx - 1:
                self.num = self.num + 1
                mt = self.t[self.num]
                self.draw1(mt)
                st1 = '这是' + str(self.num+ 1 )+ '步,总共' + str(self.maxx + 1) + '步'
                self.pushButton_4.setText(st1)
    def setupUi(self, Form):
        self.tt=0
        self.maxx=0
        self.t=[]
        self.num=0
        self.data=[]
        Form.setObjectName("Form")
        Form.resize(718, 646)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('请输入整数，分割符为.,，/;[等....')
        self.lineEdit.setToolTip('请输入整数，分割符为.,，/;[等....')
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(409, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.k()
        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.b)


        self.pushButton_2.clicked.connect(self.p2)


        self.pushButton_3.clicked.connect(self.p3)


        self.pushButton_4.clicked.connect(self.p4)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox_2.setItemText(0, _translate("Form", "null"))
        self.comboBox_2.setItemText(1, _translate("Form", "冒泡排序"))
        self.comboBox_2.setItemText(2, _translate("Form", "快速排序"))
        self.comboBox_2.setItemText(3, _translate("Form", "归并排序"))
        self.comboBox_2.setItemText(4, _translate("Form", "选择排序"))
        self.comboBox_2.setItemText(5, _translate("Form", "希尔排序"))
        self.comboBox_2.setItemText(6, _translate("Form", "插入排序"))
        self.comboBox_2.setItemText(7, _translate("Form", "计数排序"))
        self.comboBox_2.setItemText(8, _translate("Form", "基数排序"))
        self.comboBox_2.setItemText(9, _translate("Form", "堆排序"))
        self.comboBox_2.setItemText(10, _translate("Form", "桶排序"))
        self.pushButton_4.setText(_translate("Form", "下一步"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.pushButton_2.setText(_translate("Form", "开始测试"))
        self.pushButton_3.setText(_translate("Form", "上一步"))


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QApplication,QWidget,QMovie
import  sys

if __name__ == '__main__':
    app=QApplication(sys.argv)
    tem=QWidget()
    a=Ui_Form()
    test=a.setupUi(tem)
    tem.show()
    app.exec()