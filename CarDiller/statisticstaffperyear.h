#ifndef STATISTICSTAFFPERYEAR_H
#define STATISTICSTAFFPERYEAR_H

#include <QMainWindow>

namespace Ui {
class StatisticStaffPerYear;
}

class StatisticStaffPerYear : public QMainWindow
{
    Q_OBJECT

public:
    explicit StatisticStaffPerYear(QWidget *parent = nullptr);
    ~StatisticStaffPerYear();

private:
    Ui::StatisticStaffPerYear *ui;
};

#endif // STATISTICSTAFFPERYEAR_H
