# -*- coding: utf-8 -*-

# Form222 implementation generated from reading ui file 'verifyfinal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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

class Ui_Form222(object):
    def fpass(self):
	con = sqlite3.connect("Analysis.db")

	c = con.cursor()
	
	opasswd=str(self.old_pwd.text())
	npasswd = str(self.new_pwd.text())
	cpasswd =str(self.conf_pwd.text())
	
	c.execute("select password from User")
	a =c.fetchall()
	#print a
	#print list(zip(*a)[0])
	b =list(zip(*a)[0])
	if opasswd in b:
		if npasswd == cpasswd:
			c.execute(("UPDATE User SET password =? where password =?"),(npasswd,opasswd))
			print "Changed"
		else:
			print "Password doesn't match"
	else:
		print "Wrong old password"
		
	con.commit()
	
	con.close()

    def setupUi(self, Form222):
        Form222.setObjectName(_fromUtf8("Form222"))
        Form222.resize(851, 472)
        Form222.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/OS-X-Wallpaper.jpg);"))
        self.label_5 = QtGui.QLabel(Form222)
        self.label_5.setGeometry(QtCore.QRect(150, 250, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.conf_pwd = QtGui.QLineEdit(Form222)
        self.conf_pwd.setGeometry(QtCore.QRect(390, 240, 261, 41))
        self.conf_pwd.setObjectName(_fromUtf8("conf_pwd"))

        self.conf_pwd.setEchoMode(QtGui.QLineEdit.Password)

        self.label_2 = QtGui.QLabel(Form222)
        self.label_2.setGeometry(QtCore.QRect(150, 170, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.new_pwd = QtGui.QLineEdit(Form222)
        self.new_pwd.setGeometry(QtCore.QRect(390, 170, 261, 41))
        self.new_pwd.setObjectName(_fromUtf8("new_pwd"))

        self.new_pwd.setEchoMode(QtGui.QLineEdit.Password)

        self.jatankra = QtGui.QPushButton(Form222)
        self.jatankra.setGeometry(QtCore.QRect(270, 350, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.jatankra.setFont(font)
        self.jatankra.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.jatankra.setObjectName(_fromUtf8("jatankra"))

	self.jatankra.clicked.connect(self.fpass)

        self.label_6 = QtGui.QLabel(Form222)
        self.label_6.setGeometry(QtCore.QRect(150, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.old_pwd = QtGui.QLineEdit(Form222)
        self.old_pwd.setGeometry(QtCore.QRect(390, 100, 261, 41))
        self.old_pwd.setObjectName(_fromUtf8("old_pwd"))

        self.old_pwd.setEchoMode(QtGui.QLineEdit.Password)

        self.retranslateUi(Form222)
        QtCore.QMetaObject.connectSlotsByName(Form222)

    def retranslateUi(self, Form222):
        Form222.setWindowTitle(_translate("Form222", "Enter Password", None))
        self.label_5.setText(_translate("Form222", "कन्फर्म पासवर्ड ", None))
        self.label_2.setText(_translate("Form222", "न्यू पासवर्ड ", None))
        self.jatankra.setText(_translate("Form222", "जतन करा ", None))
        self.label_6.setText(_translate("Form222", "ओल्ड पासवर्ड ", None))

import forgot_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form222 = QtGui.QWidget()
    ui = Ui_Form222()
    ui.setupUi(Form222)
    Form222.show()
    sys.exit(app.exec_())

