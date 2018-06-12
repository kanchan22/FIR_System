# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from Reset1 import Ui_Form0
from Verify1 import Ui_Form333
from homeFinal import Ui_Frame
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

class Ui_Form(object):
    def login(self):
	con = sqlite3.connect("Analysis.db")
	c = con.cursor()

	#c.execute("""create table User (id number,email varchar(30),username varchar(10),password varchar(10))""")

	#c.execute("insert into User values(1,'kanchansangle22@gmail.com','kanchan22','kanchan')")

	#uname = 'kanchan22'
	uname = str(self.username.text())

	c.execute("select username from User")
	a =c.fetchall()
	#print a
	#print list(zip(*a)[0])
	b =list(zip(*a)[0])
	if uname in b:
		print "yes"
		c.execute(("select password from User where username = ?"),(uname,))
		p =c.fetchone()
		print p
		q =str(p[0])
		print q
		passwd = str(self.password.text())
		if q == passwd :
			self.login_btn.clicked.connect(self.openWindow)
			print "login successful"
				
		else:
			print "login unsuccessful"

	else:
		print "User does not exists"
	
	con.commit()
	con.close()
    def openWindow0(self):
	self.window = QtGui.QWidget()
	self.ui=Ui_Form0()
	self.ui.setupUi(self.window)
	self.window.show()
    def openWindow222(self):
	self.window = QtGui.QWidget()
	self.ui=Ui_Form333()
	self.ui.setupUi(self.window)
	self.window.show()
    def openWindow(self):
	self.window = QtGui.QWidget()
	self.ui=Ui_Frame()
	self.ui.setupUi(self.window)
	self.window.show()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1040, 508)
        Form.setStyleSheet(_fromUtf8("\n""background-image: url(:/newPrefix/OS-X-Wallpaper.jpg);"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.reset_btn = QtGui.QPushButton(Form)
        self.reset_btn.setGeometry(QtCore.QRect(270, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reset_btn.setFont(font)
        self.reset_btn.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.reset_btn.setObjectName(_fromUtf8("reset_btn"))

        self.reset_btn.clicked.connect(self.openWindow0)

        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 190, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.password = QtGui.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(480, 190, 261, 41))
        self.password.setObjectName(_fromUtf8("password"))

        self.password.setEchoMode(QtGui.QLineEdit.Password)
	
        self.login_btn = QtGui.QPushButton(Form)
        self.login_btn.setGeometry(QtCore.QRect(410, 280, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
	######################################################################
        self.login_btn.clicked.connect(self.login)

	####################################################################

        self.forget_btn = QtGui.QPushButton(Form)
        self.forget_btn.setGeometry(QtCore.QRect(610, 360, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.forget_btn.setFont(font)
        self.forget_btn.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.forget_btn.setObjectName(_fromUtf8("forget_btn"))

	
	self.forget_btn.clicked.connect(self.openWindow222)

        self.username = QtGui.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(480, 110, 261, 41))
        self.username.setObjectName(_fromUtf8("username"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 110, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Login", None))
        self.label_3.setText(_translate("Form", "WELCOME TO FIR SYSTEM", None))
        self.reset_btn.setText(_translate("Form", "रिसेट  पासवर्ड ", None))
        self.label_2.setText(_translate("Form", "पासवर्ड ", None))
        self.login_btn.setText(_translate("Form", "लॉगीन ", None))
        self.forget_btn.setText(_translate("Form", "फॉरगॉट  पासवर्ड ", None))
        self.label.setText(_translate("Form", "यूजरनेम ", None))

import login_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

