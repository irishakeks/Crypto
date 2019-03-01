from PyQt5 import QtWidgets
import scytaleDesign


class Cipher(QtWidgets.QDialog, scytaleDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)

    def encrypt(self):
        input_text = self.textEdit.toPlainText()
        result = str()
        key = self.get_key()
        cols_sum = int((len(input_text) - 1) / key) + 1
        while len(input_text) != key*cols_sum:
            input_text += "\xa0"

        for i in range(key):
            j = i
            while j < len(input_text):
                result += input_text[j]
                j += key

        self.textBrowser.setPlainText("".join(str(x) for x in result))

    def decrypt(self):
        input_text = self.textEdit.toPlainText()
        result = str()
        key = self.get_key()
        cols_sum = int((len(input_text) - 1) / key) + 1

        for i in range(cols_sum):
            j = i
            while j < len(input_text):
                if input_text[j] != "\xa0":
                    result += input_text[j]
                    j += cols_sum
                else:
                    j += cols_sum
                    continue
        self.textBrowser.setPlainText("".join(str(x) for x in result))

    def get_key(self):
        key = self.keyEdit.text()
        try:
            if int(key) > 0:
                return int(key)
            else:
                return self.show_msg()
        except:
            return self.show_msg()

    def show_msg(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText("Введено недопустимое значение ключа")
        self.msg.exec_()
        return -1

