from PyQt4.QtGui import QDesktopWidget

from ui import Pertama, FungsiKedua
from ui.Kedua import *
import ntpath

from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QPixmap

from Crypto.PublicKey import RSA
from Crypto import Random

import rsa

import hashlib

class MyQtApp(Pertama.Ui_MainWindow, QtGui.QMainWindow):
    def position(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(x, y)

    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setupUi(self)
        # self.showMaximized()
        self.setWindowTitle("Proses Digital Signature")
        self.btn_search.clicked.connect(self.select_file)
        self.btn_process.clicked.connect(self.select_hash)
        self.btn_next.clicked.connect(self.next)

        button = self.btn_next
        button.setIcon(QtGui.QIcon("images/next-arrow.png"))
        button.setIconSize(QtCore.QSize(35,35))

        label_nilaihash = self.label_nilaihash
        label_hash = self.label_hash


        label = self.label_pic_2
        label2 = self.label_pic_4

        image = QPixmap("images/down-arrow.png")
        label.setPixmap(image.scaled(25, 25))
        label2.setPixmap(image.scaled(25, 25))

    def select_file(self):
        dialog = QtGui.QFileDialog()
        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
        dialog.setDefaultSuffix('pdf')
        dialog.setNameFilters(['PDF (*.pdf)'])
        if dialog.exec_()== QtGui.QDialog.Accepted:
            self.edit_file.setText(dialog.selectedFiles()[0])
        else:
            print("Canceled")

    def select_hash(self):
        combo = self.box_funsihash
        result = ""

        if combo.currentIndex() == 0:
            result = self.make_md5()
        if combo.currentIndex() == 1:
            result = " ".join(str(x) for x in self.make_rsa())
        if combo.currentIndex() == 2:
            result = self.make_sha()

        filename = ntpath.basename(self.edit_file.text())
        fungsi_hash = combo.currentText()
        output = "File (M) = \n" + filename + \
                 "\n\nFungsi Hash (f(H)) =\n" + fungsi_hash + \
                 "\n\nNilai Hash (H(M)) = \n" + str(result)
        self.nilai_output.setText(output)

        label_fungsi = self.label_hash
        label_fungsi.setText(fungsi_hash)

        label_nilai = self.label_nilaihash
        # frame = self.frame_m_3
        # frame.setMaximumWidth(200)
        label_nilai.setText("H(M)")

        if not filename:
            self.nilai_output.setText(str())
            label_fungsi.setText(str())
            label_nilai.setText(str())
            return ''

        return result

    def make_md5(self):
        file = self.edit_file.text()
        if not file:
            QtGui.QMessageBox.about(self, "File Required", "Hey! Masukkan file")
            return
        md5 = hashlib.md5(open(file, 'rb').read())
        return md5.hexdigest()

    def make_sha(self):
        file = self.edit_file.text()
        if not file:
            QtGui.QMessageBox.about(self, "File Required", "Hey! Masukkan file")
            return
        sha = hashlib.sha512(open(file, 'rb').read())
        return sha.hexdigest()

    def make_rsa(self):
        # Pembuatan kunci
        # Fungsi untuk menghasilkan data random
        rng = Random.new().read
        # Generate kunci dengan panjang 5120 bit
        key = RSA.generate(256 * 20, rng)
        # Export private-key ke private.pem
        open('output/private.pem', 'wb').write(key.exportKey())
        # Export public-key ke public.pem
        open('output/public.pem', 'wb').write(key.publickey().exportKey())

        # Enkripsi
        file = self.edit_file.text()
        if not file:
            QtGui.QMessageBox.about(self, "File Required", "Hey! Masukkan file")
            return
        file_to_encrypt = open(file, 'rb').read()
        key = open('output/public.pem', 'rb').read()
        # pub_key = open('my_pub_key.pem', 'rb').read()
        o = RSA.importKey(key)

        to_join = []
        step = 0

        while 1:
            # Read 128 characters at a time.
            s = file_to_encrypt[step * 128:(step + 1) * 128]
            if not s: break
            # Encrypt with RSA and append the result to list.
            # RSA encryption returns a tuple containing 1 string, so i fetch the string.
            to_join.append(o.encrypt(s, 0)[0])
            step += 1

        # Join the results.
        # I hope the \r\r\r sequence won't appear in the encrypted result,
        # when i explode the string back for decryption.
        return to_join

    def next(self):
        file = self.edit_file.text()
        if not file:
            QtGui.QMessageBox.about(self, "File Required", "Hey! Masukkan file")
            return

        self.select_hash()

        file = open('output/dokumen.txt', 'w')
        dokumen = ntpath.basename(self.edit_file.text())
        file.write(dokumen)
        file.close()

        file = open('output/fungsihash.txt', 'w')
        hash = self.label_hash.text()
        file.write(hash)
        file.close()

        file2 = open('output/nilaihash.txt', 'w')
        nilai_hash = str(self.select_hash())
        file2.write(nilai_hash)
        file2.close()

        self.hide()
        kedua = FungsiKedua.MyQtApp(self)
        kedua.position()
        kedua.show()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    qt_app = MyQtApp()
    screen = QtGui.QDesktopWidget().screenGeometry()
    x = (screen.width() - qt_app.geometry().width()) / 2
    y = (screen.height() - qt_app.geometry().height()) / 2
    qt_app.move(x,y)
    qt_app.show()
    app.exec()