#include "showsellerview.h"
#include "ui_showsellerview.h"

ShowSellerView::ShowSellerView(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ShowSellerView)
{
    ui->setupUi(this);
}

ShowSellerView::~ShowSellerView()
{
    delete ui;
}
