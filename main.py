import os
import sqlite3
import sys
from qtpy import QtWidgets
from PyQt5.QtWidgets import *
from PIL import Image
from PyQt5.QtGui import *
import matplotlib.pyplot as plt

from CarDiller.mainwindow import Ui_MainWindow
from CarDiller.addnewvehicle import Ui_AddNewVehicle
from CarDiller.displayvehicletable import Ui_DisplayVehicleTable
from CarDiller.selectsinglevehicle import Ui_SelectSingleVehicle
from CarDiller.addnewcarsseller import Ui_AddNewCarsSeller
from CarDiller.showsellerview import Ui_ShowSellerView
from CarDiller.selectsingleseller import Ui_SelectSingleSeller
from CarDiller.addnewcustomer import Ui_AddNewCustomer
from CarDiller.showcostumerstable import Ui_ShowCostumersTable
from CarDiller.showsinglecustumer import Ui_ShowSingleCustumer
from CarDiller.deal import Ui_Deal
from CarDiller.makedeal import Ui_MakeDeal
from CarDiller.statisticstaffpermonth import Ui_StatisticStaffPerMonth
from CarDiller.statisticstaffperyear import Ui_StatisticStaffPerYear
from CarDiller.statisticcustomerperyear import Ui_StatisticCustomerPerYear
from CarDiller.monthlyoverview import Ui_MonthlyOverview
from CarDiller.annualoverview import Ui_AnnualOverview

replacementPicture = 'question.jpg'
con = sqlite3.connect("car dealer.db")
cur = con.cursor()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))

        self.ui.actionadd_new_vehicleMenu_toolbar.setIcon(QIcon('icons/label.png'))
        self.ui.actionadd_new_car_seller_toolbar.setIcon(QIcon('icons/new-arrival.png'))
        self.ui.actionAdd_new_custumer_toolbar.setIcon(QIcon('icons/team-member.png'))
        self.ui.label_PictureMainWindow.setPixmap(QPixmap('pictures/lamborghini.Yellow.png'))
        self.ui.actionDeal_toolbar.setIcon(QIcon('icons/deal.png'))
        self.ui.actionDo_business_menu.setIcon(QIcon('icons/deal.png'))
        self.ui.actionstatistic_staff_per_month_toolbar.setIcon((QIcon('icons/confirm.png')))
        self.ui.actionStatistic_staff_per_month_menu.setIcon((QIcon('icons/confirm.png')))
        self.ui.actionStatistic_staff_per_year.setIcon(QIcon('icons/google-docs.png'))
        self.ui.actionStatistic_staff_per_year_toolbar.setIcon(QIcon('icons/google-docs.png'))
        self.ui.actionStatistic_customer_per_year.setIcon(QIcon('icons/brand-identity.png'))
        self.ui.actionStatistic_customer_per_year_toolbar.setIcon(QIcon('icons/brand-identity.png'))
        self.ui.actionMonthly_overview.setIcon(QIcon('icons/product.png'))
        self.ui.actionMonthly_overview_toolbar.setIcon(QIcon('icons/product.png'))
        self.ui.actionAnnual_overview.setIcon(QIcon('icons/money.png'))
        self.ui.actionAnnual_overview_toolbar.setIcon(QIcon('icons/money.png'))

        self.ui.actionAdd_new_vehicleMenu.triggered.connect(self.showAddNewVehicleMenu)
        self.ui.actionadd_new_vehicleMenu_toolbar.triggered.connect(self.showAddNewVehicleMenuToolbar)
        self.ui.actionShow_existing_vehiclesMenu.triggered.connect(self.showVehicleTable)
        self.ui.actionAdd_new_car_seller.triggered.connect(self.showCarSellerWindowMenu)
        self.ui.actionadd_new_car_seller_toolbar.triggered.connect(self.showCarSellerWindowMenuToolbar)
        self.ui.actionShow_existing_sellersMenu.triggered.connect(self.showSellerTable)
        self.ui.actionAdd_new_custumer_menu.triggered.connect(self.showAddNewCustomer)
        self.ui.actionAdd_new_custumer_toolbar.triggered.connect(self.showAddNewCustomer)
        self.ui.actionShow_existing_custumers_menu.triggered.connect(self.showCostumersTable)
        self.ui.actionDo_business_menu.triggered.connect(self.showDealWindow)
        self.ui.actionDeal_toolbar.triggered.connect(self.showDealWindow)
        self.ui.actionStatistic_staff_per_month_menu.triggered.connect(self.showStatisticPerMonth)
        self.ui.actionstatistic_staff_per_month_toolbar.triggered.connect(self.showStatisticPerMonth)
        self.ui.actionStatistic_staff_per_year.triggered.connect(self.showStatisticPerYear)
        self.ui.actionStatistic_staff_per_year_toolbar.triggered.connect(self.showStatisticPerYear)
        self.ui.actionStatistic_customer_per_year.triggered.connect(self.showCustomerPerYear)
        self.ui.actionStatistic_customer_per_year_toolbar.triggered.connect(self.showCustomerPerYear)
        self.ui.actionMonthly_overview.triggered.connect(self.showMonthlyOverview)
        self.ui.actionMonthly_overview_toolbar.triggered.connect(self.showMonthlyOverview)
        self.ui.actionAnnual_overview.triggered.connect(self.showAnnualOverview)
        self.ui.actionAnnual_overview_toolbar.triggered.connect(self.showAnnualOverview)

    def showAddNewVehicleMenu(self):
        self.ui.showaddnewvehiclewindow = AddNewVehicle()
        self.ui.showaddnewvehiclewindow.show()
        self.close()

    def showAddNewVehicleMenuToolbar(self):
        self.ui.showaddnewvehiclewindowtoolbar = AddNewVehicle()
        self.ui.showaddnewvehiclewindowtoolbar.show()
        self.close()

    def showVehicleTable(self):
        self.ui.showvehicletable = DisplayVehicleTable()
        self.ui.showvehicletable.show()
        self.close()

    def showCarSellerWindowMenu(self):
        self.ui.showcarsellermenu = AddNewCarsSeller()
        self.ui.showcarsellermenu.show()
        self.close()

    def showCarSellerWindowMenuToolbar(self):
        self.ui.showcarsellermenu = AddNewCarsSeller()
        self.ui.showcarsellermenu.show()
        self.close()

    def showSellerTable(self):
        self.ui.showsellertable = ShowSellerView()
        self.ui.showsellertable.show()
        self.close()

    def showAddNewCustomer(self):
        self.ui.showcustomerwindow = AddNewCustumer()
        self.ui.showcustomerwindow.show()
        self.close()

    def showCostumersTable(self):
        self.ui.showcostumerstable = ShowCostumersTable()
        self.ui.showcostumerstable.show()
        self.close()

    def showDealWindow(self):
        self.ui.showdealwindow = Deal()
        self.ui.showdealwindow.show()
        self.close()

    def showStatisticPerMonth(self):
        self.ui.statisticpermonth = StatisticStaffPerMonth()
        self.ui.statisticpermonth.show()
        self.close()

    def showStatisticPerYear(self):
        self.ui.statisticstaffperyear = StatisticStaffPerYear()
        self.ui.statisticstaffperyear.show()
        self.close()

    def showCustomerPerYear(self):
        self.ui.statisticcustomerperyear = StatisticCustomerPerYear()
        self.ui.statisticcustomerperyear.show()
        self.close()

    def showMonthlyOverview(self):
        self.ui.showmonthlyoverview = MonthlyOverview()
        self.ui.showmonthlyoverview.show()
        self.close()

    def showAnnualOverview(self):
        self.ui.showannualoverview = AnnualOverview()
        self.ui.showannualoverview.show()
        self.close()

