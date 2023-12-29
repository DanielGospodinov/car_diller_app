#include "monthlyoverview.h"
#include "ui_monthlyoverview.h"

MonthlyOverview::MonthlyOverview(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MonthlyOverview)
{
    ui->setupUi(this);
}

MonthlyOverview::~MonthlyOverview()
{
    delete ui;
}
