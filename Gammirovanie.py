from PyQt5 import QtWidgets
import GammirovanieDesign
from collections import OrderedDict

class Cipher(QtWidgets.QDialog, GammirovanieDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.encrypt)
        self.swapButton.clicked.connect(self.swap)
        self.radioButton.setChecked(True)

    def encrypt(self):
        input = ""
        input = self.textEdit.toPlainText()

        keys = ""
        keys += self.get_key()

        place_w = self.radioButton.isChecked()
        place_f = self.radioButton_File.isChecked()

        alpha = [[65, 91], [97, 123], [1040, 1072], [1072, 1104]]

        self.Alpha = [chr(j) for i in alpha for j in range(i[0], i[1])] + [chr(1025)] + [chr(1105)] + [chr(32)] + [
            chr(46)] + [
                    chr(44)] + [chr(33)] + [chr(37)] + [chr(35)] + [chr(40)] + [chr(41)] + [chr(45)] + [chr(47)]

        if place_w == True:
            self.crypto_window(input,keys)
        elif place_f == True:
            self.crypto_file(input)


    def crypto_window(self, input, keys):
        res10 = ''
        res2 = ''
        key2 = ''
        text2 = ''

        sum = 0
        input_ = ''
        for el in input:
            temp = self.Alpha.index(el)
            input_ += self.binary(temp)
            sum += len(self.binary(temp))

        key = self.make_key(keys, sum)
        for c in input:
            tmp = ''
            m = self.Alpha.index(c)
            c = self.binary(m)
            k = self.make_key(keys, len(c))
            c = '0' * (7 - len(c)) + c
            key2 += k + "  "
            text2 += c + "  "
            for s1, s2 in zip(c, k):
                tmp += self.XOR(s1, s2)
            res2 += tmp + "  "
            res10 += self.Alpha[self.INT(tmp)]

        result = res10 + "\n" + res2 + '\n' + key + "\n" + key2 + "\n" + input + "\n" + text2
        self.textBrowser.setPlainText("".join(x for x in result))

    def crypto_file(self, file_name):
        try:
            file = open(file_name)
        except OSError:
            self.show_msg(2)






    def XOR(self, s1, s2):
        if s1 == s2:
            return '0'
        if s1 != s2:
            return '1'

    def binary(self, s1):
        b = ''
        if s1 == 0:
            return '0'
        while s1 > 0:
            b = str(s1 % 2) + b
            s1 = s1 // 2
        return b

    def INT(self, s1):
        decimal = 0
        for digit in s1:
            decimal = decimal * 2 + int(digit)
        return decimal

    def swap(self):
        input_text = self.textEdit.toPlainText()
        tmp = self.textBrowser.toPlainText()
        self.textBrowser.setPlainText(input_text)
        self.textEdit.setPlainText(tmp)

    def make_key(self, keys, lenght):
        tmp = keys.split(" ")

        a = int(tmp[0])
        b = int(tmp[1])
        gamma = int(tmp[2])

        if b%2 == 0:
            self.show_msg(0)

        if a%4 != 1:
            self.show_msg(1)
        key = ''

        while len(key) < lenght:
            gamma = (a*gamma + b)%2017
            key += self.binary(gamma)
        return key

    def swap(self):
        input_text = self.textEdit.toPlainText()
        tmp = self.textBrowser.toPlainText()
        self.textBrowser.setPlainText(input_text)
        self.textEdit.setPlainText(tmp)

    def get_key(self):
        key = self.keyEdit.text()
        return key

    def show_msg(self,par):
        self.msg = QtWidgets.QMessageBox()
        if par == 0:
            self.msg.setText("Введите нечетное b!")
        if par == 1:
            self.msg.setText("Введите такое a, остаток от деления на 4 которого будет равен 1!")
        if par == 2:
            self.msg.setText("Файл не найден!")
        self.msg.exec_()
        return -1