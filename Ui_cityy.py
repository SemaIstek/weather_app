# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\umut\Desktop\weather-app\cityy.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(898, 735)
        self.frame_ = QtWidgets.QFrame(Form)
        self.frame_.setGeometry(QtCore.QRect(10, 10, 801, 561))
        self.frame_.setStyleSheet(";\n"
"background-color: rgb(255, 217, 247);")
        self.frame_.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_.setObjectName("frame_")
        self.label_3 = QtWidgets.QLabel(self.frame_)
        self.label_3.setGeometry(QtCore.QRect(410, 50, 311, 211))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\Users\\umut\\Desktop\\weather-app\\../Downloads/pngwing.com.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_)
        self.tableWidget.setGeometry(QtCore.QRect(40, 310, 681, 181))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 246, 248);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label_2 = QtWidgets.QLabel(self.frame_)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 121, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame_)
        self.label_7.setGeometry(QtCore.QRect(110, 210, 131, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_)
        self.label_8.setGeometry(QtCore.QRect(100, 160, 101, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.frame_)
        self.label_5.setGeometry(QtCore.QRect(200, 160, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("c:\\Users\\umut\\Desktop\\weather-app\\../Downloads/Harita işareti Halka açık vektörler.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.frame_)
        self.label_4.setGeometry(QtCore.QRect(90, 180, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame_)
        self.label_6.setGeometry(QtCore.QRect(100, 190, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Today"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "Tomarrow"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "wednesday"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Day"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Night"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Humudity"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Wind"))
        self.label_2.setText(_translate("Form", "7 °C"))
        self.label_7.setText(_translate("Form", "ma, 10.29"))
        self.label_8.setText(_translate("Form", "Amsterdam"))
        self.label_6.setText(_translate("Form", " 10°C/ 7°C feels like 4°C"))
