#include "showsinglecustumer.h"
#include "ui_showsinglecustumer.h"

ShowSingleCustumer::ShowSingleCustumer(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ShowSingleCustumer)
{
    ui->setupUi(this);
}

ShowSingleCustumer::~ShowSingleCustumer()
{
    delete ui;
}