class AddNewVehicle(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddNewVehicle()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))
        self.ui.label_pictureAddNewVehicle.setPixmap(QPixmap('pictures/label.png'))

        self.ui.pushButton_UploadVehiclePictureAddNewVehicle.clicked.connect(self.uploadVehiclePicture)
        self.ui.pushButton_SubmitAddNewVehicle.clicked.connect(self.addNewVehicle)

    def uploadVehiclePicture(self):
        global replacementPicture
        size = (700,250)

        file,imageFile = QFileDialog.getOpenFileName(self, "Upload Pictures", "C:\\", "Pictures Files(*.jpg *.png)")
        if imageFile:
            replacementPicture = os.path.basename(file)
            picture = Image.open(file)
            picture = picture.resize(size)
            picture.save("pictures/{}".format(replacementPicture))

    def addNewVehicle(self):
        global replacementPicture

        vehicleName = self.ui.lineEditVehicleNameAddNewVehicle.text()
        manufacturer = self.ui.lineEditManufacturerAddNewVehicle.text()
        constructionYear = self.ui.lineEditConnstructionYearAddNewVehicle.text()
        kmStood = self.ui.lineEditKmStoodAddNewVehicle.text()
        vehicleCondition = self.ui.comboBox_VehicleConditionAddNewVehicle.currentText()
        numberOfPieces = self.ui.lineEditNumberOfPiecesAddNewVehicle.text()
        price = self.ui.lineEditPriceAddNewVehicle.text()
        currency = self.ui.comboBox_CurrencyAddNewVehicle.currentText()

        if (vehicleName and manufacturer and constructionYear and kmStood and vehicleCondition and numberOfPieces and price !=''):
            try:
                query = "INSERT INTO vehicle(vehicle_name,manufacturer,construction_year,km_stood,vehicle_condition,pieces,price,curency,picture) VALUES(?,?,?,?,?,?,?,?,?)"
                cur.execute(query,(vehicleName,manufacturer,constructionYear,kmStood,vehicleCondition,numberOfPieces,price,currency,replacementPicture))
                con.commit()
                QMessageBox.information(self,"Info","Vehicle has been added")
                self.close()
                self.mainWindow = MainWindow()
                self.mainWindow.close()
                self.displayvehicles = DisplayVehicleTable()
                self.displayvehicles.show()
            except:
                QMessageBox.warning(self, "Warning", "Vehicle has not been added")
        else:
            QMessageBox.warning(self, "Warning", "Fields can not be empty!")

    def closeEvent(self, event):
        self.ui.mainWindow = MainWindow()
        self.ui.mainWindow.show()

