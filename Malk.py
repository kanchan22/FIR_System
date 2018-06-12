# -*- coding: utf-8 -*-

# Form8 implementation generated from reading ui file 'Malk.ui'
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

class Ui_Form8(object):
    def insert_db(self):

	flist =[] 
	
	date =str(self.lineEdit.text())
	time =str(self.lineEdit_2.text())
	officer =str(self.comboBox.currentText())
	mname =str(self.lineEdit_4.text())
	madd =str(self.lineEdit_5.text())
	mocc =str(self.lineEdit_6.text())
	ph_no1 =str(self.lineEdit_7.text())
	ph_no2 =str(self.lineEdit_8.text())
	proof=str(self.lineEdit_9.text())
	
	list1 = [date, time, officer, mname, madd, mocc, ph_no1, ph_no2, proof]
	flist.append(list1)
	
	rows = [date, time, officer, mname, madd, mocc, ph_no1, ph_no2, proof]
	con = sqlite3.connect("Analysis.db")
	c = con.cursor()
	#c.execute("create table malak(date DATE, time TIME, officer varchar(25), mname varchar(50), madd varchar(100), mocc varchar(25), ph_no1 number, ph_no2 number, proof varcar(50))")
			
	sql = "insert into malak(date, time, officer, mname, madd, mocc, ph_no1, ph_no2, proof) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
	print rows
	c.execute(sql, rows)
	c.execute("select * from malak")
	x = c.fetchall()
	print x
	con.commit()
	con.close()

    def setupUi(self, Form8):
        Form8.setObjectName(_fromUtf8("Form8"))
        Form8.resize(747, 818)
        self.label = QtGui.QLabel(Form8)
        self.label.setGeometry(QtCore.QRect(90, 40, 131, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(Form8)
        self.label_6.setGeometry(QtCore.QRect(140, 260, 131, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(Form8)
        self.label_8.setGeometry(QtCore.QRect(30, 220, 131, 31))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.listView = QtGui.QListView(Form8)
        self.listView.setGeometry(QtCore.QRect(80, 80, 591, 651))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label_2 = QtGui.QLabel(Form8)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 91, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form8)
        self.label_3.setGeometry(QtCore.QRect(100, 160, 131, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form8)
        self.label_4.setGeometry(QtCore.QRect(100, 220, 131, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form8)
        self.label_5.setGeometry(QtCore.QRect(320, 270, 131, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(Form8)
        self.label_7.setGeometry(QtCore.QRect(100, 320, 91, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(Form8)
        self.label_9.setGeometry(QtCore.QRect(100, 370, 91, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Form8)
        self.label_10.setGeometry(QtCore.QRect(110, 510, 91, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Form8)
        self.label_11.setGeometry(QtCore.QRect(100, 450, 101, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Form8)
        self.label_12.setGeometry(QtCore.QRect(100, 560, 91, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Form8)
        self.label_13.setGeometry(QtCore.QRect(100, 620, 111, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit = QtGui.QLineEdit(Form8)
        self.lineEdit.setGeometry(QtCore.QRect(250, 110, 371, 41))
        self.lineEdit.setInputMask(_fromUtf8("9999-99-99"))
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form8)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 160, 371, 41))
        self.lineEdit_2.setInputMask(_fromUtf8("99:99:99"))
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_4 = QtGui.QLineEdit(Form8)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 310, 371, 41))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Form8)
        self.lineEdit_5.setGeometry(QtCore.QRect(250, 360, 371, 71))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Form8)
        self.lineEdit_6.setGeometry(QtCore.QRect(250, 440, 371, 41))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Form8)
        self.lineEdit_7.setGeometry(QtCore.QRect(250, 500, 371, 41))
        self.lineEdit_7.setInputMask(_fromUtf8("9999999999"))
        self.lineEdit_7.setMaxLength(10)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(Form8)
        self.lineEdit_8.setGeometry(QtCore.QRect(250, 560, 371, 41))
        self.lineEdit_8.setInputMask(_fromUtf8("9999999999"))
        self.lineEdit_8.setMaxLength(10)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(Form8)
        self.lineEdit_9.setGeometry(QtCore.QRect(250, 620, 371, 81))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.pushButton_2 = QtGui.QPushButton(Form8)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 10, 151, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.comboBox = QtGui.QComboBox(Form8)
        self.comboBox.setGeometry(QtCore.QRect(250, 210, 371, 41))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Form8)
        self.pushButton.setGeometry(QtCore.QRect(570, 270, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
##############################################################
        self.pushButton.clicked.connect(self.insert_db)
##############################################################
        self.retranslateUi(Form8)
        QtCore.QMetaObject.connectSlotsByName(Form8)

    def retranslateUi(self, Form8):
        Form8.setWindowTitle(_translate("Form8", "तकरार दाखला ", None))
        self.label.setText(_translate("Form8", "मालकाची माहिती", None))
        self.label_6.setText(_translate("Form8", "मालकाची माहिती", None))
        self.label_2.setText(_translate("Form8", "तारीख*", None))
        self.label_3.setText(_translate("Form8", "वेळ*", None))
        self.label_4.setText(_translate("Form8", "या अधिकाऱ्यासाठी नोंद ", None))
        self.label_5.setText(_translate("Form8", "मालकाची माहिती", None))
        self.label_7.setText(_translate("Form8", "मालकाचे नाव", None))
        self.label_9.setText(_translate("Form8", "मालकाचा पत्ता", None))
        self.label_10.setText(_translate("Form8", "मोबाईल नं.", None))
        self.label_11.setText(_translate("Form8", "मालकाचा व्यवसाय", None))
        self.label_12.setText(_translate("Form8", "दूरध्वनी क्रमांक.", None))
        self.label_13.setText(_translate("Form8", "ओळख पटवण्यासाठी", None))
        self.pushButton_2.setText(_translate("Form8", "मालकाची माहिती ", None))
        self.comboBox.setItemText(0, _translate("Form8", "निवडा ", None))
        self.comboBox.setItemText(1, _translate("Form8", "S.S .Deshpande", None))
        self.comboBox.setItemText(2, _translate("Form8", "S.P Jadhav", None))
        self.comboBox.setItemText(3, _translate("Form8", "R.M Patil", None))
        self.pushButton.setText(_translate("Form8", "जतन करा ", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form8 = QtGui.QWidget()
    ui = Ui_Form8()
    ui.setupUi(Form8)
    Form8.show()
    sys.exit(app.exec_())

