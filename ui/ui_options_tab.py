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
        self.widgetFlipButtons.setGeometry(QtCore.QRect(1, 90, 344, 90))
        self.widgetFlipButtons.setObjectName("widgetFlipButtons")
        self.gridLayoutFlips = QtWidgets.QGridLayout(self.widgetFlipButtons)
        self.gridLayoutFlips.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutFlips.setObjectName("gridLayoutFlips")
        self.label_3 = QtWidgets.QLabel(self.widgetFlipButtons)
        self.label_3.setObjectName("label_3")
        self.gridLayoutFlips.addWidget(self.label_3, 0, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.widgetFlipButtons)
        self.label_4.setObjectName("label_4")
        self.gridLayoutFlips.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widgetFlipButtons)
        self.label_5.setObjectName("label_5")
        self.gridLayoutFlips.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widgetFlipButtons)
        self.label_6.setObjectName("label_6")
        self.gridLayoutFlips.addWidget(self.label_6, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widgetFlipButtons)
        self.label_7.setObjectName("label_7")
        self.gridLayoutFlips.addWidget(self.label_7, 2, 0, 1, 1)
        self.checkBoxCoronalFlipX = QtWidgets.QCheckBox(self.widgetFlipButtons)
        self.checkBoxCoronalFlipX.setText("")
        self.checkBoxCoronalFlipX.setObjectName("checkBoxCoronalFlipX")
        self.gridLayoutFlips.addWidget(self.checkBoxCoronalFlipX, 2, 2, 1, 1)
        self.checkBoxAxialFlipx = QtWidgets.QCheckBox(self.widgetFlipButtons)
        self.checkBoxAxialFlipx.setText("")
        self.checkBoxAxialFlipx.setObjectName("checkBoxAxialFlipx")
        self.gridLayoutFlips.addWidget(self.checkBoxAxialFlipx, 2, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widgetFlipButtons)
        self.label_8.setObjectName("label_8")
        self.gridLayoutFlips.addWidget(self.label_8, 3, 0, 1, 1)
        self.checkBoxSagittalFlipZ = QtWidgets.QCheckBox(self.widgetFlipButtons)
        self.checkBoxSagittalFlipZ.setText("")
        self.checkBoxSagittalFlipZ.setObjectName("checkBoxSagittalFlipZ")
        self.gridLayoutFlips.addWidget(self.checkBoxSagittalFlipZ, 3, 1, 1, 1)
        self.checkBoxCoronalFlipZ = QtWidgets.QCheckBox(self.widgetFlipButtons)
        self.checkBoxCoronalFlipZ.setText("")
        self.checkBoxCoronalFlipZ.setObjectName("checkBoxCoronalFlipZ")
        self.gridLayoutFlips.addWidget(self.checkBoxCoronalFlipZ, 3, 2, 1, 1)
        self.checkBoxAxialFlipZ = QtWidgets.QCheckBox(self.widgetFlipButtons)
        self.checkBoxAxialFlipZ.setText("")
        self.checkBoxAxialFlipZ.setObjectName("checkBoxAxialFlipZ")
        self.gridLayoutFlips.addWidget(self.checkBoxAxialFlipZ, 3, 3, 1, 1)
        self.checkBoxSagittalFlipX = QtWidgets.QCheckBox(self.widgetFlipButtons)
        self.checkBoxSagittalFlipX.setText("")
        self.checkBoxSagittalFlipX.setObjectName("checkBoxSagittalFlipX")
        self.gridLayoutFlips.addWidget(self.checkBoxSagittalFlipX, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(options)
        self.label_9.setGeometry(QtCore.QRect(370, 110, 62, 15))
        self.label_9.setObjectName("label_9")
        self.checkBoxImpcView = QtWidgets.QCheckBox(options)
        self.checkBoxImpcView.setGeometry(QtCore.QRect(370, 131, 62, 20))
        self.checkBoxImpcView.setText("")
        self.checkBoxImpcView.setObjectName("checkBoxImpcView")

        self.retranslateUi(options)
        QtCore.QMetaObject.connectSlotsByName(options)

    def retranslateUi(self, options):
        _translate = QtCore.QCoreApplication.translate
        options.setWindowTitle(_translate("options", "Form"))
        self.label_2.setText(_translate("options", "Options"))
        self.label_3.setText(_translate("options", "Orientationns"))
        self.label_4.setText(_translate("options", "Sagittal"))
        self.label_5.setText(_translate("options", "coronal"))
        self.label_6.setText(_translate("options", "axial"))
        self.label_7.setText(_translate("options", "Flip horizontal"))
        self.label_8.setText(_translate("options", "Reverse slice ordering"))
        self.label_9.setText(_translate("options", "impc view"))

import resources_rc
