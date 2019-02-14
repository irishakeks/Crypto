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


        # говнокод Иры

        upper_english = [["A", "B", "C", "D", "E"],
                         ["F", "G", "H", "I", "J"],
                         ["K", "L", "M", "N", "O"],
                         ["P", "Q", "R", "S", "T"],
                         ["U", "V", "W", "X", "Y"],
                         ["Z", "B", "C", "D", "E"]]

        result = ""

        for symbol in input_text:
            for string in upper_english:
                for element in string:
                    if symbol == element:
                        index = string.index(element)
                        indexU = upper_english.index(string)
                        symbol = upper_english[indexU+1][index]
                        result += symbol
                        print(index, indexU)
                        print(symbol, element)
                        break
                    break
                continue

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

