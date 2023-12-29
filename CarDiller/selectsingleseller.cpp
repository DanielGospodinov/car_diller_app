#include "selectsingleseller.h"
#include "ui_selectsingleseller.h"

SelectSingleSeller::SelectSingleSeller(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::SelectSingleSeller)
{
    ui->setupUi(this);
}

SelectSingleSeller::~SelectSingleSeller()
{
    delete ui;
}