class DisplayVehicleTable(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DisplayVehicleTable()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))
        self.DisplayVehicleTable()

        self.ui.tableWidget_ShowVehicle.setColumnWidth(0, 35)
        self.ui.tableWidget_ShowVehicle.setColumnWidth(1, 340)
        self.ui.tableWidget_ShowVehicle.setColumnWidth(2, 200)
        self.ui.tableWidget_ShowVehicle.setColumnWidth(3, 230)
        self.ui.tableWidget_ShowVehicle.setColumnWidth(4, 150)
        self.ui.tableWidget_ShowVehicle.setColumnWidth(5, 120)
        self.ui.tableWidget_ShowVehicle.setColumnWidth(6, 100)
        self.ui.tableWidget_ShowVehicle.setColumnWidth(7, 140)
        self.ui.tableWidget_ShowVehicle.setColumnWidth(8, 130)
        self.ui.tableWidget_ShowVehicle.setColumnWidth(9, 155)

        self.ui.pushButton_SearchForVehicle.clicked.connect(self.searchForVehicle)
        self.ui.tableWidget_ShowVehicle.doubleClicked.connect(self.showSingleVehicle)
        self.ui.pushButton_ShowVehicles.clicked.connect(self.showVehicles)

    def DisplayVehicleTable(self):
        query = "SELECT vehicle_id, vehicle_name, manufacturer, construction_year, km_stood, vehicle_condition, pieces, price, curency, availability FROM vehicle"
        result = cur.execute(query,)

        for row in result:
            rowNumber = self.ui.tableWidget_ShowVehicle.rowCount()
            self.ui.tableWidget_ShowVehicle.insertRow(rowNumber)
            for columnNumber,data in enumerate(row):
                self.ui.tableWidget_ShowVehicle.setItem(rowNumber,columnNumber,QTableWidgetItem(str(data)))

    def showVehicles(self):
        if self.ui.radioButton_AllVehicles.isChecked() == True:
            self.ui.tableWidget_ShowVehicle.setRowCount(0)
            self.DisplayVehicleTable()
        if self.ui.radioButton_AvailableVehicles.isChecked() == True:
            query = "SELECT vehicle_id, vehicle_name, manufacturer, construction_year, km_stood, vehicle_condition, pieces, price, curency, availability FROM vehicle WHERE availability = 'Available'"
            result = cur.execute(query, )
            self.ui.tableWidget_ShowVehicle.setRowCount(0)
            for row in result:
                rowNumber = self.ui.tableWidget_ShowVehicle.rowCount()
                self.ui.tableWidget_ShowVehicle.insertRow(rowNumber)
                for columnNumber, data in enumerate(row):
                    self.ui.tableWidget_ShowVehicle.setItem(rowNumber, columnNumber, QTableWidgetItem(str(data)))
        if self.ui.radioButton_UnavailableVehicles.isChecked() == True:
            query = "SELECT vehicle_id, vehicle_name, manufacturer, construction_year, km_stood, vehicle_condition, pieces, price, curency, availability FROM vehicle WHERE availability = 'unavailable'"
            result = cur.execute(query, )
            self.ui.tableWidget_ShowVehicle.setRowCount(0)
            for row in result:
                rowNumber = self.ui.tableWidget_ShowVehicle.rowCount()
                self.ui.tableWidget_ShowVehicle.insertRow(rowNumber)
                for columnNumber, data in enumerate(row):
                    self.ui.tableWidget_ShowVehicle.setItem(rowNumber, columnNumber, QTableWidgetItem(str(data)))

    def searchForVehicle(self):
        value = self.ui.lineEdit_SerachForVehicle.text()
        if value == '':
            QMessageBox.warning(self,"warning","Search Box shouldn't be empty!")
        else:
            query = "SELECT vehicle_id, vehicle_name, manufacturer, construction_year, km_stood, vehicle_condition, pieces, " \
                    "price, curency, availability FROM vehicle WHERE vehicle_name LIKE? or manufacturer LIKE?"
            result = cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall()

            if result == []:
                QMessageBox.warning(self, "warning", "Vehicle not found!")
                self.ui.lineEdit_SerachForVehicle.setText("")
                return
            else:
                self.ui.tableWidget_ShowVehicle.setRowCount(0)
                for row in result:
                    rowNumber = self.ui.tableWidget_ShowVehicle.rowCount()
                    self.ui.tableWidget_ShowVehicle.insertRow(rowNumber)
                    for columnNumber, data in enumerate(row):
                        self.ui.tableWidget_ShowVehicle.setItem(rowNumber, columnNumber, QTableWidgetItem(str(data)))

    def showSingleVehicle(self):
        self.ui.showsinglevehicle = SelectSingleVehicle()
        self.ui.showsinglevehicle.show()
        self.close()
        self.ui.mainWindow = MainWindow()
        self.ui.mainWindow.close()

        global vehicleId
        global replacementPicture
        listVehicle = []

        for i in range(0,10):
            listVehicle.append(self.ui.tableWidget_ShowVehicle.item(self.ui.tableWidget_ShowVehicle.currentRow(),i).text())

        vehicleId = listVehicle[0]
        query = "SELECT * FROM vehicle WHERE vehicle_id = ?"
        result = cur.execute(query,(vehicleId,)).fetchone()
        vehicleName = result[1]
        manufacturer = result[2]
        constructionYear = result[3]
        kmStood = result[4]
        vehicleCondition = result[5]
        pieces = result[6]
        price = result[7]
        currency = result[8]
        availability = result[9]
        replacementPicture = result[10]

        self.ui.showsinglevehicle.ui.label_pictureUpdateVehicleData.setPixmap(QPixmap("pictures/{}".format(replacementPicture)))
        self.ui.showsinglevehicle.ui.lineEdit_vehicleNameUpdateVehicle.setText(vehicleName)
        self.ui.showsinglevehicle.ui.lineEdit_manufacturerUpdateVehicle.setText(manufacturer)
        self.ui.showsinglevehicle.ui.lineEdit_constructionYearUpdateVehicle.setText(constructionYear)
        self.ui.showsinglevehicle.ui.lineEdit_kmStoodUpdateVehicle.setText(str(kmStood))
        self.ui.showsinglevehicle.ui.comboBox_vehicleConditionVehicleUpdate.setCurrentText(vehicleCondition)
        self.ui.showsinglevehicle.ui.lineEdit_numberOfPiecesUpdateVehicle.setText(str(pieces))
        self.ui.showsinglevehicle.ui.lineEdit_priceUpdateVehicle.setText(str(price))
        self.ui.showsinglevehicle.ui.comboBox_currencyUpdateVehicle.setCurrentText(currency)
        self.ui.showsinglevehicle.ui.comboBox_availabilityUpdateVehicle.setCurrentText(availability)

    def closeEvent(self, event):
        self.ui.mainWindow = MainWindow()
        self.ui.mainWindow.show()

