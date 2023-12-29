#ifndef STATISTICSTAFFPERMONTH_H
#define STATISTICSTAFFPERMONTH_H

#include <QMainWindow>

namespace Ui {
class StatisticStaffPerMonth;
}

class StatisticStaffPerMonth : public QMainWindow
{
    Q_OBJECT

public:
    explicit StatisticStaffPerMonth(QWidget *parent = nullptr);
    ~StatisticStaffPerMonth();

private:
    Ui::StatisticStaffPerMonth *ui;
};

#endif // STATISTICSTAFFPERMONTH_H
