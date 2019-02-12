import time
from time import sleep

from PyQt4.QtGui import QDesktopWidget

from ui import Kesembilan

from PyQt4 import QtGui, QtCore

import sympy
import hashlib

class MyQtApp(Kesembilan.Ui_MainWindow9, QtGui.QMainWindow):
    def position(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(x, y)

    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setup9(self)
        # self.showMaximized()
        self.setWindowTitle("Proses Digital Signature")
        self.btn_search.clicked.connect(self.file)
        self.btn_process.clicked.connect(self.verify)

    def file(self):
        dialog = QtGui.QFileDialog()
        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
        dialog.setDefaultSuffix('pdf')
        dialog.setNameFilters(['PDF (*.pdf)'])
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.edit_file.setText(dialog.selectedFiles()[0])
            print("Masuk")
        else:
            print("Canceled")

    def verify(self):
        # file = self.edit_file.text()
        # if not file:
        #     QtGui.QMessageBox.about(self, "File Required", "Hey! Masukkan file")
        #     return

        label_verify = self.label_verify

        # p = 283
        # q = 47
        # g = 60
        # y = 158
        # h = 41
        # r = 19
        # s = 30

        fungsihash = open('output/fungsihash.txt', 'r').read()
        r = int(open('output/nilair.txt', 'r').read())
        print(r)
        s = int(open('output/nilais.txt', 'r').read())
        print(s)
        q = int(open('output/nilaipembagiutama.txt', 'r').read())
        print(q)
        g = int(open('output/nilaig.txt', 'r').read())
        print(g)
        p = int(open('output/nilaip.txt', 'r').read())
        print(p)
        x = int(open('output/nilaix.txt', 'r').read())
        print(x)

        if r & s in range (1 , q-1):
            w = sympy.mod_inverse(s, q)
            print("w = " + str(w))

            h = " "

            if fungsihash == 'MD5':
                h =  self.md5()
            if fungsihash == 'SHA':
                h =  self.sha()
            if fungsihash == 'RSA':
                h =  self.rsa()

            u1 = (h * w) % q
            print("u1 = " + str(u1))
            u2 = (r * w) % q
            print("u2 = " + str(u2))

            y = (g ** x) % p

            x = ((g ** u1) * (y ** u2)) % p
            print("x = " + str(x))

            v = x % q
            print("v = " + str(v))

            if v == r:
                label_verify.setText("Accept!")
            else:
                label_verify.setText("Reject!")
        else:
            label_verify.setText("Reject!")

    def md5(self):
        file = self.edit_file.text()
        if not file:
            QtGui.QMessageBox.about(self, "File Required", "Hey! Masukkan file")
            return

        h = hashlib.md5(open(file, 'rb').read()).hexdigest()
        # print("h = " + h)
        return int(h, 32)

    def sha(self):
        file = self.edit_file.text()
        if not file:
            QtGui.QMessageBox.about(self, "File Required", "Hey! Masukkan file")
            return

        h = hashlib.sha512(open(file, 'rb').read()).hexdigest()
        return int(h, 32)

    def rsa(self):
        file = self.edit_file.text()
        if not file:
            QtGui.QMessageBox.about(self, "File Required", "Hey! Masukkan file")
            return

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