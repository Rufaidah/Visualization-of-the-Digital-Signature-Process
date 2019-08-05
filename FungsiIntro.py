from PyQt4.QtGui import QDesktopWidget

import Intro, FungsiPertama

from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QPixmap


class MyQtApp(Intro.Ui_MainWindow0, QtGui.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setup0(self)
        # self.showMaximized()
        self.setWindowTitle("Proses Digital Signature")
        self.btn_next.clicked.connect(self.next)

        button = self.btn_next
        button.setIcon(QtGui.QIcon("images/next-arrow.png"))
        button.setIconSize(QtCore.QSize(35,35))

        image_digital_signature = QPixmap("images/digital-signature.png")
        image_signing = QPixmap("images/signing.jpg")
        image_verifying = QPixmap("images/verifying.jpg")

        label_digital_signature = self.label_digital_signature
        label_digital_signature.setPixmap(image_digital_signature.scaledToHeight(170))
        label_signing = self.label_signing
        label_signing.setPixmap(image_signing.scaledToHeight(100))
        label_verifying = self.label_verifying
        label_verifying.setPixmap(image_verifying.scaledToHeight(120))

    def next(self):
        self.hide()
        pertama = FungsiPertama.MyQtApp(self)
        pertama.position()
        pertama.show()

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