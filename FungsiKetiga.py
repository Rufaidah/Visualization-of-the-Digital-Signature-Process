from PyQt4.QtGui import QDesktopWidget

from ui import Ketiga, FungsiKeempat

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPixmap

import random

class MyQtApp(Ketiga.Ui_MainWindow3, QtGui.QMainWindow):
    def position(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(x, y)

    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setup3(self)
        # self.showMaximized()
        self.setWindowTitle("Proses Digital Signature")
        self.btn_ok.clicked.connect(self.select_pembagi)
        self.btn_next.clicked.connect(self.next)

        button = self.btn_next
        button.setIcon(QtGui.QIcon("images/next-arrow.png"))
        button.setIconSize(QtCore.QSize(35, 35))

        label = self.label_pic
        label2 = self.label_pic_2
        label3 = self.label_pic_3
        label4 = self.label_pic_4
        label5 = self.label_pic_5

        image = QPixmap("images/down-arrow.png")
        label.setPixmap(image.scaled(25, 25))
        label2.setPixmap(image.scaled(25, 25))
        label3.setPixmap(image.scaled(25, 25))
        label4.setPixmap(image.scaled(25, 25))
        label5.setPixmap(image.scaled(25, 25))

        label_fungsi = self.label_hash
        label_fungsi.setText(open('output/fungsihash.txt', 'r').read())

        label_nilai = self.label_nilaihash
        label_nilai.setText("H(M)")

        label_L = self.label_nilaiL
        label_L.setText(open('output/nilaiL.txt', 'r').read())

        label_nilaiprima = self.label_nilaip
        label_nilaiprima.setText(open('output/nilaip.txt', 'r').read())

    def select_pembagi(self):
        lower = 2**159
        upper = 2**160

        q = random.randint(lower, upper)

        output = "Pembagi utama = " + str(q)
        self.nilai_output.setText(output)

        label_nilaipembagi = self.label_nilaiq
        label_nilaipembagi.setText(str(q))
        file = open('output/nilaipembagiutama.txt', 'w')
        file.write(str(q))
        file.close()

        return q

    def next(self):
        self.hide()
        keempat = FungsiKeempat.MyQtApp(self)
        keempat.position()
        keempat.show()

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