#include "annualoverview.h"
#include "ui_annualoverview.h"

AnnualOverview::AnnualOverview(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::AnnualOverview)
{
    ui->setupUi(this);
}

AnnualOverview::~AnnualOverview()
{
    delete ui;
}
