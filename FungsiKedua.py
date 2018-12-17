from PyQt4.QtGui import QDesktopWidget

from ui import Kedua, FungsiKetiga

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPixmap

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
        # combo = self.box_nilaiL
        # l = int(combo.currentText())
        #
        # lower = 2**(l-1)
        # upper = 2**(l)
        lower = 2**31
        upper = 2**32

        result = ''

        for num in range(lower, upper + 1):
            if num % 2 == 0:
                pass
            else:
                prime = True
                pmax = int(math.sqrt(num))
                for p in range(3, pmax + 1, 2):
                    if (num % p) == 0:
                        prime = False
                        break
                if prime:
                    result = str(num)
                    break

        # self.nilai_output.setText("L = " + str(l) + "\np = " + result)
        self.nilai_output.setText("L = " + "\np = " + result)

        label_nilaiprima = self.label_nilaip
        label_nilaiprima.setText(result)

        label_nilaiL = self.label_nilaiL
        
        # label_nilaiL.setText("L = " + str(l))
        
        print(lower)
        print(upper)

        return result
        

    def next(self):
        prima = self.select_L()
        if not prima:
            QtGui.QMessageBox.about(self, "Prima Required", "Prima tidak boleh kosong! Pilih nilai L yang lain")
            return

        file = open('output/nilaiL.txt', 'w')
        nilaiL = self.label_nilaiL.text()
        file.write(nilaiL)
        file.close()

        file2 = open('output/nilaip.txt', 'w')
        p = str(self.select_L())
        file2.write(p)
        file2.close()

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