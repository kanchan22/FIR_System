# -*- coding: utf-8 -*-

# Form6 implementation generated from reading ui file 'Takrardarachatapship.ui'
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

class Ui_Form6(object):
    def insert_db(self):		
	flist =[] 
	date =str(self.lineEdit.text())
	time =str(self.lineEdit_2.text())
	officer =str(self.comboBox.currentText())
	uid =str(self.lineEdit_3.text())
	fname =str(self.lineEdit_4.text())
	mname =str(self.lineEdit_5.text())
	lname =str(self.lineEdit_6.text())
	relation =str(self.comboBox_2.currentText())
	rel_name =str(self.lineEdit_7.text())
	gender =str(self.comboBox_5.currentText())
	dob =str(self.lineEdit_8.text())
	age =str(self.lineEdit_12.text())
	marital =str(self.comboBox_6.currentText())
	mob =str(self.lineEdit_10.text())
	email =str(self.lineEdit_14.text())
	blkno =str(self.lineEdit_15.text())
	'''rd_name =str(self.lineEdit_5.text())
	area =str(self.lineEdit_5.text())
	city =str(self.lineEdit_5.text())
	tahashil =str(self.lineEdit_5.text())
	perm_add =str(self.lineEdit_5.text())
	country =str(self.comboBox_2.currentText())
	state =str(self.comboBox_2.currentText())
	jilha =str(self.comboBox_2.currentText())
	police_station =str(self.comboBox_2.currentText())
	pincode =str(self.lineEdit_5.text())'''

	#list1 = [c_type,]
	#flist.append(list1)
	rows = [date,time,officer,uid,fname,mname,lname,relation,rel_name,gender,dob,age,marital,mob,email,blkno]
	con = sqlite3.connect("Analysis.db")
	c = con.cursor()
	#c.execute("create table tapshil(date varchar(10),time varchar(25),officer varchar(20),uid number,fname varchar(10),mname varchar(10),lname varchar(10),relation varchar(10),rel_name varchar(10),gender varchar(10),dob  varchar(10),age varchar(10),marital varchar(10),mob number(10),email varchar(10),blkno number,rd_name varchar(25),area varchar(25),city varchar(25),tahashil varchar(25),perm_add varchar(100),country varchar(25),state varchar(25),jilha varchar(25),police_station varchar(25),pincode number)")			
	sql = "insert into tapshil(date,time,dainan_type,officer,sub ,dainandini) VALUES(?, ?, ?, ?, ?, ?)"
	print rows
	c.execute(sql, rows)
	c.execute("select * from ghatna")
	x = c.fetchall()
	print x
	con.commit()
	con.close()

    def setupUi(self, Form6):
        Form6.setObjectName(_fromUtf8("Form6"))
        Form6.resize(818, 1839)
        self.pushButton_2 = QtGui.QPushButton(Form6)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 20, 151, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_5 = QtGui.QLabel(Form6)
        self.label_5.setGeometry(QtCore.QRect(40, 80, 121, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.listWidget = QtGui.QListWidget(Form6)
        self.listWidget.setGeometry(QtCore.QRect(30, 120, 741, 1441))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_2 = QtGui.QLabel(Form6)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 61, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form6)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 51, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form6)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 161, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(Form6)
        self.lineEdit.setGeometry(QtCore.QRect(200, 150, 371, 41))
        self.lineEdit.setInputMask(_fromUtf8("9999-99-99"))
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form6)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 200, 371, 41))
        self.lineEdit_2.setInputMask(_fromUtf8("99:99:99"))
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.comboBox = QtGui.QComboBox(Form6)
        self.comboBox.setGeometry(QtCore.QRect(200, 250, 371, 41))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(Form6)
        self.label.setGeometry(QtCore.QRect(40, 310, 621, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(Form6)
        self.label_6.setGeometry(QtCore.QRect(50, 350, 161, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Form6)
        self.label_7.setGeometry(QtCore.QRect(40, 510, 111, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form6)
        self.label_8.setGeometry(QtCore.QRect(40, 480, 111, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Form6)
        self.label_9.setGeometry(QtCore.QRect(50, 430, 71, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Form6)
        self.label_10.setGeometry(QtCore.QRect(50, 390, 61, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Form6)
        self.label_11.setGeometry(QtCore.QRect(50, 590, 111, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Form6)
        self.label_12.setGeometry(QtCore.QRect(60, 670, 111, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Form6)
        self.label_13.setGeometry(QtCore.QRect(60, 700, 111, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Form6)
        self.label_14.setGeometry(QtCore.QRect(40, 550, 111, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(Form6)
        self.label_15.setGeometry(QtCore.QRect(50, 620, 621, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(Form6)
        self.label_16.setGeometry(QtCore.QRect(50, 920, 111, 21))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(Form6)
        self.label_17.setGeometry(QtCore.QRect(50, 890, 111, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(Form6)
        self.label_18.setGeometry(QtCore.QRect(50, 850, 111, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(Form6)
        self.label_19.setGeometry(QtCore.QRect(50, 810, 111, 21))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(Form6)
        self.label_20.setGeometry(QtCore.QRect(50, 730, 111, 21))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(Form6)
        self.label_21.setGeometry(QtCore.QRect(50, 990, 111, 21))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(Form6)
        self.label_22.setGeometry(QtCore.QRect(40, 1030, 111, 21))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(Form6)
        self.label_23.setGeometry(QtCore.QRect(40, 1150, 111, 21))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(Form6)
        self.label_24.setGeometry(QtCore.QRect(40, 1110, 111, 21))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(Form6)
        self.label_25.setGeometry(QtCore.QRect(40, 1070, 131, 21))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(Form6)
        self.label_26.setGeometry(QtCore.QRect(50, 1270, 111, 21))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(Form6)
        self.label_27.setGeometry(QtCore.QRect(50, 1310, 111, 21))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(Form6)
        self.label_28.setGeometry(QtCore.QRect(50, 1390, 71, 31))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(Form6)
        self.label_29.setGeometry(QtCore.QRect(50, 1350, 111, 21))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(Form6)
        self.label_30.setGeometry(QtCore.QRect(50, 1450, 111, 21))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(Form6)
        self.label_31.setGeometry(QtCore.QRect(10, 960, 621, 20))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.lineEdit_3 = QtGui.QLineEdit(Form6)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 340, 371, 41))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Form6)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 390, 371, 41))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Form6)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 430, 371, 41))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Form6)
        self.lineEdit_6.setGeometry(QtCore.QRect(210, 470, 371, 41))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.comboBox_2 = QtGui.QComboBox(Form6)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 510, 61, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.lineEdit_7 = QtGui.QLineEdit(Form6)
        self.lineEdit_7.setGeometry(QtCore.QRect(210, 540, 371, 41))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.comboBox_5 = QtGui.QComboBox(Form6)
        self.comboBox_5.setGeometry(QtCore.QRect(210, 590, 61, 31))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.lineEdit_8 = QtGui.QLineEdit(Form6)
        self.lineEdit_8.setGeometry(QtCore.QRect(210, 640, 371, 41))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(Form6)
        self.lineEdit_9.setGeometry(QtCore.QRect(210, 680, 371, 41))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(Form6)
        self.lineEdit_10.setGeometry(QtCore.QRect(210, 840, 371, 41))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(Form6)
        self.lineEdit_11.setGeometry(QtCore.QRect(210, 760, 371, 41))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(Form6)
        self.lineEdit_12.setGeometry(QtCore.QRect(210, 720, 371, 41))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(Form6)
        self.lineEdit_13.setGeometry(QtCore.QRect(210, 880, 371, 41))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(Form6)
        self.lineEdit_14.setGeometry(QtCore.QRect(210, 920, 371, 41))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.comboBox_6 = QtGui.QComboBox(Form6)
        self.comboBox_6.setGeometry(QtCore.QRect(210, 810, 61, 31))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.setItemText(3, _fromUtf8(""))
        self.lineEdit_15 = QtGui.QLineEdit(Form6)
        self.lineEdit_15.setGeometry(QtCore.QRect(210, 980, 371, 41))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(Form6)
        self.lineEdit_16.setGeometry(QtCore.QRect(210, 1020, 371, 41))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.lineEdit_17 = QtGui.QLineEdit(Form6)
        self.lineEdit_17.setGeometry(QtCore.QRect(210, 1060, 371, 41))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_18 = QtGui.QLineEdit(Form6)
        self.lineEdit_18.setGeometry(QtCore.QRect(210, 1100, 371, 41))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.lineEdit_19 = QtGui.QLineEdit(Form6)
        self.lineEdit_19.setGeometry(QtCore.QRect(210, 1140, 371, 41))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.label_32 = QtGui.QLabel(Form6)
        self.label_32.setGeometry(QtCore.QRect(50, 1200, 211, 31))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.radioButton = QtGui.QRadioButton(Form6)
        self.radioButton.setGeometry(QtCore.QRect(270, 1190, 117, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Form6)
        self.radioButton_2.setGeometry(QtCore.QRect(270, 1220, 117, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.comboBox_3 = QtGui.QComboBox(Form6)
        self.comboBox_3.setGeometry(QtCore.QRect(210, 1260, 371, 41))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_7 = QtGui.QComboBox(Form6)
        self.comboBox_7.setGeometry(QtCore.QRect(210, 1350, 371, 41))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_8 = QtGui.QComboBox(Form6)
        self.comboBox_8.setGeometry(QtCore.QRect(210, 1400, 371, 41))
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.lineEdit_20 = QtGui.QLineEdit(Form6)
        self.lineEdit_20.setGeometry(QtCore.QRect(210, 1450, 371, 41))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.comboBox_4 = QtGui.QComboBox(Form6)
        self.comboBox_4.setGeometry(QtCore.QRect(210, 1300, 371, 41))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Form6)
        self.pushButton.setGeometry(QtCore.QRect(620, 960, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.insert_db)
        self.pushButton_3 = QtGui.QPushButton(Form6)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 1510, 99, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Form6)
        QtCore.QMetaObject.connectSlotsByName(Form6)

    def retranslateUi(self, Form6):
        Form6.setWindowTitle(_translate("Form6", "तक्रारदाराचा तपशील ", None))
        self.pushButton_2.setText(_translate("Form6", "तक्रारदाराचा तपशील ", None))
        self.label_5.setText(_translate("Form6", "तक्रारदाराचा तपशील ", None))
        self.label_2.setText(_translate("Form6", "तारीख*", None))
        self.label_3.setText(_translate("Form6", "वेळ*", None))
        self.label_4.setText(_translate("Form6", "या अधिकाऱ्यासाठी नोंद ", None))
        self.comboBox.setItemText(0, _translate("Form6", "निवडा ", None))
        self.comboBox.setItemText(1, _translate("Form6", "S.S .Deshpande", None))
        self.comboBox.setItemText(2, _translate("Form6", "S.P Jadhav", None))
        self.comboBox.setItemText(3, _translate("Form6", "R.M Patil", None))
        self.label.setText(_translate("Form6", "                                                                          तक्रारदारचा तपशील माहिती ", None))
        self.label_6.setText(_translate("Form6", "युआयडी", None))
        self.label_7.setText(_translate("Form6", "नाते प्रकार", None))
        self.label_8.setText(_translate("Form6", "शेवटचे नाव/आडनाव", None))
        self.label_9.setText(_translate("Form6", "मधले नाव", None))
        self.label_10.setText(_translate("Form6", "प्रथम नाव*", None))
        self.label_11.setText(_translate("Form6", "लिंग ", None))
        self.label_12.setText(_translate("Form6", "जन्मतारीख ", None))
        self.label_13.setText(_translate("Form6", "जन्मवर्ष ", None))
        self.label_14.setText(_translate("Form6", "नातेवाईकाचे नाव", None))
        self.label_15.setText(_translate("Form6", "                                                                                वय पॅनल ", None))
        self.label_16.setText(_translate("Form6", "ई-मेल-आयडी", None))
        self.label_17.setText(_translate("Form6", "दूरध्वनी क्रमांक ", None))
        self.label_18.setText(_translate("Form6", "मोबाईल नं ", None))
        self.label_19.setText(_translate("Form6", "वैवाहिक स्थिती ", None))
        self.label_20.setText(_translate("Form6", "वय(वर्ष/महिना) ", None))
        self.label_21.setText(_translate("Form6", "घर नं ", None))
        self.label_22.setText(_translate("Form6", "रस्त्याचे नाव", None))
        self.label_23.setText(_translate("Form6", "तहसिल/गट/मंडळ ", None))
        self.label_24.setText(_translate("Form6", "गाव/शहर ", None))
        self.label_25.setText(_translate("Form6", "वसाहत/परिसर/ क्षेत्र", None))
        self.label_26.setText(_translate("Form6", "देश *", None))
        self.label_27.setText(_translate("Form6", "राज्य *", None))
        self.label_28.setText(_translate("Form6", "      \n"
"पोलीस ठाणे    ", None))
        self.label_29.setText(_translate("Form6", "जिल्हा *", None))
        self.label_30.setText(_translate("Form6", "पिन कोड", None))
        self.label_31.setText(_translate("Form6", "                                                                               कायमचा पत्ता ", None))
        self.comboBox_2.setItemText(0, _translate("Form6", "parent ", None))
        self.comboBox_2.setItemText(1, _translate("Form6", "brother", None))
        self.comboBox_2.setItemText(2, _translate("Form6", "sister ", None))
        self.comboBox_2.setItemText(3, _translate("Form6", "other ", None))
        self.comboBox_5.setItemText(0, _translate("Form6", "निवडा ", None))
        self.comboBox_5.setItemText(1, _translate("Form6", "male", None))
        self.comboBox_5.setItemText(2, _translate("Form6", "female ", None))
        self.comboBox_5.setItemText(3, _translate("Form6", "otehr ", None))
        self.comboBox_6.setItemText(0, _translate("Form6", "निवडा ", None))
        self.comboBox_6.setItemText(1, _translate("Form6", "married ", None))
        self.comboBox_6.setItemText(2, _translate("Form6", "unmarried ", None))
        self.label_32.setText(_translate("Form6", "सध्याचा पत्ता कायमच्या पत्याप्रमाणे आहे *", None))
        self.radioButton.setText(_translate("Form6", "होय ", None))
        self.radioButton_2.setText(_translate("Form6", "नाही ", None))
        self.comboBox_3.setItemText(0, _translate("Form6", "भारत ", None))
        self.comboBox_3.setItemText(1, _translate("Form6", "New Item", None))
        self.comboBox_7.setItemText(0, _translate("Form6", "निवडा ", None))
        self.comboBox_7.setItemText(1, _translate("Form6", "अकोला ", None))
        self.comboBox_7.setItemText(2, _translate("Form6", "अमरावती ", None))
        self.comboBox_7.setItemText(3, _translate("Form6", "उस्मानाबाद ", None))
        self.comboBox_7.setItemText(4, _translate("Form6", "औरंगाबाद ", None))
        self.comboBox_7.setItemText(5, _translate("Form6", "कोल्हापुर ", None))
        self.comboBox_7.setItemText(6, _translate("Form6", "गडचिरोली ", None))
        self.comboBox_7.setItemText(7, _translate("Form6", "गोंदिया ", None))
        self.comboBox_7.setItemText(8, _translate("Form6", "चंद्रपुर", None))
        self.comboBox_7.setItemText(9, _translate("Form6", "जळगाव ", None))
        self.comboBox_7.setItemText(10, _translate("Form6", "जलना ", None))
        self.comboBox_7.setItemText(11, _translate("Form6", "धुले ", None))
        self.comboBox_7.setItemText(12, _translate("Form6", "नंदुरबार ", None))
        self.comboBox_7.setItemText(13, _translate("Form6", "नागपुर ", None))
        self.comboBox_7.setItemText(14, _translate("Form6", "नाशिक ", None))
        self.comboBox_7.setItemText(15, _translate("Form6", "नांदेड़ ", None))
        self.comboBox_7.setItemText(16, _translate("Form6", "ठाणे ", None))
        self.comboBox_7.setItemText(17, _translate("Form6", "परभणी ", None))
        self.comboBox_7.setItemText(18, _translate("Form6", "पुणे ", None))
        self.comboBox_7.setItemText(19, _translate("Form6", "बिड ", None))
        self.comboBox_7.setItemText(20, _translate("Form6", "बुलढाणा ", None))
        self.comboBox_7.setItemText(21, _translate("Form6", "भंडारा ", None))
        self.comboBox_7.setItemText(22, _translate("Form6", "मुंबई जिल्हा ", None))
        self.comboBox_7.setItemText(23, _translate("Form6", "मुंबई उपनगर ", None))
        self.comboBox_7.setItemText(24, _translate("Form6", "यवतमाल ", None))
        self.comboBox_7.setItemText(25, _translate("Form6", "रायगढ़ ", None))
        self.comboBox_7.setItemText(26, _translate("Form6", "लातूर ", None))
        self.comboBox_7.setItemText(27, _translate("Form6", "वर्धा ", None))
        self.comboBox_7.setItemText(28, _translate("Form6", "वाशिम ", None))
        self.comboBox_7.setItemText(29, _translate("Form6", "सांगली ", None))
        self.comboBox_7.setItemText(30, _translate("Form6", "सातारा  ", None))
        self.comboBox_7.setItemText(31, _translate("Form6", "सोलापुर ", None))
        self.comboBox_7.setItemText(32, _translate("Form6", "हिंगोली ", None))
        self.comboBox_8.setItemText(0, _translate("Form6", "निवडा ", None))
        self.comboBox_8.setItemText(1, _translate("Form6", "New Item", None))
        self.comboBox_4.setItemText(0, _translate("Form6", "निवडा ", None))
        self.comboBox_4.setItemText(1, _translate("Form6", "आंध्र प्रदेश ", None))
        self.comboBox_4.setItemText(2, _translate("Form6", "अरुणाचल प्रदेश ", None))
        self.comboBox_4.setItemText(3, _translate("Form6", "बिहार ", None))
        self.comboBox_4.setItemText(4, _translate("Form6", "छत्तीसगड ", None))
        self.comboBox_4.setItemText(5, _translate("Form6", "गोआ ", None))
        self.comboBox_4.setItemText(6, _translate("Form6", "गुजरात ", None))
        self.comboBox_4.setItemText(7, _translate("Form6", "हरियाणा ", None))
        self.comboBox_4.setItemText(8, _translate("Form6", "हिमाचल प्रदेश ", None))
        self.comboBox_4.setItemText(9, _translate("Form6", "जम्मू काश्मीर ", None))
        self.comboBox_4.setItemText(10, _translate("Form6", "झारखंड ", None))
        self.comboBox_4.setItemText(11, _translate("Form6", "कर्नाटक ", None))
        self.comboBox_4.setItemText(12, _translate("Form6", "केरळ ", None))
        self.comboBox_4.setItemText(13, _translate("Form6", "मध्यप्रदेश ", None))
        self.comboBox_4.setItemText(14, _translate("Form6", "महाराष्ट्र ", None))
        self.comboBox_4.setItemText(15, _translate("Form6", "मणिपूर ", None))
        self.comboBox_4.setItemText(16, _translate("Form6", "मेघालय ", None))
        self.comboBox_4.setItemText(17, _translate("Form6", "मेघालय ", None))
        self.comboBox_4.setItemText(18, _translate("Form6", "नागालँड ", None))
        self.comboBox_4.setItemText(19, _translate("Form6", "उडीसा ", None))
        self.comboBox_4.setItemText(20, _translate("Form6", "पंजाब ", None))
        self.comboBox_4.setItemText(21, _translate("Form6", "राजस्थान", None))
        self.comboBox_4.setItemText(22, _translate("Form6", "सिक्कम ", None))
        self.comboBox_4.setItemText(23, _translate("Form6", "तामिळनाडू ", None))
        self.comboBox_4.setItemText(24, _translate("Form6", "तेलंगणा ", None))
        self.comboBox_4.setItemText(25, _translate("Form6", "तिरपुरा ", None))
        self.comboBox_4.setItemText(26, _translate("Form6", "उत्तर प्रदेश ", None))
        self.comboBox_4.setItemText(27, _translate("Form6", "उत्तरांचल ", None))
        self.comboBox_4.setItemText(28, _translate("Form6", "पश्चिम बंगाल ", None))
        self.pushButton.setText(_translate("Form6", "जतन करा ", None))
        self.pushButton_3.setText(_translate("Form6", "रिक्त करा ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form6 = QtGui.QWidget()
    ui = Ui_Form6()
    ui.setupUi(Form6)
    Form6.show()
    sys.exit(app.exec_())

