# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_options_tab.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_options(object):
    def setupUi(self, options):
        options.setObjectName("options")
        options.resize(761, 737)
        self.label_2 = QtWidgets.QLabel(options)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 118, 29))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(options)
        self.line.setGeometry(QtCore.QRect(0, 50, 741, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(options)
        self.label.setGeometry(QtCore.QRect(20, 20, 16, 29))
        self.label.setText("")
        self.label.setObjectName("label")
        self.widgetFlipButtons = QtWidgets.QWidget(options)
        self.widgetFlipButtons.setGeometry(QtCore.QRect(10, 80, 344, 161))
        self.widgetFlipButtons.setObjectName("widgetFlipButtons")
        self.label_3 = QtWidgets.QLabel(self.widgetFlipButtons)
        self.label_3.setGeometry(QtCore.QRect(9, 9, 85, 17))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.widgetFlipButtons)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 304, 100))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.checkBoxSagittalFlipX = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxSagittalFlipX.setText("")
        self.checkBoxSagittalFlipX.setObjectName("checkBoxSagittalFlipX")
        self.gridLayout.addWidget(self.checkBoxSagittalFlipX, 1, 1, 1, 1)
        self.checkBoxCoronalFlipX = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxCoronalFlipX.setText("")
        self.checkBoxCoronalFlipX.setObjectName("checkBoxCoronalFlipX")
        self.gridLayout.addWidget(self.checkBoxCoronalFlipX, 1, 2, 1, 1)
        self.checkBoxAxialFlipx = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxAxialFlipx.setText("")
        self.checkBoxAxialFlipx.setObjectName("checkBoxAxialFlipx")
        self.gridLayout.addWidget(self.checkBoxAxialFlipx, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.checkBoxSagittalFlipY = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxSagittalFlipY.setText("")
        self.checkBoxSagittalFlipY.setObjectName("checkBoxSagittalFlipY")
        self.gridLayout.addWidget(self.checkBoxSagittalFlipY, 2, 1, 1, 1)
        self.checkBoxCoronalFlipY = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxCoronalFlipY.setText("")
        self.checkBoxCoronalFlipY.setObjectName("checkBoxCoronalFlipY")
        self.gridLayout.addWidget(self.checkBoxCoronalFlipY, 2, 2, 1, 1)
        self.checkBoxAxialFlipY = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxAxialFlipY.setText("")
        self.checkBoxAxialFlipY.setObjectName("checkBoxAxialFlipY")
        self.gridLayout.addWidget(self.checkBoxAxialFlipY, 2, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.checkBoxSagittalFlipZ = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxSagittalFlipZ.setText("")
        self.checkBoxSagittalFlipZ.setObjectName("checkBoxSagittalFlipZ")
        self.gridLayout.addWidget(self.checkBoxSagittalFlipZ, 3, 1, 1, 1)
        self.checkBoxCoronalFlipZ = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxCoronalFlipZ.setText("")
        self.checkBoxCoronalFlipZ.setObjectName("checkBoxCoronalFlipZ")
        self.gridLayout.addWidget(self.checkBoxCoronalFlipZ, 3, 2, 1, 1)
        self.checkBoxAxialFlipZ = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxAxialFlipZ.setText("")
        self.checkBoxAxialFlipZ.setObjectName("checkBoxAxialFlipZ")
        self.gridLayout.addWidget(self.checkBoxAxialFlipZ, 3, 3, 1, 1)
        self.checkBoxImpcView = QtWidgets.QCheckBox(options)
        self.checkBoxImpcView.setGeometry(QtCore.QRect(20, 270, 62, 20))
        self.checkBoxImpcView.setText("")
        self.checkBoxImpcView.setObjectName("checkBoxImpcView")
        self.textBrowser = QtWidgets.QTextBrowser(options)
        self.textBrowser.setGeometry(QtCore.QRect(50, 270, 256, 151))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(options)
        QtCore.QMetaObject.connectSlotsByName(options)

    def retranslateUi(self, options):
        _translate = QtCore.QCoreApplication.translate
        options.setWindowTitle(_translate("options", "Form"))
        self.label_2.setText(_translate("options", "Options"))
        self.label_3.setText(_translate("options", "Orientations"))
        self.label_4.setText(_translate("options", "Sagittal"))
        self.label_5.setText(_translate("options", "coronal"))
        self.label_6.setText(_translate("options", "axial"))
        self.label_7.setText(_translate("options", "Flip horizontal"))
        self.label_10.setText(_translate("options", "flip vertical"))
        self.label_8.setText(_translate("options", "Reverse slice ordering"))
        self.textBrowser.setHtml(_translate("options", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">IMPC view. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Checking this button with ensure that data downloaded from the DCC will be in the agreed orientation. For other data you may have to use the individual flip options.</p></body></html>"))

import resources_rc