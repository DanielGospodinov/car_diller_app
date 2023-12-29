#ifndef SHOWSINGLECUSTUMER_H
#define SHOWSINGLECUSTUMER_H

#include <QMainWindow>

namespace Ui {
class ShowSingleCustumer;
}

class ShowSingleCustumer : public QMainWindow
{
    Q_OBJECT

public:
    explicit ShowSingleCustumer(QWidget *parent = nullptr);
    ~ShowSingleCustumer();

private:
    Ui::ShowSingleCustumer *ui;
};

#endif // SHOWSINGLECUSTUMER_H
