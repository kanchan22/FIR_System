# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeFinal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from tapasadhikari_event import Ui_Form1
#from Ghatna_form import Ui_Form5
from Shodha import Ui_Form3
from Thane_dainandini import Ui_Form4
from Takrardarachatapship import Ui_Form6
from Malk import Ui_Form8
from year2 import Ui_Frame20
from final_form import Ui_Form30
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

class Ui_Frame(object):
    def openWindow(self):
	self.window = QtGui.QWidget()
	self.ui=Ui_Form1()
	self.ui.setupUi(self.window)
	self.window.show()

    def openWindow1(self):
	self.window = QtGui.QWidget()
	self.ui=Ui_Form3()
	self.ui.setupUi(self.window)
	self.window.show()

    def openWindow2(self):
	self.window = QtGui.QWidget()
	self.ui=Ui_Form4()
	self.ui.setupUi(self.window)
	self.window.show()

    def openWindow3(self):
	self.window = QtGui.QWidget()
	self.ui=Ui_Form30()
	self.ui.setupUi(self.window)
	self.window.show()

    def openWindow4(self):
	self.window = QtGui.QWidget()
	self.ui=Ui_Form6()
	self.ui.setupUi(self.window)
	self.window.show()

    def openWindow5(self):
	self.window = QtGui.QWidget()
	self.ui=Ui_Form8()
	self.ui.setupUi(self.window)
	self.window.show()
    def openWindow6(self):	
	self.window = QtGui.QWidget()
	self.ui=Ui_Frame20()
	self.ui.setupUi(self.window)
	self.window.show()
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(1137, 656)
        Frame.setStyleSheet(_fromUtf8("image: url(:/newPrefix/police1.jpg);"))
        #Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        #Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.pushButton_6 = QtGui.QPushButton(Frame)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 105, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_8 = QtGui.QPushButton(Frame)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 10, 157, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))

	self.pushButton_8.clicked.connect(self.openWindow2)

        self.pushButton_9 = QtGui.QPushButton(Frame)
        self.pushButton_9.setGeometry(QtCore.QRect(780, 10, 130, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))

	self.pushButton_9.clicked.connect(self.openWindow)

        self.pushButton = QtGui.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(1020, 10, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

	self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.pushButton_10 = QtGui.QPushButton(Frame)
        self.pushButton_10.setGeometry(QtCore.QRect(280, 10, 157, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))

        self.pushButton_10.clicked.connect(self.openWindow3)

        self.pushButton_11 = QtGui.QPushButton(Frame)
        self.pushButton_11.setGeometry(QtCore.QRect(440, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))

	self.pushButton_11.clicked.connect(self.openWindow4)


        self.pushButton_12 = QtGui.QPushButton(Frame)
        self.pushButton_12.setGeometry(QtCore.QRect(610, 10, 157, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))

        self.pushButton_12.clicked.connect(self.openWindow5)

        self.pushButton_2 = QtGui.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 10, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_2.clicked.connect(self.openWindow1)

        self.pushButton_3 = QtGui.QPushButton(Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

	self.pushButton_3.clicked.connect(self.openWindow6)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "मुखप्रुष्ठ", None))
        self.pushButton_6.setText(_translate("Frame", "मुखप्रुष्ठ", None))
        self.pushButton_8.setText(_translate("Frame", "पोलीस ठाणे दैनंदिनी", None))
        self.pushButton_9.setText(_translate("Frame", "तपास अधिकारी", None))
        self.pushButton.setText(_translate("Frame", "लॉगआउट ", None))
        self.pushButton_10.setText(_translate("Frame", "घटना ", None))
        self.pushButton_11.setText(_translate("Frame", "तक्रारदाराचा तपशील ", None))
        self.pushButton_12.setText(_translate("Frame", "तकरार दाखला ", None))
        self.pushButton_2.setText(_translate("Frame", "शोधा", None))
        self.pushButton_3.setText(_translate("Frame", "विश्लेषण", None))

import abc_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

