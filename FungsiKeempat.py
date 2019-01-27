from PyQt4.QtGui import QDesktopWidget

from ui import Keempat, FungsiKelima

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPixmap

import random

class MyQtApp(Keempat.Ui_MainWindow4, QtGui.QMainWindow):
    def position(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(x, y)

    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setup4(self)
        # self.showMaximized()
        self.setWindowTitle("Proses Digital Signature")
        self.btn_ok.clicked.connect(self.select_nilaixk)
        self.btn_next.clicked.connect(self.next)

        button = self.btn_next
        button.setIcon(QtGui.QIcon("images/next-arrow.png"))
        button.setIconSize(QtCore.QSize(35, 35))

        label = self.label_pic
        label2 = self.label_pic_2
        label3 = self.label_pic_3
        label4 = self.label_pic_4
        label5 = self.label_pic_5
        label6 = self.label_pic_6
        label7 = self.label_pic_7

        image = QPixmap("images/down-arrow.png")
        label.setPixmap(image.scaled(25, 25))
        label2.setPixmap(image.scaled(25, 25))
        label3.setPixmap(image.scaled(25, 25))
        label4.setPixmap(image.scaled(25, 25))
        label5.setPixmap(image.scaled(25, 25))
        label6.setPixmap(image.scaled(25, 25))
        label7.setPixmap(image.scaled(25, 25))

        label_fungsi = self.label_hash
        label_fungsi.setText(open('output/fungsihash.txt', 'r').read())

        label_nilai = self.label_nilaihash
        label_nilai.setText("H(M)")

        label_nilaiprima = self.label_nilaip
        label_nilaiprima.setText("p = " +open('output/nilaip.txt', 'r').read()[0:3]+"..")

        label_L = self.label_nilaiL
        label_L.setText("L = " + open('output/nilaiL.txt', 'r').read())

        label_nilaipembagi = self.label_nilaiq
        label_nilaipembagi.setText("q = " +open('output/nilaipembagiutama.txt', 'r').read()[0:3]+"..")

    def select_nilaixk(self):
        lower = 1
        upper = int(open('output/nilaipembagiutama.txt', 'r').read()) - 1

        x = random.randint(lower, upper)
        k = random.randint(lower, upper)

        output = "Nilai x = " + str(x) + "\n\nNilai k = " + str(k)
        self.nilai_output.setText(output)

        label_x = self.label_nilaix
        label_x.setText("x = " +str(x)[0:3]+"..")
        file = open('output/nilaix.txt', 'w')
        file.write(str(x))
        file.close()

        label_k = self.label_nilaik
        label_k.setText("k = " +str(k)[0:3]+"..")
        file2 = open('output/nilaik.txt', 'w')
        file2.write(str(k))
        file.close()

        return x, k

    def next(self):
        # self.select_nilaixk()

        self.hide()
        kelima = FungsiKelima.MyQtApp(self)
        kelima.position()
        kelima.show()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    qt_app = MyQtApp()
    screen = QtGui.QDesktopWidget().screenGeometry()
    x = (screen.width() - qt_app.geometry().width()) / 2
    y = (screen.height() - qt_app.geometry().height()) / 2
    qt_app.move(x, y)
    qt_app.show()
    app.exec()