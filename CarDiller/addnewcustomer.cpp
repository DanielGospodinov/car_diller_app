#include "addnewcustomer.h"
#include "ui_addnewcustomer.h"

AddNewCustomer::AddNewCustomer(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::AddNewCustomer)
{
    ui->setupUi(this);
}

AddNewCustomer::~AddNewCustomer()
{
    delete ui;
}
