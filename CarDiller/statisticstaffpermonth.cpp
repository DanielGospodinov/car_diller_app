#include "statisticstaffpermonth.h"
#include "ui_statisticstaffpermonth.h"

StatisticStaffPerMonth::StatisticStaffPerMonth(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::StatisticStaffPerMonth)
{
    ui->setupUi(this);
}

StatisticStaffPerMonth::~StatisticStaffPerMonth()
{
    delete ui;
}
