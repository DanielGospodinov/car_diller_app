# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarDiller\statisticstaffperyear.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StatisticStaffPerYear(object):
    def setupUi(self, StatisticStaffPerYear):
        StatisticStaffPerYear.setObjectName("StatisticStaffPerYear")
        StatisticStaffPerYear.resize(600, 800)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        StatisticStaffPerYear.setFont(font)
        StatisticStaffPerYear.setStyleSheet("color: rgb(0, 170, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(StatisticStaffPerYear)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_show = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton_show.setFont(font)
        self.pushButton_show.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_show.setObjectName("pushButton_show")
        self.gridLayout.addWidget(self.pushButton_show, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_year = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEdit_year.setFont(font)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.gridLayout.addWidget(self.lineEdit_year, 0, 1, 1, 1)
        self.lineEdit_sellerLastname = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEdit_sellerLastname.setFont(font)
        self.lineEdit_sellerLastname.setObjectName("lineEdit_sellerLastname")
        self.gridLayout.addWidget(self.lineEdit_sellerLastname, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 1, 1, 1)
        self.label_sellerLastname = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_sellerLastname.setFont(font)
        self.label_sellerLastname.setText("")
        self.label_sellerLastname.setObjectName("label_sellerLastname")
        self.gridLayout_2.addWidget(self.label_sellerLastname, 0, 1, 1, 1)
        self.label_numberOfSoldCars = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_numberOfSoldCars.setFont(font)
        self.label_numberOfSoldCars.setText("")
        self.label_numberOfSoldCars.setObjectName("label_numberOfSoldCars")
        self.gridLayout_2.addWidget(self.label_numberOfSoldCars, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_totalSales = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_totalSales.setFont(font)
        self.label_totalSales.setText("")
        self.label_totalSales.setObjectName("label_totalSales")
        self.gridLayout_2.addWidget(self.label_totalSales, 3, 1, 1, 1)
        self.label_sellYear = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_sellYear.setFont(font)
        self.label_sellYear.setText("")
        self.label_sellYear.setObjectName("label_sellYear")
        self.gridLayout_2.addWidget(self.label_sellYear, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        StatisticStaffPerYear.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StatisticStaffPerYear)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 33))
        self.menubar.setObjectName("menubar")
        StatisticStaffPerYear.setMenuBar(self.menubar)

        self.retranslateUi(StatisticStaffPerYear)
        QtCore.QMetaObject.connectSlotsByName(StatisticStaffPerYear)

    def retranslateUi(self, StatisticStaffPerYear):
        _translate = QtCore.QCoreApplication.translate
        StatisticStaffPerYear.setWindowTitle(_translate("StatisticStaffPerYear", "Statistic staff per year"))
        StatisticStaffPerYear.setToolTip(_translate("StatisticStaffPerYear", "Statistic staff per year"))
        self.groupBox.setTitle(_translate("StatisticStaffPerYear", "Show overview of seller per year"))
        self.pushButton_show.setText(_translate("StatisticStaffPerYear", "Show"))
        self.label_3.setText(_translate("StatisticStaffPerYear", "Seller Lastname"))
        self.label_2.setText(_translate("StatisticStaffPerYear", "Year"))
        self.lineEdit_year.setPlaceholderText(_translate("StatisticStaffPerYear", "please enter years"))
        self.lineEdit_sellerLastname.setPlaceholderText(_translate("StatisticStaffPerYear", "please enter seller lasname"))
        self.label_6.setText(_translate("StatisticStaffPerYear", "number of sold cars"))
        self.label_5.setText(_translate("StatisticStaffPerYear", "Sell year"))
        self.label_7.setText(_translate("StatisticStaffPerYear", "Total sales"))
        self.label_4.setText(_translate("StatisticStaffPerYear", "Seller lastname"))
