# -*- coding: utf-8 -*-

# Form1 implementation generated from reading ui file 'tapasadhikari.ui'
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

class Ui_Form1(object):
    def insert_db(self):		
	officer =str(self.comboBox.currentText())
	addr =str(self.lineEdit.text())
	email =str(self.lineEdit_2.text())
	ph_no =str(self.lineEdit_3.text())
	gender =str(self.comboBox_2.currentText())
	report_no =str(self.lineEdit_4.text())

	rows = [officer,addr,email,ph_no,gender,report_no]
	con = sqlite3.connect("Analysis.db")
	c = con.cursor()
	c.execute("create table Officers(officer varchar(25),addr varchar(100),email varchar(25),ph_no number(10),gender varchar(25),report_no number)")		
	sql = "insert into Officers(officer,addr,email,ph_no,gender,report_no) VALUES(?, ?, ?, ?, ?, ? )"
	print rows
	c.execute(sql, rows)
	c.execute("select * from Officers")
	x = c.fetchall()
	print x
	con.commit()
	con.close()
    def setupUi(self, Form1):
        Form1.setObjectName(_fromUtf8("Form1"))
        Form1.resize(677, 563)
        self.label = QtGui.QLabel(Form1)
        self.label.setGeometry(QtCore.QRect(40, 30, 121, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.listView = QtGui.QListView(Form1)
        self.listView.setGeometry(QtCore.QRect(20, 70, 611, 491))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.comboBox = QtGui.QComboBox(Form1)
        self.comboBox.setGeometry(QtCore.QRect(230, 100, 371, 41))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8("निवडा "))
        self.comboBox.addItem(_fromUtf8("S.S .Deshpande"))
        self.comboBox.addItem(_fromUtf8("S.P Jadhav"))
        self.comboBox.addItem(_fromUtf8("R.M Patil"))
        self.label_4 = QtGui.QLabel(Form1)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 161, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form1)
        self.label_5.setGeometry(QtCore.QRect(40, 150, 161, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit = QtGui.QLineEdit(Form1)
        self.lineEdit.setGeometry(QtCore.QRect(230, 150, 371, 121))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_6 = QtGui.QLabel(Form1)
        self.label_6.setGeometry(QtCore.QRect(40, 310, 161, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_9 = QtGui.QLabel(Form1)
        self.label_9.setGeometry(QtCore.QRect(30, 460, 161, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Form1)
        self.label_10.setGeometry(QtCore.QRect(30, 410, 161, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Form1)
        self.label_11.setGeometry(QtCore.QRect(30, 360, 161, 31))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_2 = QtGui.QLineEdit(Form1)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 300, 371, 41))
####################################################################
        regexp = QtCore.QRegExp("^[0-9a-zA-Z]+([0-9a-zA-Z]*[-._+])*[0-9a-zA-Z]+@[0-9a-zA-Z]+([-.][0-9a-zA-Z]+)*([0-9a-zA-Z]*[.])[a-zA-Z]{2,6}$")
        validator = QtGui.QRegExpValidator(regexp)
        self.lineEdit_2.setValidator(validator)
####################################################################
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form1)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 350, 371, 41))
        self.lineEdit_3.setInputMask(_fromUtf8("9999999999"))
        self.lineEdit_3.setMaxLength(10)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Form1)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 450, 371, 41))
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_4.setInputMask(_fromUtf8("9999999999"))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.comboBox_2 = QtGui.QComboBox(Form1)
        self.comboBox_2.setGeometry(QtCore.QRect(230, 400, 371, 41))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.pushButton_3 = QtGui.QPushButton(Form1)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 510, 99, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.insert_db)
        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        Form1.setWindowTitle(_translate("Form1", "तपास अधिकारी", None))
        self.label.setText(_translate("Form1", " तपास अधिकारी ", None))
        self.comboBox.setItemText(0, _translate("Form1", "निवडा ", None))
        self.comboBox.setItemText(1, _translate("Form1", "S S Deshpande", None))
        self.comboBox.setItemText(2, _translate("Form1", "S P jadhav", None))
        self.comboBox.setItemText(3, _translate("Form1", "A N Patil", None))
        self.label_4.setText(_translate("Form1", "या अधिकाऱ्यासाठी नोंद ", None))
        self.label_5.setText(_translate("Form1", "पत्ता", None))
        self.label_6.setText(_translate("Form1", "इमेल ", None))
        self.label_9.setText(_translate("Form1", "तक्रार क्रमांक ", None))
        self.label_10.setText(_translate("Form1", "लिंग ", None))
        self.label_11.setText(_translate("Form1", " फोन नं.:", None))
        self.comboBox_2.setItemText(0, _translate("Form1", "निवडा ", None))
        self.comboBox_2.setItemText(1, _translate("Form1", "Male", None))
        self.comboBox_2.setItemText(2, _translate("Form1", "Female", None))
        self.pushButton_3.setText(_translate("Form1", "जतन करा", None))
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form1 = QtGui.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form1)
    Form1.show()
    sys.exit(app.exec_())

