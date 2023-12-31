# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarDiller\displayvehicletable.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DisplayVehicleTable(object):
    def setupUi(self, DisplayVehicleTable):
        DisplayVehicleTable.setObjectName("DisplayVehicleTable")
        DisplayVehicleTable.resize(1645, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        DisplayVehicleTable.setFont(font)
        DisplayVehicleTable.setStyleSheet("color: rgb(0, 170, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(DisplayVehicleTable)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_SerachForVehicle = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEdit_SerachForVehicle.setFont(font)
        self.lineEdit_SerachForVehicle.setObjectName("lineEdit_SerachForVehicle")
        self.gridLayout.addWidget(self.lineEdit_SerachForVehicle, 0, 0, 1, 1)
        self.pushButton_SearchForVehicle = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton_SearchForVehicle.setFont(font)
        self.pushButton_SearchForVehicle.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 255);")
        self.pushButton_SearchForVehicle.setObjectName("pushButton_SearchForVehicle")
        self.gridLayout.addWidget(self.pushButton_SearchForVehicle, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_AllVehicles = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.radioButton_AllVehicles.setFont(font)
        self.radioButton_AllVehicles.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.radioButton_AllVehicles.setObjectName("radioButton_AllVehicles")
        self.gridLayout_2.addWidget(self.radioButton_AllVehicles, 0, 0, 1, 1)
        self.radioButton_AvailableVehicles = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.radioButton_AvailableVehicles.setFont(font)
        self.radioButton_AvailableVehicles.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 0);")
        self.radioButton_AvailableVehicles.setObjectName("radioButton_AvailableVehicles")
        self.gridLayout_2.addWidget(self.radioButton_AvailableVehicles, 0, 1, 1, 1)
        self.radioButton_UnavailableVehicles = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.radioButton_UnavailableVehicles.setFont(font)
        self.radioButton_UnavailableVehicles.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.radioButton_UnavailableVehicles.setObjectName("radioButton_UnavailableVehicles")
        self.gridLayout_2.addWidget(self.radioButton_UnavailableVehicles, 0, 2, 1, 1)
        self.pushButton_ShowVehicles = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton_ShowVehicles.setFont(font)
        self.pushButton_ShowVehicles.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 255);")
        self.pushButton_ShowVehicles.setObjectName("pushButton_ShowVehicles")
        self.gridLayout_2.addWidget(self.pushButton_ShowVehicles, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.tableWidget_ShowVehicle = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.tableWidget_ShowVehicle.setFont(font)
        self.tableWidget_ShowVehicle.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_ShowVehicle.setAlternatingRowColors(True)
        self.tableWidget_ShowVehicle.setColumnCount(10)
        self.tableWidget_ShowVehicle.setObjectName("tableWidget_ShowVehicle")
        self.tableWidget_ShowVehicle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowVehicle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowVehicle.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowVehicle.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowVehicle.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowVehicle.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowVehicle.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowVehicle.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowVehicle.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowVehicle.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowVehicle.setHorizontalHeaderItem(9, item)
        self.gridLayout_3.addWidget(self.tableWidget_ShowVehicle, 2, 0, 1, 1)
        DisplayVehicleTable.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DisplayVehicleTable)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1645, 33))
        self.menubar.setObjectName("menubar")
        DisplayVehicleTable.setMenuBar(self.menubar)

        self.retranslateUi(DisplayVehicleTable)
        QtCore.QMetaObject.connectSlotsByName(DisplayVehicleTable)

    def retranslateUi(self, DisplayVehicleTable):
        _translate = QtCore.QCoreApplication.translate
        DisplayVehicleTable.setWindowTitle(_translate("DisplayVehicleTable", "Display Vehicle Table"))
        DisplayVehicleTable.setToolTip(_translate("DisplayVehicleTable", "DisplayVehicleTable"))
        self.groupBox.setTitle(_translate("DisplayVehicleTable", "Search for vehicle"))
        self.lineEdit_SerachForVehicle.setPlaceholderText(_translate("DisplayVehicleTable", "Please enter vehicle name or maufacturer"))
        self.pushButton_SearchForVehicle.setText(_translate("DisplayVehicleTable", "Search for vehicle"))
        self.groupBox_2.setTitle(_translate("DisplayVehicleTable", "Show vehicle status"))
        self.radioButton_AllVehicles.setText(_translate("DisplayVehicleTable", "all vehicles"))
        self.radioButton_AvailableVehicles.setText(_translate("DisplayVehicleTable", "available vehicles"))
        self.radioButton_UnavailableVehicles.setText(_translate("DisplayVehicleTable", "unavailable vehicles"))
        self.pushButton_ShowVehicles.setText(_translate("DisplayVehicleTable", "Show vehicles"))
        item = self.tableWidget_ShowVehicle.horizontalHeaderItem(0)
        item.setText(_translate("DisplayVehicleTable", "id"))
        item = self.tableWidget_ShowVehicle.horizontalHeaderItem(1)
        item.setText(_translate("DisplayVehicleTable", "vehicle name"))
        item = self.tableWidget_ShowVehicle.horizontalHeaderItem(2)
        item.setText(_translate("DisplayVehicleTable", "manufacturer"))
        item = self.tableWidget_ShowVehicle.horizontalHeaderItem(3)
        item.setText(_translate("DisplayVehicleTable", "construction year"))
        item = self.tableWidget_ShowVehicle.horizontalHeaderItem(4)
        item.setText(_translate("DisplayVehicleTable", "km stood"))
        item = self.tableWidget_ShowVehicle.horizontalHeaderItem(5)
        item.setText(_translate("DisplayVehicleTable", "condition"))
        item = self.tableWidget_ShowVehicle.horizontalHeaderItem(6)
        item.setText(_translate("DisplayVehicleTable", "pieces"))
        item = self.tableWidget_ShowVehicle.horizontalHeaderItem(7)
        item.setText(_translate("DisplayVehicleTable", "price"))
        item = self.tableWidget_ShowVehicle.horizontalHeaderItem(8)
        item.setText(_translate("DisplayVehicleTable", "currency"))
        item = self.tableWidget_ShowVehicle.horizontalHeaderItem(9)
        item.setText(_translate("DisplayVehicleTable", "availability"))
