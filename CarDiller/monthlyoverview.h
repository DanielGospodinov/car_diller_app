#ifndef MONTHLYOVERVIEW_H
#define MONTHLYOVERVIEW_H

#include <QMainWindow>

namespace Ui {
class MonthlyOverview;
}

class MonthlyOverview : public QMainWindow
{
    Q_OBJECT

public:
    explicit MonthlyOverview(QWidget *parent = nullptr);
    ~MonthlyOverview();

private:
    Ui::MonthlyOverview *ui;
};

#endif // MONTHLYOVERVIEW_H
