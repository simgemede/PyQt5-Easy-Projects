from PyQt5.QtWidgets import *

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.hbox = QHBoxLayout(self)
        self.hbox.setContentsMargins(0,0,0,0)
        self.tab_widget = QTabWidget()
        self.hbox.addWidget(self.tab_widget)

        self.tab_widget.addTab(QWidget(), "Sekme1")
        self.tab_widget.addTab(QWidget(), "Sekme2")
        self.tab_widget.addTab(QWidget(), "Sekme3")

        self.tab_widget.setTabsClosable(True)

        self.tab_widget.tabCloseRequested.connect(self.tab_kapa)

        self.tbutton = QToolButton(self.tab_widget)
        self.tbutton.setText("+")
        w = self.tab_widget.tabBar().sizeHint().width()
        self.tbutton.move(w+10,5)
        self.tbutton.clicked.connect(self.tab_ekle)

        self.tbutton.setStyleSheet("QToolButton{border:none; height : 25px; width: 25px")

        self.resize(800,500)
        self.show()

    def tab_kapa(self,i):
        self.tab_widget.removeTab(i)
        w = self.tab_widget.tabBar().sizeHint().width()
        self.tbutton.move(w+10,5)

    def tab_ekle(self):
        self.tab_widget.addTab(QWidget(),"Yeni Sekme")
        w = self.tab_widget.tabBar().sizeHint().width()
        self.tbutton.move(w+10,5)

app = QApplication([])
pencere = main()
app.exec()
