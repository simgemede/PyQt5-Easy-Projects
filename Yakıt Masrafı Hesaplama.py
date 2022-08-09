from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yakıt Masrafı Hesaplama")

        self.label_km = QLabel("Gidilen Yol",self)
        self.label_ortalama = QLabel("Ortalama Yakıt Tüketimi",self)
        self.label_fiyat = QLabel("Yakıt Ücreti",self)
        self.label_sonuc = QLabel("Sonuç                                   ",self)

        self.label_km.move(20,20)
        self.label_ortalama.move(20,60)
        self.label_fiyat.move(20,100)
        self.label_sonuc.move(20,180)

        self.lineEdit_km = QLineEdit(self)
        self.lineEdit_ortalama = QLineEdit(self)
        self.lineEdit_fiyat = QLineEdit(self)

        self.lineEdit_km.move(180,20)
        self.lineEdit_ortalama.move(180,60)
        self.lineEdit_fiyat.move(180,100)

        self.buton = QPushButton("Hesapla",self)
        self.buton.move(200,140)

        self.buton.clicked.connect(self.fonk)

    def fonk(self):
            self.line_liste = [self.lineEdit_km,self.lineEdit_ortalama,self.lineEdit_fiyat]

            for i in self.line_liste:
                if i.text() != "":
                    if i.text().isnumeric():
                        pass
                    else:
                        self.label_sonuc.setText("Sayısal karakter girin")
                else:
                    self.label_sonuc.setText("Alanları boş bırakmayın")
            else:
                sonuc = float(self.lineEdit_km.text())*float(self.lineEdit_ortalama.text())*float(self.lineEdit_fiyat.text())/100
                self.label_sonuc.setText("%0.2f" % sonuc)

app = QApplication([])
pencere = main()
pencere.resize(350,250)
pencere.show()
app.exec()