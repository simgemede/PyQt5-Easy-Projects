from PyQt5.QtWidgets import *

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.label_isim = QLabel("İsim",self)
        self.label_soyisim = QLabel("Soyisim", self)
        self.label_yas = QLabel("Yaş", self)
        self.label_cinsiyet = QLabel("Cinsiyet", self)
        self.label_telefon = QLabel("Telefon Numarası", self)
        self.label_email = QLabel("E-mail", self)
        self.label_boy = QLabel("Boy", self)
        self.label_kilo = QLabel("Kilo", self)
        self.label_kan_grubu = QLabel("Kan Grubu", self)

        self.label_isim.move(20, 20)
        self.label_soyisim.move(250, 20)
        self.label_yas.move(20, 100)
        self.label_cinsiyet.move(20, 180)
        self.label_telefon.move(20, 260)
        self.label_email.move(20, 340)
        self.label_boy.move(20, 420)
        self.label_kilo.move(180, 420)
        self.label_kan_grubu.move(350, 420)

        self.line_isim = QLineEdit(self)
        self.line_soyisim = QLineEdit(self)
        self.line_yas = QLineEdit(self)
        self.line_telefon = QLineEdit(self)
        self.line_email = QLineEdit(self)
        self.line_boy = QLineEdit(self)
        self.line_kilo = QLineEdit(self)

        self.line_boy.setMaxLength(3)
        self.line_kilo.setMaxLength(3)

        self.line_isim.move(20, 40)
        self.line_soyisim.move(250, 40)
        self.line_yas.move(20, 120)
        self.line_telefon.move(20, 280)
        self.line_email.move(20, 360)
        self.line_boy.move(20, 440)
        self.line_kilo.move(180, 440)

        self.radiobutton1 = QRadioButton("Erkek",self)
        self.radiobutton2 = QRadioButton("Kadın", self)
        self.radiobutton1.move(20, 210)
        self.radiobutton2.move(100, 210)

        self.combobox = QComboBox(self)
        self.combobox.addItems(["Seçin","A+", "A-", "B+", "B-", "0+", "0-", "AB+", "AB-"])
        self.combobox.move(350, 440)

        self.buton1 = QPushButton("Kaydet", self)
        self.buton2 = QPushButton("Sil", self)
        self.buton3 = QPushButton("Çıkış", self)

        self.buton1.move(100, 500)
        self.buton2.move(200, 500)
        self.buton3.move(300, 500)

        self.buton3.clicked.connect(self.close)
        self.buton2.clicked.connect(self.reset)

    def reset(self):
        self.line_isim.setText("")
        self.line_soyisim.setText("")
        self.line_yas.setText("")
        self.line_telefon.setText("")
        self.line_email.setText("")
        self.line_boy.setText("")
        self.line_kilo.setText("")

app = QApplication([])
pencere = main()
pencere.show()
pencere.resize(450, 550)
app.exec()
