from PyQt5 import QtWidgets
import GammirovanieDesign
from collections import OrderedDict
import FileDialog

class Cipher(QtWidgets.QDialog, GammirovanieDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.encrypt)
        self.swapButton.clicked.connect(self.swap)
        self.radioButton.setChecked(True)

    def encrypt(self):
        if self.radioButton.isChecked():
            text = self.textEdit.toPlainText()
        else:
            text = self.open_text()
            print(text)
            self.textEdit.setPlainText(text)
        a = self.some_meth(text)
        self.textBrowser.setPlainText("".join(x for x in a[0]))

    def some_meth(self, input):
        keys = ""
        keys += self.get_key()
        if len(keys) == 0:
            self.show_msg(1)
            return "Неверная длина введенного текста"

        keys = keys.split()

        input = bytearray(input.encode('mbcs'))

        amount = len(input)
        res10 = bytearray(b'')
        res10 += input

        i = 0
        j = 0

        key = self.LCG(amount, keys)

        for c in input:
            tmp = ''
            c = self.BIN(c)
            c = '0' * (8 - len(c)) + c
            k = self.BIN(key[j])
            k = '0' * (8 - len(k)) + k
            for s1, s2 in zip(c, k):
                tmp += self.XOR(s1, s2)
            res10[i] = self.INT(tmp)
            i += 1
            if keys[3] == 1:
                if j == 63:
                    keys[2] = key[63]
                    key = self.LCG(amount, keys)
                    j = 0
                else:
                    j += 1
            else:
                j += 1

        return res10.decode('mbcs'), res10

    def XOR(self, s1, s2):
        if s1 == s2:
            return '0'
        if s1 != s2:
            return '1'

    def BIN(self, s1):
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

    def LCG(self, amount, param):
        a = int(param[0])
        b = int(param[1])
        if b % 2 == 0:
            self.show_msg(0)
            # return
        if a % 4 != 1:
            self.show_msg(1)
            # return
        gamma = int(param[2])
        key = []
        if int(param[3]) == 1:
            n = 64
        else:
            n = amount
        while len(key) < n:
            gamma = (a * gamma + b) % 16661
            key.append(gamma % 256)
        return key

    def crypto_file(self, file_name):
        try:
            file = open(file_name)
        except OSError:
            self.show_msg(2)
            return "Неверная длина введенного текста"


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
        # return -1

    def open_text(self):
        app = FileDialog.App()
        app.show()
        if app.path:
            with open(app.path, encoding='utf-8') as f:
                text = f.read()
                return text