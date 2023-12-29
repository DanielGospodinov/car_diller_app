#include "selectsinglevehicle.h"
#include "ui_selectsinglevehicle.h"

SelectSingleVehicle::SelectSingleVehicle(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::SelectSingleVehicle)
{
    ui->setupUi(this);
}

SelectSingleVehicle::~SelectSingleVehicle()
{
    delete ui;
}
