#include "displayvehicletable.h"
#include "ui_displayvehicletable.h"

DisplayVehicleTable::DisplayVehicleTable(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::DisplayVehicleTable)
{
    ui->setupUi(this);
}

DisplayVehicleTable::~DisplayVehicleTable()
{
    delete ui;
}
