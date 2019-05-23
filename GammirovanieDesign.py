# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gammirovanie.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AtbashForm(object):
    def setupUi(self, AtbashForm):
        AtbashForm.setObjectName("AtbashForm")
        AtbashForm.resize(492, 686)
        self.gridLayout = QtWidgets.QGridLayout(AtbashForm)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(AtbashForm)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(AtbashForm)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 7, 0, 1, 1)
        self.inputLabel = QtWidgets.QLabel(AtbashForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputLabel.setFont(font)
        self.inputLabel.setMidLineWidth(1)
        self.inputLabel.setTextFormat(QtCore.Qt.AutoText)
        self.inputLabel.setObjectName("inputLabel")
        self.gridLayout.addWidget(self.inputLabel, 0, 0, 1, 1)
        self.outputLabel = QtWidgets.QLabel(AtbashForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outputLabel.setFont(font)
        self.outputLabel.setMidLineWidth(1)
        self.outputLabel.setTextFormat(QtCore.Qt.AutoText)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout.addWidget(self.outputLabel, 6, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(AtbashForm)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_File = QtWidgets.QRadioButton(AtbashForm)
        self.radioButton_File.setObjectName("radioButton_File")
        self.horizontalLayout_2.addWidget(self.radioButton_File)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.keyEdit = QtWidgets.QLineEdit(AtbashForm)
        self.keyEdit.setInputMask("")
        self.keyEdit.setText("")
        self.keyEdit.setPlaceholderText("")
        self.keyEdit.setObjectName("keyEdit")
        self.gridLayout.addWidget(self.keyEdit, 3, 0, 1, 1)

        self.retranslateUi(AtbashForm)
        QtCore.QMetaObject.connectSlotsByName(AtbashForm)

    def retranslateUi(self, AtbashForm):
        _translate = QtCore.QCoreApplication.translate
        AtbashForm.setWindowTitle(_translate("AtbashForm", "Гаммирование"))
        self.inputLabel.setText(_translate("AtbashForm", "Исходный текст:"))
        self.outputLabel.setText(_translate("AtbashForm", "Результат:"))
        self.encryptButton.setText(_translate("AtbashForm", "Зашифровать"))
        self.decryptButton.setText(_translate("AtbashForm", "Расшифровать"))
        self.swapButton.setText(_translate("AtbashForm", "Swap"))
        self.radioButton.setText(_translate("AtbashForm", "c окна"))
        self.radioButton_File.setText(_translate("AtbashForm", "с файла"))

