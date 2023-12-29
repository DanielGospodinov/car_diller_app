#include "showcostumerstable.h"
#include "ui_showcostumerstable.h"

ShowCostumersTable::ShowCostumersTable(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ShowCostumersTable)
{
    ui->setupUi(this);
}

ShowCostumersTable::~ShowCostumersTable()
{
    delete ui;
}
