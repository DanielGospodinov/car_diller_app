#ifndef SELECTSINGLEVEHICLE_H
#define SELECTSINGLEVEHICLE_H

#include <QMainWindow>

namespace Ui {
class SelectSingleVehicle;
}

class SelectSingleVehicle : public QMainWindow
{
    Q_OBJECT

public:
    explicit SelectSingleVehicle(QWidget *parent = nullptr);
    ~SelectSingleVehicle();

private:
    Ui::SelectSingleVehicle *ui;
};

#endif // SELECTSINGLEVEHICLE_H
