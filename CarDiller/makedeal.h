#ifndef MAKEDEAL_H
#define MAKEDEAL_H

#include <QMainWindow>

namespace Ui {
class MakeDeal;
}

class MakeDeal : public QMainWindow
{
    Q_OBJECT

public:
    explicit MakeDeal(QWidget *parent = nullptr);
    ~MakeDeal();

private:
    Ui::MakeDeal *ui;
};

#endif // MAKEDEAL_H
