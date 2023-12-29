#ifndef ADDNEWCARSSELLER_H
#define ADDNEWCARSSELLER_H

#include <QMainWindow>

namespace Ui {
class AddNewCarsSeller;
}

class AddNewCarsSeller : public QMainWindow
{
    Q_OBJECT

public:
    explicit AddNewCarsSeller(QWidget *parent = nullptr);
    ~AddNewCarsSeller();

private:
    Ui::AddNewCarsSeller *ui;
};

#endif // ADDNEWCARSSELLER_H
