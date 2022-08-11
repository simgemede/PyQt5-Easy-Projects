from PyQt5.QtWidgets import *

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.label_kullanici = QLabel("Kullanıcı Adı",self)
        self.label_parola = QLabel("Parola",self)

        self.label_kullanici.move(20,20)
        self.label_parola.move(20,60)

        self.lineedit_kullanici = QLineEdit(self)
        self.lineedit_parola = QLineEdit(self)

        self.lineedit_kullanici.move(120,20)
        self.lineedit_parola.move(120,60)

        self.buton_giris = QPushButton("Giriş",self)
        self.buton_iptal = QPushButton("İptal",self)

        self.buton_giris.move(80,100)
        self.buton_iptal.move(190,100)

        self.buton_giris.clicked.connect(self.giris)
        self.buton_iptal.clicked.connect(self.iptal)

    def iptal(self):
        self.close()

    def giris(self):
        if self.lineedit_kullanici.text() == "Simge" and self.lineedit_parola.text() == "simge1234":
           self.setStyleSheet("background-color:green")
        else:
            self.setStyleSheet("background-color:red")

        self.resize(300,150)

app = QApplication([])
pencere = main()
pencere.show()
app.exec()
