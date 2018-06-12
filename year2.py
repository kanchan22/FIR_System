# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'year.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from yearBar import year_bar
from year_vs_crime import pie
#from lineYear import line_year
from Murderpie import murder_pie
from Placebar import place_bar
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

class Ui_Frame20(object):
    def setupUi(self, Frame20):
        Frame20.setObjectName(_fromUtf8("Frame20"))
        Frame20.resize(658, 562)
        #Frame20.setFrameShape(QtGui.QFrame.StyledPanel)
        #Frame20.setFrameShadow(QtGui.QFrame.Raised)
        self.label = QtGui.QLabel(Frame20)
        self.label.setGeometry(QtCore.QRect(230, 50, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.listView = QtGui.QListView(Frame20)
        self.listView.setGeometry(QtCore.QRect(100, 90, 441, 391))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.splitter = QtGui.QSplitter(Frame20)
        self.splitter.setGeometry(QtCore.QRect(140, 120, 351, 301))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
	
        self.crime_rate_pie = QtGui.QPushButton(self.splitter)
        self.crime_rate_pie.setObjectName(_fromUtf8("crime_rate_pie"))
        self.crime_rate_pie.clicked.connect(lambda : place_bar())	

        self.yr_vs_rate_bar = QtGui.QPushButton(self.splitter)
        self.yr_vs_rate_bar.setObjectName(_fromUtf8("yr_vs_rate_bar"))
        self.yr_vs_rate_bar.clicked.connect(lambda : year_bar())	
	
        self.murder_vs_city = QtGui.QPushButton(self.splitter)
        self.murder_vs_city.setObjectName(_fromUtf8("murder_vs_city"))
        self.murder_vs_city.clicked.connect(lambda : murder_pie())	
	
        self.pie_year = QtGui.QPushButton(self.splitter)
        self.pie_year.setObjectName(_fromUtf8("pie_year"))
        self.pie_year.clicked.connect(lambda : pie())	

        self.retranslateUi(Frame20)
        QtCore.QMetaObject.connectSlotsByName(Frame20)

    def retranslateUi(self, Frame20):
        Frame20.setWindowTitle(_translate("Frame20", "Frame20", None))
        self.label.setText(_translate("Frame20", "Graphical Analysis", None))
        self.crime_rate_pie.setText(_translate("Frame20", "Crime rate in Different Cities", None))
        self.yr_vs_rate_bar.setText(_translate("Frame20", "Year vs Rate Of Crime", None))
        self.murder_vs_city.setText(_translate("Frame20", "Murder Rate Different Cities ", None))
        self.pie_year.setText(_translate("Frame20", "Crimes in The Year 2000", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame20 = QtGui.QFrame()
    ui = Ui_Frame20()
    ui.setupUi(Frame20)
    Frame20.show()
    sys.exit(app.exec_())

