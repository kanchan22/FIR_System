# -*- coding: utf-8 -*-

# Form4 implementation generated from reading ui file 'Thane_dainandini.ui'
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

class Ui_Form4(object):
    def insert_into(self):		
	flist =[] 
	date =str(self.lineEdit.text())
	time =str(self.lineEdit_2.text())
	dainan_type =str(self.lineEdit_3.text())
	officer =str(self.comboBox.currentText())
	sub =str(self.lineEdit_4.text())
	dainandini =str(self.lineEdit_5.text())
		
	#list1 = [c_type,]
	#flist.append(list1)
	rows = [date,time,dainan_type,officer,sub,dainandini]
	con = sqlite3.connect("Analysis.db")
	c = con.cursor()
	#c.execute("create table dainandini(date varchar(15),time varchar(10),dainan_type varchar(100),officer varchar(25),sub varchar(150),dainandini varchar(100))")			
	sql = "insert into dainandini(date,time,dainan_type,officer,sub ,dainandini) VALUES(?, ?, ?, ?, ?, ?)"
	print rows
	c.execute(sql, rows)
	c.execute("select * from ghatna")
	x = c.fetchall()
	print x
	con.commit()
	con.close()

    def setupUi(self, Form4):
	
        Form4.setObjectName(_fromUtf8("Form4"))
        Form4.resize(621, 608)
        self.label = QtGui.QLabel(Form4)
        self.label.setGeometry(QtCore.QRect(40, 20, 201, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget = QtGui.QListWidget(Form4)
        self.listWidget.setGeometry(QtCore.QRect(30, 50, 541, 561))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_6 = QtGui.QLabel(Form4)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 161, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(Form4)
        self.label_5.setGeometry(QtCore.QRect(40, 90, 61, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_4 = QtGui.QLabel(Form4)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 51, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_7 = QtGui.QLabel(Form4)
        self.label_7.setGeometry(QtCore.QRect(40, 200, 161, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form4)
        self.label_8.setGeometry(QtCore.QRect(40, 320, 91, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Form4)
        self.label_9.setGeometry(QtCore.QRect(40, 380, 161, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_2 = QtGui.QLineEdit(Form4)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 150, 371, 41))
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_2.setInputMask(_fromUtf8("99:99:99"))
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        
        self.comboBox = QtGui.QComboBox(Form4)
        self.comboBox.setGeometry(QtCore.QRect(170, 250, 371, 41))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8("निवडा "))
        self.comboBox.addItem(_fromUtf8("S.S .Deshpande"))
        self.comboBox.addItem(_fromUtf8("S.P Jadhav"))
        self.comboBox.addItem(_fromUtf8("R.M Patil"))
        self.lineEdit = QtGui.QLineEdit(Form4)
        self.lineEdit.setGeometry(QtCore.QRect(170, 90, 371, 41))
        self.lineEdit.setInputMask(_fromUtf8("9999-99-99"))
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_3 = QtGui.QLineEdit(Form4)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 200, 371, 41))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Form4)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 310, 371, 41))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Form4)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 370, 361, 171))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.jatan = QtGui.QPushButton(Form4)
        self.jatan.setGeometry(QtCore.QRect(210, 550, 99, 27))
        self.jatan.setObjectName(_fromUtf8("jatan"))
        self.jatan.clicked.connect(self.insert_into)


        self.retranslateUi(Form4)
        QtCore.QMetaObject.connectSlotsByName(Form4)

    def retranslateUi(self, Form4):
        Form4.setWindowTitle(_translate("Form4", "पोलीस ठाणे दैनंदिनी", None))
        self.label.setText(_translate("Form4", "ठाणे दैनंदिनी तपशील समाविष्ट करा", None))
        self.label_6.setText(_translate("Form4", "या अधिकाऱ्यासाठी नोंद ", None))
        self.label_5.setText(_translate("Form4", "तारीख*", None))
        self.label_4.setText(_translate("Form4", "वेळ*", None))
        self.label_7.setText(_translate("Form4", "ठाणे दैनंदिनी प्रकार *", None))
        self.label_8.setText(_translate("Form4", "विषय", None))
        self.label_9.setText(_translate("Form4", "ठाणे दैनंदिनी", None))
        self.comboBox.setItemText(0, _translate("Form4", "निवडा ", None))
        self.comboBox.setItemText(1, _translate("Form4", "S S Deshpande", None))
        self.comboBox.setItemText(2, _translate("Form4", "S P jadhav", None))
        self.comboBox.setItemText(3, _translate("Form4", "A N Patil", None))
        self.jatan.setText(_translate("Form4", "जतन करा ", None))
	


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form4 = QtGui.QWidget()
    ui = Ui_Form4()
    ui.setupUi(Form4)
    Form4.show()
    sys.exit(app.exec_())

