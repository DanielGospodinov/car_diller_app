#ifndef SHOWSELLERVIEW_H
#define SHOWSELLERVIEW_H

#include <QMainWindow>

namespace Ui {
class ShowSellerView;
}

class ShowSellerView : public QMainWindow
{
    Q_OBJECT

public:
    explicit ShowSellerView(QWidget *parent = nullptr);
    ~ShowSellerView();

private:
    Ui::ShowSellerView *ui;
};

#endif // SHOWSELLERVIEW_H
