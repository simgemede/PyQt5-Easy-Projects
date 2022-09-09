from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random

kazanan = [("Taş","Makas"),("Kağıt","Taş"),("Makas","Kağıt")]
kaybeden = [("Taş","Kağıt"),("Kağıt","Makas"),("Makas","Taş")]

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout(self)

        self.hbox = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.tbutton = QToolButton()
        self.tbutton1 = QToolButton()
        self.tbutton2 = QToolButton()

        self.tbutton.setText("Taş")
        self.tbutton1.setText("Kağıt")
        self.tbutton2.setText("Makas")

        self.hbox.addWidget(self.tbutton)
        self.hbox.addWidget(self.tbutton1)
        self.hbox.addWidget(self.tbutton2)

        self.label_pc = QLabel("Bilgisayar")
        self.label_pc.setAlignment(Qt.AlignCenter)
        self.label_secim = QLabel("Seçim")
        self.label_secim.setAlignment(Qt.AlignCenter)

        self.hbox1.addWidget(self.label_pc)
        self.hbox1.addWidget(self.label_secim)

        self.label_sonuc = QLabel("Sonuç")
        self.label_sonuc.setAlignment(Qt.AlignCenter)

        self.score = QLabel("0")
        self.score1 = QLabel("0")
        self.score.setFrameShape(QFrame.Box)
        self.score1.setFrameShape(QFrame.Box)

        self.hbox2.addWidget(self.score)
        self.hbox2.addWidget(self.score1)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addWidget(self.label_sonuc)
        self.vbox.addLayout(self.hbox2)

        self.resize(350,250)

        self.tbutton.clicked.connect(lambda: self.sec("Taş"))
        self.tbutton1.clicked.connect(lambda: self.sec("Kağıt"))
        self.tbutton2.clicked.connect(lambda: self.sec("Makas"))

    def sec(self,choose):
        random_pc = random.choice(["Taş","Kağıt","Makas"])
        choose_tuple = (choose,random_pc)

        if choose_tuple in kazanan:
            self.label_sonuc.setText("Kazandınız")
            self.score.setText(str(int(self.score.text())+1))
        elif choose_tuple in kaybeden:
            self.label_sonuc.setText("Kaybettiniz")
            self.score1.setText(str(int(self.score1.text()) + 1))
        else:
            self.label_sonuc.setText("Berabere")

app = QApplication([])
pencere = main()
pencere.show()
app.exec()
