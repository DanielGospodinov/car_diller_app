#ifndef SELECTSINGLESELLER_H
#define SELECTSINGLESELLER_H

#include <QMainWindow>

namespace Ui {
class SelectSingleSeller;
}

class SelectSingleSeller : public QMainWindow
{
    Q_OBJECT

public:
    explicit SelectSingleSeller(QWidget *parent = nullptr);
    ~SelectSingleSeller();

private:
    Ui::SelectSingleSeller *ui;
};

#endif // SELECTSINGLESELLER_H
