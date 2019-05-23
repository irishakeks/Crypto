from PyQt5 import QtWidgets
import VernamDesign
from collections import OrderedDict

class Cipher(QtWidgets.QDialog, VernamDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.encrypt)
        self.swapButton.clicked.connect(self.swap)


    def encrypt(self):

        key = ""
        key += self.get_key()
        input = ""
        input = self.textEdit.toPlainText()

        alpha = [[65, 91], [97, 123], [1040, 1072], [1072, 1104]]

        Alpha = [chr(j) for i in alpha for j in range(i[0], i[1])] + [chr(1025)] + [chr(1105)] + [chr(32)] + [
            chr(46)] + [
                    chr(44)] + [chr(33)] + [chr(37)] + [chr(35)] + [chr(40)] + [chr(41)] + [chr(45)] + [chr(47)]
        if len(key) < len(input):
            self.show_msg()
        res10 = ''
        res2 = ''
        key2 = ''
        text2 = ''
        for c, k in zip(input, key):
            tmp = ''
            m = Alpha.index(c)
            c = self.bin(m)
            c = '0' * (7 - len(c)) + c
            k = self.bin(Alpha.index(k))
            k = '0' * (7 - len(k)) + k
            key2 += k + "  "
            text2 += c + "  "
            for s1, s2 in zip(c, k):
                tmp += self.XOR(s1, s2)
            res2 += tmp + "  "
            res10 += Alpha[self.INT(tmp)]

        result = res10 + "\n" + res2 + '\n' + key + "\n" + key2 + "\n" + input + "\n" + text2
        self.textBrowser.setPlainText("".join(x for x in result))

    def XOR(self,s1, s2):
        if s1 == s2:
            return '0'
        if s1 != s2:
            return '1'

    def bin(self,s1):
        b = ''
        if s1 == 0:
            return '0'
        while s1 > 0:
            b = str(s1 % 2) + b
            s1 = s1 // 2
        return b

    def INT(self,s1):
        decimal = 0
        for digit in s1:
            decimal = decimal * 2 + int(digit)
        return decimal


    def swap(self):
        input_text = self.textEdit.toPlainText()
        tmp = self.textBrowser.toPlainText()
        self.textBrowser.setPlainText(input_text)
        self.textEdit.setPlainText(tmp)

    def get_key(self):
        key = self.keyEdit.text()
        return key

    def show_msg(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText("Длина входного текста больше длины ключа!")
        self.msg.exec_()
        return -1


