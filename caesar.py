from PyQt5 import QtWidgets
import scytaleDesign


class Cipher(QtWidgets.QDialog, scytaleDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)

    def encrypt(self):
        result = ""
        key = self.get_key()
        input_text = self.textEdit.toPlainText()
        for character in input_text:
            num = ord(character)
            num += key
            result += chr(num)

        self.textBrowser.setPlainText("".join(str(x) for x in result))

    def decrypt(self):
        result = ""
        key = self.get_key()
        input_text = self.textEdit.toPlainText()
        for character in input_text:
            num = ord(character)
            num -= key
            result += chr(num)

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

