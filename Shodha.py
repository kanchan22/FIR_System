# -*- coding: utf-8 -*-

# Form3 implementation generated from reading ui file 'Shodha.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName(_fromUtf8("Form3"))
        Form3.resize(730, 455)
        self.tableWidget = QtGui.QTableWidget(Form3)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 101, 101))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget_2 = QtGui.QTableWidget(Form3)
        self.tableWidget_2.setGeometry(QtCore.QRect(120, 100, 81, 101))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_3 = QtGui.QTableWidget(Form3)
        self.tableWidget_3.setGeometry(QtCore.QRect(300, 100, 101, 101))
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.tableWidget_4 = QtGui.QTableWidget(Form3)
        self.tableWidget_4.setGeometry(QtCore.QRect(200, 100, 101, 101))
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.tableWidget_5 = QtGui.QTableWidget(Form3)
        self.tableWidget_5.setGeometry(QtCore.QRect(400, 100, 101, 101))
        self.tableWidget_5.setObjectName(_fromUtf8("tableWidget_5"))
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        self.tableWidget_6 = QtGui.QTableWidget(Form3)
        self.tableWidget_6.setGeometry(QtCore.QRect(500, 100, 101, 101))
        self.tableWidget_6.setObjectName(_fromUtf8("tableWidget_6"))
        self.tableWidget_6.setColumnCount(1)
        self.tableWidget_6.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        self.label = QtGui.QLabel(Form3)
        self.label.setGeometry(QtCore.QRect(50, 60, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.listView = QtGui.QListView(Form3)
        self.listView.setGeometry(QtCore.QRect(20, 210, 581, 141))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label_2 = QtGui.QLabel(Form3)
        self.label_2.setGeometry(QtCore.QRect(50, 230, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(Form3)
        self.comboBox.setGeometry(QtCore.QRect(190, 220, 271, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(Form3)
        self.label_3.setGeometry(QtCore.QRect(50, 290, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Form3)
        self.lineEdit.setGeometry(QtCore.QRect(190, 270, 281, 51))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Form3)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        Form3.setWindowTitle(_translate("Form3", "शोधा", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form3", "तारीख", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form3", "वेळ", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form3", "अधिकाऱ् नोंद ", None))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Form3", "ठाणे दैनंदिनी प्रकार", None))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("Form3", "विषय", None))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("Form3", "ठाणे दैनंदिनी", None))
        self.label.setText(_translate("Form3", "शोधा", None))
        self.label_2.setText(_translate("Form3", "अधिकाऱ्याचे नाव ", None))
        self.comboBox.setItemText(0, _translate("Form3", "निवडा ", None))
        self.label_3.setText(_translate("Form3", "दिनांक ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form3 = QtGui.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form3)
    Form3.show()
    sys.exit(app.exec_())

