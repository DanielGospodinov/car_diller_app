#include "addnewcarsseller.h"
#include "ui_addnewcarsseller.h"

AddNewCarsSeller::AddNewCarsSeller(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::AddNewCarsSeller)
{
    ui->setupUi(this);
}

AddNewCarsSeller::~AddNewCarsSeller()
{
    delete ui;
}