class SelectSingleVehicle(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SelectSingleVehicle()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))

        self.ui.pushButton_updateVehiclePicture.clicked.connect(self.updateVehiclePicture)
        self.ui.pushButton_updateVehicleData.clicked.connect(self.updateVehicleData)
        self.ui.pushButton_deleteVehicleData.clicked.connect(self.deleteVehicleData)

    def updateVehiclePicture(self):
        self.ui.addnewvehicle = AddNewVehicle()
        self.ui.addnewvehicle.uploadVehiclePicture()

    def updateVehicleData(self):
        global vehicleId
        global replacementPicture

        vehicleName = self.ui.lineEdit_vehicleNameUpdateVehicle.text()
        manufacturer = self.ui.lineEdit_manufacturerUpdateVehicle.text()
        constructionYear = self.ui.lineEdit_constructionYearUpdateVehicle.text()
        kmStood = self.ui.lineEdit_kmStoodUpdateVehicle.text()
        vehicleCondition = self.ui.comboBox_vehicleConditionVehicleUpdate.currentText()
        pieces = self.ui.lineEdit_numberOfPiecesUpdateVehicle.text()
        price = self.ui.lineEdit_priceUpdateVehicle.text()
        currency = self.ui.comboBox_currencyUpdateVehicle.currentText()
        availability = self.ui.comboBox_availabilityUpdateVehicle.currentText()

        if vehicleName and manufacturer and constructionYear and kmStood and vehicleCondition and pieces and price and currency and availability:
            try:
                querry = 'UPDATE vehicle set vehicle_name =?, manufacturer =?, construction_year =?, km_stood =?, vehicle_condition =?, pieces =?, price =?, curency =?, availability =?, picture =? WHERE vehicle_id =?'
                result = cur.execute(querry,(vehicleName,manufacturer,constructionYear,kmStood,vehicleCondition,pieces,price,currency,availability,replacementPicture,vehicleId))
                print(result)
                con.commit()
                QMessageBox.information(self,"Info", "Vehicle data has been updated!")
                self.ui.displayvehicletable = DisplayVehicleTable()
                self.close()
                self.ui.displayvehicletable.show()
            except:
                QMessageBox.warning(self,"Warning", "Vehicle data has not been updated!")
        else:
            QMessageBox.warning(self, "Warning", "Fields can not be empty!")

    def deleteVehicleData(self):
        global vehicleId

        msg = QMessageBox.question(self,'question','Are you sure that you want to delete this vehicle', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if msg == QMessageBox.Yes:
            try:
                query = 'DELETE FROM vehicle WHERE vehicle_id =?'
                cur.execute(query,(vehicleId,))
                con.commit()
                QMessageBox.information(self, "Info", "Vehicle data has been deleted!")
                self.close()
                self.ui.displayvehicletable = DisplayVehicleTable()
                self.ui.displayvehicletable.show()
            except:
                QMessageBox.warning(self, "Warning", "Vehicle data has not been deleted!")

    def closeEvent(self, event):
        self.ui.displayvehicletable = DisplayVehicleTable()
        self.ui.displayvehicletable.show()

class AddNewCarsSeller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddNewCarsSeller()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))

        self.ui.label_pictureAddNewSeller.setPixmap(QPixmap('pictures/new-arrival.png'))
        self.ui.pushButton_uploadSellerPicture.clicked.connect(self.uploadSellerPicture)
        self.ui.pushButton_addNewCarsSeller.clicked.connect(self.addNewCarSeller)

    def uploadSellerPicture(self):
        self.ui.addnewvehicle = AddNewVehicle()
        self.ui.addnewvehicle.uploadVehiclePicture()

    def addNewCarSeller(self):
        global replacementPicture
        name = self.ui.lineEdit_sellerName.text()
        lastname = self.ui.lineEdit_sellerLastname.text()
        phone = self.ui.lineEdit_sellerPhone.text()
        email = self.ui.lineEdit_sellerEmail.text()
        address = self.ui.lineEdit_sellerAddress.text()
        picture = replacementPicture

        if(name and lastname and phone and email and address != ''):
            try:
                query = 'INSERT INTO seller (seller_name, seller_lastname, seller_phone, seller_email, seller_address, seller_picture) VALUES(?,?,?,?,?,?)'
                cur.execute(query,(name,lastname,phone,email,address,picture))
                con.commit()
                QMessageBox.information(self,'Info','Seller has been added')
                self.close()
            except:
                QMessageBox.warning(self,'Warning','Seller has not been added')
        else:
            QMessageBox.warning(self, 'Warning', 'Field can not be empty')

    def closeEvent(self, event):
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.show()

class ShowSellerView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShowSellerView()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))
        self.displaySellerTable()

        self.ui.pushButton_searchSeller.clicked.connect(self.searchForSeller)
        self.ui.pushButton_allSellers.clicked.connect(self.displaySellerTable)
        self.ui.tableWidget_ShowSellerView.doubleClicked.connect(self.showSingleSeller)

        self.ui.tableWidget_ShowSellerView.setColumnWidth(0, 50)
        self.ui.tableWidget_ShowSellerView.setColumnWidth(1, 200)
        self.ui.tableWidget_ShowSellerView.setColumnWidth(2, 200)
        self.ui.tableWidget_ShowSellerView.setColumnWidth(3, 250)
        self.ui.tableWidget_ShowSellerView.setColumnWidth(4, 350)
        self.ui.tableWidget_ShowSellerView.setColumnWidth(5, 560)

    def displaySellerTable(self):
        self.ui.tableWidget_ShowSellerView.setRowCount(0)
        query = "SELECT seller_id, seller_name, seller_lastname, seller_phone, seller_email, seller_address FROM seller"
        result = cur.execute(query,).fetchall()

        for row in result:
            rowNumber = self.ui.tableWidget_ShowSellerView.rowCount()
            self.ui.tableWidget_ShowSellerView.insertRow(rowNumber)
            for columnNum, data in enumerate(row):
                self.ui.tableWidget_ShowSellerView.setItem(rowNumber, columnNum, QTableWidgetItem(str(data)))

    def searchForSeller(self):
        value = self.ui.lineEdit_name.text()
        if value == '':
            QMessageBox.warning(self,'Warning', 'Searched text can not be empty!')
            self.ui.lineEdit_name.setText('')
        else:
            query = "SELECT seller_id, seller_name, seller_lastname, seller_phone, seller_email, seller_address FROM seller WHERE seller_name LIKE? or seller_lastname LIKE?"
            result = cur.execute(query,('%' + value + '%', '%' + value + '%')).fetchall()
            print(result)
            if result == []:
                QMessageBox.warning((self, 'Warning', 'Seller not found'))
                self.ui.lineEdit_name.setText('')
            else:
                self.ui.tableWidget_ShowSellerView.setRowCount(0)
                for row in result:
                    rowNumber = self.ui.tableWidget_ShowSellerView.rowCount()
                    self.ui.tableWidget_ShowSellerView.insertRow(rowNumber)
                    for columnNum, data in enumerate(row):
                        self.ui.tableWidget_ShowSellerView.setItem(rowNumber, columnNum, QTableWidgetItem(str(data)))

    def showSingleSeller(self):
        self.ui.selectsingleseller = SelectSingleSeller()
        self.ui.selectsingleseller.show()
        self.close()
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.close()
        global sellerId
        global replacementPicture
        listSeller = []

        for i in range(0,6):
            listSeller.append(self.ui.tableWidget_ShowSellerView.item(self.ui.tableWidget_ShowSellerView.currentRow(), i).text())
        sellerId = listSeller[0]

        query = "SELECT * FROM seller WHERE seller_id=?"
        result = cur.execute(query,(sellerId,)).fetchone()

        sellername = result[1]
        sellerLastname = result[2]
        sellerPhone = result[3]
        sellerEmail = result[4]
        sellerAddress = result[5]
        replacementPicture = result[6]
        self.ui.selectsingleseller.ui.label_showPicture.setPixmap(QPixmap('pictures/{}'.format(replacementPicture)))
        self.ui.selectsingleseller.ui.lineEdit_name.setText(sellername)
        self.ui.selectsingleseller.ui.lineEdit_lastname.setText(sellerLastname)
        self.ui.selectsingleseller.ui.lineEdit_phone.setText(sellerPhone)
        self.ui.selectsingleseller.ui.lineEdit_email.setText(sellerEmail)
        self.ui.selectsingleseller.ui.lineEdit_address.setText(sellerAddress)

    def closeEvent(self, event):
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.show()

