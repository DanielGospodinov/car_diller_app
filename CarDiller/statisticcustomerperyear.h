#ifndef STATISTICCUSTOMERPERYEAR_H
#define STATISTICCUSTOMERPERYEAR_H

#include <QMainWindow>

namespace Ui {
class StatisticCustomerPerYear;
}

class StatisticCustomerPerYear : public QMainWindow
{
    Q_OBJECT

public:
    explicit StatisticCustomerPerYear(QWidget *parent = nullptr);
    ~StatisticCustomerPerYear();

private:
    Ui::StatisticCustomerPerYear *ui;
};

#endif // STATISTICCUSTOMERPERYEAR_H
