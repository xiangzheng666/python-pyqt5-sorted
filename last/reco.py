# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reco.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(339, 261)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.label.setOpenExternalLinks(True)
        self.label.setText("<a href=https://sort.hust.cc >gitbook上的排序参考书</a>")


        QtCore.QMetaObject.connectSlotsByName(Form)


if __name__ == '__main__':
    from PyQt5.Qt import QWidget,QApplication
    import sys
    app=QApplication(sys.argv)
    w=QWidget()
    m=Ui_Form()
    m.setupUi(w)
    w.show()

    sys.exit(app.exec_())