class SelectSingleSeller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SelectSingleSeller()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))

        self.ui.pushButton_addPicture.clicked.connect(self.updateSellerPicture)
        self.ui.pushButton_updateSellerData.clicked.connect(self.updateSellerData)
        self.ui.pushButton_deleteSellerData.clicked.connect(self.deleteSeller)

    def updateSellerPicture(self):
        self.ui.showaddvehicle = AddNewVehicle()
        self.ui.showaddvehicle.uploadVehiclePicture()

    def updateSellerData(self):
        global sellerId
        global replacementPicture

        sellerName = self.ui.lineEdit_name.text()
        sellerLastname = self.ui.lineEdit_lastname.text()
        sellerPhone = self.ui.lineEdit_phone.text()
        sellerEmail = self.ui.lineEdit_email.text()
        sellerAddress = self.ui.lineEdit_address.text()

        if (sellerName and sellerLastname and sellerPhone and sellerEmail and sellerAddress != ''):
            try:
                query = 'UPDATE seller set seller_name =?, seller_lastname =?, seller_phone =?, seller_email =?, seller_address =?, seller_picture =? WHERE seller_id =?'
                cur.execute(query,(sellerName,sellerLastname,sellerPhone,sellerEmail,sellerAddress,replacementPicture,sellerId))
                con.commit()
                QMessageBox.information(self,'info','Seller has been updated')
                self.close()
            except:
                QMessageBox.warning(self,'warning','Seller has not been updated')

        else:
            QMessageBox.warning(self, 'warning', 'Fields can not be empty!')

    def deleteSeller(self):
        global sellerId

        msg = QMessageBox.question(self,'question', 'Are you sure?', QMessageBox.Yes | QMessageBox.No)

        if msg == QMessageBox.Yes:
            try:
                query = 'DELETE FROM seller WHERE seller_id =?'
                cur.execute(query,(sellerId,))
                con.commit()
                QMessageBox.information(self,'info','Seller has been deleted!')
                self.close()
            except:
                QMessageBox.warning(self,'info','Seller has not been deleted!')

    def closeEvent(self, event):
        self.ui.showsellerview = ShowSellerView()
        self.ui.showsellerview.show()

class AddNewCustumer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddNewCustomer()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))
        self.ui.label_picture.setPixmap(QPixmap('pictures/add-user.png'))

        self.ui.pushButton_addCustumer.clicked.connect(self.addNewCustumer)

    def addNewCustumer(self):

        custumerName = self.ui.lineEdit_name.text()
        custumerLastname = self.ui.lineEdit_lastname.text()
        custumerPhone = self.ui.lineEdit_phone.text()
        custumerEmail = self.ui.lineEdit_email.text()
        custumerAddress = self.ui.lineEdit_address.text()

        if (custumerName and custumerLastname and custumerPhone and custumerEmail and custumerAddress != ''):
            try:
                query = 'INSERT INTO custumer (custumer_name, custumer_lastname, custumer_phone, custumer_email, custumer_address) VALUES(?,?,?,?,?)'
                cur.execute(query,(custumerName,custumerLastname,custumerPhone,custumerEmail,custumerAddress))
                con.commit()
                QMessageBox.information(self,'info','Custumer has been added!')
                self.close()
            except:
                QMessageBox.warning(self,'warning','Custumer has not been added!')
        else:
            QMessageBox.warning(self,'warning','Field must not be empty!')

    def closeEvent(self, event):
        self.ui.showcostumertable = ShowCostumersTable()
        self.ui.showcostumertable.show()

class ShowCostumersTable(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShowCostumersTable()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))

        self.displayCustomerTable()

        self.ui.tableWidget.setColumnWidth(0,50)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 200)
        self.ui.tableWidget.setColumnWidth(3, 250)
        self.ui.tableWidget.setColumnWidth(4, 370)
        self.ui.tableWidget.setColumnWidth(5, 550)

        self.ui.pushButton_search.clicked.connect(self.searchForCustumer)
        self.ui.pushButton_show.clicked.connect(self.displayCustomerTable)
        self.ui.tableWidget.doubleClicked.connect(self.showSingleCustumer)

    def displayCustomerTable(self):
        self.ui.tableWidget.setRowCount(0)
        query = 'SELECT * FROM custumer'
        result = cur.execute(query,).fetchall()

        for row in result:
            rowNumber = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowNumber)
            for columnNumber, data in enumerate(row):
                self.ui.tableWidget.setItem(rowNumber,columnNumber,QTableWidgetItem(str(data)))

    def searchForCustumer(self):
        value = self.ui.lineEdit_nameOrLastname.text()

        if value == '':
            QMessageBox.warning(self, 'warning', 'Searched fields can not be empty!')
            self.ui.lineEdit_nameOrLastname.setText('')
        else:
            query = 'SELECT * FROM custumer WHERE custumer_name LIKE? or custumer_lastname LIKE?'
            result = cur.execute(query,('%' + value + '%', '%' + value + '%')).fetchall()
            if result == []:
                QMessageBox.warning(self, 'warning', 'Custumer not found')
                self.ui.lineEdit_nameOrLastname.setText('')
            else:
                self.ui.tableWidget.setRowCount(0)
                for row in result:
                    rowNumber = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(rowNumber)
                    for columnNumber, data in enumerate(row):
                        self.ui.tableWidget.setItem(rowNumber, columnNumber, QTableWidgetItem(str(data)))

    def showSingleCustumer(self):
        self.ui.showsinglecustumer = ShowSingleCustumer()
        self.ui.showsinglecustumer.show()
        self.close()
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.close()

        global customerId
        customerList = []
        for i in range(0,6):
            customerList.append(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),i).text())

        customerId = customerList[0]
        query = 'SELECT * FROM custumer WHERE custumer_id =?'
        result = cur.execute(query,(customerId,)).fetchone()

        self.ui.showsinglecustumer.ui.lineEdit_name.setText(result[1])
        self.ui.showsinglecustumer.ui.lineEdit_lastname.setText(result[2])
        self.ui.showsinglecustumer.ui.lineEdit_phone.setText(result[3])
        self.ui.showsinglecustumer.ui.lineEdit_email.setText(result[4])
        self.ui.showsinglecustumer.ui.lineEdit_address.setText(result[5])
        self.ui.showsinglecustumer.ui.label_picture.setPixmap(QPixmap('pictures/Mann.png'))

    def closeEvent(self, event):
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.show()

