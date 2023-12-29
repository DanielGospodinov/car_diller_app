#ifndef ADDNEWVEHICLE_H
#define ADDNEWVEHICLE_H

#include <QMainWindow>

namespace Ui {
class AddNewVehicle;
}

class AddNewVehicle : public QMainWindow
{
    Q_OBJECT

public:
    explicit AddNewVehicle(QWidget *parent = nullptr);
    ~AddNewVehicle();

private:
    Ui::AddNewVehicle *ui;
};

#endif // ADDNEWVEHICLE_H
