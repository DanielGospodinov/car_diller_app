#ifndef SHOWCOSTUMERSTABLE_H
#define SHOWCOSTUMERSTABLE_H

#include <QMainWindow>

namespace Ui {
class ShowCostumersTable;
}

class ShowCostumersTable : public QMainWindow
{
    Q_OBJECT

public:
    explicit ShowCostumersTable(QWidget *parent = nullptr);
    ~ShowCostumersTable();

private:
    Ui::ShowCostumersTable *ui;
};

#endif // SHOWCOSTUMERSTABLE_H