class ShowSingleCustumer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShowSingleCustumer()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))

        self.ui.pushButton_updateData.clicked.connect(self.updateCustomerData)
        self.ui.pushButton_DeleteData.clicked.connect(self.deleteCustomerData)

    def updateCustomerData(self):
        global customerId
        name = self.ui.lineEdit_name.text()
        lastname = self.ui.lineEdit_lastname.text()
        phone = self.ui.lineEdit_phone.text()
        email = self.ui.lineEdit_email.text()
        address = self.ui.lineEdit_address.text()

        if(name and lastname and phone and email and address !=''):
            try:
                query = 'UPDATE custumer set custumer_name =?, custumer_lastname =?, custumer_phone =?, custumer_email =?, custumer_address =? WHERE custumer_id =?'
                result = cur.execute(query,(name,lastname,phone,email,address,customerId))
                con.commit()
                QMessageBox.information(self,'info', 'Customer has been updated')
                self.close()
            except:
                QMessageBox.warning(self,'warning', 'Customer has not been updated')
        else:
            QMessageBox.warning(self, 'warning', 'Fields can not be empty!')

    def deleteCustomerData(self):
        global customerId
        msg = QMessageBox.question(self, 'question', 'Are you sure?', QMessageBox.Yes | QMessageBox.No)

        if msg == QMessageBox.Yes:
            try:
                query = 'DELETE FROM custumer WHERE custumer_id =?'
                cur.execute(query,(customerId))
                con.commit()
                QMessageBox.information(self, 'info', 'Customer has been deleted!')
                self.close()
            except:
                QMessageBox.warning(self, 'warning', 'Customer has not been deleted!')

    def closeEvent(self, event):
        self.ui.showcustumertable = ShowCostumersTable()
        self.ui.showcustumertable.show()

class Deal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Deal()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))
        self.ui.label_picture.setPixmap(QPixmap('pictures/deal.png'))

        self.sellCars()
        self.ui.comboBox_sold_vehice.currentIndexChanged.connect(self.updateComboPieces)
        self.ui.pushButton_submit.clicked.connect(self.submit)

    def sellCars(self):
        queryVehicle = 'SELECT * FROM vehicle WHERE availability =?'
        resultqueryVehicle = cur.execute(queryVehicle,('Available',)).fetchall()

        for vehicle in resultqueryVehicle:
            self.ui.comboBox_sold_vehice.addItem(vehicle[1], vehicle[0])

        queryCustomer = 'SELECT custumer_id, custumer_lastname FROM custumer'
        resultqueryCustumer = cur.execute(queryCustomer,).fetchall()

        for customer in resultqueryCustumer:
            self.ui.comboBox_customer_lastname.addItem(customer[1], customer[0])

        querySeller = 'SELECT seller_id, seller_lastname FROM seller'
        resultquerySeller = cur.execute(querySeller,).fetchall()

        for seller in resultquerySeller:
            self.ui.comboBox_seller_lastname.addItem(seller[1], seller[0])

        vehiclePieces = resultqueryVehicle[0][6]
        for i in range(1, vehiclePieces+1):
            self.ui.comboBox_number_of_sold_vehicles.addItem(str(i))

    def updateComboPieces(self):
        hidenVehicleId = self.ui.comboBox_sold_vehice.currentData()
        queryVehiclePieces = 'SELECT pieces FROM vehicle WHERE vehicle_id =?'
        resultqueryVehiclePieces = cur.execute(queryVehiclePieces,(hidenVehicleId,)).fetchone()
        vehicleCount = resultqueryVehiclePieces[0]

        self.ui.comboBox_number_of_sold_vehicles.clear()

        for i in range(1, vehicleCount+1):
            self.ui.comboBox_number_of_sold_vehicles.addItem(str(i))

    def submit(self):
        self.ui.makedeal = MakeDeal()
        self.ui.makedeal.show()
        self.close()
        self.ui.mainwindow.close()

        global vehicleName
        global hiddenVehicleId
        global customerLastName
        global hiddenCustomerId
        global sellerLastName
        global hiddenSellerId
        global numberSoldVehicles
        global dateDay
        global dateMonth
        global dateYear
        global currency
        global amount

        vehicleName = self.ui.comboBox_sold_vehice.currentText()
        hiddenVehicleId = self.ui.comboBox_sold_vehice.currentData()
        customerLastName = self.ui.comboBox_customer_lastname.currentText()
        hiddenCustomerId =  self.ui.comboBox_customer_lastname.currentData()
        sellerLastName = self.ui.comboBox_seller_lastname.currentText()
        hiddenSellerId = self.ui.comboBox_seller_lastname.currentData()
        numberSoldVehicles = self.ui.comboBox_number_of_sold_vehicles.currentText()
        dateDay = self.ui.lineEdit_date_day.text()
        dateMonth = self.ui.lineEdit_date_month.text()
        dateYear = self.ui.lineEdit_date_year.text()

        currencyAndPriceQuery = 'SELECT price, curency FROM vehicle where vehicle_id =?'
        result = cur.execute(currencyAndPriceQuery,(hiddenVehicleId,)).fetchone()

        currency = result[1]
        price = result[0]
        amount = int(numberSoldVehicles) * price

        self.ui.makedeal.ui.label_soldVehicle.setText(vehicleName)
        self.ui.makedeal.ui.label_customer_lastname.setText(customerLastName)
        self.ui.makedeal.ui.label_sellerLastname.setText(sellerLastName)
        self.ui.makedeal.ui.label_numberSoldVehicles.setText(numberSoldVehicles)
        self.ui.makedeal.ui.label_sellerDate.setText(dateDay + '.' + dateMonth + '.' + dateYear)
        self.ui.makedeal.ui.label_price.setText((str(round(amount,2)) + ' ' + currency))

    def closeEvent(self, event):
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.show()

