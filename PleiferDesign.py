# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kardano.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AtbashForm(object):
    def setupUi(self, AtbashForm):
        AtbashForm.setObjectName("AtbashForm")
        AtbashForm.resize(492, 480)
        self.gridLayout = QtWidgets.QGridLayout(AtbashForm)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.encryptButton = QtWidgets.QPushButton(AtbashForm)
        self.encryptButton.setObjectName("encryptButton")
        self.horizontalLayout.addWidget(self.encryptButton)
        self.decryptButton = QtWidgets.QPushButton(AtbashForm)
        self.decryptButton.setObjectName("decryptButton")
        self.horizontalLayout.addWidget(self.decryptButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.swapButton = QtWidgets.QPushButton(AtbashForm)
        self.swapButton.setObjectName("swapButton")
        self.horizontalLayout.addWidget(self.swapButton)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(AtbashForm)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 5, 0, 1, 1)
        self.outputLabel = QtWidgets.QLabel(AtbashForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outputLabel.setFont(font)
        self.outputLabel.setMidLineWidth(1)
        self.outputLabel.setTextFormat(QtCore.Qt.AutoText)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout.addWidget(self.outputLabel, 4, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(AtbashForm)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.inputLabel = QtWidgets.QLabel(AtbashForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputLabel.setFont(font)
        self.inputLabel.setMidLineWidth(1)
        self.inputLabel.setTextFormat(QtCore.Qt.AutoText)
        self.inputLabel.setObjectName("inputLabel")
        self.gridLayout.addWidget(self.inputLabel, 0, 0, 1, 1)
        self.keyEdit = QtWidgets.QLineEdit(AtbashForm)
        self.keyEdit.setInputMask("")
        self.keyEdit.setPlaceholderText("")
        self.keyEdit.setObjectName("keyEdit")
        self.gridLayout.addWidget(self.keyEdit, 2, 0, 1, 1)

        self.retranslateUi(AtbashForm)
        QtCore.QMetaObject.connectSlotsByName(AtbashForm)

    def retranslateUi(self, AtbashForm):
        _translate = QtCore.QCoreApplication.translate
        AtbashForm.setWindowTitle(_translate("AtbashForm", "Плейфер"))
        self.encryptButton.setText(_translate("AtbashForm", "Зашифровать"))
        self.decryptButton.setText(_translate("AtbashForm", "Расшифровать"))
        self.swapButton.setText(_translate("AtbashForm", "Swap"))
        self.outputLabel.setText(_translate("AtbashForm", "Результат:"))
        self.inputLabel.setText(_translate("AtbashForm", "Исходный текст:"))
       # self.keyEdit.setText(_translate("AtbashForm", "2,1,3-2,1-4,3,2,1-1,2,3,4,5,6,7,8-5,4,3,2,1-1,2,3-7,6,5,4,3,2,1-1,2"))

