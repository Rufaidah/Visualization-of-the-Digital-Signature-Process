# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Intro.ui'
#
# Created: Sun Feb 17 23:06:29 2019
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow0(object):
    def setup0(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(778, 605)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.frame_signing = QtGui.QFrame(self.frame)
        self.frame_signing.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame_signing.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame_signing.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_signing.setObjectName(_fromUtf8("frame_signing"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_signing)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.signing = QtGui.QLabel(self.frame_signing)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.signing.setFont(font)
        self.signing.setStyleSheet(_fromUtf8("background-color: rgb(255, 166, 77);\n"
"color: rgb(255, 255, 255);"))
        self.signing.setScaledContents(False)
        self.signing.setAlignment(QtCore.Qt.AlignCenter)
        self.signing.setMargin(10)
        self.signing.setObjectName(_fromUtf8("signing"))
        self.verticalLayout_3.addWidget(self.signing)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.frame_signing)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_digital_signature = QtGui.QLabel(self.frame_signing)
        self.label_digital_signature.setText(_fromUtf8(""))
        self.label_digital_signature.setAlignment(QtCore.Qt.AlignCenter)
        self.label_digital_signature.setObjectName(_fromUtf8("label_digital_signature"))
        self.verticalLayout.addWidget(self.label_digital_signature)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame_signing)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.frame_signing)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 166, 77);"))
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.frame_signing)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 166, 77);"))
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_signing = QtGui.QLabel(self.frame_signing)
        self.label_signing.setText(_fromUtf8(""))
        self.label_signing.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_signing.setObjectName(_fromUtf8("label_signing"))
        self.horizontalLayout_2.addWidget(self.label_signing)
        self.label_verifying = QtGui.QLabel(self.frame_signing)
        self.label_verifying.setText(_fromUtf8(""))
        self.label_verifying.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_verifying.setObjectName(_fromUtf8("label_verifying"))
        self.horizontalLayout_2.addWidget(self.label_verifying)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btn_next = QtGui.QPushButton(self.frame_signing)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_next.setFont(font)
        self.btn_next.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.btn_next.setStyleSheet(_fromUtf8(""))
        self.btn_next.setText(_fromUtf8(""))
        self.btn_next.setAutoDefault(False)
        self.btn_next.setDefault(False)
        self.btn_next.setFlat(True)
        self.btn_next.setObjectName(_fromUtf8("btn_next"))
        self.horizontalLayout_4.addWidget(self.btn_next)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_signing, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Digital Signature", None))
        self.signing.setText(_translate("MainWindow", "DIGITAL SIGNATURE ALGORITHM", None))
        self.label.setText(_translate("MainWindow", "Berikut Digital Signature Algoritm (DSA) menurut William Stallings pada bukunya yaitu\n"
"\"Cryptography and Network Security Principles and Practice\"", None))
        self.label_2.setText(_translate("MainWindow", "Setelah algoritma tersebut di analisis, didapatkan proses untuk memudahkan\n"
"dalam mendapatkan hasil signing dan verifying yang akan di visualisasikan pada aplikasi ini.\n"
"Berikut adalah keseluruhan dari proses ", None))
        self.label_3.setText(_translate("MainWindow", "Signing", None))
        self.label_4.setText(_translate("MainWindow", "Verifying", None))



