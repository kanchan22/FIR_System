# -*- coding: utf-8 -*-

# Form0 implementation generated from reading ui file 'Reset1.ui'
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

class Ui_Form0(object):
    '''def changeP(self):
	con = sqlite3.connect("Analysis.db")
	c = con.cursor()

	#c.execute("""create table User (id number,email varchar(30),username varchar(10),password varchar(10))""")

	#c.execute("insert into User values(1,'kanchansangle22@gmail.com','kanchan22','kanchan')")

	passwd = str(self.old_pwd.text())
	npasswd = str(self.new_psd.text())
	cpasswd =str(self.conf_pwd.text())
	
	if npasswd == cpasswd:
		c.execute(("UPDATE User SET password =? where password =?"),(npasswd,passwd))
	else:
		print "Password Doesn't match"

	#c.execute("select * from User")

	p = c.fetchall()	
	print p

	con.commit()

	con.close()'''


    def changePass(self):
	con = sqlite3.connect("Analysis.db")
	c = con.cursor()

	#c.execute("""create table User (id number,email varchar(30),username varchar(10),password varchar(10))""")

	#c.execute("insert into User values(1,'kanchansangle22@gmail.com','kanchan22','kanchan')")
	#c.execute("insert into User values(3,'kanchansangale@gmail.com','Prakash','moody')")

	#c.execute("delete from user where id=3")

	uname = str(self.username.text())
	opasswd = str(self.old_pwd.text())

	c.execute("select username from User")
	a =c.fetchall()
	#print a
	#print list(zip(*a)[0])
	b =list(zip(*a)[0])
	if uname in b:
		c.execute(("select password from User where username=?"),(uname,))
		a =c.fetchone()
		print a[0]
		if a[0] == opasswd:
			print "success"
			#changeP(self)
			npasswd = str(self.new_psd.text())
			cpasswd =str(self.conf_pwd.text())
	
			if npasswd == cpasswd:
				c.execute(("UPDATE User SET password =? where password =?"),(npasswd,opasswd))
			else:
				print "Password Doesn't match"
		else:
			print "Unsucess"
	else:
		print "User does not exists"

	con.commit()

	con.close()

    def setupUi(self, Form0):
        Form0.setObjectName(_fromUtf8("Form0"))
        Form0.resize(858, 517)
        Form0.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/OS-X-Wallpaper.jpg);"))
        self.label_5 = QtGui.QLabel(Form0)
        self.label_5.setGeometry(QtCore.QRect(110, 150, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.new_psd = QtGui.QLineEdit(Form0)
        self.new_psd.setGeometry(QtCore.QRect(440, 220, 261, 41))
        self.new_psd.setObjectName(_fromUtf8("new_psd"))
	
        self.new_psd.setEchoMode(QtGui.QLineEdit.Password)

        self.label_4 = QtGui.QLabel(Form0)
        self.label_4.setGeometry(QtCore.QRect(110, 300, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.old_pwd = QtGui.QLineEdit(Form0)
        self.old_pwd.setGeometry(QtCore.QRect(440, 150, 261, 41))
        self.old_pwd.setObjectName(_fromUtf8("old_pwd"))

        self.old_pwd.setEchoMode(QtGui.QLineEdit.Password)	

        self.badla = QtGui.QPushButton(Form0)
        self.badla.setGeometry(QtCore.QRect(340, 400, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.badla.setFont(font)
        self.badla.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.badla.setObjectName(_fromUtf8("badla"))

	self.badla.clicked.connect(self.changePass)

        self.label_2 = QtGui.QLabel(Form0)
        self.label_2.setGeometry(QtCore.QRect(110, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.conf_pwd = QtGui.QLineEdit(Form0)
        self.conf_pwd.setGeometry(QtCore.QRect(440, 290, 261, 41))
        self.conf_pwd.setObjectName(_fromUtf8("conf_pwd"))

        self.conf_pwd.setEchoMode(QtGui.QLineEdit.Password)

        self.username = QtGui.QLineEdit(Form0)
        self.username.setGeometry(QtCore.QRect(440, 80, 261, 41))
        self.username.setObjectName(_fromUtf8("username"))
        self.label = QtGui.QLabel(Form0)
        self.label.setGeometry(QtCore.QRect(110, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form0)
        QtCore.QMetaObject.connectSlotsByName(Form0)

    def retranslateUi(self, Form0):
        Form0.setWindowTitle(_translate("Form0", "Reset Password", None))
        self.label_5.setText(_translate("Form0", "ओल्ड पासवर्ड ", None))
        self.label_4.setText(_translate("Form0", "कन्फर्म पासवर्ड ", None))
        self.badla.setText(_translate("Form0", "बदला ", None))
        self.label_2.setText(_translate("Form0", "न्यू पासवर्ड ", None))
        self.label.setText(_translate("Form0", "यूजरनेम ", None))

import login_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form0 = QtGui.QWidget()
    ui = Ui_Form0()
    ui.setupUi(Form0)
    Form0.show()
    sys.exit(app.exec_())

