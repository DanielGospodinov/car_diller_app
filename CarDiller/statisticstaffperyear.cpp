#include "statisticstaffperyear.h"
#include "ui_statisticstaffperyear.h"

StatisticStaffPerYear::StatisticStaffPerYear(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::StatisticStaffPerYear)
{
    ui->setupUi(this);
}

StatisticStaffPerYear::~StatisticStaffPerYear()
{
    delete ui;
}
