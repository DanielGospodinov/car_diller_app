# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarDiller\addnewvehicle.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddNewVehicle(object):
    def setupUi(self, AddNewVehicle):
        AddNewVehicle.setObjectName("AddNewVehicle")
        AddNewVehicle.resize(600, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        AddNewVehicle.setFont(font)
        AddNewVehicle.setStyleSheet("color: rgb(0, 170, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(AddNewVehicle)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_pictureAddNewVehicle = QtWidgets.QLabel(self.centralwidget)
        self.label_pictureAddNewVehicle.setText("")
        self.label_pictureAddNewVehicle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pictureAddNewVehicle.setObjectName("label_pictureAddNewVehicle")
        self.gridLayout.addWidget(self.label_pictureAddNewVehicle, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEditVehicleNameAddNewVehicle = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEditVehicleNameAddNewVehicle.setFont(font)
        self.lineEditVehicleNameAddNewVehicle.setObjectName("lineEditVehicleNameAddNewVehicle")
        self.gridLayout_2.addWidget(self.lineEditVehicleNameAddNewVehicle, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEditManufacturerAddNewVehicle = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEditManufacturerAddNewVehicle.setFont(font)
        self.lineEditManufacturerAddNewVehicle.setObjectName("lineEditManufacturerAddNewVehicle")
        self.gridLayout_2.addWidget(self.lineEditManufacturerAddNewVehicle, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEditConnstructionYearAddNewVehicle = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEditConnstructionYearAddNewVehicle.setFont(font)
        self.lineEditConnstructionYearAddNewVehicle.setObjectName("lineEditConnstructionYearAddNewVehicle")
        self.gridLayout_2.addWidget(self.lineEditConnstructionYearAddNewVehicle, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEditKmStoodAddNewVehicle = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEditKmStoodAddNewVehicle.setFont(font)
        self.lineEditKmStoodAddNewVehicle.setObjectName("lineEditKmStoodAddNewVehicle")
        self.gridLayout_2.addWidget(self.lineEditKmStoodAddNewVehicle, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        self.comboBox_VehicleConditionAddNewVehicle = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.comboBox_VehicleConditionAddNewVehicle.setFont(font)
        self.comboBox_VehicleConditionAddNewVehicle.setObjectName("comboBox_VehicleConditionAddNewVehicle")
        self.comboBox_VehicleConditionAddNewVehicle.addItem("")
        self.comboBox_VehicleConditionAddNewVehicle.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_VehicleConditionAddNewVehicle, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineEditNumberOfPiecesAddNewVehicle = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEditNumberOfPiecesAddNewVehicle.setFont(font)
        self.lineEditNumberOfPiecesAddNewVehicle.setObjectName("lineEditNumberOfPiecesAddNewVehicle")
        self.gridLayout_2.addWidget(self.lineEditNumberOfPiecesAddNewVehicle, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)
        self.lineEditPriceAddNewVehicle = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.lineEditPriceAddNewVehicle.setFont(font)
        self.lineEditPriceAddNewVehicle.setObjectName("lineEditPriceAddNewVehicle")
        self.gridLayout_2.addWidget(self.lineEditPriceAddNewVehicle, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 1)
        self.comboBox_CurrencyAddNewVehicle = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.comboBox_CurrencyAddNewVehicle.setFont(font)
        self.comboBox_CurrencyAddNewVehicle.setObjectName("comboBox_CurrencyAddNewVehicle")
        self.comboBox_CurrencyAddNewVehicle.addItem("")
        self.comboBox_CurrencyAddNewVehicle.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_CurrencyAddNewVehicle, 7, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 8, 0, 1, 1)
        self.pushButton_UploadVehiclePictureAddNewVehicle = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton_UploadVehiclePictureAddNewVehicle.setFont(font)
        self.pushButton_UploadVehiclePictureAddNewVehicle.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.pushButton_UploadVehiclePictureAddNewVehicle.setObjectName("pushButton_UploadVehiclePictureAddNewVehicle")
        self.gridLayout_2.addWidget(self.pushButton_UploadVehiclePictureAddNewVehicle, 8, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 9, 0, 2, 1)
        self.pushButton_SubmitAddNewVehicle = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton_SubmitAddNewVehicle.setFont(font)
        self.pushButton_SubmitAddNewVehicle.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 127);")
        self.pushButton_SubmitAddNewVehicle.setObjectName("pushButton_SubmitAddNewVehicle")
        self.gridLayout_2.addWidget(self.pushButton_SubmitAddNewVehicle, 10, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 11, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        AddNewVehicle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddNewVehicle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 33))
        self.menubar.setObjectName("menubar")
        AddNewVehicle.setMenuBar(self.menubar)

        self.retranslateUi(AddNewVehicle)
        QtCore.QMetaObject.connectSlotsByName(AddNewVehicle)

    def retranslateUi(self, AddNewVehicle):
        _translate = QtCore.QCoreApplication.translate
        AddNewVehicle.setWindowTitle(_translate("AddNewVehicle", "Add New Vehicle"))
        AddNewVehicle.setToolTip(_translate("AddNewVehicle", "Add New Vehicle"))
        self.label.setText(_translate("AddNewVehicle", "add new vehicle"))
        self.label_3.setText(_translate("AddNewVehicle", "Vehicle name"))
        self.lineEditVehicleNameAddNewVehicle.setPlaceholderText(_translate("AddNewVehicle", "Please enter vehicle name"))
        self.label_4.setText(_translate("AddNewVehicle", "Manufacturer"))
        self.lineEditManufacturerAddNewVehicle.setPlaceholderText(_translate("AddNewVehicle", "Please enter manufacturer"))
        self.label_5.setText(_translate("AddNewVehicle", "Construction year"))
        self.lineEditConnstructionYearAddNewVehicle.setPlaceholderText(_translate("AddNewVehicle", "Please enter construction year"))
        self.label_6.setText(_translate("AddNewVehicle", "Km stood"))
        self.lineEditKmStoodAddNewVehicle.setPlaceholderText(_translate("AddNewVehicle", "Please enter km stood"))
        self.label_7.setText(_translate("AddNewVehicle", "Vehicle condition"))
        self.comboBox_VehicleConditionAddNewVehicle.setItemText(0, _translate("AddNewVehicle", "new vehicle"))
        self.comboBox_VehicleConditionAddNewVehicle.setItemText(1, _translate("AddNewVehicle", "used vehicle"))
        self.label_8.setText(_translate("AddNewVehicle", "number of pieces"))
        self.lineEditNumberOfPiecesAddNewVehicle.setPlaceholderText(_translate("AddNewVehicle", "Please enter number of pieces"))
        self.label_9.setText(_translate("AddNewVehicle", "price"))
        self.lineEditPriceAddNewVehicle.setPlaceholderText(_translate("AddNewVehicle", "Please enter price"))
        self.label_10.setText(_translate("AddNewVehicle", "currency"))
        self.comboBox_CurrencyAddNewVehicle.setItemText(0, _translate("AddNewVehicle", "€"))
        self.comboBox_CurrencyAddNewVehicle.setItemText(1, _translate("AddNewVehicle", "$"))
        self.label_11.setText(_translate("AddNewVehicle", "Vehicle picture"))
        self.pushButton_UploadVehiclePictureAddNewVehicle.setText(_translate("AddNewVehicle", "Upload vehicle picture"))
        self.pushButton_SubmitAddNewVehicle.setText(_translate("AddNewVehicle", "Submit"))