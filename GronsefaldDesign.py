# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atbash.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AtbashForm(object):
    def setupUi(self, AtbashForm):
        AtbashForm.setObjectName("AtbashForm")
        AtbashForm.resize(418, 480)
        self.gridLayout = QtWidgets.QGridLayout(AtbashForm)
        self.gridLayout.setObjectName("gridLayout")
        self.inputLabel = QtWidgets.QLabel(AtbashForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputLabel.setFont(font)
        self.inputLabel.setMidLineWidth(1)
        self.inputLabel.setTextFormat(QtCore.Qt.AutoText)
        self.inputLabel.setObjectName("inputLabel")
        self.gridLayout.addWidget(self.inputLabel, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(AtbashForm)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.keyEdit = QtWidgets.QLineEdit(AtbashForm)
        self.keyEdit.setPlaceholderText("Enter key")
        self.horizontalLayout.addWidget(self.keyEdit)
        self.encryptButton = QtWidgets.QPushButton(AtbashForm)
        self.encryptButton.setObjectName("encryptButton")
        self.horizontalLayout.addWidget(self.encryptButton)
        self.decryptButton = QtWidgets.QPushButton(AtbashForm)
        self.decryptButton.setObjectName("decryptButton")
        self.horizontalLayout.addWidget(self.decryptButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.outputLabel = QtWidgets.QLabel(AtbashForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outputLabel.setFont(font)
        self.outputLabel.setMidLineWidth(1)
        self.outputLabel.setTextFormat(QtCore.Qt.AutoText)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout.addWidget(self.outputLabel, 3, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(AtbashForm)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 4, 0, 1, 1)

        self.retranslateUi(AtbashForm)
        QtCore.QMetaObject.connectSlotsByName(AtbashForm)

    def retranslateUi(self, AtbashForm):
        _translate = QtCore.QCoreApplication.translate
        AtbashForm.setWindowTitle(_translate("AtbashForm", "Шифр Гронсфельда"))
        self.inputLabel.setText(_translate("AtbashForm", "Исходный текст:"))
        self.encryptButton.setText(_translate("AtbashForm", "Зашифровать"))
        self.decryptButton.setText(_translate("AtbashForm", "Расшифровать"))
        self.outputLabel.setText(_translate("AtbashForm", "Результат:"))

        # def encrypt(self):
        #     input_text = self.textEdit.toPlainText()
        #     result = [""] * (len((input_text)) + 1)
        #     symbols_sum = int(len(input_text))
        #     key = 3  # strings
        #     cols_sum = int(((symbols_sum - 2) / key) // 1) + 1
        #     print("n = ", key, " m = ", cols_sum)
        #
        #     for i in range(symbols_sum):
        #         index = int((key * (i % cols_sum) + (i // cols_sum)))
        #         result[index] = input_text[i]
        #
        #     self.textBrowser.setPlainText(" ".join(str(x) for x in result))
        #
        # def decrypt(self):
        #     input_text = self.textEdit.toPlainText()
        #     result = [""] * (len((input_text)) + 1)
        #     symbols_sum = int(len(input_text))
        #     cols_sum = 3  # strings
        #     key = int(((symbols_sum - 2) / cols_sum) // 1) + 1
        #     print("n = ", key, " m = ", cols_sum)
        #
        #     for i in range(symbols_sum):
        #         index = int((key * (i % cols_sum) + (i // cols_sum)))
        #         result[index] = input_text[i]

