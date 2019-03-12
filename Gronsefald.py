from PyQt5 import QtWidgets
import GronsefaldDesign
import random

class Cipher(QtWidgets.QDialog, GronsefaldDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)

        self.rusABC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.rusABC_lower = self.rusABC.lower()
        self.engABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.engABC_lower = self.engABC.lower()



    def encrypt(self):
        input_text = self.textEdit.toPlainText()

        key = self.get_key()
        result = ""

        iter = 0
        for letter in input_text:
            flag = False
            if iter > len(key) - 1:
                key_n = key[iter % len(key)]
            else:
                key_n = key[iter]
            for element in self.rusABC:
                if letter == element:
                    flag = True
                    index = self.rusABC.index(element)
                    key_n = int(key_n)
                    a = self.rusABC[index + key_n]
                    iter = iter + 1
                    result += a
                    continue
            for element in self.rusABC_lower:
                if letter == element:
                    flag = True
                    index = self.rusABC_lower.index(element)
                    key_n = int(key_n)
                    a = self.rusABC_lower[index + key_n]
                    iter = iter + 1
                    result += a
                    continue

            for element in self.engABC:
                if letter == element:
                    flag = True
                    index = self.engABC.index(element)
                    key_n = int(key_n)
                    a = self.engABC[index + key_n]
                    iter = iter + 1
                    result += a
                    continue
            for element in self.engABC_lower:
                if letter == element:
                    flag = True
                    index = self.engABC_lower.index(element)
                    key_n = int(key_n)
                    a = self.engABC_lower[index + key_n]
                    iter = iter + 1
                    result += a
                    continue

            if flag == False:
                result += letter


        self.textBrowser.setPlainText("".join(x for x in result))





    def decrypt(self):
        input_text = self.textEdit.toPlainText()

        key = self.get_key()
        result = ""

        iter = 0
        for letter in input_text:
            flag = False
            if iter > len(key) - 1:
                key_n = key[iter % len(key)]
            else:
                key_n = key[iter]
            for element in self.rusABC:
                if letter == element:
                    flag = True
                    index = self.rusABC.index(element)
                    key_n = int(key_n)
                    a = self.rusABC[index - key_n]
                    iter = iter + 1
                    result += a
                    continue
            for element in self.rusABC_lower:
                if letter == element:
                    flag = True
                    index = self.rusABC_lower.index(element)
                    key_n = int(key_n)
                    a = self.rusABC_lower[index - key_n]
                    iter = iter + 1
                    result += a
                    continue

            for element in self.engABC:
                if letter == element:
                    flag = True
                    index = self.engABC.index(element)
                    key_n = int(key_n)
                    a = self.engABC[index - key_n]
                    iter = iter + 1
                    result += a
                    continue
            for element in self.engABC_lower:
                if letter == element:
                    flag = True
                    index = self.engABC_lower.index(element)
                    key_n = int(key_n)
                    a = self.engABC_lower[index - key_n]
                    iter = iter + 1
                    result += a
                    continue

            if flag == False:
                result += letter


        self.textBrowser.setPlainText("".join(x for x in result))




    def get_key(self):
        key = self.keyEdit.text()
        try:
            if int(key) > 0:
                return key
            else:
                return self.show_msg()
        except:
            return self.show_msg()