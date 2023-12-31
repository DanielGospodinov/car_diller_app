# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarDiller\showsellerview.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowSellerView(object):
    def setupUi(self, ShowSellerView):
        ShowSellerView.setObjectName("ShowSellerView")
        ShowSellerView.resize(1645, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        ShowSellerView.setFont(font)
        ShowSellerView.setStyleSheet("color: rgb(0, 170, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(ShowSellerView)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 0, 1, 1)
        self.pushButton_searchSeller = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton_searchSeller.setFont(font)
        self.pushButton_searchSeller.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_searchSeller.setObjectName("pushButton_searchSeller")
        self.gridLayout.addWidget(self.pushButton_searchSeller, 1, 0, 1, 1)
        self.pushButton_allSellers = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton_allSellers.setFont(font)
        self.pushButton_allSellers.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 0);")
        self.pushButton_allSellers.setObjectName("pushButton_allSellers")
        self.gridLayout.addWidget(self.pushButton_allSellers, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tableWidget_ShowSellerView = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.tableWidget_ShowSellerView.setFont(font)
        self.tableWidget_ShowSellerView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_ShowSellerView.setAlternatingRowColors(True)
        self.tableWidget_ShowSellerView.setColumnCount(6)
        self.tableWidget_ShowSellerView.setObjectName("tableWidget_ShowSellerView")
        self.tableWidget_ShowSellerView.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowSellerView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowSellerView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowSellerView.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowSellerView.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowSellerView.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_ShowSellerView.setHorizontalHeaderItem(5, item)
        self.gridLayout_2.addWidget(self.tableWidget_ShowSellerView, 1, 0, 1, 1)
        ShowSellerView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ShowSellerView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1645, 26))
        self.menubar.setObjectName("menubar")
        ShowSellerView.setMenuBar(self.menubar)

        self.retranslateUi(ShowSellerView)
        QtCore.QMetaObject.connectSlotsByName(ShowSellerView)

    def retranslateUi(self, ShowSellerView):
        _translate = QtCore.QCoreApplication.translate
        ShowSellerView.setWindowTitle(_translate("ShowSellerView", "Show existing sellers"))
        ShowSellerView.setToolTip(_translate("ShowSellerView", "Show existing sellers"))
        self.groupBox.setTitle(_translate("ShowSellerView", "Search for seller"))
        self.lineEdit_name.setPlaceholderText(_translate("ShowSellerView", "Please enter seller name"))
        self.pushButton_searchSeller.setText(_translate("ShowSellerView", "Search for seller"))
        self.pushButton_allSellers.setText(_translate("ShowSellerView", "All sellers"))
        item = self.tableWidget_ShowSellerView.horizontalHeaderItem(0)
        item.setText(_translate("ShowSellerView", "id"))
        item = self.tableWidget_ShowSellerView.horizontalHeaderItem(1)
        item.setText(_translate("ShowSellerView", "Name"))
        item = self.tableWidget_ShowSellerView.horizontalHeaderItem(2)
        item.setText(_translate("ShowSellerView", "New Column"))
        item = self.tableWidget_ShowSellerView.horizontalHeaderItem(3)
        item.setText(_translate("ShowSellerView", "Lastname"))
        item = self.tableWidget_ShowSellerView.horizontalHeaderItem(4)
        item.setText(_translate("ShowSellerView", "Phone"))
        item = self.tableWidget_ShowSellerView.horizontalHeaderItem(5)
        item.setText(_translate("ShowSellerView", "Address"))
