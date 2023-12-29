#include "addnewvehicle.h"
#include "ui_addnewvehicle.h"

AddNewVehicle::AddNewVehicle(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::AddNewVehicle)
{
    ui->setupUi(this);
}

AddNewVehicle::~AddNewVehicle()
{
    delete ui;
}
