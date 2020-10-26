# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import power as p
import re

class Ui_Form(object):
    def setupUi(self, Form):
        self.data=[]
        Form.setObjectName("Form")
        Form.resize(848, 662)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 10, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.gridLayout.addLayout(self.verticalLayout_2, 11, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 9, 0, 1, 2)
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
        self.gridLayout.addWidget(self.comboBox_2, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 12, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 13, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout, 7, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        def b():
            k=[]
            kk=[]
            xx=self.lineEdit.text()
            if xx.endswith('.') or xx=='' or xx.endswith('，') or xx.endswith(',') or xx.endswith(' '):
                pass
            else:
                for i in list(re.split('[^\w]',xx)):
                    kk.append(int(i))
                    k.append(i)
                self.data=kk.copy()
                self.label_2.setText('==='.join(k))

        self.pushButton.clicked.connect(b)

        def b2():
            c1 = self.comboBox_2.currentText()
            c2 = self.comboBox_4.currentText()
            if self.data and c1 !='null' and c2 !='null':
                max1=max(self.data)
                #c1:
                cc1=str(c1)
                cc2=self.data.copy()
                out1,process1,ti1,we1,n1=p.k(cc1,cc2,max1)
                #时间
                s1='运行时间：'+str(ti1)+'s'
                self.label_3.setText(s1)
                #过程
                qq=''
                ii1=0
                # 稳定
                self.label_5.setText(we1)
                # 内存
                self.label_4.setText(n1)
                for i in process1:
                    i=map(str,i)
                    str1='-'.join(i)
                    s="第"+str(ii1)+'步:     '+str1+'\n'
                    qq=qq+s
                    ii1+=1
                self.textEdit.setText(qq)
                # c2:
                cc3 = self.data.copy()
                out2, process2, ti2,wen2,n2 = p.k(str(c2), cc3, max1)
                # 时间
                s2 = '运行时间：' + str(ti2) + 's'
                self.label_8.setText(s2)
                #稳定
                self.label_10.setText(wen2)
                #内存
                self.label_9.setText(n2)
                # 过程
                qq1 = ''
                ii = 0
                for i in process2:
                    i = map(str, i)
                    str2 = '-'.join(i)
                    s = "第" + str(ii) + '步' + ':    '+str2+'\n'
                    qq1 = qq1 + s
                    ii += 1
                self.textEdit_2.setText(qq1)


        self.pushButton_2.clicked.connect(b2)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox_4.setItemText(0, _translate("Form", "null"))
        self.comboBox_4.setItemText(1, _translate("Form", "冒泡排序"))
        self.comboBox_4.setItemText(2, _translate("Form", "快速排序"))
        self.comboBox_4.setItemText(3, _translate("Form", "归并排序"))
        self.comboBox_4.setItemText(4, _translate("Form", "选择排序"))
        self.comboBox_4.setItemText(5, _translate("Form", "希尔排序"))
        self.comboBox_4.setItemText(6, _translate("Form", "插入排序"))
        self.comboBox_4.setItemText(7, _translate("Form", "计数排序"))
        self.comboBox_4.setItemText(8, _translate("Form", "基数排序"))
        self.comboBox_4.setItemText(9, _translate("Form", "堆排序"))
        self.comboBox_4.setItemText(10, _translate("Form", "桶排序"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.label_2.setText(_translate("Form", "数据"))
        self.label.setText(_translate("Form", "输入数据          int型    不是数字，字母就是分割符   最后面是数字  不要写两个分割，不然。。"))
        self.pushButton_2.setText(_translate("Form", "开始测试比较"))
        self.label_8.setText(_translate("Form", "运行时间："))
        self.label_9.setText(_translate("Form", "所占内存："))
        self.label_10.setText(_translate("Form", "稳定性："))
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
        self.label_7.setText(_translate("Form", "运行过程："))
        self.label_12.setText(_translate("Form", "选择比较算法"))
        self.label_6.setText(_translate("Form", "运行过程："))
        self.label_3.setText(_translate("Form", "运行时间："))
        self.label_4.setText(_translate("Form", "所占内存："))
        self.label_5.setText(_translate("Form", "稳定性："))
