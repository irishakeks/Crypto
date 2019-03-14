from PyQt5 import QtWidgets
import VigenerDesign
import random

class Cipher(QtWidgets.QDialog, VigenerDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.swapButton.clicked.connect(self.swap)


        self.rusABC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" #33
        self.rusABC_lower = self.rusABC.lower()
        self.engABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #26
        self.engABC_lower = self.engABC.lower()


    def encrypt(self):
        input_text = self.textEdit.toPlainText()

        key = self.get_key()
        result = ""

        iter = 0
        for letter in input_text:
            flag = False
            if iter > len(key) - 1:
                key_n = self.take_key(key[iter % len(key)])
            else:
                key_n = self.take_key(key[iter])
            count = 0
            for element in self.rusABC:
                if letter == element:
                    flag = True
                    index = self.rusABC.index(element)
                    key_n = int(key_n)
                    a = index + key_n
                    if a > 32:
                        a = a % 33
                    iter = iter + 1
                    result += self.rusABC[a]
                    break
            for element in self.rusABC_lower:
                if letter == element:
                    flag = True
                    index = self.rusABC_lower.index(element)
                    key_n = int(key_n)
                    a = index + key_n
                    if a > 32:
                        a = a % 33
                    iter = iter + 1
                    result += self.rusABC_lower[a]
                    break

            for element in self.engABC:
                count += 1
                if letter == element:
                    flag = True
                    index = self.engABC.index(element)
                    key_n = int(key_n)
                    a = index + key_n
                    if a > 25:
                        a = a % 26
                    iter = iter + 1
                    result += self.engABC[a]
                    break

            for element in self.engABC_lower:
                if letter == element:
                    flag = True
                    index = self.engABC_lower.index(element)
                    key_n = int(key_n)
                    a = index + key_n
                    if a > 25:
                        a = a % 26
                    iter = iter + 1
                    result += self.engABC_lower[a]
                    break

            if flag == False:
                result += letter


        self.textBrowser.setPlainText("".join(x for x in result))


    def take_key(self,letter):
        for element in self.rusABC:
            if letter == element:
                key = self.rusABC.index(element)
                return key

        for element in self.rusABC_lower:
            if letter == element:
                key = self.rusABC_lower.index(element)
                return key
        for element in self.engABC:
            if letter == element:
                key = self.engABC.index(element)
                return key

        for element in self.engABC_lower:
            if letter == element:
                key = self.engABC_lower.index(element)
                return key

    def decrypt(self):
        input_text = self.textEdit.toPlainText()

        key = self.get_key()
        result = ""

        iter = 0
        for letter in input_text:
            flag = False
            if iter > len(key) - 1:
                key_n = self.take_key(key[iter % len(key)])
            else:
                key_n = self.take_key(key[iter])
            count = 0
            for element in self.rusABC:
                if letter == element:
                    flag = True
                    index = self.rusABC.index(element)
                    key_n = int(key_n)
                    a = index - key_n
                    if a > 32:
                        a = a % 33
                    iter = iter + 1
                    result += self.rusABC[a]
                    break
            for element in self.rusABC_lower:
                if letter == element:
                    flag = True
                    index = self.rusABC_lower.index(element)
                    key_n = int(key_n)
                    a = index - key_n
                    if a > 32:
                        a = a % 33
                    iter = iter + 1
                    result += self.rusABC_lower[a]
                    break

            for element in self.engABC:
                count += 1
                if letter == element:

                    flag = True
                    index = self.engABC.index(element)
                    key_n = int(key_n)
                    a = index - key_n
                    if a > 25:
                        a = a % 26
                    iter = iter + 1
                    result += self.engABC[a]
                    break

            for element in self.engABC_lower:
                if letter == element:
                    flag = True
                    index = self.engABC_lower.index(element)
                    key_n = int(key_n)
                    a = index - key_n
                    if a > 25:
                        a = a % 26
                    iter = iter + 1
                    result += self.engABC_lower[a]
                    break

            if flag == False:
                result += letter


        self.textBrowser.setPlainText("".join(x for x in result))


    def swap(self):
        input_text = self.textEdit.toPlainText()
        tmp = self.textBrowser.toPlainText()
        self.textBrowser.setPlainText(input_text)
        self.textEdit.setPlainText(tmp)

    def get_key(self):
        key = self.keyEdit.text()
   #     try:
   #         if int(key) > 0:
        return key
   #         else:
   #             return self.show_msg()
   #     except:
   #         return self.show_msg()