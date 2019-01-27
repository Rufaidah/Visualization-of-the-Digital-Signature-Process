from PyQt4.QtGui import QDesktopWidget

from ui import Kedelapan, FungsiKesembilan

from PyQt4 import QtGui, QtCore

class MyQtApp(Kedelapan.Ui_MainWindow8, QtGui.QMainWindow):
    def position(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(x, y)

    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setup8(self)
        # self.showMaximized()
        self.setWindowTitle("Proses Digital Signature")
        self.btn_next.clicked.connect(self.next)

        label_dokumen = self.label_dokumen
        label_dokumen.setText(open('output/dokumen.txt', 'r').read())

        label_r = self.label_nilair
        label_r.setText(open('output/nilair.txt', 'r').read())

        label_s = self.label_nilais
        label_s.setText(open('output/nilais.txt', 'r').read())

        button = self.btn_next
        button.setIcon(QtGui.QIcon("images/next-arrow.png"))
        button.setIconSize(QtCore.QSize(35, 35))

    def next(self):
        self.hide()
        kesembilan = FungsiKesembilan.MyQtApp(self)
        kesembilan.position()
        kesembilan.show()

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