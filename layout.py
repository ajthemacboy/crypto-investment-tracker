# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver3.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(261, 261)
        Dialog.setAcceptDrops(False)
        self.label_static_tracker = QtWidgets.QLabel(Dialog)
        self.label_static_tracker.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.label_static_tracker.setStyleSheet("font-family: Segoe UI, Frutiger, Frutiger Linotype, Dejavu Sans, Helvetica Neue, Arial, sans-serif;\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"")
        self.label_static_tracker.setObjectName("label_static_tracker")
        self.label_static_holdings = QtWidgets.QLabel(Dialog)
        self.label_static_holdings.setGeometry(QtCore.QRect(140, 100, 111, 21))
        self.label_static_holdings.setStyleSheet("font-family: Segoe UI, Frutiger, Frutiger Linotype, Dejavu Sans, Helvetica Neue, Arial, sans-serif;\n"
"font-size: 16px;\n"
"")
        self.label_static_holdings.setObjectName("label_static_holdings")
        self.box_variable_holdings = QtWidgets.QDoubleSpinBox(Dialog)
        self.box_variable_holdings.setGeometry(QtCore.QRect(10, 100, 111, 22))
        self.box_variable_holdings.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.box_variable_holdings.setStyleSheet("font-family: Consolas, monaco, monospace;\n"
"font-size: 12px;")
        self.box_variable_holdings.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.box_variable_holdings.setDecimals(8)
        self.box_variable_holdings.setMaximum(9999999999.99999)
        self.box_variable_holdings.setSingleStep(0.0001)
        self.box_variable_holdings.setObjectName("box_variable_holdings")
        self.label_static_origprice = QtWidgets.QLabel(Dialog)
        self.label_static_origprice.setGeometry(QtCore.QRect(140, 40, 111, 21))
        self.label_static_origprice.setStyleSheet("font-family: Segoe UI, Frutiger, Frutiger Linotype, Dejavu Sans, Helvetica Neue, Arial, sans-serif;\n"
"font-size: 16px;\n"
"")
        self.label_static_origprice.setObjectName("label_static_origprice")
        self.label_static_currentworth = QtWidgets.QLabel(Dialog)
        self.label_static_currentworth.setGeometry(QtCore.QRect(140, 160, 111, 21))
        self.label_static_currentworth.setStyleSheet("font-family: Segoe UI, Frutiger, Frutiger Linotype, Dejavu Sans, Helvetica Neue, Arial, sans-serif;\n"
"font-size: 16px;\n"
"")
        self.label_static_currentworth.setObjectName("label_static_currentworth")
        self.label_variable_currentworth = QtWidgets.QLabel(Dialog)
        self.label_variable_currentworth.setGeometry(QtCore.QRect(10, 160, 111, 21))
        self.label_variable_currentworth.setStyleSheet("font-family: Consolas, monaco, monospace;\n"
"font-size: 12px;")
        self.label_variable_currentworth.setFrameShape(QtWidgets.QFrame.Box)
        self.label_variable_currentworth.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_variable_currentworth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_variable_currentworth.setObjectName("label_variable_currentworth")
        self.label_variable_origworth = QtWidgets.QLabel(Dialog)
        self.label_variable_origworth.setGeometry(QtCore.QRect(10, 130, 111, 21))
        self.label_variable_origworth.setStyleSheet("font-family: Consolas, monaco, monospace;\n"
"font-size: 12px;")
        self.label_variable_origworth.setFrameShape(QtWidgets.QFrame.Box)
        self.label_variable_origworth.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_variable_origworth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_variable_origworth.setObjectName("label_variable_origworth")
        self.label_static_origworth = QtWidgets.QLabel(Dialog)
        self.label_static_origworth.setGeometry(QtCore.QRect(140, 130, 111, 21))
        self.label_static_origworth.setStyleSheet("font-family: Segoe UI, Frutiger, Frutiger Linotype, Dejavu Sans, Helvetica Neue, Arial, sans-serif;\n"
"font-size: 16px;\n"
"")
        self.label_static_origworth.setObjectName("label_static_origworth")
        self.label_variable_worthchange = QtWidgets.QLabel(Dialog)
        self.label_variable_worthchange.setGeometry(QtCore.QRect(10, 190, 111, 21))
        self.label_variable_worthchange.setStyleSheet("font-family: Consolas, monaco, monospace;\n"
"font-size: 12px;")
        self.label_variable_worthchange.setFrameShape(QtWidgets.QFrame.Box)
        self.label_variable_worthchange.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_variable_worthchange.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_variable_worthchange.setObjectName("label_variable_worthchange")
        self.label_static_worthchange = QtWidgets.QLabel(Dialog)
        self.label_static_worthchange.setGeometry(QtCore.QRect(140, 190, 111, 21))
        self.label_static_worthchange.setStyleSheet("font-family: Segoe UI, Frutiger, Frutiger Linotype, Dejavu Sans, Helvetica Neue, Arial, sans-serif;\n"
"font-size: 16px;\n"
"")
        self.label_static_worthchange.setObjectName("label_static_worthchange")
        self.box_variable_origprice = QtWidgets.QDoubleSpinBox(Dialog)
        self.box_variable_origprice.setGeometry(QtCore.QRect(10, 40, 111, 22))
        self.box_variable_origprice.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.box_variable_origprice.setStyleSheet("font-family: Consolas, monaco, monospace;\n"
"font-size: 12px;")
        self.box_variable_origprice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.box_variable_origprice.setDecimals(8)
        self.box_variable_origprice.setMaximum(9999999999.99999)
        self.box_variable_origprice.setObjectName("box_variable_origprice")
        self.label_static_currentprice = QtWidgets.QLabel(Dialog)
        self.label_static_currentprice.setGeometry(QtCore.QRect(140, 70, 111, 21))
        self.label_static_currentprice.setStyleSheet("font-family: Segoe UI, Frutiger, Frutiger Linotype, Dejavu Sans, Helvetica Neue, Arial, sans-serif;\n"
"font-size: 16px;\n"
"")
        self.label_static_currentprice.setObjectName("label_static_currentprice")
        self.label_variable_currentprice = QtWidgets.QLabel(Dialog)
        self.label_variable_currentprice.setGeometry(QtCore.QRect(10, 70, 111, 21))
        self.label_variable_currentprice.setStyleSheet("font-family: Consolas, monaco, monospace;\n"
"font-size: 12px;")
        self.label_variable_currentprice.setFrameShape(QtWidgets.QFrame.Box)
        self.label_variable_currentprice.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_variable_currentprice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_variable_currentprice.setObjectName("label_variable_currentprice")
        self.button_static_updateprice = QtWidgets.QPushButton(Dialog)
        self.button_static_updateprice.setGeometry(QtCore.QRect(60, 230, 91, 23))
        self.button_static_updateprice.setStyleSheet("font-family: Segoe UI, Frutiger, Frutiger Linotype, Dejavu Sans, Helvetica Neue, Arial, sans-serif;\n"
"font-size: 12px;\n"
"")
        self.button_static_updateprice.setObjectName("button_static_updateprice")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(120, 40, 21, 181))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 210, 241, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.button_static_close = QtWidgets.QPushButton(Dialog)
        self.button_static_close.setGeometry(QtCore.QRect(160, 230, 91, 23))
        self.button_static_close.setStyleSheet("font-family: Segoe UI, Frutiger, Frutiger Linotype, Dejavu Sans, Helvetica Neue, Arial, sans-serif;\n"
"font-size: 12px;\n"
"")
        self.button_static_close.setObjectName("button_static_close")
        self.check_variable_pin = QtWidgets.QCheckBox(Dialog)
        self.check_variable_pin.setGeometry(QtCore.QRect(10, 230, 41, 21))
        self.check_variable_pin.setObjectName("check_variable_pin")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.box_variable_origprice, self.box_variable_holdings)
        Dialog.setTabOrder(self.box_variable_holdings, self.button_static_updateprice)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BTC Investment Tracker"))
        self.label_static_tracker.setText(_translate("Dialog", "BTC Investment Tracker"))
        self.label_static_holdings.setText(_translate("Dialog", "Holdings"))
        self.label_static_origprice.setText(_translate("Dialog", "Original Price"))
        self.label_static_currentworth.setText(_translate("Dialog", "Current Worth"))
        self.label_variable_currentworth.setText(_translate("Dialog", "0.0"))
        self.label_variable_origworth.setText(_translate("Dialog", "0.0"))
        self.label_static_origworth.setText(_translate("Dialog", "Original Worth"))
        self.label_variable_worthchange.setText(_translate("Dialog", "0.0"))
        self.label_static_worthchange.setText(_translate("Dialog", "Worth Change"))
        self.label_static_currentprice.setText(_translate("Dialog", "Current Price"))
        self.label_variable_currentprice.setText(_translate("Dialog", "0.0"))
        self.button_static_updateprice.setText(_translate("Dialog", "Update Price"))
        self.button_static_close.setText(_translate("Dialog", "Close"))
        self.check_variable_pin.setText(_translate("Dialog", "Pin"))

