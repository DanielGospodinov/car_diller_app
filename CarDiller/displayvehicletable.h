#ifndef DISPLAYVEHICLETABLE_H
#define DISPLAYVEHICLETABLE_H

#include <QMainWindow>

namespace Ui {
class DisplayVehicleTable;
}

class DisplayVehicleTable : public QMainWindow
{
    Q_OBJECT

public:
    explicit DisplayVehicleTable(QWidget *parent = nullptr);
    ~DisplayVehicleTable();

private:
    Ui::DisplayVehicleTable *ui;
};

#endif // DISPLAYVEHICLETABLE_H
