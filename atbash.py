from PyQt5 import QtWidgets
import atbashDesign


class Cipher(QtWidgets.QDialog, atbashDesign.Ui_AtbashForm):
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
        for char in input_text:
            if char == " ":
                result += " "
            elif char in self.rusABC:
                index = self.rusABC.find(char)
                result += (self.rusABC[-1*index - 1])
            elif char in self.rusABC_lower:
                index = self.rusABC_lower.find(char)
                result += (self.rusABC_lower[-1*index - 1])
            elif char in self.engABC:
                index = self.engABC.find(char)
                result += (self.engABC[-1 * index - 1])
            elif char in self.engABC_lower:
                index = self.engABC_lower.find(char)
                result += (self.engABC_lower[-1 * index - 1])
            else:
                result += char

        self.textBrowser.setPlainText(result)

    def decrypt(self):
        self.encrypt()