class MakeDeal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MakeDeal()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))
        self.ui.label_picture.setPixmap(QPixmap('pictures/brand-identity.png'))

        self.ui.pushButton_confirm.clicked.connect(self.confirm)

    def confirm(self):
        global vehicleName
        global hiddenVehicleId
        global customerLastName
        global hiddenCustomerId
        global sellerLastName
        global hiddenSellerId
        global numberSoldVehicles
        global dateDay
        global dateMonth
        global dateYear
        global currency
        global amount

        query = 'INSERT INTO deal (sold_vehicle_id, sold_customer_id, sold_seller_id, sold_number_vehicles, sold_day, sold_month, sold_year, amount, currency, seller_name, customer_name) VALUES(?,?,?,?,?,?,?,?,?,?,?)'
        cur.execute(query,(hiddenVehicleId,hiddenCustomerId,hiddenSellerId,numberSoldVehicles,dateDay,dateMonth,dateYear,amount,currency,sellerLastName,customerLastName))
        con.commit()

        queryVehiclePieces = 'SELECT pieces FROM vehicle WHERE vehicle_id =?'
        resultqueryVehiclePieces = cur.execute(queryVehiclePieces,(hiddenVehicleId,)).fetchone()
        vehiclePieces = resultqueryVehiclePieces[0]

        if vehiclePieces > int(numberSoldVehicles):
            newVehiclePieces = vehiclePieces - int(numberSoldVehicles)
            updateQueryPieces = 'UPDATE vehicle set pieces =? WHERE vehicle_id =?'
            cur.execute(updateQueryPieces,(newVehiclePieces,hiddenVehicleId))
            con.commit()
            QMessageBox.information(self,'info','There are still a few of them.')
            self.close()
            self.ui.deal = Deal()
            self.ui.deal.show()
        else:
            querySoldoutVehicles = 'UPDATE vehicle set pieces =?, availability =? WHERE vehicle_id =?'
            cur.execute(querySoldoutVehicles,(0, 'unavailable', hiddenVehicleId))
            con.commit()
            QMessageBox.information(self, 'info', 'Lat vehicle of the brand is sold.')
            self.close()
            self.ui.deal = Deal()
            self.ui.deal.show()

    def closeEvent(self, event):
        self.ui.deal = Deal()
        self.ui.deal.show()

class StatisticStaffPerMonth(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StatisticStaffPerMonth()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))

        self.ui.pushButton_show.clicked.connect(self.showOverviewSellerPerMonth)

    def showOverviewSellerPerMonth(self):
        valueMonth = self.ui.lineEdit_month.text()
        valueYear = self.ui.lineEdit_year.text()
        valueSellerLastName = self.ui.lineEdit_sellerLastname.text()

        if valueMonth == '' or valueYear == '' or valueSellerLastName == '':
            QMessageBox.warning(self, 'Warning', 'Search fields can not be empty!')
            self.ui.lineEdit_month.setText('')
            self.ui.lineEdit_year.setText('')
            self.ui.lineEdit_sellerLastname.setText('')

        else:
            valueMonthResult = '%' + valueMonth + '%'
            valueYearResult = '%' + valueYear + '%'
            valueSellerLastNameResult = '%' + valueSellerLastName + '%'

            query = 'SELECT * FROM deal WHERE sold_month LIKE? and sold_year LIKE? and seller_name LIKE?'
            result = cur.execute(query,(valueMonthResult, valueYearResult, valueSellerLastNameResult)).fetchall()

            if result == []:
                QMessageBox.warning(self, 'Warning', 'Some of the data not found!')
                self.ui.lineEdit_month.setText('')
                self.ui.lineEdit_year.setText('')
                self.ui.lineEdit_sellerLastname.setText('')
            else:
                querySum = 'SELECT SUM(sold_number_vehicles), SUM(amount) FROM deal WHERE sold_month LIKE? and sold_year LIKE? and seller_name LIKE?'
                resultQuerySum = cur.execute(querySum,(valueMonthResult, valueYearResult, valueSellerLastNameResult)).fetchall()
                soldVehicleSum = resultQuerySum[0][0]
                sumAmount = resultQuerySum[0][1]

                self.ui.label_sellerLastname.setText(result[0][10])
                self.ui.label_sellMonthYear.setText(result[0][6] + '.' + result[0][7])
                self.ui.label_numberOfSoldCars.setText(str(soldVehicleSum))
                self.ui.label_totalSales.setText(str(sumAmount) + ' ' + result[0][9])

                list_day = []
                list_amount_day = []

                for i in result:
                    day = i[5]
                    amount = i[8]
                    list_day.append(day)
                    list_amount_day.append(amount)

                plt.plot(list_day, list_amount_day, label='overview seller per month')
                plt.legend()
                plt.xlabel('days/month', color='red')
                plt.ylabel('amount', color='red')
                plt.show()

    def closeEvent(self, event):
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.show()

