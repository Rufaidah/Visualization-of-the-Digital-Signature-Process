from PyQt4.QtGui import QDesktopWidget

from ui import Ketujuh

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPixmap

import random

class MyQtApp(Ketujuh.Ui_MainWindow7, QtGui.QMainWindow):
    def position(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(x, y)

    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setup7(self)
        # self.showMaximized()
        self.setWindowTitle("Proses Digital Signature")
        self.btn_ok.clicked.connect(self.select_nilais)
        # self.btn_next.clicked.connect(self.next)

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
        label11 = self.label_pic_11
        label12 = self.label_pic_12
        label13 = self.label_pic_13
        label16 = self.label_pic_16
        label19 = self.label_pic_19

        image = QPixmap("images/down-arrow.png")
        label.setPixmap(image.scaled(25, 25))
        label2.setPixmap(image.scaled(25, 25))
        label3.setPixmap(image.scaled(25, 25))
        label4.setPixmap(image.scaled(25, 25))
        label5.setPixmap(image.scaled(25, 25))
        label6.setPixmap(image.scaled(25, 25))
        label7.setPixmap(image.scaled(25, 25))
        label11.setPixmap(image.scaled(25, 25))
        label12.setPixmap(image.scaled(25, 25))
        label13.setPixmap(image.scaled(25, 25))
        label16.setPixmap(image.scaled(25, 25))
        label19.setPixmap(image.scaled(25, 25))

        label_fungsi = self.label_hash
        label_fungsi.setText(open('output/fungsihash.txt', 'r').read())

        label_nilai = self.label_nilaihash
        label_nilai.setText("H(M)")

        label_nilaiprima = self.label_nilaip
        label_nilaiprima.setText(open('output/nilaip.txt', 'r').read())

        label_L = self.label_nilaiL
        label_L.setText(open('output/nilaiL.txt', 'r').read())

        label_nilaipembagi = self.label_nilaiq
        label_nilaipembagi.setText(open('output/nilaipembagiutama.txt', 'r').read())

        label_x = self.label_nilaix
        label_x.setText(open('output/nilaix.txt', 'r').read())

        label_k = self.label_nilaik
        label_k.setText(open('output/nilaik.txt', 'r').read())

        label_h = self.label_nilaih
        label_h.setText("h = " + open('output/nilaik.txt', 'r').read())

        label_g = self.label_nilaig
        label_g.setText(open('output/nilaig.txt', 'r').read())

        label_r = self.label_nilair
        label_r.setText(open('output/nilair.txt', 'r').read())

    def select_nilais(self):
        nilaihash = int(open('output/nilaihash.txt', 'r').read())
        nilaix = int(open('output/nilaix.txt', 'r').read())
        nilaik = int(open('output/nilaik.txt', 'r').read())
        nilaiq = int(open('output/nilaipembagiutama.txt', 'r').read())
        nilair = float(open('output/nilair.txt', 'r').read())


        s = 0

        output = "Nilai s = " + str(s)
        self.nilai_output.setText(output)

        lebel_s = self.label_nilais
        lebel_s.setText(str(s))
        file = open('output/nilais.txt', 'w')
        file.write(str(s))
        file.close()

        return s

    # def next(self):
    #     self.hide()
    #     kelima = FungsiKeenam.MyQtApp(self)
    #     kelima.position()
    #     kelima.show()

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