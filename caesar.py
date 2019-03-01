from PyQt5 import QtWidgets
import caesarDesign


class Cipher(QtWidgets.QDialog, caesarDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.rusABC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.rusABC_lower = self.rusABC.lower()
        self.engABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.engABC_lower = self.engABC.lower()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)

    def encrypt(self):
        input_text = self.textEdit.toPlainText()
        result = ""
        key = self.get_key()
        for char in input_text:
            if char == " ":
                result += " "
            elif char in self.rusABC:
                index = self.rusABC.find(char)
                result += (self.rusABC[(index + key) % len(self.rusABC)])
            elif char in self.rusABC_lower:
                index = self.rusABC_lower.find(char)
                result += (self.rusABC_lower[(index + key) % len(self.rusABC)])
            elif char in self.engABC:
                index = self.engABC.find(char)
                result += (self.engABC[(index + key) % len(self.engABC)])
            elif char in self.engABC_lower:
                index = self.engABC_lower.find(char)
                result += (self.engABC_lower[(index + key) % len(self.engABC)])
            else:
                result += char

        self.textBrowser.setPlainText("".join(str(x) for x in result))

    def decrypt(self):
        input_text = self.textEdit.toPlainText()
        result = ""
        key = self.get_key()
        for char in input_text:
            if char == " ":
                result += " "
            elif char in self.rusABC:
                index = self.rusABC.find(char)
                result += (self.rusABC[(index - key) % len(self.rusABC)])
            elif char in self.rusABC_lower:
                index = self.rusABC_lower.find(char)
                result += (self.rusABC_lower[(index - key) % len(self.rusABC)])
            elif char in self.engABC:
                index = self.engABC.find(char)
                result += (self.engABC[(index - key) % len(self.engABC)])
            elif char in self.engABC_lower:
                index = self.engABC_lower.find(char)
                result += (self.engABC_lower[(index - key) % len(self.engABC)])
            else:
                result += char

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