class StatisticStaffPerYear(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StatisticStaffPerYear()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))

        self.ui.pushButton_show.clicked.connect(self.showOverviewSellerPerYear)

    def showOverviewSellerPerYear(self):
        valueYear = self.ui.lineEdit_year.text()
        valueSellerLastName = self.ui.lineEdit_sellerLastname.text()

        if valueYear == '' or valueSellerLastName == '':
            QMessageBox.warning(self, 'Warning', 'Search fields can not be empty!')
            self.ui.lineEdit_year.setText('')
            self.ui.lineEdit_sellerLastname.setText('')

        else:
            valueYearResult = '%' + valueYear + '%'
            valueSellerLastNameResult = '%' + valueSellerLastName + '%'

            query = 'SELECT * FROM deal WHERE sold_year LIKE? and seller_name LIKE?'
            result = cur.execute(query, (valueYearResult, valueSellerLastNameResult)).fetchall()

            if result == []:
                QMessageBox.warning(self, 'Warning', 'Some of the data not found!')
                self.ui.lineEdit_year.setText('')
                self.ui.lineEdit_sellerLastname.setText('')
            else:
                querySum = 'SELECT SUM(sold_number_vehicles), SUM(amount) FROM deal WHERE sold_year LIKE? and seller_name LIKE?'
                resultQuerySum = cur.execute(querySum, (valueYearResult, valueSellerLastNameResult)).fetchall()
                soldVehicleSum = resultQuerySum[0][0]
                sumAmount = resultQuerySum[0][1]

                self.ui.label_sellerLastname.setText(result[0][10])
                self.ui.label_sellYear.setText(result[0][6] + '.' + result[0][7])
                self.ui.label_numberOfSoldCars.setText(str(soldVehicleSum))
                self.ui.label_totalSales.setText(str(sumAmount) + ' ' + result[0][9])

    def closeEvent(self, event):
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.show()

class StatisticCustomerPerYear(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StatisticCustomerPerYear()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))

        self.ui.pushButton_show.clicked.connect(self.showStatisticCustomer)

    def showStatisticCustomer(self):
        valueYear = self.ui.lineEdit_year.text()
        valueCustomerLastName = self.ui.lineEdit_customerLastname.text()

        if valueYear == '' or valueCustomerLastName == '':
            QMessageBox.warning(self, 'Warning', 'Search fields can not be empty!')
            self.ui.lineEdit_year.setText('')
            self.ui.lineEdit_customerLastname.setText('')

        else:
            valueYearResult = '%' + valueYear + '%'
            valueCustomerLastNameResult = '%' + valueCustomerLastName + '%'

            query = 'SELECT * FROM deal WHERE sold_year LIKE? and customer_name LIKE?'
            result = cur.execute(query, (valueYearResult, valueCustomerLastNameResult)).fetchall()

            if result == []:
                QMessageBox.warning(self, 'Warning', 'Some of the data not found!')
                self.ui.lineEdit_year.setText('')
                self.ui.lineEdit_customerLastname.setText('')
            else:
                querySum = 'SELECT SUM(sold_number_vehicles), SUM(amount) FROM deal WHERE sold_year LIKE? and customer_name LIKE?'
                resultQuerySum = cur.execute(querySum, (valueYearResult, valueCustomerLastNameResult)).fetchall()
                soldVehicleSum = resultQuerySum[0][0]
                sumAmount = resultQuerySum[0][1]

                self.ui.label_customerLastname.setText(result[0][10])
                self.ui.label_sellYear.setText(result[0][6] + '.' + result[0][7])
                self.ui.label_numberOfSoldCars.setText(str(soldVehicleSum))
                self.ui.label_totalSales.setText(str(sumAmount) + ' ' + result[0][9])

    def closeEvent(self, event):
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.show()

class MonthlyOverview(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MonthlyOverview()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))
        self.ui.pushButton_show.clicked.connect(self.showMonthlyOverviewTable)

    def showMonthlyOverviewTable(self):
        valueMonth = self.ui.lineEdit_month.text()
        valueYear = self.ui.lineEdit_year.text()

        if valueMonth == '' or valueYear == '':
            QMessageBox.warning(self, 'Warning', 'Search fields can not be empty!')
            self.ui.lineEdit_month.setText('')
            self.ui.lineEdit_year.setText('')

        else:
            valueMonthResult = '%' + valueMonth + '%'
            valueYearResult = '%' + valueYear + '%'

            query = 'SELECT * FROM deal WHERE sold_month LIKE? and sold_year LIKE?'
            result = cur.execute(query,(valueMonthResult, valueYearResult)).fetchall()

            if result == []:
                QMessageBox.warning(self, 'Warning', 'Some of the data not found!')
                self.ui.lineEdit_month.setText('')
                self.ui.lineEdit_year.setText('')
            else:
                querySum = 'SELECT SUM(sold_number_vehicles), SUM(amount) FROM deal WHERE sold_month LIKE? and sold_year LIKE?'
                resultQuerySum = cur.execute(querySum,(valueMonthResult, valueYearResult)).fetchall()
                soldVehicleSum = resultQuerySum[0][0]
                sumAmount = resultQuerySum[0][1]

                self.ui.label_sellMonthYear.setText(result[0][6] + '.' + result[0][7])
                self.ui.label_numberOfSoldCars.setText(str(soldVehicleSum))
                self.ui.label_totalSales.setText(str(sumAmount) + ' ' + result[0][9])

    def closeEvent(self, event):
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.show()

class AnnualOverview(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AnnualOverview()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/deal.png'))
        self.ui.pushButton_show.clicked.connect(self.showAnnualOverviewTable)

    def showAnnualOverviewTable(self):
        valueYear = self.ui.lineEdit_year.text()

        if valueYear == '':
            QMessageBox.warning(self, 'Warning', 'Search fields can not be empty!')
            self.ui.lineEdit_year.setText('')

        else:
            valueYearResult = '%' + valueYear + '%'

            query = 'SELECT * FROM deal WHERE sold_year LIKE?'
            result = cur.execute(query, (valueYearResult,)).fetchall()

            if result == []:
                QMessageBox.warning(self, 'Warning', 'Some of the data not found!')
                self.ui.lineEdit_year.setText('')
            else:
                querySum = 'SELECT SUM(sold_number_vehicles), SUM(amount) FROM deal WHERE sold_year LIKE?'
                resultQuerySum = cur.execute(querySum, (valueYearResult,)).fetchall()
                soldVehicleSum = resultQuerySum[0][0]
                sumAmount = resultQuerySum[0][1]

                self.ui.label_sellYear.setText(result[0][7])
                self.ui.label_numberOfSoldCars.setText(str(soldVehicleSum))
                self.ui.label_totalSales.setText(str(sumAmount) + ' ' + result[0][9])

    def closeEvent(self, event):
        self.ui.mainwindow = MainWindow()
        self.ui.mainwindow.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())