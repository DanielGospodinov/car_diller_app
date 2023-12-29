#ifndef ANNUALOVERVIEW_H
#define ANNUALOVERVIEW_H

#include <QMainWindow>

namespace Ui {
class AnnualOverview;
}

class AnnualOverview : public QMainWindow
{
    Q_OBJECT

public:
    explicit AnnualOverview(QWidget *parent = nullptr);
    ~AnnualOverview();

private:
    Ui::AnnualOverview *ui;
};

#endif // ANNUALOVERVIEW_H
