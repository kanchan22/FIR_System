# -*- coding: utf-8 -*-

# Form333 implementation generated from reading ui file 'Verify1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from verifyfinal import Ui_Form222
import sqlite3

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

class Ui_Form333(object):
    def forget(self):
	con = sqlite3.connect("Analysis.db")

	c = con.cursor()
	
	#c.execute("""create table User (id number,email varchar(30),username varchar(10),password varchar(10))""")

	#c.execute("insert into User values(1,'kanchansangle22@gmail.com','kanchan22','kanchan')")

	uname =str(self.username.text())
	uemail =str(self.email.text())
	c.execute("select username from User")
	a =c.fetchall()
	#print a
	#print list(zip(*a)[0])
	b =list(zip(*a)[0])
	if uname in b:
		c.execute(("select email from User where username=?"),(uname,))
		p = c.fetchone()
		#print p
		q =str(p[0])
		#print q
		if q == uemail:
			print "successful"
			self.verify.clicked.connect(self.openWindow222)
		else:
			print "Unsuccessful"
	else:
		print "User does not exists"

	con.commit()

	con.close()

    '''def fpass():
	con = sqlite3.connect("Analysis.db")

	c = con.cursor()
	
	opasswd = "prakash"
	npasswd = "omsangale"
	cpasswd ="omsangale"
	
	if npasswd == cpasswd:
		c.execute(("UPDATE User SET password =? where password =?"),(npasswd,opasswd))
	else
		print "Password doesn't match"
		
	con.commit()
	
	con.close()'''


    def openWindow222(self):
	self.window = QtGui.QWidget()
	self.ui=Ui_Form222()
	self.ui.setupUi(self.window)
	self.window.show()

    def setupUi(self, Form333):
        Form333.setObjectName(_fromUtf8("Form333"))
        Form333.resize(742, 425)
        Form333.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/OS-X-Wallpaper.jpg);"))
        self.label_2 = QtGui.QLabel(Form333)
        self.label_2.setGeometry(QtCore.QRect(140, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.email = QtGui.QLineEdit(Form333)
        self.email.setGeometry(QtCore.QRect(360, 180, 261, 41))
        self.email.setText(_fromUtf8(""))
        self.email.setObjectName(_fromUtf8("email"))
        self.username = QtGui.QLineEdit(Form333)
        self.username.setGeometry(QtCore.QRect(360, 110, 261, 41))
        self.username.setText(_fromUtf8(""))
        self.username.setObjectName(_fromUtf8("username"))
        self.label = QtGui.QLabel(Form333)
        self.label.setGeometry(QtCore.QRect(140, 120, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verify = QtGui.QPushButton(Form333)
        self.verify.setGeometry(QtCore.QRect(290, 290, 121, 31))
        self.verify.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.verify.setObjectName(_fromUtf8("verify"))

	self.verify.clicked.connect(self.forget	)

        self.retranslateUi(Form333)
        QtCore.QMetaObject.connectSlotsByName(Form333)

    def retranslateUi(self, Form333):
        Form333.setWindowTitle(_translate("Form333", "forget Password", None))
        self.label_2.setText(_translate("Form333", "ई-मेल", None))
        self.label.setText(_translate("Form333", "यूजरनेम ", None))
        self.verify.setText(_translate("Form333", "तपास  करा ", None))

import reset_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form333 = QtGui.QWidget()
    ui = Ui_Form333()
    ui.setupUi(Form333)
    Form333.show()
    sys.exit(app.exec_())

