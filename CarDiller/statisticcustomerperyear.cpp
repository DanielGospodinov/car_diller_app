#include "statisticcustomerperyear.h"
#include "ui_statisticcustomerperyear.h"

StatisticCustomerPerYear::StatisticCustomerPerYear(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::StatisticCustomerPerYear)
{
    ui->setupUi(this);
}

StatisticCustomerPerYear::~StatisticCustomerPerYear()
{
    delete ui;
}
