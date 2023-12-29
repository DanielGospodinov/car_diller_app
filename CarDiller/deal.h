#ifndef DEAL_H
#define DEAL_H

#include <QMainWindow>

namespace Ui {
class Deal;
}

class Deal : public QMainWindow
{
    Q_OBJECT

public:
    explicit Deal(QWidget *parent = nullptr);
    ~Deal();

private:
    Ui::Deal *ui;
};

#endif // DEAL_H
