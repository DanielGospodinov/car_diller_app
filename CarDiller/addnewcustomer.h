#ifndef ADDNEWCUSTOMER_H
#define ADDNEWCUSTOMER_H

#include <QMainWindow>

namespace Ui {
class AddNewCustomer;
}

class AddNewCustomer : public QMainWindow
{
    Q_OBJECT

public:
    explicit AddNewCustomer(QWidget *parent = nullptr);
    ~AddNewCustomer();

private:
    Ui::AddNewCustomer *ui;
};

#endif // ADDNEWCUSTOMER_H
