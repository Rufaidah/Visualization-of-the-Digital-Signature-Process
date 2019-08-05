from PyQt4.QtGui import QDesktopWidget

import Kedua, FungsiKetiga

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPixmap

import sympy
import math
import random

class MyQtApp(Kedua.Ui_MainWindow2, QtGui.QMainWindow):
    def position(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(x, y)

    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setup2(self)
        # self.showMaximized()
        self.setWindowTitle("Proses Digital Signature")
        self.btn_ok.clicked.connect(self.select_L)
        self.btn_next.clicked.connect(self.next)

        button = self.btn_next
        button.setIcon(QtGui.QIcon("images/next-arrow.png"))
        button.setIconSize(QtCore.QSize(35, 35))

        label = self.label_pic
        label2 = self.label_pic_2
        label3 = self.label_pic_3
        label4 = self.label_pic_4

        image = QPixmap("images/down-arrow.png")
        label.setPixmap(image.scaled(25, 25))
        label2.setPixmap(image.scaled(25, 25))
        label3.setPixmap(image.scaled(25, 25))
        label4.setPixmap(image.scaled(25, 25))

        label_fungsi = self.label_hash
        label_fungsi.setText(open('output/fungsihash.txt', 'r').read())

        label_nilai = self.label_nilaihash
        label_nilai.setText("H(M)")

    def select_L(self):
        combo = self.box_nilaiL
        l = int(combo.currentText())

        lower = (2**(l-1)) + 1
        upper = (2**(l)) - 1

        num = sympy.randprime(lower, upper)

        self.nilai_output.setText("L = " + str(l) + "\np = " + str(num))

        label_nilaiL = self.label_nilaiL
        label_nilaiL.setText("L = " + str(l))
        file = open('output/nilaiL.txt', 'w')
        file.write(str(l))
        file.close()

        label_nilaiprima = self.label_nilaip
        label_nilaiprima.setText("p = " + str(num)[0:3]+"..")
        file2 = open('output/nilaip.txt', 'w')
        file2.write(str(num))
        file2.close()

        # print(lower)
        # print(upper)

        return num
        

    def next(self):
        self.hide()
        ketiga = FungsiKetiga.MyQtApp(self)
        ketiga.position()
        ketiga.show()

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